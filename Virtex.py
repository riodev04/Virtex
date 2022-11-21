#!/usr/bin/python3
#coding=utf-8

import os
import sys
import time
import json
import random
import socket
import shutil
import webbrowser
import concurrent.futures

try:
  __import__('requests')
except ModuleNotFoundError:
  os.system ('pip install requests')
finally:
  import requests

try:
  __import__('bs4')
except ModuleNotFoundError:
  os.system ("pip install bs4")
finally:
  from bs4 import BeautifulSoup as parser

UPDATE = "21-11-2022"

if 'linux' in sys.platform:
  r = "\033[91m" # Red
  g = "\033[92m" # Green
  y = "\033[93m" # Yellow
  p = "\033[94m" # Purple
  P = "\033[95m" # Pink
  c = "\033[96m" # Cyan
  w = "\033[97m" # White
  a = "\033[0m"  # Reset
else:
  # Convert String To Variabel Name
  for i in ['r','g','y','p','P','c','w','a']:
    globals()[i] = ""

try:
  print (f"\n{p}[{y}!{p}] {r}Connecting To Server")
  data = requests.get("https://www.mediafire.com/api/1.4/folder/get_content.php?content_type=files&filter=all&order_by=name&order_direction=asc&chunk=1&version=1.5&folder_key=ueti9cij4zf3i&response_format=json").json()
  files = data['response']['folder_content']['files']
except requests.exceptions.RequestException:
  exit(f"{p}[{y}!{p}] {r}No Connection!{a}")

colors = lambda : random.choice([r,g,y,p,P,c,w])
logo = f"""{r}
██╗░░░██╗██╗██████╗░████████╗███████╗██╗░░██╗
██║░░░██║██║██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
╚██╗░██╔╝██║██████╔╝░░░██║░░░█████╗░░░╚███╔╝░
░╚████╔╝░██║██╔══██╗░░░██║░░░██╔══╝░░░██╔██╗░
░░╚██╔╝░░██║██║░░██║░░░██║░░░███████╗██╔╝╚██╗
░░░╚═╝░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝\n\n{p}╔══════════════════════════════════════╗\n║[{y}•{p}] {c}Author  : {g}Rio Dev                 {p}║\n║[{y}•{p}] {c}GitHub  : {w}github.com/riodev04     {p}║\n║[{y}•{p}] {c}Youtube : {y}youtube.com/@riodev    {p} ║\n║[{y}•{p}] {c}Python  : {colors()}{sys.version[0:6]}                 {p} ║\n║[{y}•{p}] {c}OS      : {colors()}{sys.platform}{' '*(23 - len(sys.platform))}{p} ║\n║[{y}•{p}] {c}Host    : {colors()}{socket.gethostname()}{' '*(24 - len(socket.gethostname()))}{p}║\n║[{y}•{p}] {c}Team    : {colors()}TERMUX {r}INDO{w}NESIA{p}        ║\n╚══════════════════════════════════════╝{a}"""

try:
  os.mkdir('virtex')
except FileExistsError:
  pass

def Moya(file):
   with requests.Session() as sesi:
     print (f"{p}[{y}!{p}] {y}Downloading {file['filename']}")
     a = sesi.get(file['links']['normal_download'])
     b = parser(a.content,'html.parser').find('a',class_ = 'popsok')['href']
     c = sesi.get(b).content
     d = os.path.join('virtex',file['filename'])
     e = os.open(d,os.O_CREAT | os.O_WRONLY)
     os.write(e,c)
     os.close(e)


