#write to end of txt file
#accepts string


def w_txt(query_str,output='listoutput.txt', directory = 'C:\\Users\\Owner\\', endl = '\n'):#takes list writes to text
   
    name = directory + output
    with open(name, 'a') as wf:
        wf.write(query_str + '\n')
