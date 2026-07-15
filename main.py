from app.importer import ExcelImporter


def main():
    print("===================================")
    print(" Park&Rent Scheduler")
    print(" Connecteam Converter")
    print("===================================\n")

    excel_file = "sample/2026.02.xlsx"

    importer = ExcelImporter(excel_file)
    workbook = importer.load()

    print("Excel sikeresen betöltve!")
    print("Munkalapok:")

    for sheet in workbook.sheetnames:
        print(f" - {sheet}")


if __name__ == "__main__":
    main()
