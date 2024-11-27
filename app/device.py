from pprint import pprint

import cups

conn = cups.Connection()
printer_name = "Printer_USB_Printer_P"


def test():
    printers = conn.getPrinters()
    # 获取所有可用打印机
    for idx, printer in enumerate(printers):
        print(f"可使用的打印机{idx+1}号:{printer}")


if __name__ == "__main__":

    file_path = "./output.pdf"
    job_id = conn.printFile(
        printer_name,
        file_path,
        "Test Print Job",
        {},
    )
    print(job_id)
    print("打印完成")

    test()
    # conn.cancelAllJobs(printer_name)
    pass
