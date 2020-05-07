import datetime


class BotDecorators:
    @classmethod
    def logging(cls, func):
        def wrapper(*args):
            func(*args)
            with open('log.txt', 'a') as f:
                f.write(f'{func.__name__} executed - {datetime.datetime.today()}\n')
        return wrapper
