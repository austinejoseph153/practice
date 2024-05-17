import requests
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import os
import json
from pathlib import Path

class WebpageDownload():

    def __init__(self, base_url, base_dir):
        self.base_url = base_url
        self.base_dir = base_dir

    def get_base_dir(self, path=None):
        if path:
            return f"{self.base_dir}/{path}/"
        else:
            return f"{self.base_dir}/"
    
    def get_absolute_url(self, file_dir, file_name):
        if not file_dir.startswith("/"):
            return f"{self.base_url}/{file_dir}/{file_name}"
        else:
            return f"{self.base_url}{file_dir}/{file_name}"
    
    def parse_html_page(self, content):
        soup = BeautifulSoup(content, "html.parser")
        return soup

    # return active urls from a list of urls
    def filter_active_urls(self, urls):
        pages_urls = []
        for url in urls:
            response = requests.get(f"{self.base_url}{url}")
            if response.status_code == 200:
                pages_urls.append(url)
        return pages_urls
    
    # save the datas to a file
    def save_to_file(self, datas, path, filename):
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path+"/"+filename,"w") as file:
            json.dump(datas, file, indent=6)
    
    def get_page_list_object(self, urls):
        pages_urls = []
        for url in urls:
            relPath = f"{self.base_url}{url}"
            if url.endswith(".html") and not url.startswith("/"):
                relPath = f"{self.base_url}/{url}"
            pages_urls.append({url:relPath})
        return pages_urls
    
    def get_pages_url(self):
        page_list = []
        response = requests.get(f"{self.base_url}")
        if response.status_code == 200:
            soup = self.parse_html_page(response.content)
            a_tags = soup.findAll("a")
            for a in a_tags:
                try:
                    if a["href"].startswith("/") or a["href"].endswith(".html"):
                            absolute_path = a["href"]
                            if absolute_path not in page_list:
                                page_list.append(absolute_path)
                except KeyError:
                    continue
            pages_urls = self.get_page_list_object(page_list)
            base_dir = self.get_base_dir("fixtures")
            self.save_to_file(pages_urls, base_dir, "themeforest.json")
            return pages_urls

    # download media files to local machine
    def download_media_files(self, files):
        for file in files:
            file_url = file["file_url"]
            filename = file["filename"]
            file_dir = file["file_dir"]
            path = self.get_base_dir(file_dir)
            full_path = path+filename 
            if not os.path.exists(full_path):
                response = requests.get(file_url)
                if response.status_code == 200:   
                    content = response.content
                    if not os.path.exists(path):
                        os.makedirs(path)
                    with open(full_path,"wb") as file_path:
                        file_path.write(content)
        
    def get_all_css_files(self):
        css_files = []
        response = requests.get(f"{self.base_url}")
        if response.status_code == 200:
            soup = self.parse_html_page(response.content)
            links = soup.find_all("link")
            for link in links:
                data = {}
                if link["rel"] == ['stylesheet'] and not link["href"].startswith("http"):
                    file_name = str(link["href"]).split("/")[-1]
                    file_dir = "/".join(str(link["href"]).split("/")[:-1])
                    file_url = self.get_absolute_url(file_dir, file_name)
                    data["filename"] = file_name
                    data["file_dir"] = file_dir
                    data["file_url"] = file_url
                    if not data in css_files:
                        css_files.append(data)
            self.download_media_files(css_files)
    
    def get_all_js_files(self):
        js_files = []
        response = requests.get(f"{self.base_url}")
        if response.status_code == 200:
            soup = self.parse_html_page(response.content)
            scripts = soup.find_all("script")
            for script in scripts:
                data = {}
                try:
                    if not script["src"].startswith("http"):
                        file_name = str(script["src"]).split("/")[-1]
                        file_dir = "/".join(str(script["src"]).split("/")[:-1])
                        file_url = self.get_absolute_url(file_dir, file_name)
                        data["filename"] = file_name
                        data["file_dir"] = file_dir
                        data["file_url"] = file_url
                        if not data in js_files:
                            js_files.append(data)
                except KeyError:
                    continue
            self.download_media_files(js_files)
    
    def get_all_images(self):
        images_list = []
        pages = self.get_pages_url()
        for page in pages:
            for v in page.values():
                response = requests.get(v)
                if response.status_code == 200:
                    soup = self.parse_html_page(response.content)
                    images = soup.find_all("img")
                    for image in images:
                        data = {}
                        file_name = str(image["src"]).split("/")[-1]
                        file_dir = "/".join(str(image["src"]).split("/")[:-1])
                        file_url = self.get_absolute_url(file_dir, file_name)
                        data["filename"] = file_name
                        data["file_dir"] = file_dir
                        data["file_url"] = file_url
                        if not data in images_list:
                            images_list.append(data)
                            
            self.download_media_files(images_list)

    def get_all_html_page(self):
        pages = self.get_pages_url()
        path = self.get_base_dir()
        if not os.path.exists(path):
            os.makedirs(path)
        for page in pages:
            for k, v in page.items():
                if not k.endswith(".html"):
                    filename = str(k).split("/")[-1]+".html"
                    if k == "/":
                        filename="index.html"
                else:
                    filename = str(k).split("/")[-1]
                full_path = path+filename
                if not os.path.exists(full_path):
                    response = requests.get(v)
                    if response.status_code == 200:
                        webcontent = response.content
                        try:
                            with open(full_path, "wb") as file:
                                file.write(webcontent)
                        except:
                            continue
    
# page_download = WebpageDownload("https://swigo.w3itexpert.com","travels")
# page_download = WebpageDownload("https://validthemes.net/site-template/recafe","restaurants")
# page_download = WebpageDownload("https://demo.themeregion.com/playbit","music-1")
# page_download = WebpageDownload("http://preview.enroutedigitallab.com/html/beats/","music-2")
page_download = WebpageDownload("https://pixio.dexignzone.com/xhtml/index-3.html","portfolio")
# page_download.get_all_html_page()
