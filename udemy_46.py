
# xip関数について

days = ['Mon', 'Tue', 'Wed']
fruit = ['Apple', 'Banana', 'Orange']
drinks = ['Coffee', 'Tea', 'Beer']

# それぞれのリストから値を取り出す
for i in range(len(days)):
    print(days[i], fruit[i], drinks[i])


# zip関数を用いる事で複数のリストから同時に値を取り出す事ができる。
for day, fruits, drink in zip(days, fruit, drinks):
    print(day, fruits, drink)