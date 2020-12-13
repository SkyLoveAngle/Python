#lambda表达式和匿名函数
f=lambda a,b,c:a+b+c
print(f)
print(f(2,3,4))

g=[lambda a:a*2,lambda b:b*3,lambda c:c*4]
print({g[0](6),g[1](7),g[2](8)})
k=g[0](6)
print(k)