from pathlib import Path
from sys import path


base_dir = Path(path[0])

file3_path = base_dir / 'files3'
log_path = base_dir / 'files3.log'


lines = [
    'Tic\n',
    'Tac\n',
    'Tic\n',
    'Tac\n',
]
with file3_path.open('w', encoding='utf-8') as fileout:
    fileout.writelines(lines)

text = '''ещё
какой-то
текст'''

log_path.write_text(text, encoding='utf-8')
