# Import thư viện tkinter
from multiprocessing.sharedctypes import Value
from tkinter import *
import tkinter
from tkinter import font
# Thêm thư viện để tạo combo box là một danh sách xổ xuống
from tkinter.ttk import *
from tkinter import messagebox
# dòng dưới có nghĩa là đặt biến là window có Tk() nghĩa là cửa số đó có các nút tắt, thu nhỏ,...
window = Tk()
# đặt tên cửa sổ
window.title("Password")
# độ phân giải của sổ
window.geometry("800x600")

# Thêm label (fg là màu chữ, font là kiểu chữ và sau đó là cỡ chữ)
lbl = tkinter.Label(window, text = "This program is to generate random password", fg = "red", font = ("Arial", 20))
# Đặt vị trí của chữ trên màn hình (cột = , hàng = )
lbl.grid(column=0, row= 0)

# Thêm textbox(trong cửa sổ, chiều rộng = )
txt = Entry(window, width=20)
# Đặt vị trí của textbox trên màn hình (cột = , hàng = )
txt.grid(column=0,row=1)

# Tạo hàm để khi ấn nút thì đổi cái tiêu đề thành nội dung trong textbox vừa tạo
def handlebutton():
    # configure = đổi(nội dung = ...) (txt.get() có nghĩa là trả về giá trị theo nội dung trong textbox)
    lbl.configure(text = "Hi, " + txt.get())
    return

# Thêm nút nhấn
# Đưa hàm vào tham số command
btnHello = Button(window, text = "Say Hello", command = handlebutton)
# Cho nút nhấn này cùng hàng (cũng đồng nghĩa là phải khác cột để không bị đè lên)
btnHello.grid(column=1,row=1)

# Thêm combobox là một danh sách xổ xuống
combo = Combobox(window) # Tức là vẽ combo box ở window
combo['values'] = ("Nguyễn Lê Tuấn" , "Nathan", "Gold")
# Mặc định khi mở lên là lựa chọn mấy
combo.current(0)
combo.grid(column=0, row=2)

# Hàm in ra nội dung chọn trong combobox
def handlebutton1():
    # configure = đổi(nội dung = ...) (txt.get() có nghĩa là trả về giá trị theo nội dung trong textbox)
    #lbl.configure(text = "Hi, " + combo.get())

    # Hiển thị trong messagebox
    messagebox.showinfo("Test thử", "Hi," + combo.get())
    return

# Thêm nút nhấn combo
# Đưa hàm vào tham số command
btnHello1 = Button(window, text = "Say Hello Combo", command = handlebutton1)
# Cho nút nhấn này cùng hàng (cũng đồng nghĩa là phải khác cột để không bị đè lên)
btnHello1.grid(column=1,row=2)

window.mainloop() 