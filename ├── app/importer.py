from openpyxl import load_workbook


class ExcelImporter:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        workbook = load_workbook(self.filename, data_only=True)
        return workbook
