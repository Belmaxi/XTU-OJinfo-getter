# -*- coding:utf-8 -*-
# @Author : Belmaxi

from utils.autoload_required import check_pack
import os
from utils.parser import Parser
import requests
from bs4 import BeautifulSoup
from export.xlsx_exporter import XlsxExport
import pandas as pd
#自动安装依赖
check_pack()

exporter = XlsxExport("standing.xlsx")
idx2tit = ["总表","班级","专业","学号"]

urls = []
res = []
file = open("urls","r")
for i in idx2tit:
    try:
        url = file.readline()
    except Exception:
        break
    if len(url) > 4:
        # urls.append([url,i])
        parser = Parser(url)
        print(f"========正在爬取{i}信息=======")

        info = parser.get_all_standing()
        res.append([info, i])

file.close()

print(f"======================")
print("正在导出excel")
exporter.export(res,)
exporter.set_style()
print("导出完成")
print("================================")
input("press any to continue...")