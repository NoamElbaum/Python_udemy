# functions manipulation
def func():
    local = 8
    print(locals())
    print(globals())
    print(globals()['__name__'])

func()

def hello():
    print('Hello')
    def inside():
        return 'im inside'
    print(inside())
    return inside

hello()
greet = hello
greet()

x = hello()
print(x)
print(x())

def hi():
    return 'hi'

def other(func):
    print("HELLO")
    print(func())

other(hi)

#Decorators

def new_decorator(func):

    def wrap_func():
        print('code here before executing func')
        func()
        print('func() has been called')

    return wrap_func

def func_needs_decorator():
    print('needs a decorator')

func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()