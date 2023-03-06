from fpdf import FPDF
import pandas

pdf = FPDF(orientation='p', unit='mm', format='A4')   # orientation, p:portrait纵向 l:landscape横向; unit:画图时尺寸单位

data = pandas.read_csv("topics.csv", sep=',')

for index, row in data.iterrows():
    topic = row['Topic']
    pages = int(row['Pages'])

    while pages > 0:
        pdf.add_page()
        pdf.set_font(family="Times", style='B', size=15)
        pdf.set_text_color(50, 132, 86)
        pdf.cell(w=0, h=25, txt=topic, ln=1)  # (单位像素) border:0无边框1有边框 w:边框宽度 ln:0下一行不换行1换行
        pdf.line(10, 30, 200, 30)

        pages = pages - 1


pdf.output("result.pdf")
