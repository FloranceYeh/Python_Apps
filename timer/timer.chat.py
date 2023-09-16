from tkinter import *
from datetime import datetime


def calculate_time_difference():
    start = datetime(int(start_year_entry.get()), int(start_month_entry.get()), int(start_day_entry.get()), int(start_hour_entry.get()), int(start_minute_entry.get()), int(start_second_entry.get()))
    end = datetime(int(end_year_entry.get()), int(end_month_entry.get()), int(end_day_entry.get()), int(end_hour_entry.get()), int(end_minute_entry.get()), int(end_second_entry.get()))

    # 计算时间差
    time_difference = end - start

    # 提取天数、小时数、分钟数和秒数
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # 显示结果
    result_label.config(text=f"时间差：\n天数：{days}\n小时数：{hours}\n分钟数：{minutes}\n秒数：{seconds}")


# 创建GUI窗口
window = Tk()
window.title("时间差计算器")

# 创建标签和输入框
start_year_label = Label(window, text="起始年份：")
start_year_label.grid(row=0, column=0)
start_year_entry = Entry(window)
start_year_entry.grid(row=0, column=1)

start_month_label = Label(window, text="起始月份：")
start_month_label.grid(row=1, column=0)
start_month_entry = Entry(window)
start_month_entry.grid(row=1, column=1)

start_day_label = Label(window, text="起始日期：")
start_day_label.grid(row=2, column=0)
start_day_entry = Entry(window)
start_day_entry.grid(row=2, column=1)

start_hour_label = Label(window, text="起始小时：")
start_hour_label.grid(row=3, column=0)
start_hour_entry = Entry(window)
start_hour_entry.grid(row=3, column=1)

start_minute_label = Label(window, text="起始分钟：")
start_minute_label.grid(row=4, column=0)
start_minute_entry = Entry(window)
start_minute_entry.grid(row=4, column=1)

start_second_label = Label(window, text="起始秒数：")
start_second_label.grid(row=5, column=0)
start_second_entry = Entry(window)
start_second_entry.grid(row=5, column=1)

end_year_label = Label(window, text="结束年份：")
end_year_label.grid(row=0, column=2)
end_year_entry = Entry(window)
end_year_entry.grid(row=0, column=3)

end_month_label = Label(window, text="结束月份：")
end_month_label.grid(row=1, column=2)
end_month_entry = Entry(window)
end_month_entry.grid(row=1, column=3)

end_day_label = Label(window, text="结束日期：")
end_day_label.grid(row=2, column=2)
end_day_entry = Entry(window)
end_day_entry.grid(row=2, column=3)

end_hour_label = Label(window, text="结束小时：")
end_hour_label.grid(row=3, column=2)
end_hour_entry = Entry(window)
end_hour_entry.grid(row=3, column=3)

end_minute_label = Label(window, text="结束分钟：")
end_minute_label.grid(row=4, column=2)
end_minute_entry = Entry(window)
end_minute_entry.grid(row=4, column=3)

end_second_label = Label(window, text="结束秒数：")
end_second_label.grid(row=5, column=2)
end_second_entry = Entry(window)
end_second_entry.grid(row=5, column=3)

# 默认起始时间为当前时间
current_time = datetime.now()
start_year_entry.insert(0, current_time.year)
start_month_entry.insert(0, current_time.month)
start_day_entry.insert(0, current_time.day)
start_hour_entry.insert(0, current_time.hour)
start_minute_entry.insert(0, current_time.minute)
start_second_entry.insert(0, current_time.second)

# 创建计算按钮
calculate_button = Button(window, text="计算", command=calculate_time_difference)
calculate_button.grid(row=6, column=1)

# 创建结果标签
result_label = Label(window, text="时间差：")
result_label.grid(row=7, column=1)

# 实时更新时间差
def update_time_difference(event):
    calculate_time_difference()

end_year_entry.bind("<KeyRelease>", update_time_difference)
end_month_entry.bind("<KeyRelease>", update_time_difference)
end_day_entry.bind("<KeyRelease>", update_time_difference)
end_hour_entry.bind("<KeyRelease>", update_time_difference)
end_minute_entry.bind("<KeyRelease>", update_time_difference)
end_second_entry.bind("<KeyRelease>", update_time_difference)

# 运行GUI窗口
window.mainloop()