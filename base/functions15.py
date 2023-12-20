# демонстрация бесперспективности сохранения анонимных функций в переменные (в глобальном пространстве имён)

from types import ModuleType, FunctionType

import functions12, functions14


def print_module_docs(module_obj: ModuleType) -> None:
    print(
        '\n'
        f' = динамически генерируемая документация к модулю {module_obj.__name__} = ',
        '',
        module_obj.__doc__,
        sep='\n'
    )
    for obj in module_obj.__dict__.values():
        if isinstance(obj, FunctionType):
            print(
                '',
                f'{obj.__name__}({obj.__annotations__}):',
                f'\t{obj.__doc__}',
                sep='\n'
            )
    print()


print_module_docs(functions12)
print_module_docs(functions14)
