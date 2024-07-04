"""
Controller (MVC): управляющий модуль, точка входа.
"""

import model
import view


def start() -> None:
    view.greeting()


def get_command() -> None:
    while True:
        match view.get_command().split():
            case ['all']:
                get_all_people()
            case ['lang', lang]:
                lang = lang.upper()
                if lang not in model.all_langs:
                    view.wrong_lang(model.all_langs)
                else:
                    get_people_by_lang(lang)
            case ['quit']:
                break


def get_all_people() -> None:
    view.people(str(pers) for pers in model.storage)


def get_people_by_lang(lang: str) -> None:
    view.people(str(pers) for pers in model.storage if lang in pers.langs)


def end() -> None:
    view.bye()



def main() -> None:
    """Точка входа."""
    model.storage = model.FileIO.read_all_people()
    start()
    if view.__name__.endswith('cli'):
        get_command()
    end()



if __name__ == '__main__':
    main()

