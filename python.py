def f1(fun):
    def wraper(*args,**kwargs):
        print("befor")
        fun()
        print("After")
    return wraper
@f1
def f2():
    print("This is decorator")
f2()