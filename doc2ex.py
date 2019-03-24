import os
import os.path
from win32com import client as wc

c = []

i = "E:\\bd\\caozuo\\stu\\ch" # 以该路径为实验


def txt(j, c):
    word = wc.Dispatch('Word.Application')

    doc = word.Documents.Open(c[j])

    newname = c[j][:-5] + "（translate txt)"

    doc.SaveAs(newname, 4)

    doc.Close()

    word.Quit()

    os.remove(c[j])

    print("完成")


def wordt(c):  # 定义函数，进行筛选

    for j in range(0, len(c)):

        if c[j][-5:] == ".docx":  # 寻找docx文件

            txt(j, c)  #

        else:
            pass


for parent, dirnames, filenames in os.walk(i):

        for filename in filenames:
            c.append(os.path.join(parent, filename))

wordt(c)