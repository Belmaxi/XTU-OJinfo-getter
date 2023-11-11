# -*- coding:utf-8 -*-
# @Author : Belmaxi

from utils.autoload_required import check_pack
from utils.parser import Parser
from export.xlsx_exporter import XlsxExport
from utils.printer import Printer

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
        Printer.console_print_warning(f"========正在爬取{i}信息=======")

        info = parser.get_all_standing()
        res.append([info, i])

file.close()

exporter.export(res)
exporter.set_style()
Printer.console_print_success("导出完成")
Printer.console_print_success("================================")
input("press any to continue...")