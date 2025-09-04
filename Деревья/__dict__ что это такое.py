class A:
    n = 10
    def f(self, x):
        return x + self.n
z = A()

print(z.__dict__)

print()
print('присвоим Z новое значение = 8')    
z.n = 8
print(z.__dict__)   