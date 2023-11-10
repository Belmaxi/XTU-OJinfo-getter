# -*- coding:utf-8 -*-
# @Author : Belmaxi

from utils.autoload_required import check_pack
import os
from utils.parser import Parser
import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Alignment
#自动安装依赖

url = "https://acm.xtu.edu.cn/exam/index.php/solution/stat/cids/409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430"
urls = [
    [
        f"https://acm.xtu.edu.cn/exam/index.php/solution/stat/order/{i[0]}/cids/409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430",
        i[1]] for i in [[1, "班级"], [2, "专业"], [3, "学号"]]
]


check_pack()

print("========正在爬取总表=======")
parser = Parser(url)
res = [["总数", pd.DataFrame(parser.get_all_standing())]]
for i in urls:
    print(f"========正在爬取{i[1]}顺序表=======")
    parser = Parser(i[0])
    res.append([i[1], pd.DataFrame(parser.get_all_standing())])

print(f"======================")
print("正在导出excel")
input("press any to continue...")
with pd.ExcelWriter('standing.xlsx') as writer:
    for i in res:
        i[1].to_excel(writer, sheet_name=i[0], index=False)

wb = load_workbook('standing.xlsx')

for ws in wb._sheets:
    ws.column_dimensions['C'].width = 20.0  # 调整列A宽
    ws.column_dimensions['D'].width = 30.0

wb.save("standing.xlsx")

print("导出完成")
input("press any to continue...")
print("================================")
input("press any to continue...")