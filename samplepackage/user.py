# モジュール化----------------------------------------------------

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
