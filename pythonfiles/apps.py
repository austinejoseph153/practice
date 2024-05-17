import socket,ipaddress,device_detector,datetime
from ip2geotools.databases.noncommercial import DbIpCity
import socket,subprocess
import requests,os
from bs4 import BeautifulSoup


# response = requests.get("http://127.0.0.1:8000/desmond/")
# contents = response.content
# print(contents)
# print(socket.gethostbyaddr("192.168.40.67"))
# print(socket.gethostbyname(socket.gethostname()))
# results = subprocess.check_output(["hostname"]).decode("utf-8").split()
# # print(results)
# for x in os.popen("arp -a"): print(x) 

def scan_open_ports():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(20)
    conn = sock.connect_ex(("3.232.162.172"))
    print(conn)
# scan_open_ports()
# print(socket.gethostbyname("www.shorexc.com"))