import datetime


class BotDecorators:
    """All custom decorators for the app will be housed here."""
    @classmethod
    def logging(cls, func):
        """Logs output to a text file in the project directory."""
        def wrapper(*args, **kwargs):
            total_chars = func(*args, **kwargs)
            with open('log.txt', 'a') as f:
                curr_date = datetime.datetime.today()
                f.write(f'"{func.__name__}" executed in {total_chars} characters - {str(curr_date)[0:19]}\n')
        return wrapper

    @classmethod
    def on_error(cls, func):
        """Decorator for error handling."""
        def wrapper(*args, **kwargs):
            pass
