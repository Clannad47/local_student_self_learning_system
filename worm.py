import threading
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import webbrowser
from CSDN_Download import get_title, get_html
from CSDN_checkredian import check_redian
import requests
from plumbum import local
class Worm:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500+300+200")
        self.root.title('学生自助学习系统')

        self.frame0 = Frame(self.root)
        self.frame1 = Frame(self.root)
        self.frame2 = Frame(self.root)

        self.setup_frame0()
        self.setup_frame1()
        
        
        self.frame0.pack()  

    def setup_frame0(self):
        label0 = Label(self.frame0, text="CSDN每日热点", font=('华文行楷', 18))
        label0.pack()
        self.link_dict={}
        self.text1 = Text(self.frame0, font=('微软雅黑', 12), width=65, height=18,cursor="hand2")
        index=0
        for key, value in check_redian()[0].items():
            tag_name = f"link_{index}"
            self.text1.insert(END, key, tag_name)
            self.link_dict[tag_name] = value
            self.text1.tag_config(tag_name, foreground="blue", underline=True,justify='center',font=("Times",18,"bold"))
            # 使用默认参数来保存当前的 key
            self.text1.tag_bind(tag_name, "<Button-1>", lambda e, k=tag_name: self.open_link(k))
            self.text1.insert(END, '\n')
            index+=1
        self.text1.pack()



        button0 = Button(self.frame0, text='CSDN文章爬取系统', command=self.frame_go0, font=('微软雅黑', 15))
        button0.pack(side=LEFT)

        button1 = Button(self.frame0, text='AI聊天机器人', command=self.frame_go1, font=('微软雅黑', 15))
        button1.pack(side=RIGHT)

        button4 = Button(self.frame0, text='点击查看每日一言', command=self.frame_go2, font=('微软雅黑', 15))
        button4.pack(anchor='center')
       

    def setup_frame1(self):
        label1 = Label(self.frame1, text="请在下框输入要解析的网址", font=('华文行楷', 18))
        label1.grid(columnspan=2)

        self.entry = Entry(self.frame1, font=('微软雅黑', 14), width=52)
        self.entry.grid(row=1, columnspan=2)

        self.text = Text(self.frame1, font=('微软雅黑', 12), width=80, wrap=WORD, height=17)
        self.text.grid(row=2, columnspan=2)

        button2 = Button(self.frame1, text="开始下载", font=('微软雅黑', 15), command=self.go, relief=GROOVE)
        button2.grid(row=3, column=0, sticky=W)

        button3 = Button(self.frame1, text="返回", font=('微软雅黑', 15), command=self.go_back, relief=GROOVE)
        button3.grid(row=3, column=1, sticky=E)  
   
    def open_link(self, title):
        
        url = self.link_dict.get(title)
        if url:
            webbrowser.open(url)
        else:
            print(f"Link not found for: {title}")


    def refresh_text(self):
        title = get_title(self.entry.get())
        self.text.insert(END, "正在下载：-----------" + title + '\n')
        self.text.see(END)
        self.text.update()

        self.text.insert(END, "下载完成-----------" + title + '\n')

    def go(self):
        self.root.after(2000, self.refresh_text)
        def run_get_html():
            get_html(self.entry.get())
        get_html_thread = threading.Thread(target = run_get_html)
        get_html_thread.start()

    def frame_go0(self):
        self.frame0.pack_forget()
        self.frame1.pack()

    def frame_go1(self):
        #新开线程解决卡顿问题
        def run_streamlit():
               start_aiweb = local[r"streamlit"][r"run", r".\chatproject.py",r"--server.port=52025"]
               start_aiweb()
        thread = threading.Thread(target = run_streamlit)
        thread.start()
        

    def go_back(self):
        self.frame2.pack_forget()
        self.frame1.pack_forget()
        self.frame0.pack()

    def frame_go2(self):
        url = "https://v1.hitokoto.cn/?c=f&encode=text"
        response = requests.request("GET", url)
        return messagebox.showinfo('您的每日一言',response.text)

 
if __name__ == "__main__":
    root = tk.Tk()
    Worm(root)

    root.mainloop()
