import tkinter as tk
from tkinter import ttk
import xlwt

#先他妈的给这个工作簿搞好
workbook = xlwt.Workbook()
sheets = {day: workbook.add_sheet(day) for day in ['一', '二', '三', '四', '五']}

# 他妈的还得初始化
row_numbers = {day: 0 for day in sheets}

# 给这他妈的该死的课保存下去
def save_course():
    day = day_combobox.get()
    start_time = start_time_entry.get()
    course_name = course_name_entry.get()
    end_time = end_time_entry.get()

    sheet = sheets[day]
    row_number = row_numbers[day]

    sheet.write(row_number, 0, start_time)
    sheet.write(row_number, 1, course_name)
    sheet.write(row_number, 2, end_time)

    row_numbers[day] += 1

    # 全他妈给你清空了
    start_time_entry.delete(0, tk.END)
    course_name_entry.delete(0, tk.END)
    end_time_entry.delete(0, tk.END)

# 保存一下
def save_workbook():
    workbook.save('schedule.xls')
    root.destroy()

# 把窗口他妈的给我搞出来
root = tk.Tk()
root.title("创建")

# 给傻逼输的
tk.Label(root, text="周").grid(row=0, column=0)
day_combobox = ttk.Combobox(root, values=list(sheets.keys()))
day_combobox.grid(row=0, column=1)

tk.Label(root, text="上课时间").grid(row=1, column=0)
start_time_entry = tk.Entry(root)
start_time_entry.grid(row=1, column=1)

tk.Label(root, text="学科名称").grid(row=2, column=0)
course_name_entry = tk.Entry(root)
course_name_entry.grid(row=2, column=1)

tk.Label(root, text="下课时间").grid(row=3, column=0)
end_time_entry = tk.Entry(root)
end_time_entry.grid(row=3, column=1)

# 傻逼按钮
save_button = tk.Button(root, text="保存这一节课", command=save_course)
save_button.grid(row=4, column=0, columnspan=2)

save_workbook_button = tk.Button(root, text="保存整个课表", command=save_workbook)
save_workbook_button.grid(row=5, column=0, columnspan=2)

# 一直他妈的循环
root.mainloop()
#不愧是我经过不断的学习终于他妈的把这狗屎写完了（应该没人看吧