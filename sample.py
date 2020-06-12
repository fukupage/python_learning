# 内包表記--------------------------------------------------------------------

# print([i for i in range (10)])
# print([i * 3 for i in range (10)])
# print([i * 3 for i in range (10) if i % 2 == 0])

#ジェネレーターとして
# print((i * 3 for i in range (10) if i % 2 == 0))
print(i * 3 for i in range (10) if i % 2 == 0)
print({i * 3 for i in range (10) if i % 2 == 0})

# #filter(関数,イテレータ)--------------------------------------------------------------------

# # def is_even(n):
# #   return n % 2 == 0

# # print(list(filter(is_even, range(10))))
# print(list(filter(lambda n: n % 2 == 0, range(100))))

#map(関数,イテレータ)--------------------------------------------------------------------

# # def triple(n):
# #   return n * 3

# # print(list(map(triple,[1,2,3])))

# #lambda 引数:処理
# print(list(map(lambda n:n * 3, [1,2,3])))
