import os
import getpass
import pyfiglet
import socket
import subprocess as sp
from espeakng import ESpeakNG as es
import pyttsx3
os.system("clear")
#design
os.system("tput setaf 4")
title = pyfiglet.figlet_format("Virtual Assistant", font = "digital" )
print(title)
os.system("tput setaf 2")
msg = pyfiglet.figlet_format("Welcome", font = "digital" )
print(msg)

engine = pyttsx3.init("espeak.py")
engine.say('Welcome')
engine.runAndWAit()
#pyttsx3.say("Welcome to my tool")

passwd = getpass.getpass(" Enter The Password : ")

if passwd != "myva":
	print("Password is Incorrect...")
	exit()


where = input(" Where you want to run this menu ? (local/remote) : ")
print(where)


def print_msg_box(msg, indent=1, width=None, title=None):
    os.system("tput setaf 2")
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width: 
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)
while True:
	os.system("clear")
	os.system("tput setaf 3")
	print("\t\t\t Menu Bar")
	os.system("tput setaf 7")
	print("\t\t-----------------------")
	msg = "press 0 : Linux\n" \
	      "Press 1 : Hadoop\n" \
	      "Press 2 : Web Server\n" \
	      "Press 3 : Exit\n"
	print_msg_box(msg=msg, indent=2, title='All Services') 

	if where == "local":
		os.system("tput setaf 4")
		ch = input("Enter choice (service): ")
		print(ch)

		if int(ch) == 0:
			while True:
				os.system("clear")
				os.system("tput setaf 2")
				msg ="Press 1 : Check Date\n" \
				     "Press 2 : Check Calender\n" \
				     "Press 3 : Check your IP \n" \
				     "Press 4 : Check RAM Status \n" \
				     "Press 5 : Check Storage details \n" \
				     "press 6 : To Clear Cache\n" \
			       	 "press 7 : To Transfer File to Other Linux System\n" \
				     "press 8 : To Launch Firefox \n" \
                                     "press 9 : To open an editor \n" \
                                     "press 10 : Go to Last Menu\n" \
				     "press 11 : To Exit" 
				print_msg_box(msg=msg, indent=2, title='Linux Command:') 
				os.system("tput setaf 4")
				ch=input("What's your choice : ")
				os.system("tput setaf 3")
				print(ch)
				if int(ch) == 0:
					exit()
				elif int(ch) == 1:
					os.system("date")


				elif int(ch) == 2:
					os.system("cal")

				elif int(ch) == 3:
					os.system("ifconfig")

				elif int(ch) == 4:
					os.system("free -m")
				elif int(ch) == 5:
					os.system("df -h")
				elif int(ch) == 6:
					os.system("echo 3 > /proc/sys/vm/drop_caches")
				elif int(ch) == 7:
					ip = input("Enter IP of target system : ")
					user = input("Enter username : ")
					src = input("Enter your source file path : ")
					dest = input("Enter destination folder path where you want to copy : ")
					output = sp.getstatusoutput("scp {} {}@{}:{}".format(src, user,ip,dest))
				elif int(ch) == 8:
					os.system("firefox")
				elif int(ch) == 9:
					editor = input("Which editor you want to open (Vim/Gedit)? ")
					if editor == 'vim':
						os.system("vim")
					elif editor == 'gedit':
						os.system("gedit")
					else:
						print("Invalid Choice")
				elif int(ch) == 10:
					break
				elif int(ch) == 11:
					exit()

				else:
					print("Incorrect Input")
				input("\nEnter To Continue...")

		elif int(ch) == 1:
			while True:
				os.system("clear")
				os.system("tput setaf 4")
				msg ="Press 1 : Install Jdk and Hadoop\n" \
				     "Press 2 : Configure  DataNode\n" \
				     "Press 3 : Configure  NameNode\n" \
				     "Press 4 : Configure Client\n" \
				     "Press 5 : Cluster Report\n" \
				     "press 6 : Check SafeMode(nameNode)\n" \
				     "press 7 : Disable Safemode in Namenode \n" \
				     "press 8 : Upload a File into Cluster\n" \
				     "press 9 : Go Back\n" \
				     "press 10 : Exit.."
				print_msg_box(msg=msg, indent=2, title='Hadoop Command:')
				os.system("tput setaf 4") 
				ch=input("choose your option : ")
				print(ch)
						#Hadoop-installation


				if int(ch) == 1:
					os.system("rpm -ivh jdk-8u171-linux-x64.rpm;rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")


						#namenode

				elif int(ch) == 2:
					os.system("rm -rf /nn")
					os.system("mkdir /nn")
					f=open("/etc/hadoop/hdfs-site.xml","w")
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
					
					<!-- Put site-specific property overrides in this file. -->
						
					<configuration>
					<property>
					<name>dfs.name.dir</name>
					<value>/nn</value>
					</property>
					</configuration>""")
					f.write(x)
					f.close
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
					<!-- Put site-specific property overrides in this file. -->
				
					<configuration>
					<property>
					<name>fs.default.name</name>
					<value>hdfs://0.0.0.0:9001</value>
					</property>
					</configuration> 
					""")
					f=open("/etc/hadoop/core-site.xml","w")
					f.write(x)
					f.close
					os.system('hadoop namenode -format ')
					os.system('hadoop-daemon.sh start namenode')

						#dataNode

				elif int(ch) == 3:
					masterip=input("Enter the master's ip : ")
					os.system("rm -rf /dn")
					os.system("mkdir /dn")
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
					<!-- Put site-specific property overrides in this file. -->
				
					<configuration>
					<property>
					<name>dfs.data.dir</name>
					<value>/dn</value>
					</property>
					</configuration>""")
					f=open("/etc/hadoop/hdfs-site.xml","w")
					f.write(x)
					f.close
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
					<!-- Put site-specific property overrides in this file. -->
				
					<configuration>
					<property>
					<name>fs.default.name</name>
					<value>hdfs://{}:9001</value>
					</property>
					</configuration> 
					""".format(masterip))
					f=open("/etc/hadoop/core-site.xml","w")
					f.write(x)
					f.close
					os.system('hadoop-daemon.sh start datanode')


						#client

				elif int(ch) == 4:
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
					<!-- Put site-specific property overrides in this file. -->
				
					<configuration>
					<property>
					<name>fs.default.name</name>
					<value>hdfs://192.168.43.102:9001</value>
					</property>
					</configuration> """)
					f=open("/etc/hadoop/core-site.xml","w")
					f.write(x)
					f.close

						#other  basic commands

				elif int(ch) == 5:
					os.system("hadoop dfsadmin -report | less")

				elif int(ch) == 6:
					os.system("hadoop dfsadmin -safemode get")
				elif int(ch) == 7:
					os.system("hadoop dfsadmin -safemode leave")
				elif int(ch) == 8:
					name = input('Enter File Name :')
					os.system(f"hadoop fs -put {name}/")
				elif int(ch) == 9:
					break
				elif int(ch) == 10:
					exit()

				else:
					print("Incorrect Number")
				input("\ncontinue...")
			
					#Apache webserver
						
		elif int(ch) == 2:
			while True:
				os.system("clear")
				os.system("tput setaf 2")
				msg = "press 0 : Check Apache Web Server is Installed or Not\n" \
				      "Press 1 : Start Httpd Service\n" \
				      "Press 2 : Disable Firewall and Set Enforcing\n" \
				      "Press 3 : Restart Httpd Service\n" \
				      "Press 4 : Configure Total Webserver\n" \
				      "Press 5 : Go Back\n" \
				      "press 6 : Exit.. "
				print_msg_box(msg=msg, indent=2, title='Web Server Commands:')
				os.system("tput setaf 4") 
				ch=input("choose your option : ")
				print(ch)
				if int(ch) == 0:
					os.system("rpm -q httpd")

				elif int(ch) == 1:
					os.system('yum install httpd;systemctl start httpd')
				elif int(ch) == 2:
					os.system('systemctl stop firewalld;setenforce 0')
				elif int(ch) == 3:
					os.system('systemctl restart httpd')
				elif int(ch) == 4:
					Soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
					IP=Soc.getsockname()[0]
					T=input("\tEnter your message to preview on web :")
					
					os.system('yum install httpd')
					os.system('cd /var/www/html/')
					os.system('touch web.html')
					os.system(f'echo "{T}" > /var/www/html/web.html')
					os.system('systemctl start httpd')
					os.system('systemctl stop firewalld')
					os.system('setenforce 0')
					os.system(f'firefox http://"{IP}"/web.html')
				elif int(ch) == 5:
					break
				elif int(ch) == 6:
					exit()

				else:
					print("Incorrect Number")
				input("\ncontinue...")

		
		elif int(ch) == 3:
			exit()



	elif where == "remote":
		ip = input("Enter remote IP: ")
		print(ip)
		ch = input("Enter choice (service): ")
		print(ch)

		if int(ch) == 0:
			while True:
				os.system("clear")
				os.system("tput setaf 2")
				msg ="Press 1 : Check Date\n" \
				     "Press 2 : Check Calender\n" \
				     "Press 3 : Check IP\n" \
				     "Press 4 : Check Httpd Status\n" \
				     "Press 5 : Start Httpd \n" \
				     "press 6 : To Clear Cache\n" \
			       	 "press 7 : To see files in any directory\n" \
				     "press 8 : Go Back \n" \
				     "press 9 : To Exit\n" 
				print_msg_box(msg=msg, indent=2, title='Linux Command:') 
				os.system("tput setaf 4")
				ch=input("choose your option : ")
				print(ch)
				if int(ch) == 1:
					os.system("ssh {} date".format(ip))
				elif int(ch) == 2:
					os.system("ssh {} cal".format(ip))
				elif int(ch) == 3:
					os.system("ssh {} ifconfig".format(ip))
				elif int(ch) == 4:
					os.system("ssh {} systemctl status httpd".format(ip))
				elif int(ch) == 5:
					os.system("ssh {} systemctl start httpd".format(ip))
				elif int(ch) == 6:
					os.system("ssh {} echo 3 > /proc/sys/vm/drop_caches".format(ip))
				elif int(ch) == 7:
					path=input("Enter the desired path of the directory: ") 
					os.system("ssh {} ls {}".format(ip,path))
				elif int(ch) == 8:
					break
				elif int(ch) == 9:
					exit()
				else:
					print("Incorrect Number")
				input("\nEnter To Continue...")
 
						#hadoop

		elif int(ch) == 1:
			while True:
				os.system("clear")
				os.system("tput setaf 4")
				msg="press 0 : To Exit\n"\
					"Press 1 : Install Jdk and Hadoop\n"\
				    "Press 2 : Configure  DataNode\n" \
				    "Press 3 : Configure  NameNode\n" \
				    "Press 4 : Configure Client\n" \
				    "Press 5 : Check the Connected Datanodes\n" \
				    "press 6 : Check SafeMode in NameNode\n" \
				    "press 7 : Disable Safemode in Namenode\n " \
				    "press 8 : Go Back..\n" \
				    "press 9 : Exit \n"
				print_msg_box(msg=msg, indent=2, title='Hadoop Command:')
				os.system("tput setaf 4")
				ch=input("choose your option : ")
				print(ch)
						#Hadoop-installation


				if int(ch) == 1:
					os.system("ssh {} rpm -ivh jdk-8u171-linux-x64.rpm".format(ip))
					os.system("ssh {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(ip))

						#namenode

				elif int(ch) == 2:
					os.system("ssh {} rm -rf /nn".format(ip))
					os.system("ssh {} mkdir /nn".format(ip))
					os.system("ssh {} ".format(ip))
					f=open("/etc/hadoop/hdfs-site.xml","w")
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
					
					<!-- Put site-specific property overrides in this file. -->
						
					<configuration>
					<property>
					<name>dfs.name.dir</name>
					<value>/nn</value>
					</property>
					</configuration>""")
					f.write(x)
					f.close
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
					<!-- Put site-specific property overrides in this file. -->
				
					<configuration>
					<property>
					<name>fs.default.name</name>
					<value>hdfs://0.0.0.0:9001</value>
					</property>
					</configuration> 
					""")
					f=open("/etc/hadoop/core-site.xml","w")
					f.write(x)
					f.close
					os.system("ssh {} hadoop namenode -format".format(ip))
					os.system("ssh {} hadoop-daemon.sh start namenode".format(ip))

						#dataNode

				elif int(ch) == 3:
					os.system("ssh {} rm -rf /nn".format(ip))
					os.system("ssh {} mkdir /nn".format(ip))
					os.system("ssh {} ".format(ip))
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
					<!-- Put site-specific property overrides in this file. -->
				
					<configuration>
					<property>
					<name>dfs.data.dir</name>
					<value>/dn</value>
					</property>
					</configuration>""")
					f=open("/etc/hadoop/hdfs-site.xml","w")
					f.write(x)
					f.close
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
					<!-- Put site-specific property overrides in this file. -->
				
					<configuration>
					<property>
					<name>fs.default.name</name>
					<value>hdfs://{}:9001</value>
					</property>
					</configuration> 
					""".format(masterip))
					f=open("/etc/hadoop/core-site.xml","w")
					f.write(x)
					f.close
					os.system("ssh {} hadoop-daemon.sh start datanode".format(ip))


						#client

				elif int(ch) == 4:
					os.system("ssh {} ".format(ip))
					x=("""<?xml version="1.0"?> 
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
					<!-- Put site-specific property overrides in this file. -->
				
					<configuration>
					<property>
					<name>fs.default.name</name>
					<value>hdfs://{}:9001</value>
					</property>
					</configuration> """.format(masterip))
					f=open("/etc/hadoop/core-site.xml","w")
					f.write(x)
					f.close

						#other basic commands

				elif int(ch) == 5:
					os.system("ssh {} hadoop dfsadmin -report | less".format(ip))
				elif int(ch) == 6:
					os.system("ssh {} hadoop dfsadmin -safemode get".format(ip))
				elif int(ch) == 7:
					os.system("ssh {} hadoop dfsadmin -safemode leave".format(ip))
				elif int(ch) == 8:
					break
				elif int(ch) == 9:
					exit()
				else:
					print("Incorrect Number")
				input("\ncontinue...")
		elif int(ch) == 3:
			while True:
				os.system("clear")
				os.system("tput setaf 2")
				msg = "press 0 : Check Apache Web Server is Installed or Not\n" \
				      "Press 1 : Start Httpd Service\n" \
				      "Press 2 : Disable Firewall and Set Enforcing\n" \
				      "Press 3 : Restart Httpd Service\n" \
				      "Press 4 : Configure Total Webserver\n" \
				      "Press 5 : Go Back\n" \
				      "press 6 : Exit.. "
				print_msg_box(msg=msg, indent=2, title='AWS Commands:')
				os.system("tput setaf 4") 
				ch=input("choose your option : ")
				print(ch)
				if int(ch) == 0:
					os.system("rpm -q httpd")

				elif int(ch) == 1:
					os.system('yum install httpd;systemctl start httpd')
				elif int(ch) == 2:
					os.system('systemctl stop firewalld;setenforce 0')
				elif int(ch) == 3:
					os.system('systemctl restart httpd')
				elif int(ch) == 4:
					Soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
					IP=Soc.getsockname()[0]
					T=input("\tEnter your message to preview on web :")
					
					os.system('yum install httpd')
					os.system('cd /var/www/html/')
					os.system('touch web.html')
					os.system(f'echo "{T}" > /var/www/html/web.html')
					os.system('systemctl start httpd')
					os.system('systemctl stop firewalld')
					os.system('setenforce 0')
					os.system(f'firefox http://"{IP}"/web.html')
				elif int(ch) == 5:
					break
				elif int(ch) == 6:
					exit()

				else:
					print("Incorrect Number")
				input("\ncontinue...")

						


	else:
		os.system("tput setaf 1")
		print("login is not supported....")
		os.system("tput setaf 7")
		exit()

	input("\nPress Enter to Continue....")





















