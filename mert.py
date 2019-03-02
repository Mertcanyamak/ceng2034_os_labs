import os,os.path, time

os.chdir('/home')              		      # I changed my location to /home

os.system('mkdir -p ~/os_lab_0')		#I created a folder with using os.system ( can use linux command like mkdir touch ls ...) also with (-p " to use parent directory")
		

os.chdir('/home/'+os.getlogin()+'/os_lab_0/')    #I Changed my path according to login user(computer)


os.system('touch 2.txt $HOME/os_lab_0')		# I created a file 2.txt under same path with using os.system('touch')

os.system('touch 1.py $HOME/os_lab_0')		# I created a file 1.py under same path with using os.system('touch')

													
	
for file in os.listdir(os.getcwd()):		# these are to see last modification which i created files.
	print("~~~~" + file + "~~~~")
	print("Last Modified time is  : %s" % time.ctime(os.path.getmtime(file)))		



for file in os.listdir(os.getcwd()):		#It shows that to find ending with '.txt' files under the same path
	if file.endswith(".txt"):
		print(os.path.join(os.getcwd(),file))					




