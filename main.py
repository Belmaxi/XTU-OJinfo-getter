# -*- coding:utf-8 -*-
# @Author : Belmaxi

from utils.autoload_required import check_pack
from utils.parser import Parser
from export.xlsx_exporter import XlsxExport
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
        parser = Parser(url)
        print(f"========正在爬取{i}信息=======")

        info = parser.get_all_standing()
        res.append([info, i])

file.close()


exporter.export(res)
exporter.set_style()
print("\033[92m导出完成\033[0m")
print("================================")
input("press any to continue...")