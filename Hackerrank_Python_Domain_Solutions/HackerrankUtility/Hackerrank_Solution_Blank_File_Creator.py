"""
Title     : Hackerrank_Solution_Blank_File_Creator
Subdomain : None
Domain    : None
Author    : Ahmedur Rahman Shovon
Created   : 12 July 2017
"""
import datetime
import os
import re
import sys

extension = ".py"
domain = "Python"
author = "Ahmedur Rahman Shovon"
created_date = datetime.datetime.today().strftime("%d %B %Y")
info_file_name = "python_info.txt"


def valid_name(given_name):
    return re.sub(r"[^\w]", "", given_name)


def write_file_header(title, subdomain):
    header_str = "'''\n"
    header_str += "Title     : " + title + "\n"
    header_str += "Subdomain : " + subdomain + "\n"
    header_str += "Domain    : " + domain + "\n"
    header_str += "Author    : " + author + "\n"
    header_str += "Created   : " + created_date + "\n"
    header_str += "'''\n"
    return header_str


problem_list = ""
subdomain_name = ""

info_file = open(info_file_name, "r")
info_file_lines = info_file.readlines()
info_file.close()
for line in info_file_lines:
    line = line.strip()
    if line == "":
        continue
    elif line[0] == "[":
        problem_list = line
    else:
        subdomain_name = line
    if subdomain_name != "" and problem_list != "":
        folder_name = valid_name(subdomain_name)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        title_ar = re.findall(r'("[^"]*")', problem_list)
        title_ar_len = len(title_ar)

        for title in title_ar:
            file_header_str = write_file_header(title[1:-1], subdomain_name)
            title_valid = valid_name(title)
            f = open(folder_name + "\\" + title_valid + extension, "w")
            f.write(file_header_str)
            f.close()

        print("Folder: " + str(folder_name) + ". Total files: " + str(title_ar_len))
        subdomain_name = ""
        problem_list = ""
