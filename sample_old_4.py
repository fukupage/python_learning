# イテレータ -------------------------------------------------------------------------------

# scores = [40,50,70,90,60]
# it = iter(scores)
# print(next(it))
# print("-------------------------------------------------------------------")
# print(next(it))
# print("-------------------------------------------------------------------")
# print("Hello World!!")
# print("-------------------------------------------------------------------")
# print(next(it))
# print("-------------------------------------------------------------------")
# print(next(it))
# print("-------------------------------------------------------------------")
# print(next(it))
# print("-------------------------------------------------------------------")

def get_infinate(): #ジェネレーター
  i = 0
  while True:
    yield i * 2
    i += 1

g = get_infinate()
print(next(g))
print("-------------------------------------------------------------------")
print(next(g))
print("-------------------------------------------------------------------")
print(next(g))







# # 辞書型 -------------------------------------------------------------------------------
# sales = {"Rei":200,"Fukuda":150}
# print(sales["Rei"])
# print(sales["Fukuda"])
# print("-------------------------------------------------------------------")
# sales["Rei"] = 350
# sales["Fukuda"] = 300
# print(sales["Rei"])
# print(sales["Fukuda"])
# print(sales)
# print("-------------------------------------------------------------------")
# sales["Bowworks"] = 600
# # del(sales["Rei"])
# # del(sales["Fukuda"])
# print(sales["Bowworks"])
# print(sales)
# print("-------------------------------------------------------------------")
# for key, value in sales.items():
#   print("{0}:{1}".format(key,value))

# 集合型 -------------------------------------------------------------------------------
# a = set([5,8,9,3])

# print(a)
# print(len(a))
# print(8 in a)
# print(5 in a)
# a.add(10)
# a.add(25)
# a.remove(9)
# print(a)
# print(len(a))

# a = {9,8,3,4,6}
# b = {10,4,3,8,25}

# print(a)
# print(b)
# print(a | b)
# print(a & b)
# print(a - b)


# スライス -------------------------------------------------------------------------------
# scores = [40,50,90,80,60]

# print(scores[1:4])
# print(scores[:3])
# print(scores[3:-1])
# print(scores[3:])
# print(scores[-3:])

# s = "Hello_World!"

# print(s[1:4])
# print(s[:3])
# print(s[3:-1])
# print(s[3:])
# print(s[-3:])


# # データ型 -------------------------------------------------------------------------------
# #リスト型とタプル・集合型・辞書型
# #タプル
# items = (50, "Rei", 3.141592)
# print(items[0])
# print(items[1])
# print(items[2])

# print("------------------------------------------------------------------------------------")

# print(list((1, 3, 5)))
# print(tuple([1, 3, 5]))

# #リスト型
# scores = [40,50]
# print(len(scores))
# print(scores[0])
# print(scores[1])
# scores[0] = 100
# scores[1] = 35
# scores.append(1352)
# print("-------------------------------")

# print(scores[0])
# print(scores[1])
# print(scores[2])
# print("-------------------------------")

# for score in scores:
#   print(score)

# print("-------------------------------")

# for i, score in enumerate(scores):
#   print("{0}/{1}".format(i, score) )


# 例外処理 -------------------------------------------------------------------------------
# class MyException(Exception):
#     pass

# def div(a, b):
#     try:
#         if(b < 0):
#             raise MyException("まいなすじゃないお")
#         print(a/b)
#     except MyException as e:
#         print(e)
#     except ZeroDivisionError:
#         print("すとろんぐぜろじゃわれない")
#     else:
#         print("すとぜろはおいしい")
#     finally:
#         print("-- ときはきた --")


# div(10, -3)
# div(10, 3)
# div(10, 0)
