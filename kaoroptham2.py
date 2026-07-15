quantity = int(input("จำนวนปืนที่รับมาขาย: "))
cost_price = float(input("ต้นทุนของปืนที่รับมา (บาท/กระบอก): "))
selling_price = float(input("ราคาขายของปืน (บาท/กระบอก): "))
team_members = int(input("จำนวนลูกน้องในทีมที่ไปทำงาน (คน): "))

total_cost = quantity * cost_price
print(f"ต้นทุนรวม: {total_cost} บาท")

total_revenue = quantity * selling_price
print(f"รายได้รวม: {total_revenue} บาท")

profit = total_revenue - total_cost
print(f"กำไรที่ได้: {profit} บาท")

WHT = profit * 20 / 100
print(f"จำนวนเงินที่หักไปให้บอส: {WHT} บาท")

salary_per_member = (profit - WHT) / team_members
print(f"เงินเดือนที่ลูกน้องแต่ละคนจะได้รับ: {salary_per_member} บาท")