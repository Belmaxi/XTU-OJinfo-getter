import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Alignment

class XlsxExport:

    def __init__(self, _name = "Untitled.xlsx") -> None:
        self.xlsx_name = _name

    def export(self,info) -> None:
        print(f"======================")
        print("正在导出excel")
        with pd.ExcelWriter(self.xlsx_name) as writer:
            for i in info:
                i[0] = pd.DataFrame(i[0])
                i[0].to_excel(writer, sheet_name=i[1], index=False)

    def set_style(self) -> None:
        wb = load_workbook(self.xlsx_name)

        for ws in wb._sheets:
            ws.column_dimensions['C'].width = 20.0  # 调整列A宽
            ws.column_dimensions['D'].width = 30.0

        wb.save(self.xlsx_name)
