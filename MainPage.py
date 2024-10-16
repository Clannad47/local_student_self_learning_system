import tkinter as tk
from views import  *

class MainPage:
    def __init__(self,rot: tk.Tk):
        self.root = rot
        self.root.title('用户信息管理系统')
        self.root.geometry('450x350+450+200')
        self.create_page()

    def create_page(self):
        self.change_frmae = ChangeFrame(self.root)
        # tk.Label(self.change_frmae,text = '修改界面').pack()
        self.delete_frame = DeleteFrame(self.root)
        # tk.Label(self.delete_frame, text='删除界面').pack()
        self.add_frame = AddFrame(self.root)
        # tk.Label(self.add_frame, text='增添界面').pack()
        self.search_frame = SearchFrame(self.root)
        # tk.Label(self.search_frame, text='查询界面').pack()


        menu = tk.Menu(self.root)
        menu.add_command(label='录入',command=self.show_add)
        menu.add_command(label='查询',command=self.show_search)
        menu.add_command(label='删除',command=self.show_delete)
        menu.add_command(label='修改',command=self.show_change)
        self.root['menu'] = menu

    def show_change(self):
        self.delete_frame.grid_forget()
        self.add_frame.grid_forget()
        self.search_frame.grid_forget()
        self.change_frmae.grid()

    def show_delete(self):
        self.add_frame.grid_forget()
        self.search_frame.grid_forget()
        self.change_frmae.grid_forget()
        self.delete_frame.grid()

    def show_add(self):
        self.delete_frame.grid_forget()
        self.search_frame.grid_forget()
        self.change_frmae.grid_forget()
        self.add_frame.grid()


    def show_search(self):
        self.delete_frame.grid_forget()
        self.add_frame.grid_forget()
        self.change_frmae.grid_forget()
        self.search_frame.grid()
        #






if __name__ == '__main__':
    r = tk.Tk()
    MainPage(rot=r)
    r.mainloop()