from fpdf import FPDF
import pandas

pdf = FPDF(orientation='p', unit='mm', format='A4')   # orientation, p:portrait纵向 l:landscape横向; unit:画图时尺寸单位

data = pandas.read_csv("topics.csv", sep=',')
r = 0
g = 0
b = 0
for index, row in data.iterrows():
    topic = row['Topic']
    pages = int(row['Pages'])

    for i in range(pages):
        pdf.add_page()
        r = r + 5
        g = g + 2
        b = b + 1
        pdf.set_font(family="Times", style='B', size=20)
        pdf.set_text_color(r, g, b)
        pdf.cell(w=0, h=25, txt=topic, ln=1)  # (单位像素) border:0无边框1有边框 w:边框宽度 ln:0下一行不换行1换行
        pdf.line(10, 27, 200, 27)


pdf.output("result.pdf")
