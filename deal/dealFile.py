#coding:utf8
'''
Created on 2016-4-24

@author: 浮生若梦
'''

from bs4 import BeautifulSoup
import os


html_cont = open("output_weibo_cont.html","r").read()
soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
trs = soup.findAll("tr")
length = len(trs)
boot_dir = "E:/python_file/"
userCount = 1
for tr in trs:
    tds = tr.findAll("td")
    i = 0
    name = ""
    time = ""
    cont = ""
    for td in tds:
        i = i + 1
        if i == 2:
            name = td.get_text().strip().decode("utf8")
        if i == 3:
            time = td.get_text().decode("utf8")
        if i == 4:
            cont = td.get_text().decode("utf8")
    dir_name = (boot_dir+name)
    if os.path.exists(dir_name):
        file_out = open(dir_name+"/"+name+"_"+str(userCount)+".html","w")
        file_out.write("<html>\n")
        file_out.write("<head><meta http-equiv='Content-Type' content='text/html; charset=utf-8'/></head>\n")
        file_out.write("<body>\n")
        file_out.write(cont)
        file_out.write("</body>\n")
        file_out.write("</html>")
        file_out.close()
        userCount = userCount + 1
    else:
        userCount = 1
        os.makedirs(dir_name)
        file_out = open(dir_name+"/"+name+"_"+str(userCount)+".html","w")
        file_out.write("<html>\n")
        file_out.write("<head><meta http-equiv='Content-Type' content='text/html; charset=utf-8'/></head>\n")
        file_out.write("<body>\n")
        file_out.write(cont)
        file_out.write("</body>\n")
        file_out.write("</html>")
        file_out.close()
        userCount = userCount + 1









