class A:
    n = 10
    def f(obj,x):
        return x + obj.n
a = A()
# a.n = 5
print(a.f(20))

b = A()
