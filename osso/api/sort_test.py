list_data = [
    ['ขอใบอนุญาตใหม่', 42],
    ['ขอใบแทนใบอนุญาต', 9],
    ['ขอใบเปลี่ยนแปลงใบอนุญาต', 2],
    ['ขอยกเลิกใบอนุญาต', 18],
]

print(list_data)

def sort_foo(x):
    return x[0]

list = sorted(list_data, key=sort_foo)
print(list)


