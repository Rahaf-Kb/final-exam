#    (رقم المنتج، السعر)
products = [
    ["منتج 1", 10],
    ["منتج 2", 20],
    ["منتج 3", 30],
    ["منتج 4", 40],
    ["منتج 5", 50]
]

#  عرض المنتجات
print("اختر رقم المنتج:")
for i, item in enumerate(products, start=1):
    print(f"{i} - {item[0]}")

# أختيار رقم المنتج 
choice = int(input("اكتب الرقم: "))

# التحقق من الإدخال
if 1 <= choice <= 5:
    price = products[choice - 1][1]
    total_with_tax = price + (price * 0.15)
    print(f"سعر المنتج شامل الضريبة: {total_with_tax}")
else:
    print("رقم غير صحيح! يرجى اختيار رقم من 1 إلى 5.")
