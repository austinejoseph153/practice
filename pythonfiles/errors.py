import subprocess,platform
import requests,os,re,sys,csv
import browserhistory as bh
import socket,ipaddress,device_detector,datetime
from ip2geotools.databases.noncommercial import DbIpCity
import socket
from pathlib import Path

host = socket.gethostname()
ip = socket.gethostbyname(host)
# print(socket.getservbyname("www.google.com",80))
def get_location(ip):
    ip_address = ip
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    # location_data = {
    #     "ip": ip_address,
    #     "city": response.get("city"),
    #     "region": response.get("region"),
    #     "country": response.get("country_name")
    # }
    return response
# print(get_location(socket.gethostbyname("www.bsum.edu.ng")))

def main():
    # new_datas = []
    datas = subprocess.check_output(["ipconfig"]).decode("utf-8").split("\n")
    for data in datas:
        # if "IPv4 Address" in data:
        print(data)
    # # print(new_datas)
# main()

def get_wifi_password():
    data = subprocess.check_output(["netsh","wlan","show","profiles"]).decode("utf-8",errors="backslashreplace").split("\n")
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        try:
            results = subprocess.check_output(["netsh","wlan","show","profiles",i,"key=clear"]).decode("utf-8",errors="backslashreplace").split("\n")
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print("{:<30}| {:<}".format(i,results[0]))
            except IndexError:
                print("{:<30}| {:<}".format(i,""))
        except subprocess.CalledProcessError:
            print("{:<30}| {:<}".format(i,"ENCODING ERROR"))
get_wifi_password()

def get_device_name():
    # getting the system name
    s_hostname = socket.gethostname()
    p_hostname = platform.node()
    l_hostname = platform.uname().node
    x_name = socket.getfqdn()
    # windows version
    window_version = platform.platform()
    # operating system name
    os_sysytem_name = platform.system() #platform.uname().system
    # release 
    release = platform.release()
    # windows version
    version = platform.version()
    # processor
    processor = platform.processor()
    # architecture
    architecture = platform.machine()
    # get the system encoding
    encoding = sys.getfilesystemencoding()
    encoding = sys.getdefaultencoding()
    return{
        "s_name":s_hostname,
        "p_name":p_hostname,
        "l_name":l_hostname
    }
# print(get_device_name())
# ua = "Mozilla/5.0 (Linux; Android 6.0; 4Good Light A103 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36"
# device = device_detector.DeviceDetector(ua).parse()
# print(device.is_desktop())
def get_last_visted_sites_and_their_ips():
    data = subprocess.check_output(["ipconfig","/displaydns"]).decode("utf-8",errors="backslashreplace").split("\n")
    data = [x.split(":") for x in data if "Record Name" in x ]
    print(data)

def write_to_a_csv_file():
    field_names = ["name","age","country"]
    rows = [["austine",12,"nigeria"],
            ["sarah",23,"australia"],
            ["paul",34,"germany"],
            ["gabriel",43,"europe"]
            ]
    rows_2 = [
        {
            "name":"samuel",
            "age":56,
            "country":"tanzania"
        },
        {
            "name":"gift",
            "age":42,
            "country":"Russia"
        },
        {
            "name":"deborah",
            "age":19,
            "country":"liberia"
        },
        {
            "name":"victor",
            "age":24,
            "country":"ukraine"
        }
    ]
    # with open("student_data.csv","w") as csvfile:
    #     csv_writer = csv.writer(csvfile)
    #     csv_writer.writerow(field_names)
    #     csv_writer.writerows(rows)
    
    with open("student_data.csv","a") as csvfile:
        csv_writer = csv.DictWriter(csvfile,fieldnames=field_names)
        # csv_writer.writerow(field_names)
        # csv_writer.writeheader()
        if os.path.getsize("student_data.csv") == 0:
            csv_writer.writerows(rows_2)

# write_to_a_csv_file()
# rows = []
# with open("student_data.csv","r") as csvfile:
#     csv_reader = csv.DictReader(csvfile)
#     # csv_writer.writerow(field_names)
#     for row in csv_reader:
#         if row:
#             rows.append(row)
# print(rows)

def list_files_in_directories(dirname):
    pass
# print(os.listdir("C:\windows\system32\config"))
root_dir = "C:\windows\system32\config"
output = os.scandir(root_dir)
num_dir = 0
num_files = 0
files = []
total = 0
for x in output:
    total+= 1
    if os.path.isdir(os.path.join(root_dir,x)):
        num_dir+= 1
    elif os.path.isfile(os.path.join(root_dir,x)):
        num_files+=1
        files.append(x)
print(f"number of dir: {num_dir}")
print(f"number of files: {num_files}")
# print(total)
# print(files)

def generate_date_range(start_year,end_year=datetime.date.today().strftime("%Y")):
    error_message = "success"
    dates = []
    try:
        start_year = int(start_year)
        end_year = int(end_year)
    except ValueError:
        error_message = "start and end year must be valid integers"
        return {
            "message":error_message,
            "data":dates
        }
    if len(str(start_year)) != 4 or len(str(end_year)) != 4:
        error_message = "year length cannot be greater or less than four"
    elif start_year > end_year:
        error_message = "start year cannot be greater than end year"
    else:
        for x in range(start_year,end_year+1):
            if x == end_year+1:
                break
            dates.append(x)
            x+=1
    return {
        "message":error_message,
        "data":dates
    }
# print(generate_date_range("2012"))
new_date = datetime.datetime.today()
current_date = datetime.datetime.strptime("1995-08-25","%Y-%m-%d")
# print(new_date - current_date)

# print(os.path.isdir("C:\windows\system32\config"))

def access_files():
    host_url = "http://127.0.0.1:8000/themeforest/html/"
    response = requests.get(host_url+"hotel-list.html")
    soup = BeautifulSoup(response.content,"html.parser")
    page_name = response.url.split("/")[-1]
    webContent = response.content
    # with open("index.html","wb") as file:
    #     file.write(webContent)
    
    # menus = soup.find_all("div",{"class":"hotel-item"})
    # for menu in menus:
    #     image_path = host_url + menu.find("img")["src"]
    #     image_name = str(menu.find("img")["src"]).split("/")[-1]
    #     title = menu.find("div",{"class":"hotel-name"}).find("a").text
    #     places = menu.find("div",{"class":"hotel-places"})
    #     print(title)
    links = soup.find("head").find_all("link")
    for link in links:
        if not str(link["href"]).startswith("http://") and not str(link["href"]).startswith("https://"):
            css_response = requests.get(host_url+link["href"])
            if css_response.status_code == 200:
                file_name = css_response.url.split("/")[-1]
                file_path = "/".join(str(link["href"]).split("/")[:-1])
                print(file_path)
                # try:
                #     with open("new-css/"+file_name,"wb") as file:
                #         file.write(css_response.content)
                # except FileNotFoundError:
                #     os.mkdir("new-css")
                #     access_files()
