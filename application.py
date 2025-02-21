import tkinter
from selenium_wrapper import SeleniumTypingPage as stp
class Application(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root,
                         width=420, height=320,
                         borderwidth=4, relief="groove",
                         bg="lightblue")
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()
        
    def create_widgets(self):
        lbl_message = tkinter.Label(self)
        lbl_message["text"] = "自動タイピングを行います"
        lbl_message["font"] = ("Arial", 16)  # フォントとサイズ指定
        lbl_message["wraplength"] = 300  # 改行幅を設定
        lbl_message["bg"] = "systemTransparent"  # 背景を透過に設定
        lbl_message["fg"] = "black"  # 文字色を黒に設定
        lbl_message.place(relx=0.5, rely=0.3, anchor="center", width=300, height=50)
        btn_start = tkinter.Button(self)
        btn_start["text"] = "スタート"
        btn_start["command"] = stp.OpenTypingPage
        btn_start["font"] = ("Arial", 16)  # フォントとサイズ指定
        btn_start.place(relx=0.5, rely=0.5, anchor="center", width=150, height=50)
        btn_quit = tkinter.Button(self)
        btn_quit["text"] = "終了"
        btn_quit["command"] = self.root.destroy
        btn_quit["font"] = ("Arial", 16)  # フォントとサイズ指定
        btn_quit.place(relx=0.85, rely=0.9, anchor="center",width=100, height=50)
        # btn_quit.pack(side="bottom", width=100, height=50)
