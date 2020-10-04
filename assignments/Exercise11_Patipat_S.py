row = int(input("row"))
for x in range(row) :
    row -= 1 #เก็บค่าความห่างและจะลดลงทีละ 1 ช่อง
    print((" " * row) + ("*" * (x * 2 + 1)))#แบ่ง*ให้เป็นเลขคี่