import tkinter as tk
from tkinter import messagebox
from connect_mongodb import Mongodb

from MainPage import MainPage
from worm import Worm


class Login_page:

    def __init__(self,rot: tk.Tk):
        self.root = rot
        self.root.geometry('300x180+450+200')
        self.root.title('用户登录')

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.page = tk.Frame(self.root)
        self.page.pack()

        tk.Label(self.page).grid(row=0,column = 0)

        tk.Label(self.page,text='用户名：').grid(row = 1,column=1,pady= 10)
        tk.Entry(self.page,textvariable=self.username).grid(row=1,column=2)

        tk.Label(self.page,text='密码：').grid(row = 2,column=1,pady= 10)
        tk.Entry(self.page,textvariable=self.password).grid(row=2,column=2)

        tk.Button(self.page, text='登录', command=self.login).grid(row=3, column=1, pady=10)
        tk.Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=2, pady=10)


    def login(self):
        # print(self.username.get(),self.password.get())
        name = self.username.get()
        pwd = self.password.get()
        if not name or not pwd:
            messagebox.showwarning(title='警告', message='用户名或密码不能为空')
            return   
        ##调用mongodb
        mongodb=Mongodb()
        flag = mongodb.check_login(name, pwd)
        if flag:
            if name=='root':
                self.page.destroy()
                MainPage(self.root)
            else:
                self.root.destroy()     
                worm = tk.Tk()
                app = Worm(worm)
                worm.mainloop()
                
        else:
            messagebox.showwarning(title='警告', message='用户名或密码错误')


if __name__ == '__main__':
    r = tk.Tk()
    Login_page(rot =r)
    r.mainloop()