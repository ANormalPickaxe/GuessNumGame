import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ctypes import windll
import random


n,s = 0,0


def init_game():
    global n
    n = random.randint(1, 100)
    entry_number.delete(0, tk.END)
    lbl_hint.config(text="请输入1-100之间的数字")


def start_game():
    l1.pack_forget()
    btn1.pack_forget()
    game_frame.pack(pady=50)
    entry_number.focus()


def check_guess():
    global s
    try:
        guess = int(entry_number.get())
        if not 1 <= guess <= 100:
            raise ValueError
    except ValueError:
        messagebox.showerror("错误", "请输入有效数字")
        return

    if guess == n:
        lbl_hint.config(text="正好！", fg="green")
        messagebox.showinfo("成功", f"恭喜猜对了！猜了{s}次")
        init_game()
    elif guess < n:
        lbl_hint.config(text="猜小了！", fg="blue")
        s+=1
    else:
        lbl_hint.config(text="猜大了！", fg="red")
        s+=1


root = tk.Tk()
root.title("猜数字")
root.geometry("900x600")


windll.shcore.SetProcessDpiAwareness(1)
root.tk.call('tk', 'scaling', 2.0)

font_config = ("Microsoft YaHei", 12)

l1 = tk.Label(root,text=f"猜数字游戏\n作者:A Normal Pickaxe\nB站:https://space.bilibili.com/2036075820 | 一个普通的Pickaxe\n{'=' * 20}\n1-100之间的数字",font=font_config)
l1.pack(pady=80)

btn1 = ttk.Button(root,text="开始游戏",command=start_game)
btn1.pack()

game_frame = tk.Frame(root)

input_frame = tk.Frame(game_frame)
input_frame.pack(pady=20)

tk.Label(input_frame,text="输入猜测：",font=font_config).pack(side=tk.LEFT)

entry_number = ttk.Entry(input_frame,font=font_config,width=10)
entry_number.pack(side=tk.LEFT, padx=10)

ttk.Button(input_frame,text="提交",command=check_guess).pack(side=tk.LEFT)


lbl_hint = tk.Label(game_frame,text="",font=font_config)
lbl_hint.pack(pady=20)

tk.Label(game_frame,text="",font=font_config)


init_game()
root.mainloop()
