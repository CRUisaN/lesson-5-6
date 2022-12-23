# class Hello:
#     def __init__(self):
#         print("Hello")
# class Hello_World(Hello):
#     def __init__(self):
#         super().__init__()
#         print("World")
# hello_world=Hello_World()
#
# class Class1:
#     var=20
#     def __init__(self):
#         self.var=10
#
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)
# clas=Class2()
#
# class C1:
#     pass
# class C2:
#     pass
#
# class CA(C1,C2):
#     pass
class QUADRAT:
    def ploscha(self,a):
        return a*a
qua=QUADRAT()
print(qua.ploscha(100000000))