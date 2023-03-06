from fpdf import FPDF
import pandas

pdf = FPDF(orientation='p', unit='mm', format='A4')   # orientation, p:portrait纵向 l:landscape横向; unit:画图时尺寸单位
pdf.set_auto_page_break(auto=False, margin=0)  # 关闭自动换页

data = pandas.read_csv("topics.csv", sep=',')
r = 0
g = 0
b = 0

for index, row in data.iterrows():
    topic = row['Topic']
    pages = int(row['Pages'])

    for i in range(pages):
        pdf.add_page()
        # 改变每一页的text颜色
        r = r + 5
        g = g + 2
        b = b + 1
        # 设置页头text字体样式
        pdf.set_font(family="Times", style='B', size=20)
        # 设置页头text的颜色
        pdf.set_text_color(r, g, b)
        # 设置text内容
        pdf.cell(w=0, h=25, txt=topic, ln=1)  # (单位像素) border:0无边框1有边框 w:边框宽度 ln:0下一行不换行1换行
        # 打印一条横线
        pdf.line(10, 27, 200, 27)
        # 打印占278mm高的blank lines
        pdf.ln(240)
        # 设置页脚text字体样式
        pdf.set_font(family="Times", style='I', size=10)
        # 设置页脚内容
        pdf.cell(w=0, h=25, txt=f"{topic},{str(i+1)}", ln=1, align='R')  # (单位像素) border:0无边框1有边框 w:边框宽度 ln:0下一行不换行1换行

pdf.output("result.pdf")
