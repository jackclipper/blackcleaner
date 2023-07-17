

'''
choose one or more
if one:
    input the picture

    choose show them up or not
    Y/N

    choose location up&down or left&right
    do it!

if more:
    input the picture

    choose show them up or not
    Y/N

    choose location all in same or different:

    if all in same:
        choose location up&down or left&right
        do it!

    if all in different:
        for each one:
            use the (if one) code
'''
from PIL import Image
import ctypes, sys, time
import tkinter as tk
from tkinter import filedialog
from pathlib import Path


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    

def single_process():
    print("请选择单个文件:\n")
    root=tk.Tk()
    root.withdraw()
    file_path=Path(filedialog.askopenfilename())#获取文件路径

    image=Image.open(str(file_path))
    size=image.size#获取图像尺寸
    if int(input("\n单击页面以继续……\n\n请选择图片黑色部分的位置：\n1.上下两侧\n2.左右两侧\n"))==1:
        print("请稍等……\n")
        y=0
        for i in range(1,size[1]//2+1):
            if image.getpixel((1,i))!=(0,0,0):
                y=i
                break
        temp=image.crop((0,y+1,size[0],size[1]-y-1))
        temp.save(str(file_path)+'_after'+str(file_path.suffix))
        print("处理完毕！")
        time.sleep(3)
    
    else:
        print("请稍等……\n")
        x=0
        for i in range(1,size[0]//2+1):
             if image.getpixel((i,1))!=(0,0,0):
                x=i
                break
        temp=image.crop((x,0,size[0]-x,size[1]))
        temp.save(str(file_path)+'_after'+str(file_path.suffix))
        print("\n处理完毕！")
        time.sleep(3)

if is_admin():
    single_process()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)





