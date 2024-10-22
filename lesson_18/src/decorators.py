import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')

console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def logging_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"The arguments of the function: {args}")
        logger.info(f"The result of the function: {result}")
        return result
    return wrapper


def handles_exceptions_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ValueError as ve:
            print(f"!!!ValueError: {ve}")
        except TypeError as te:
            print(f"!!!TypeError: {te}")
        except OSError as ose:
            print(f"!!!OSError: {ose}")
        except Exception as e:
            print(f"!!!Exception: {e}")
        except BaseException as e:
            print(f"!!!BaseException: {e}")

    return wrapper
