# 装饰器使用

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2019-04-20')

now()
# now = log(now)


def log(text):
    def decorator(func):
        def wrapper(*args,**kw)
            print('%s %s()' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2019-04-20')


now()
# now = now(wrapper(decorator()))
