# データ型 -------------------------------------------------------------------------------
#リスト型とタプル・集合型・辞書型
#タプル
items = (50, "Rei", 3.141592)
print(items[0])
print(items[1])
print(items[2])

print("------------------------------------------------------------------------------------")

print(list((1, 3, 5)))
print(tuple([1, 3, 5]))

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
