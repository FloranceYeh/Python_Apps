from tkinter import *
from datetime import datetime

root = Tk()
root.geometry("600x400")

root.title("计时器")

t = localtime()

# Start vars
sye = IntVar()
sye.set(t.tm_year)
smo = IntVar()
smo.set(t.tm_mon)
sda = IntVar()
sda.set(t.tm_mday)
sho = IntVar()
sho.set(t.tm_hour)
smi = IntVar()
smi.set(t.tm_min)
sse = IntVar()
sse.set(t.tm_sec)

# Start Time
stl = Label(root, text = "起始:    ", font = ("Arial Bold", 20))
stl.grid(column = 0, row = 0)
# Start year
stye = Spinbox(root, from_ = 2000, to = 3000, width = 5, textvariable = sye)
stye.grid(column = 1, row = 0)
l01 = Label(root, text = ".", font = ("Arial Bold", 20))
l01.grid(column = 2, row = 0)
# Start month
stmo = Spinbox(root, from_ = 1, to = 12, width = 5, textvariable = smo)
stmo.grid(column = 3, row = 0)
l02 = Label(root, text = ".", font = ("Arial Bold", 20))
l02.grid(column = 4, row = 0)
# Start day
stda = Spinbox(root, from_ = 1, to = 31, width = 5, textvariable = sda)
stda.grid(column = 5, row = 0)
l03 = Label(root, text = "  ", font = ("Arial Bold", 20))
l03.grid(column = 6, row = 0)
# Start hour
stho = Spinbox(root, from_ = 1, to = 24, width = 5, textvariable = sho)
stho.grid(column = 7, row = 0)
l04 = Label(root, text = ":", font = ("Arial Bold", 20))
l04.grid(column = 8, row = 0)
# Start minute
stmi = Spinbox(root, from_ = 1, to = 60, width = 5, textvariable = smi)
stmi.grid(column = 9, row = 0)
l05 = Label(root, text = ":", font = ("Arial Bold", 20))
l05.grid(column = 10, row = 0)
# Start second
stse = Spinbox(root, from_ = 1, to = 60, width = 5, textvariable = sse)
stse.grid(column = 11, row = 0)

# End Time
enl = Label(root, text = "结束:    ", font = ("Arial Bold", 20))
enl.grid(column = 0, row = 1)
# End year
enye = Spinbox(root, from_ = 2000, to = 3000, width = 5, textvariable = sye)
enye.grid(column = 1, row = 1)
l11 = Label(root, text = ".", font = ("Arial Bold", 20))
l11.grid(column = 2, row = 1)
# End month
enmo = Spinbox(root, from_ = 1, to = 12, width = 5, textvariable = smo)
enmo.grid(column = 3, row = 1)
l12 = Label(root, text = ".", font = ("Arial Bold", 20))
l12.grid(column = 4, row = 1)
# End day
enda = Spinbox(root, from_ = 1, to = 31, width = 5, textvariable = sda)
enda.grid(column = 5, row = 1)
l13 = Label(root, text = "  ", font = ("Arial Bold", 20))
l13.grid(column = 6, row = 1)
# End hour
enho = Spinbox(root, from_ = 1, to = 24, width = 5, textvariable = sho)
enho.grid(column = 7, row = 1)
l14 = Label(root, text = ":", font = ("Arial Bold", 20))
l14.grid(column = 8, row = 1)
# End minute
enmi = Spinbox(root, from_ = 1, to = 60, width = 5, textvariable = smi)
enmi.grid(column = 9, row = 1)
l15 = Label(root, text = ":", font = ("Arial Bold", 20))
l15.grid(column = 10, row = 1)
# End second
ense = Spinbox(root, from_ = 1, to = 60, width = 5, textvariable = sse)
ense.grid(column = 11, row = 1)



root.mainloop()

def calculate_time_difference(start_year, start_month, start_day, start_hour, start_minute, start_second, end_year, end_month, end_day, end_hour, end_minute, end_second):
    start = datetime(start_year, start_month, start_day, start_hour, start_minute, start_second)
    end = datetime(end_year, end_month, end_day, end_hour, end_minute, end_second)

    time_difference = end - start

    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # 返回结果
    return days, hours, minutes, seconds

start_year = int(input("请输入起始年份："))
start_month = int(input("请输入起始月份："))
start_day = int(input("请输入起始日期："))
start_hour = int(input("请输入起始小时："))
start_minute = int(input("请输入起始分钟："))
start_second = int(input("请输入起始秒数："))

end_year = int(enye.get())
end_month = int(enmo.get())
end_day = int(enda.get())
end_hour = int(enho.get())
end_minute = int(enmi.get())
end_second = int(ense.get())

days_diff, hours_diff, minutes_diff, seconds_diff = calculate_time_difference(start_year, start_month, start_day, start_hour, start_minute, start_second, end_year, end_month, end_day, end_hour, end_minute, end_second)

print("时间差：")
print(f"天数：{days_diff}")
print(f"小时数：{hours_diff}")
print(f"分钟数：{minutes_diff}")
print(f"秒数：{seconds_diff}")