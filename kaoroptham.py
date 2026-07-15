name = input("ชื่อผู้สมัคร: ")
age = int(input("อายุ: "))
height = int(input("ส่วนสูง: "))
power = int(input("พละกำลัง: "))
money = int(input("เงินติดตัว: "))

if age >= 15 and height >= 160 and power >= 6 and money >= 67:
    if power >= 9 and money >= 50:
        print(name + " ได้รับตำแหน่ง: กัปตันทีม")
    elif power >= 7 and height >= 170:
        print(name + " ได้รับตำแหน่ง: ผู้ช่วยกัปตันทีม")
    elif power >= 5 and height >= 170:
        print(name + " ได้รับตำแหน่ง: ผู้ช่วยทีม")
else:
    print(name + " ไม่ผ่านการคัดกรอง")