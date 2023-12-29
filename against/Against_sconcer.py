from tkinter import *
from tkinter import messagebox
from random import randrange
from datetime import datetime
from win10toast import ToastNotifier
from time import sleep
from threading import Thread
from os import system
from pygame import mixer

threads = []

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.F1 = IntVar()
        self.F2 = IntVar()
        self.F3 = IntVar()
        self.F4 = IntVar()
        self.F5 = IntVar()
        self.F6 = IntVar()
        self.start = self.__start(self)
        self.title = self.__title(self)
        self.copyright = self.__copyright(self)
        self.help = self.__help(self)
        self.settings = self.__settings(self)
        self.title2 = self.__title2( self.settings) 
        self.gap = self.__gap( self.settings)
        self.hour = self.__hour( self.settings) 
        self.minute = self.__minute( self.settings) 
        self.functions = self.__functions(self)
        self.title3 = self.__title3( self.functions) 
        self.fun1 = self.__fun1( self.functions) 
        self.fun2 = self.__fun2( self.functions) 
        self.fun3 = self.__fun3( self.functions) 
        self.fun4 = self.__fun4( self.functions) 
        self.fun5 = self.__fun5( self.functions) 
        self.fun6 = self.__fun6( self.functions)
    

    def function1(self):
        while True:
            now = datetime.now()
            nh = now.hour
            nm = now.minute
            h = int(self.hour.get())
            m = int(self.minute.get())
            if nh == h and nm == m:
                # print("FFF1!")
                system("shutdown /p")
            sleep(5)

    def function2(self):
        toaster = ToastNotifier()
        while True:
            now = datetime.now()
            nh = now.hour
            nm = now.minute
            h = int(self.hour.get())
            m = int(self.minute.get())
            flag = False
            if (nh == h and nm == m) or flag == True:
                flag = True
                toaster.show_toast(
                    "Warning",
                    "系统出现故障",
                    icon_path = "warning.png",
                    duration = 2
                )
            sleep(5)

    def function3(self):
        def dow():
            F3window = Tk()
            F3window.title('ERROR')
            F3window.iconbitmap('warning.ico')
            F3window.resizable(width=False, height=False)
            F3window.geometry("210x50" + "+" + str(randrange(0, F3window.winfo_screenwidth())) + "+" + str(randrange(0, F3window.winfo_screenheight())))
            Label(F3window,text='WARNING',).pack()
            F3window.mainloop()
        F3threads = []
        while True:
            now = datetime.now()
            nh = now.hour
            nm = now.minute
            h = int(self.hour.get())
            m = int(self.minute.get())
            flag = False
            if (nh == h and nm == m) or flag == True:
                flag = True
                for i in range(666):
                    t = Thread(target=dow)
                    F3threads.append(t)
                    sleep(0.1)
                    F3threads[i].start()
            sleep(5)

    def function4(self):
        while True:
            now = datetime.now()
            nh = now.hour
            nm = now.minute
            h = int(self.hour.get())
            m = int(self.minute.get())
            flag = False
            mixer.init()
            if (nh == h and nm == m) or flag == True:
                flag = True
                music = mixer.music.load(r"music.mp3")
                mixer.music.play()
            sleep(666)
        

    def function5(self):
        pass

    def function6(self):
        pass
    
    def _help(self):
        messagebox.askokcancel(
            title = 'Help',message='\
                对拖堂特种，灵感来源于Chose_B以及Florance的愤怒\n\
                点击Start后窗口会消失，命令执行完毕后关闭\n\
                如果误触，请自行使用TaskManager关闭进程\n\
                功能介绍：\n\
                1.关机 定时关闭电脑，无任何警告\n\
                2.通知 疯狂弹出系统错误的假通知\n\
                3.窗口 疯狂弹出新窗口\n\
                4.音乐 播放在文件目录下名为music.mp3的音乐\n\
                5.抽风 疯狂打开电脑中的程序\n\
                6.待开发 期待你的建言献策\n\
            ')


    def clicked(self):
        f1 = Thread(target=self.function1)
        f2 = Thread(target=self.function2)
        f3 = Thread(target=self.function3)
        f4 = Thread(target=self.function4)
        f5 = Thread(target=self.function5)
        f6 = Thread(target=self.function6)
        if self.F1.get() == 1:
            threads.append(f1)
        if self.F2.get() == 1:
            threads.append(f2)
        if self.F3.get() == 1:
            threads.append(f3)
        if self.F4.get() == 1:
            threads.append(f4)
        if self.F5.get() == 1:
            threads.append(f5)
        if self.F6.get() == 1:
            threads.append(f6)
        self.withdraw()
        for f in threads:
            f.start()

    def __win(self):
        self.title("Against sconcer")
        width = 600
        height = 400
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.iconbitmap('icon.ico')
        self.resizable(width=False, height=False)

    def __start(self,parent):
        btn = Button(parent, text="开始",fg="red", takefocus=False,font=("Arial Bold", 10), command=self.clicked)
        btn.place(x=540, y=360, width=50, height=30)
        return btn
    def __title(self,parent):
        label = Label(parent,text="对拖堂宝具",font=("Arial Bold", 20), anchor="center", )
        label.place(x=11, y=12, width=145, height=36)
        return label
    def __copyright(self,parent):
        label = Label(parent,text="Made By Florance",fg="green", anchor="center", )
        label.place(x=0, y=370, width=123, height=30)
        return label
    def __help(self,parent):
        btn = Button(parent, text="HELP", command=self._help)
        btn.place(x=550, y=10)
    def __settings(self,parent):
        frame = Frame(parent,)
        frame.place(x=100, y=60, width=400, height=100)
        return frame
    def __title2(self,parent):
        label = Label(parent,text="设置",anchor="center", )
        label.place(x=10, y=10, width=50, height=30)
        return label
    def __gap(self,parent):
        label = Label(parent,text=":",anchor="center", )
        label.place(x=180, y=62, width=30, height=30)
        return label
    def __hour(self,parent):
        h = IntVar()
        h.set(11)
        ipt = Entry(parent, textvariable=h)
        ipt.place(x=140, y=60, width=30, height=30)
        return ipt
    def __minute(self,parent):
        m = IntVar()
        m.set(55)
        ipt = Entry(parent, textvariable=m)
        ipt.place(x=220, y=60, width=30, height=30)
        return ipt
    def __functions(self,parent):
        frame = Frame(parent,)
        frame.place(x=100, y=200, width=400, height=150)
        return frame
    def __title3(self,parent):
        label = Label(parent,text="选项",anchor="center", )
        label.place(x=10, y=10, width=50, height=30)
        return label
    def __fun1(self,parent):
        cb = Checkbutton(parent,text="关机",variable=self.F1, onvalue=1, offvalue=0)
        cb.place(x=30, y=60, width=80, height=30)
        return cb
    def __fun2(self,parent):
        cb = Checkbutton(parent,text="通知",variable=self.F2,onvalue=1, offvalue=0)
        cb.place(x=150, y=60, width=80, height=30)
        return cb
    def __fun3(self,parent):
        cb = Checkbutton(parent,text="窗口",variable=self.F3,onvalue=1, offvalue=0)
        cb.place(x=270, y=60, width=80, height=30)
        return cb
    def __fun4(self,parent):
        cb = Checkbutton(parent,text="音乐",variable=self.F4,onvalue=1, offvalue=0)
        cb.place(x=30, y=100, width=80, height=30)
        return cb
    def __fun5(self,parent):
        cb = Checkbutton(parent,text="抽风",variable=self.F5,onvalue=1, offvalue=0)
        cb.place(x=150, y=100, width=80, height=30)
        return cb
    def __fun6(self,parent):
        cb = Checkbutton(parent,text="待开发",variable=self.F6,onvalue=1, offvalue=0)
        cb.place(x=270, y=100, width=80, height=30)
        return cb
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.ctl.init(self)
    def __event_bind(self):
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
    
