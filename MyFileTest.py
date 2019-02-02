jackfilename = 'C:\\Users\\mcgowan31\\Desktop\\Jack.txt'
jackfile = open(jackfilename,'a')
line_count = 0
while True:
	file_input = input("Enter something you want to add to the file or type \"exit\" to exit the file: ")
	if file_input.lower() != 'exit':
		#jackfile.write('\n')
		jackfile.write(file_input + "\n")
		jackfile.flush()
	else:	
		jackfile.close()
		break

jackfile = open(jackfilename,'r')
jackread = jackfile.readlines()

for item in jackread:
	line_count += 1
jackfile.close()

strlinecount = str(line_count)
jackfile = open(jackfilename,'a')
jackoutput = ("Closing the file with " + str(line_count + 1) + " lines it in." + '\n')
jackfile.write(jackoutput)

jackfile.close()