import sys
import shutil
import os

filename=sys.argv[1]
dependency_in=sys.argv[2]
dependency_out=sys.argv[3]

#if not os.path.exists(filename+".old"):
#    shutil.copy(filename,filename+".old")

class ByteWriter:
    def __init__(self):
        self.bytes=b""

    def write_string(self,string):
        encoded=string.encode(encoding='UTF8')
        self.write_uint(len(encoded))
        self.write_bytes(encoded)

    def write_bytes(self,byte_data):
        if type(byte_data)!=bytes:
            byte_data=bytes(byte_data)
        self.bytes+=byte_data

    def write_byte(self,byte_data):
        if type(byte_data)!=bytes:
            byte_data=bytes([byte_data])
        self.bytes+=byte_data

    def write_uint(self,value):
        while True:
            cur_byte=value&0x7f
            value=value-(value&0x7f)        
            if value!=0:
                self.write_byte(cur_byte|0x80)
            else:
                self.write_byte(cur_byte)
                break
            value=value>>7

    def save(self,filename):
        with open(filename,"wb") as f:
            f.write(self.bytes)

class ByteReader:
    def __init__(self,bytes):
        self.pos=0
        self.filedata=bytes

    def next_bytes(self,count):
        self.pos+=count
        return self.filedata[self.pos-count:self.pos]
    
    def next_uint(self):
        curVal=0
        mult=1
        while (self.filedata[self.pos]&0x80)!=0:
            curVal+=mult*(self.filedata[self.pos]&0x7f)
            self.pos+=1
            mult*=0x80
        curVal+=mult*self.filedata[self.pos]
        self.pos+=1
        return curVal

    def next_byte(self):
        self.pos+=1
        return self.filedata[self.pos-1]

    def next_string(self):
        length=self.next_uint()
        bytes=self.next_bytes(length)
        return bytes.decode('utf8')

    def bytes_left(self):
        return len(self.filedata)-self.pos


class WasmSection(ByteReader):
    def __init__(self,reader):
        self.section_type=reader.next_byte()
        self.section_length=reader.next_uint()
        if self.section_type==0:
            prev_pos=reader.pos
            self.section_name=reader.next_string()
            self.custom_section_length=self.section_length-(reader.pos-prev_pos)
            self.section_data=reader.next_bytes(self.custom_section_length)
        else:
            self.section_name=["custom","type","import","function","table","memory","global","export","start","element","code","data","data_count"][self.section_type]
            self.section_data=reader.next_bytes(self.section_length)
        ByteReader.__init__(self,self.section_data)


class WasmReader(ByteReader):
    def __init__(self,filename):
        with open(filename,"rb") as f:
            self.filedata=f.read()
        ByteReader.__init__(self,self.filedata)
        wasm_sig=self.next_bytes(4)
        if wasm_sig!=b'\x00asm':
            print("Not a wasm file")
            sys.exit(-1)
        self.version=self.next_bytes(4)
            

    
    def next_section(self):
        if self.pos<len(self.filedata):
            return WasmSection(self)
        else:
            return None

r=WasmReader(filename)
writer=ByteWriter()
writer.write_bytes(b'\x00asm\x01\x00\x00\x00')

while True:
    section=r.next_section()
    if not section:
        break
    print(section.section_type,section.section_name)
    # need to also handle dylink.0 for newer emscripten
    if section.section_name=='dylink':
        memory_size=section.next_uint()
        memory_align=section.next_uint()
        table_size=section.next_uint()
        table_align=section.next_uint()
        needed_dyn_libs_count=section.next_uint()
        needed_dyn_libs=[]
        length_change=0
        for c in range(needed_dyn_libs_count):
            need_lib=section.next_string()
            if need_lib==dependency_in:
                length_change+=len(dependency_out.encode('UTF8'))-len(need_lib.encode('UTF8'))
                need_lib=dependency_out
                print(f"Relocating {dependency_in} to {dependency_out}")
            needed_dyn_libs.append(need_lib)
        writer.write_byte(section.section_type) # section header
        print(length_change)
        writer.write_byte(section.section_length+length_change)
        writer.write_string(section.section_name) # custom section name
        writer.write_uint(memory_size)
        writer.write_uint(memory_align)
        writer.write_uint(table_size)
        writer.write_uint(table_align)
        writer.write_uint(len(needed_dyn_libs))
        for l in needed_dyn_libs:
            writer.write_string(l)
    else:
        if section.section_type==0:
            # custom section
            writer.write_byte(section.section_type)
            writer.write_uint(section.section_length)
            writer.write_string(section.section_name)
            writer.write_bytes(section.next_bytes(section.custom_section_length))
        else:
            writer.write_byte(section.section_type)
            writer.write_uint(section.section_length)
            writer.write_bytes(section.next_bytes(section.section_length))

writer.save(filename)
