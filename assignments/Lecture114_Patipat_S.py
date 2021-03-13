from forex_python.converter import CurrencyRates
c = CurrencyRates()

#โปรแกรมแลกเปลี่ยนเงินธนาคาร

trade1 = input("สกุลเงินที่ต้องการแลก : ").upper()
trade2 = input("ไปยังสกุลเงินที่ต้องการแลก : ").upper()
money = int(input("จำนวนเงิน : "))

exchange = round(c.convert(trade1, trade2, money), 2) #ปัดทศนิยมเหลือ 2 ตำแหน่ง
fee = exchange * (1.5/100) #ค่าธรรมเนียม 1.5%

try:
    print("อัตตราแลกเปลี่ยนปัจจุบัน : ", exchange)
    print("ค่าธรรมเนียม : ", fee)
    print("เงินสุทธิ : ", round(exchange - fee, 2)) #ปัดทศนิยมเหลือ 2 ตำแหน่ง
except:
    print("กรุณาใส่ชื่อสกุลเงินให้ถูกต้อง")
