#write to end of txt file
#accepts string
import os

def w_txt(query_str,output='listoutput.txt', directory = 'C:\\Users\\Owner\\', endl = '\n'):
	#takes list writes to text
	if not directory:  directory = os.getcwd()

	name = directory + os.sep + output
	with open(name, 'a') as wf:
		wf.write(query_str + '\n')
