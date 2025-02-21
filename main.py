from selenium_wrapper import SeleniumTypingPage as stp
import tkinter
from application import Application as app
if __name__ == "__main__":
    # stp.OpenTypingPage()
    root = tkinter.Tk()
    root.title("タイピング練習道場(自動化)")
    
    # 画面サイズを取得
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # ウィンドウのサイズを取得
    window_width = 400
    window_height = 300
    # 画面中央に配置するための位置を計算
    position_top = int((screen_height - window_height) / 2)
    position_left = int((screen_width - window_width) / 2)

    # ウィンドウ位置を設定
    root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")
    # root.geometry("400x300")
    # コントロールを配置
    app = app(root=root)
    app.mainloop()
    