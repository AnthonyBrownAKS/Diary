import tkinter as tk
import calendar
from datetime import datetime
import btn_command as bc


# 创建日历的主窗口/标题
# geometry('XxY+偏移量')
cld = tk.Tk()
cld.geometry('400x300+550+300')
cld.title('本月日历')
# 创建提示框
label = tk.Label(cld,text='point the date and see what you need to do')
label.place(x=10,y=10)


def date():
    now = datetime.now()
    # 获取当前月份的日历
    cal = calendar.monthcalendar(now.year, now.month)
    all_dates = []
    # 遍历每一周
    for week in cal:
        # 遍历每一天
        for day in week:
            if day != 0:
                all_dates.append(day)

    print(f"当前日期:{now.month}月{now.day}号")
    print("当前月份的所有日期:", all_dates)
    return all_dates

# 创建按钮
def DateBottom(cld,date):
    # 按钮布局设置
    row = 0
    j = 0
    # 循环创建按钮并添加到窗口
    for date_btn in date:
        # 创建按钮并设置点击事件处理函数
        # 使用lambda传递参数,并且每个按钮绑定到不同的方法
        button = tk.Button(cld,text=date_btn,command=lambda i=date_btn: bc.btn_main(i),width=4,height=2)
        column = date_btn
        if date_btn % 10 == 0:
            j = j + 1
            row = row + 1
        column = column - j * 10

        # x的初始间距为55,y的初始间距为90
        button.place(y=row*50+40,x=column*35+20)



if 1 == 1:
    dates = date()
    DateBottom(cld,dates)

# 运行窗口主体
cld.mainloop()







