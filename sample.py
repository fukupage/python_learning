# coding: utf-8
#クラスの継承----------------------------------------------------
class User:
  def __init__(self, name):
    self.name = name
  def say_hi(self):
    print("ハーイ {0}".format(self.name))

class AdminUser(User):
  def __init__(self, name, age):
    super(AdminUser, self).__init__(name)
    self.age = age

  def say_hello(self):
    print("ハーイ {0}({1})".format(self.name, self.age))
  def say_hi(self):
    print("[admin]ハーイ {0}".format(self.name))

bob = AdminUser("bob",23)
print(bob.name)
bob.say_hi()
bob.say_hello()

#アクセス制限----------------------------------------------------
# class User:
#   count = 0
#   def __init__(self, name):
#     User.count += 1
#     self.__name = name

#   def say_hi(self):  #インスタンスメソッド
#     print("ハーイ {0}".format(self.__name))

#   @classmethod
#   def show_info(cls): #CLASSメソッド
#     print("{0} instances".format(cls.count))

# tom = User("tom")
# bob = User("bob")

# # print(tom.__name)#こちらではアクセスできないが
# print(tom._User__name)#こちらだとアクセスできる

# tom.say_hi()
# bob.say_hi()

# User.show_info()


#関数（メソッド）----------------------------------------------------
# class User:
#   count = 0
#   def __init__(self, name):
#     User.count += 1
#     self.name = name

#   def say_hi(self):  #インスタンスメソッド
#     print("ハーイ {0}".format(self.name))

#   @classmethod
#   def show_info(cls): #CLASSメソッド
#     print("{0} instances".format(cls.count))

# tom = User("tom")
# bob = User("bob")

# tom.say_hi()
# bob.say_hi()

# User.show_info()



#CLASS変数----------------------------------------------------
# class User:
#   count = 0
#   def __init__(self, name):
#     User.count += 1
#     self.name = name

# print(User.count)
# tom = User("tom")
# bob = User("bob")
# print(User.count)


# print(tom.name + "さんですね！")
# print(tom.count)
# print(bob.name + "さんですね！")
# print(bob.count)


# #CLASS----------------------------------------------------
# class User:
#   def __init__(self,name):
#     self.name = name

# tom = User("tom")
# bob = User("bob")

# print(tom.name + "さんですね！")
# print(bob.name + "さんですね！")


# class User:
#     pass

# tom = User()
# tom.name = "tom"
# tom.score = 20

# bob = User()
# bob.name = "bob"
# bob.level = 5

# print(tom.name)
# print(tom.score)
# print(bob.name)
# print(bob.level)



#変数のスコープ----------------------------------------------------
# msg = "hello!"

# def say_hi():
#     global msg
#     msg="hello! AGAIN"
#     print(msg)

# say_hi()
# print(msg)


# msg = "hello!"

# def say_hi():
#     msg = "hi"
#     print(msg)

# say_hi()
# print(msg)
