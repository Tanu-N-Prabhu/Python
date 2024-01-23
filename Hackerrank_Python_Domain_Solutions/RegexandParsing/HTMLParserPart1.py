"""
Title     : HTML Parser - Part 1
Subdomain : Regex and Parsing
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/html-parser-part-1/problem
"""
from html.parser import HTMLParser


class CustomHTMLParser(HTMLParser):
    def handle_attr(self, attrs):
        for attr_val_tuple in attrs:
            print("->", attr_val_tuple[0], ">", attr_val_tuple[1])

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        self.handle_attr(attrs)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        self.handle_attr(attrs)


parser = CustomHTMLParser()

n = int(input())

s = "".join(input() for _ in range(n))
parser.feed(s)

"""
2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
"""
