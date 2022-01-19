try:
    print(1/0)
except ValueError:
    print("Это ошибка значения")
finally:
    print("Это будет напечатано в любом случае.")
