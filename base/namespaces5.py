# >>> num = 10
# >>>
# >>> num.attr = 'объект во внутреннем пространстве имён'
# ...
# AttributeError: 'int' object has no attribute 'attr'
# >>>
# >>> num.__dict__
# ...
# AttributeError: 'int' object has no attribute '__dict__'. Did you mean: '__dir__'?


# >>> def func():
# ...     pass
# ...
# >>> func.attr = 'объект во внутреннем пространстве имён'
# >>>
# >>> func.__dict__
# {'attr': 'объект во внутреннем пространстве имён'}
# >>>
# >>> func.attr
# 'объект во внутреннем пространстве имён'
