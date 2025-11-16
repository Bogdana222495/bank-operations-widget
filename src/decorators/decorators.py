
import functools
import datetime
import os


def log(filename=None):
    """
    Декоратор, логирующий вызов функции и её результат.
    :param filename: Имя файла для логов. Если None — вывод в консоль.
    :return: Декорированная функция
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            func_name = func.__name__

            # Форматируем аргументы
            args_str = str(args)
            kwargs_str = str(kwargs)

            try:
                result = func(*args, **kwargs)
                message = f"{func_name} ok\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"{start_time} - {message}")
                else:
                    print(message.strip())
                return result
            except Exception as e:
                message = f"{func_name} error: {type(e).__name__}. Inputs: {args_str}, {kwargs_str}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"{start_time} - {message}")
                else:
                    print(message.strip())
                raise  # Перебрасываем исключение

        return wrapper

    return decorator