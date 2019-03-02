import os,os.path, time
print(os.getcwd()) 									 # I checked where i am.
	
os.chdir('/home/mertcan/OS/ceng2034_os_labs')    					 #Then i go to "ceng2034_os_labs" directory
print(os.getcwd())
 
os.mkdir('os_lab_0')     								 #I created a folder as "os_lab_0"
			
os.chdir('/home/mertcan/OS/ceng2034_os_labs/os_lab_0')  				 #Then i go in to that folder


with open("2.txt", "w") as file:
    file.write("Your text goes here")  							# I have created a 2.txt file in os_lab_0
with open("1.py", "w") as file:					
    file.write("Your text goes here") 							# I have created a 1.py file  in os_lab_0
 
print (os.listdir())									#  I have checked which i created file yet
	
for file in os.listdir(os.getcwd()):
	print("---" + file + "---")
	print("last modified : %s" % time.ctime(os.path.getmtime(file)))		#I printed all files last modified date in the folder


for file in os.listdir(os.getcwd()):
	if file.endswith(".txt"):
		print(os.path.join(os.getcwd(),file))					# Then i found only txt files in the folder


