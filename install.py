#!/bin/python

import os,sys,time

def bersih():
        os.system("clear")

def menu():
        print "\t \033[36;1mTools \033[35;1mBy \033[33;1mReza \033[32;1mAlfauzan\n"
        print("\033[32;1m1. \033[36;1mWajib update ya!!!")
        print("\033[32;1m2. \033[36;1mInfo Script.")
        # input
        pilih = input("\033[36;1mMasukkan \033[32;1mpilihan : ")
        if pilih ==1:
                os.system("pkg update && pkg upgrade")
                os.system("pkg install nano")
                os.system("pkg install figlet")
                os.system("pkg install toilet")
                os.system("pkg install ruby")
                os.system("gem install lolcat")
                os.system("pkg install python")
                os.system("pip install requests")
                os.system("pip install mechanize")
                os.system("pip install futures")
                os.system("pip install --upgrade pip")
                os.system("pip2 install requests")
                os.system("pip2 install mechanize")
                os.system("pip2 install futures")
                os.system("pip2 install --upgrade pip")
        if pilih ==2:
                os.system("figlet Rzaa Ajaa")
                logo = """
                      \033[32;1m===============================================
                      \033[32;1m= (+) \033[36;1mReza Yang Buat Scriptnya             \033[32;1m(+)=
                      \033[32;1m= (+) \033[36;1mGithub Gua :GRCR4K3R                 \033[32;1m(+)=
                      \033[32;1m= (+) \033[36;1mFacebook   :Rzaa Ajaa                \033[32;1m(+)=
                      \033[32;1m= (+) \033[36;1mProfil     :Stiker Pentol Itu gua!!  \033[32;1m(+)=
                      ==============================================="""
                print logo
menu()
