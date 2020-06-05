# coding: utf-8
"""
print("はろーわーるど");
print("Hello World AGAIN!");


# 変数は再代入できるが、大文字で書かれている変数は定数として扱う慣例がある。
MAIL = "hoge@fuga.bar"
print(MAIL)

msg = "Hello World!";
print(msg);

msg = "Hello World! AGAIN!!";
print(msg);

# 文字列
s = "hoge hoge fuga fuga bar bar\nhoge hoge fuga fuga bar bar\thoge hoge fuga fuga bar bar";

# html =
# <html>
# <head></head>
# <body></body>
# <header></header>
# <main></main>
# <footer></footer>
# </html>;

# print(s);
# print(html);

# #数値
# i = 1; //整数
# f = 23.4;　//浮動小数点
# flag = true //論理値


x = 10;
print (x / 3);
print (x // 3);
print (x % 3);
print (x ** 3);
print (x * 3);
print (x + 3);
print (x - 3);
x += 22;
print (x);

print(True and False);
print(True or False);
print(not True);

print("Hello " + "わーるど");
print("Hello\t" * 3);

"""

# name = "fukuda"
# score = 52.8

# # print("名前:　%s, 特典: %f" % (name, score))
# # print("名前:　%-10s, 特典: %10.2f" % (name, score))
# print("名前:　{0}, 特典: {1}".format(name, score))
# print("名前:　{0:<10s}, 特典: {1:>10.2f}".format(name, score))

# score = int(input("score ?"))
# if score > 80:
#     print("Great!");
# elif score >60:
#     print("Good")
# else:
#     print("ummmm...")
# print("Great!" if score > 80 else "ummm...")

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("print end")

# for i in range(10):
# # for i in range(0,10):
#     if i == 5:
#         # break
#         continue
#     print(i)
# else:
#     print("- - foe - -")

# def say_hi():
#     print("hi!!!")
# say_hi()
# def say_hi(name, age=20):
#     print("hi!!! {0} ({1})".format(name, age))
# say_hi("rei", 23)
# say_hi("fuku", 49)
# say_hi("jobs")
# say_hi(age = 99, name = "kame")


# def say_hi():
#     pass
#     # print("hi")
#     # return "hi"
# msg = say_hi()
# print(msg)

msg = "hello"
msg2 = "world"
def say_hi():
  global msg2 #グローバル変数を書き換えたい場合、スコープ内でグローバル変数を扱う宣言をする。
  msg = "hi"
  msg2 = "Again"
  print(msg)
  print(msg2)
say_hi()
print("-----------------------------")
print(msg)
print(msg2)
