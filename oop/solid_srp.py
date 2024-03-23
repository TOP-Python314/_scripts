"""Single Responsibility Principle — Принцип Единственной Ответственности"""

from datetime import datetime as dt
from pathlib import Path
from sys import path


class Journal(dict):
    """
    Ведение журнала, работа с записями.
    """
    _default_format: str = '%Y-%m-%d %H:%M:%S'
    # атрибут нарушает SRP — не относится к основной ответственности Журнала
    # _default_path: Path = Path(path[0]) / 'journal.log'
    
    def add_entry(self, entry: str) -> None:
        """Добавляет запись в журнал."""
        self[dt.now()] = entry
    
    def __repr__(self):
        return '\n'.join(
            f'{timestamp:{self._default_format}} — {entry}'
            for timestamp, entry in self.items()
        )
    
    # метод нарушает SRP — не относится к основной ответственности Журнала
    # def export_log_file(self, log_path: str | Path | None):
    #     """Записывает строковое представление журнала в файл."""
    #     if log_path is None:
    #         log_path = self._default_path
    #     
    #     with open(log_path, 'w', encoding='utf-8') as fileout:
    #         fileout.write(self.__repr__())


# решение без нарушения SRP — функциональность записи информации в файл выделяется в отдельную сущность
class FileSystemIO:
    """
    Работа с путями, взаимодействие с файловой системой.
    """
    _default_journal_path = Path(path[0]) / 'journal.log'
    
    @classmethod
    def export_log_file(
            cls,
            entries_representations: str,
            log_path: str | Path | None,
    ):
        """Записывает строковое представление журнала в файл и возвращает путь к файлу."""
        if log_path is None:
            log_path = cls._default_journal_path
        
        with open(log_path, 'w', encoding='utf-8') as fileout:
            fileout.write(entries_representations)
        
        return log_path

