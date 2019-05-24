def read_txt_file_str(filename):
    f=open('text_files/'+filename, "r")
    contents=f.read()
    f.close()
    return contents

def read_txt_file_list(filename):
    f=open('text_files/'+filename, "r")
    contents=f.readlines()
    f.close()
    return contents    