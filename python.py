def f1(fun):
    def wraper(*args,**kwargs):
        print("befor")
        fun()
        print("After")
    return wraper

def f2():
    print("This is decorator")
f2=f1(f2)
f2()