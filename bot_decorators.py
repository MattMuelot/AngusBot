import datetime
import threading


class BotDecorators:
    """All custom decorators for the app will be housed here."""
    @classmethod
    def logging(cls, func):
        """Logs output to a text file in the project directory."""
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            with open('log.txt', 'a') as f:
                f.write(f'"{func.__name__}" executed - {datetime.datetime.today()}\n')
        return wrapper

    @classmethod
    def bot_threader(cls, func):
        threads = []

        def wrapper(*args, **kwargs):
            t = threading.Thread(target=func, args=args, kwargs=kwargs)
            threads.append(t)
            t.start()

        for thread in threads:
            thread.join()
        return wrapper
