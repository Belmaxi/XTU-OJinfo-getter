import requests
from bs4 import BeautifulSoup

class Parser:

    def __init__(self,url):
        self.url = url

    # 解析url,返回html文本
    def _get_single_html(self):
        headers = {
            "cookie": "PHPSESSID=afpg8s9ni96hs03p0jmde9lgb7; think_template=default",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"
        }
        resp = requests.get(self.url, headers=headers)
        if resp.status_code == 200:
            return resp.text
        else:
            return None


    # 将一行信息解析，返回二维列表，[[”“,info],[]]
    # 排名 姓名 学号 班级 题单...
    def _parse_info(self, info, header):
        res = list(map(lambda x: [x], header))

        _id = (info[1].find("span", style="font-size:9px").get_text())[1:13]
        name = info[1].find("span", style="font-size:13px;color:#FF851B").get_text()
        _class = (info[1].find("span", style="font-size:9px").get_text())[13:]

        res[0] = ["排名", info[0].get_text()]
        res[1].append(name)
        res[2].append(_id)
        res[3].append(_class)

        for i in range(4,len(header)):
            res[i].append(info[i-2].get_text())

        return res


    def get_all_standing(self):
        html = self._get_single_html()
        soup = BeautifulSoup(html, "html.parser")
        standing = (
            soup.find("div", id="content")
            .find("table", id="standing")
            .find_all("tr")
        )
        head = standing[0].find_all("th")
        # 使用原表头
        lst = list(map(lambda x: x.get_text(), head))

        del lst[1]
        lst.insert(1, "班级")
        lst.insert(1, "学号")
        lst.insert(1, "姓名")

        excel_info = []
        for std in standing[1:]:
            info = std.find_all("td")
            parsed_info = self._parse_info(info, lst)
            if parsed_info[2][1][0:4] != "2023":
                continue
            dic = {}
            for i in parsed_info:
                dic[i[0]] = i[1]

            excel_info.append(dic)
        return excel_info
