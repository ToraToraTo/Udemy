
# 集合内包表記について

s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

print("######################################")
# 上記の集合を内包表記で記述する。

s = {i for i in range(10) if i % 2 == 0}
print(s)