def main():
  try:
    os.system ('clear')
    print (logo)
    print ("%sSELECT VIRTEX TYPE" % (g))
    print ("%s%s%s" % (c,'='*43,a))
    for khaneysia,rahmat in enumerate(files, start = 1):
      print (f"{p}[{r}{str(khaneysia).zfill(2)}{p}] {colors()}{os.path.splitext(rahmat['filename'])[0]}")
    print (f"{p}[{r}AL{p}] {c}DOWNLOAD ALL VIRTEX\n{p}[{r}BA{p}] {y}BACK TO MAIN MENU\n{p}[{r}EX{p}] {r}EXIT THE PROGRAM")
    echa = input("%s>>>> %s" % (g,c)).lower()
    if echa == 'al':
      with concurrent.futures.ThreadPoolExecutor(15) as executor:
        executor.map(Moya, files)
      shutil.make_archive('virtex-master','zip','virtex')
      print (f"{p}[{g}✓{p}] {g}Download Complete")
      exit (f"{p}[{g}✓{p}] {g}Download Results Saved In : {os.path.realpath('virtex')}")
    elif echa == 'ba':
      menu()
    elif echa == 'ex':
      os.abort()
    elif int(echa) in range(1,len(files) + 1):
      rahmet = files[int(echa) - 1]
      kntl = 0
      print (f"{p}[{y}!{p}] {y}Downloading {rahmet['filename']}")
      while True:
        try:
          ses = requests.Session()
          req = ses.get(rahmet['links']['normal_download'])
          res = parser(req.content,'html.parser')
          print (f"{p}[{y}✓{p}] {y}URL : {req.url}")
          print (f"{p}[{y}✓{p}] {y}Status : {req.status_code}")
          url = res.find('a',class_ = 'popsok')['href']
          path = os.path.join('virtex',rahmet['filename'])
          file = os.open(path,os.O_CREAT | os.O_WRONLY)
          txt = ses.get(url).content
          os.write(file,txt)
          os.close(file)
          byte = os.stat(path).st_size
          for b in ['B','KB','MB','GB','TB']:
            if byte < 1024.0:
              byte = "%3.2f %s" % (byte,b)
              break
            else:
              byte /= 1024.0
          print (f"{p}[{y}✓{p}] {g}File Name : {os.path.basename(path)}")
          print (f"{p}[{y}✓{p}] {g}File Size : {byte}")
          print (f"{p}[{y}✓{p}] {g}File Path : {os.path.realpath(path)}")
          show = input(f"{p}[{y}?{p}] {w}View Download Results [{g}Y/{w}{r}n{w}] {P}").lower() == 'y'
          if show:
            os.system (f"xdg-open --view virtex/'{rahmet['filename']}'")
          time.sleep(1)
          main()
          break
        except requests.exceptions.RequestException as su:
          kntl += 1
          if kntl >= 5:
            print (f"{p}[{y}!{p}] {y}Failed To Connect To Server\n\n\tTry :\n\t\t• Disable airplane mode\n\t\t• Turn on mobile data or Wi-Fi\n\t\t• Check the signal in your area{a}")
            break
          else:
            print (f"{p}[{y}!{p}] {y}Trying to Reconnect to the server")
            time.sleep(1.5)
    else:
      raise ValueError()

  except ValueError:
    print (f"{y}[!] Invalid Input!")
    time.sleep(1)
    main()

def menu():
  os.system('clear')
  print (logo)
  print (g + "MAIN COURSE")
  print ("%s%s" % (c,"="*37))
  print (f'{p}[{y}1{p}] {g}DOWNLOAD VIRTEX FILES\n{p}[{y}2{p}] {y}REPORT BUGS\n{p}[{y}3{p}] {y}ABOUT\n{p}[{y}0{p}] {r}EXIT')
  choice = input("%s>>> %s" % (y,c))
  if choice == '1' or choice == '01':
    main()
  elif choice == '2' or choice == '02':
    url = "https://wa.me/6285838762728"
    code = webbrowser.open(url)
    if code:
      time.sleep(0.9)
      menu()
    else:
      os.system ("xdg-open "+url)
      time.sleep(0.9)
      menu()
  elif choice == '3' or choice == '03':
    os.system('clear')
    print (f"{logo}\n{g}SCRIPT INFO\n========================\n{p}[{y}✓{p}] {c}Author: {g}Rio Dev\n{p}[{y}✓{p}] {c}Team  : {colors()}TERMUX {r}INDO{w}NESIA\n{p}[{y}✓{p}] {c}Script: {colors()}{os.path.basename(sys.argv[0])}\n{p}[{y}✓{p}] {c}Path  : {os.path.realpath(sys.argv[0])}\n{p}[{y}✓{p}] {c}Size  : {os.stat(os.path.realpath(sys.argv[0])).st_size} Byte\n{p}[{y}✓{p}] {c}Link  : {colors()}https://github.com/riodev04/Virtex\n{p}[{y}✓{p}] {c}Update: {colors()}{UPDATE}\n{p}[{y}✓{p}] {c}Versi : 1.1\n\n{g}Contact Me ^_^\n==================\n{p}[{y}✓{p}] {c}Github: {colors()}https://github.com/riodev04/\n{p}[{y}✓{p}] {c}Youtube : {colors()}https://www.youtube.com/@riodev\n{p}[{y}✓{p}] {c}WhatsApp : {colors()}+62 85838762728\n{p}[{y}✓{p}] {c}Email : {colors()}riodev2634@gmail.com\n{a}")
  elif choice == '00' or choice == '0':
    os.abort()
  else:
    print ("%s[!] Invalid Input!" % (y))
    time.sleep(0.9)
    menu()

if __name__ == "__main__":
  menu()
