from reportlab.pdfgen import canvas


def txt_to_pdf(txt_file, pdf_file):
    # 读取txt文件内容
    with open(txt_file, "r") as f:
        text = f.read()

    # 创建PDF文件
    c = canvas.Canvas(filename=pdf_file, pagesize=(58, 58))
    c.drawString(0, 10, text)  # 将txt内容写入PDF文件
    c.save()


# 指定txt和pdf文件路径
file_path = "./resource/test.txt"

pdf_file = "output.pdf"

# 调用函数将txt转换为pdf
txt_to_pdf(file_path, pdf_file)
