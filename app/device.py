import win32print
import win32ui


def send_to_printer(text, paper_width_mm=58):
    printer_name = win32print.GetDefaultPrinter()  # 获取默认打印机
    hPrinter = win32print.OpenPrinter(printer_name)
    try:
        # 创建一个打印作业
        hDC = win32ui.CreateDC()
        hDC.CreatePrinterDC(printer_name)
        hDC.StartDoc("Python Print Job")
        hDC.StartPage()

        # 设置字体和文本位置
        font = win32ui.CreateFont(
            {
                "name": "Arial",
                "height": 50,
            }
        )
        printer_ppi = 180
        hDC.SelectObject(font)
        paper_width_pixels = int((paper_width_mm / 25.4) * printer_ppi)

        # 自动换行处理
        lines = []
        # line = ""
        # for word in text.split():
        #     # 尝试添加下一个单词
        #     test_line = f"{line} {word}".strip()
        #     # 测量当前行宽度
        #     if hDC.GetTextExtent(test_line)[0] <= paper_width_pixels:
        #         line = test_line
        #     else:
        #         # 当前行已满，添加到行列表并重置当前行
        #         lines.append(line)
        #         line = word
        #     lines.append(line)  # 添加最后一行

        # 打印行
        cur_line = ""
        for c in text:
            if hDC.GetTextExtent(cur_line + c)[0] > paper_width_pixels:
                lines.append(cur_line)
                cur_line = c
            else:
                cur_line += c
        if cur_line != "":
            lines.append(cur_line)
        y = 0
        for line in lines:
            hDC.TextOut(0, y, line)
            y += hDC.GetTextExtent(line)[1]  # 行高
        hDC.EndPage()
        hDC.EndDoc()
    finally:
        win32print.ClosePrinter(hPrinter)


if __name__ == "__main__":
    send_to_printer("你好，世界！这是一个打印示例。")
