import sys
import os
from datetime import datetime


def addToClipBoard(text):
    command = 'echo "' + text.strip() + '"| clip'
    os.system(command)


def fmt_1():
    print('start.')
    sep = input("input separator?")
    sep = ',' if not len(sep) else sep
    needDelim = (input("need delimiter?(y/n)") == "y")
    print('\nstart input, press "Ctrl+Z","Enter" to end input.')
    print('-----------------')

    lines = sys.stdin.readlines()
    print('-----------------')
    lines = [l.strip('\n') for l in lines]
    if needDelim:
        lines = ["'{0}'".format(l) for l in lines]
    outputstr = sep.join(lines)
    print('\t'+outputstr)
    try:
        addToClipBoard(outputstr)
        print('Copied.')
    except Exception:
        print('Exception.')


def fmt_2():
    print("start")
    keystr = input()
    valstr = input()

    ls_key = keystr.split("\t")
    ls_val = valstr.split("\t")

    output_dict = dict(zip(ls_key, ls_val))
    print(repr(output_dict).replace("'", '"'))


def others():
    print("Invalid choice")


def fmt_3():
    print('\nstart input, press "Ctrl+Z","Enter" to end input.')
    lines = sys.stdin.readlines()
    hasHead = False
    headhtml = ""
    bodyhtml = ""
    for i in range(0, len(lines)):
        line = lines[i]
        if i == 0 and not str(line[0]).isdigit():
            hasHead = True
            headhtml += "<thead><tr>"
            line = line.split('\t')
            for cell in line:
                headhtml += "<th>{0}</th>".format(cell)
            headhtml += "</tr></thead>"
        else:
            bodyhtml += "<tr>"
            line = line.split('\t')
            for cell in line:
                if "http" in cell:
                    cell = '<a href="{0}" target="_blank">{0}</a>'.format(cell)
                bodyhtml += "<td>{0}</td>".format(cell)
            bodyhtml += "</tr>"
    html = "<table>" + (headhtml if hasHead else "") + "<tbody>"+bodyhtml + "</tbody></table>"
    html = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body><h1>{0}</h1>{1}</body></html>'.format(
        datetime.now().strftime("%Y/%m/%d %H:%M"), html)
    f_dst = open(r"D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\Desktop\test.html", 'w+', encoding="utf-8")
    print(html, file=f_dst)
    f_dst.close()
    os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" file:///D:/BingWei/OneDrive%20-%20stu.sbs.edu.cn/illuminera/Desktop/test.html')


if __name__ == "__main__":
    choice = input("format who?")
    switch = {
        "1": fmt_1,
        "2": fmt_2,
        "3": fmt_3
    }
    if choice in switch.keys():
        switch[choice]()
    else:
        others()
    print('\nend.')
    os.system('pause')
