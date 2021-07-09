# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")

# TODO: your code here
all_brands=[]
for i in items:
    all_brands.append(i.get("brand"))
list_brand = set(all_brands)
print(list_brand)

print("На складе больше всего товаров брэнда(ов): ")


# TODO: your code here
count_items = {x: all_brands.count(x) for x in list_brand}
#print(count_items.items())

max_count = 0
for brand, summa in count_items.items():
    if summa >= max_count:
        max_count = summa
for brand, summa in count_items.items():
    if summa == max_count:
        print(brand)


print("На складе самый дорогой товар брэнда(ов): ")

# TODO: your code here
max_price = 0
for rich in items:
    if rich.get("price") >= max_price:
        max_price = rich.get("price")
for rich in items:
    if rich.get("price") == max_price:
        print(f"{rich.get("brand")}")
