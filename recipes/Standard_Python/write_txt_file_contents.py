def create_txt_file(filename, content):
    f=open('text_files/'+filename, "w+")
    if type(content)==type('x'):
        f.write(content)
        f.close()
        msg='Wrote content successfully'
    
    elif type(content)==type([]):
        for line in content:
            f.write(line +'\n')
        f.close()        
        msg='content from list has been written'        
    return msg

