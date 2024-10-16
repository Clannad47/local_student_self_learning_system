import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from connect_mongodb import Mongodb
db=Mongodb()
class ChangeFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.password1 = tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0, pady=10)

        tk.Label(self, text='用户名：').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.username).grid(row=1, column=2, pady=10)

        tk.Label(self, text='旧密码：').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.password).grid(row=2, column=2, pady=10)

        tk.Label(self, text='新密码：').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.password1).grid(row=3, column=2, pady=10)

        tk.Button(self, text='修改', command=self.password_change).grid(row=4, column = 2)

    def password_change(self):
        ##db.check_login
        flag = db.check_login(self.username.get(),self.password.get())
        if flag:
            user = {'username': self.username.get(), 'password': self.password1.get()}
            self.username.set('')
            self.password.set('')
            self.password1.set('')
            db.UpdateByName(user['username'],user['password'])
            messagebox.showwarning(title='提示', message='修改密码成功')
        else:    
            messagebox.showwarning(title='提示', message='用户名或密码错误')
           
    
    


class DeleteFrame(tk.Frame):

    def __init__(self,root):
        super().__init__(root)
        tk.Label(self, text='删除界面').grid()

        self.username = tk.StringVar()
        tk.Label(self,text = '根据用户名删除').grid()
        tk.Entry(self,textvariable=self.username).grid()
        tk.Button(self,text='删除',command=self.delete).grid()
     
    def delete(self):
        username = self.username.get()
        db.RemoveByName(username)
        messagebox.showwarning(title='提示',message='删除成功')

class AddFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0,pady=10)

        tk.Label(self,text='用户名：').grid(row = 1,column= 1,pady=10)
        tk.Entry(self,textvariable=self.username).grid(row = 1,column= 2,pady=10)

        tk.Label(self, text='密码：').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.password).grid(row=2, column=2, pady=10)

        tk.Button(self,text = '录入',command=self.recode_info).grid(row=3,column=2)


    def recode_info(self):
        user = {'username': self.username.get(),'password': self.password.get()}
        self.username.set('')
        self.password.set('')
        db.InsertOne(user)
        print('表user为')
        print(db.user)
        messagebox.showwarning(title='提示',message='信息录入成功')

class SearchFrame(tk.Frame):
    def __init__(self, root):
         super().__init__(root)
         tk.Label(self, text='查询界面').grid()
         self.table_view = tk.Frame()
         self.table_view.grid()
         self.create_page()
       
         

    def create_page(self):
        colums = ('username','password')
        
        self.tree_view = ttk.Treeview(self,show='headings',columns= colums)
        self.tree_view.column('username',width=80,anchor='center')
        self.tree_view.column('password',width=80,anchor='center')
        self.tree_view.heading('username',text = '用户名')
        self.tree_view.heading('password',text = '密码')
        self.tree_view.grid(sticky='nsew')
        self.show_data_frame()

        tk.Button(self,text = '刷新',command= self.show_data_frame).grid(sticky = 'e',pady = 5)

    def show_data_frame(self):
        #删除旧的节点
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)
        users = db.FindAll()
        index = 0
        for u in users:
            self.tree_view.insert('',index,values = (
                u['username'],u['password']  #password
            ))

