import tkinter as tk
import os
import requests
from bs4 import BeautifulSoup as soup
import platform
import tkinter.messagebox as msgbox



window = tk.Tk()
window.title("Py B站爬图工具箱")
sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()
w = 600
h = 450
x = (sw - w) / 2
y = (sh - h) / 2
window.geometry("%dx%d+%d+%d" %(w,h,x,y))
if os.path.exists('b.ico'):
    window.iconbitmap('b.ico')
else:
    try:
        a = requests.get("https://tested-factual-basketball.glitch.me/%E5%9B%BE%E5%BA%8A/164e4b0d58c7aa613c15f23c91e6b528.ico")
        f = open("b.ico","wb")
        f.write(a.content)
        f.close()
        window.iconbitmap('b.ico')
    except:
        msgbox.showerror(message="无法获取程序ico图标！")
window.resizable(height=False,width=False)
#控件部分 The Weigets part of Window
Label1 = tk.Label(window,text="B站工具箱,以下是一些简单实用的功能，头像，视频封面，专栏头图将被分别保存为Avatar,video,cvcover.png",fg="#6A5ACD")
Label1.pack()
Label2 = tk.Label(window,text="获取头像原图，请输入用户空间的地址:",fg="blue")
Label2.pack()
text_space = tk.Text(window,height=1.5,width=50,fg="#0000FF",bg="#E6E6FA")
text_space.pack()
L_describe1 = tk.Label(window,text="(例如:https://space.bilibili.com/275212157?spm_id_from=333.1007.0.0)")
L_describe1.pack()
#getAvatar 获取头像
def getAvatar():
    if (text_space.get('0.0','end').strip() != ""):
        html = requests.get(url=text_space.get("0.0","end").strip()).text
        #print(html)
        after = soup(html,"html.parser")
        link = after.find('link',rel = "apple-touch-icon")
        processed_link = "https:" + link['href']
        print("[头像图片地址] " + processed_link)
        print("正在下载Avatar.jpg，请稍等...")
        if os.path.exists('Avatar.jpg'):
            os.remove("Avatar.jpg")
        picture = requests.get(processed_link)
        f = open("Avatar.jpg",'wb')
        f.write(picture.content)
        f.close()
        msgbox.showinfo(title="头像图片",message="下载完成")
        print("头像图片下载完成！")
    else:
        msgbox.showerror(title="错误",message="你没有输入b站个人空间的地址我怎么获取")
    
    
#define End结束

bt_ava = tk.Button(window,text="爬取头像")
bt_ava.config(command=getAvatar)
bt_ava.pack()

Label3 = tk.Label(window,text="获取视频封面的原图",fg="blue").pack()
L_describe2 = tk.Label(window,text="请输入视频地址:").pack()
text_video = tk.Text(window,height=1.5,width=50,fg="#0000FF",bg="#E6E6FA")
text_video.pack()
#get Video cover
def getVideo_cover():
    if(text_video.get('0.0','end').strip() != ""):
        html = requests.get(url=text_video.get('0.0','end').strip()).text
        aft = soup(html,"html.parser")
        i = aft.find('meta',itemprop="thumbnailUrl")
        thumbnail_url = "https:" + i['content']
        spl = thumbnail_url.split("@")
        print(spl[0])
        a = requests.get(spl[0])
        f = open("video.jpg",'wb')
        f.write(a.content)
        f.close()
        msgbox.showinfo(title="视频封面",message="下载完成!")
    else:
        print("未填写Video_cover")
        msgbox.showerror(title="???",message="你还没写视频地址!")

#End cover
bt_video = tk.Button(window,text="爬取视频封面",command=getVideo_cover).pack()
Label4 = tk.Label(window,text="获取专栏头图:",fg="blue").pack()
text_zhuanlan = tk.Text(window,height=1.5,width=50,fg="#0000FF",bg="#E6E6FA")
text_zhuanlan.pack()
def getcvc():
    str_url = text_zhuanlan.get('0.0','end').strip()
    if str_url != "":
        html = requests.get(url=str_url).text
        after_soup = soup(html,"html.parser")
        i=after_soup.find('meta',property="og:image")
        print(i['content'])
        file = requests.get(i['content'])
        f = open("cvcover.png","wb")
        f.write(file.content)
        f.close()
        msgbox.showinfo(title="保存文章头图",message="保存完成！")
    else:
        msgbox.showerror(title="!?!?!?!??",message="请务必填写地址后再获取！！！")

bt_zhuanlan = tk.Button(window,text="爬取专栏头图",command=getcvc).pack()
Label5 = tk.Label(window,text="文件保存路径默认为此程序同一目录",fg="blue").pack()

#bt_opensavedpath 点击
def open_save_path():
    sys = platform.system()
    if sys == "Windows":
        print("您使用的是Windows系统，正在使用explorer.exe打开目录")
        path = os.getcwd()
        file = r'%s'% path
        os.system(f'explorer /open, {file}')
    elif sys == "Linux":
        print("您使用的是Linux系统，正在尝试pacman打开目录")
        path1 = os.getcwd()
        file1 = r'%s' % path1
        os.system(f'pacmanfm %s' % file1)

    print("已打开保存目录!")

#end

bt_opensavedpath = tk.Button(window,text="打开文件保存目录",command=open_save_path).pack()
bt1 = tk.Button(window,text="关闭程序",command=window.quit).pack()
#End Weigets
window.mainloop()







