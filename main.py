from fpdf import FPDF
import pandas


# 设置pdf方向、画图单位、大小等参数
# orientation, p:portrait纵向 l:landscape横向; unit:尺寸单位
pdf = FPDF(orientation='p', unit='mm', format='A4')
# 关闭自动换页
pdf.set_auto_page_break(auto=False, margin=0)

# 读取csv文件
data = pandas.read_csv("topics.csv", sep=',')
r, g, b = (0, 0, 0)

#  将读取到的数据写入pdf
for index, row in data.iterrows():
    topic = row['Topic']
    pages = int(row['Pages'])

    # 设置每一类topic的pdf页面
    for i in range(pages):
        pdf.add_page()

        # 改变每一页的text颜色
        r = r + 5
        g = g + 2

        # 设置页头text字体样式
        pdf.set_font(family="Times", style='B', size=20)
        # 设置页头、页脚text的颜色
        pdf.set_text_color(r, g, b)
        # 设置页头text内容
        # (单位像素) border:0无边框1有边框 w:边框宽度 ln:0下一行不换行1换行
        pdf.cell(w=0, h=25, txt=topic, ln=1)

        # 打印页面中的横线
        for y in range(27, 280, 12):
            pdf.line(10, y, 200, y)

        # 打印占240mm高的blank lines
        pdf.ln(240)

        # 设置页脚text字体样式
        pdf.set_font(family="Times", style='I', size=10)
        # 设置页脚内容
        # (单位像素) border:0无边框1有边框 w:边框宽度 ln:0下一行不换行1换行
        pdf.cell(w=0, h=25, txt=f"{topic},{str(i+1)}", ln=1, align='R')

# 打印pdf
pdf.output("result.pdf")
