# package
# import samplepackage.user
# bob = samplepackage.user.AdminUser("bob", 23)

# import samplepackage.user as bobmodule
# bob = bobmodule.AdminUser("bob", 23)

from samplepackage.user import AdminUser
bob = AdminUser("bob", 23)

print(bob.name)
bob.say_hi()
bob.say_hello()


# # import user
# # from user import AdminUser
# from user import AdminUser,User

# # bob = user.AdminUser("bob",23)
# bob = AdminUser("bob",23)
# tom = User("tom")

# print(bob.name)
# bob.say_hi()
# bob.say_hello()

# print(tom.name)
# tom.say_hi()
