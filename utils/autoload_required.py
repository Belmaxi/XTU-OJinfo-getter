import pip
import os
pack_list = ["requests", "bs4", "pandas"]

def check_pack():
    print("正在检查依赖")
    try:
        import requests
        import bs4
        import pandas
    except ImportError:
        pip.main(["install","requests","bs4","pandas"])

if __name__ == "__main__":
    check_pack()