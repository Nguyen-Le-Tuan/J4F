import string
import random
from datetime import datetime
# Hàm tạo password
def generate_random_password():
    # Hỏi tên người dùng
    user_name = str(input("What's your username:  "))
    # Hỏi thông tin về mật khẩu
    user_information = str(input("Password for what app: "))
    # Hỏi người dùng về độ dài của password
    lenght = int(input("Lenght of the password: "))
    # Hỏi người dùng số lượng các kiểu kí tự
    alphabets_count = int(input("Enter alphabets count in password: "))
    digits_count = int(input("Enter digits count in password: "))
    special_characters_count = int(input("Enter special_characters count in password: "))
    characters_count = alphabets_count + digits_count + special_characters_count
    if characters_count > lenght:
        print("Character total count total greater than its lenght! ")
        return 0
    # Tạo list rỗng password
    password = []
    # Chọn các kí tự ngẫu nhiên từ các kiểu dữ liệu trên
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))
    for i in range(digits_count):
        password.append(random.choice(digits))
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))
    # Nếu như mà độ dài của các kiểu kí tự không bằng độ dài pass:
    
    if characters_count < lenght:
        random.shuffle(characters)# Thêm một kí tự bất kì trong list character cho đủ độ dài
        for i in range(characters_count):
            password.append(random.choice(characters))
    # Xáo trộn lại password đã tạo cho chắc chắn :))
    random.shuffle(password)
    # Kèm theo ngày tháng lưu password
    today = datetime.now()
    # Tạo dữ liệu người dùng
    user_data = user_name + ': ' + "Password for "+ user_information + ': ' + ''.join(password) + " Day saved: " + str(today)
    # Định dạng từ list password thành chuỗi password và in ra
    print('Your password is: ',''.join(password))
    # Đường dẫn file text lưu dữ liệu 
    path = 'E:\Python\Password user data.txt'
    # Lưu password vô file txt
    with open(path, 'a') as file:
        file.write("\n"+ user_data)
    # Đọc file txt đó ra command
    """ with open(path,'r') as file:
        print(file.read()) """
# Ascii letters là các kí tự từ a -> z, từ A -> Z
# Digits là các số tự nhiên từ 0 -> 9
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list('!@#$%^&*()')
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
generate_random_password()

