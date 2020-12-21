#LEGB规则（Local,Enclosed,Global,Built in）

def outer():
    str="outer"
    def inner():
        str ="inner"
        print(str)

    inner()

outer()