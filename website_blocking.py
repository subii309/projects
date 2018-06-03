from datetime import datetime
import time
host_path = r'C:\Windows\System32\drivers\etc'
tmp_host_path = r'C:\Users\hp\Desktop\hosts'


redirect = '127.0.0.1'

websites_list = ['facebook.com','www.facebook.com','twitter.com','www.twitter.com']

datetimeinf = datetime.now()
datetimeinf = datetime(2018, 5 , 6, 10)

#print(datetime(datetime.now().year, datetime.now().month(), datetime.now().day, 12))

while True:
    if datetime(datetime.now().year, datetime.now().month, datetime.now().day, 12) < datetimeinf < datetime(datetime.now().year, datetime.now().month, datetime.now().day, 16):
        fileobj = open(tmp_host_path,'r+')
        content = fileobj.read()
        fileobj.close()
        for websites in websites_list :
            if websites in content:
                pass
            else :
                fileobj = open(tmp_host_path,'a')
                fileobj.write(redirect+' '+websites+'\n')
                fileobj.close()
        print('blocking hours')
    else :
        fileobj = open(tmp_host_path,'r+')
        content = fileobj.readlines()
        fileobj.seek(0)
        for line in content:
            if not any(website in line for website in websites_list):
                fileobj.write(line)
        fileobj.truncate()
        print('fun hours')
    time.sleep(5)

