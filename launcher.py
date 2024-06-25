import os
import sys
import configparser
from tkinter import messagebox

def main():
    config = configparser.ConfigParser()
    config.read('mota.ini')

    if 'Mota' not in config:
        messagebox.showinfo("Error", "'Mota' section not found in mota.ini.")
        sys.exit(1)

    if 'Script' not in config['Mota']:
        messagebox.showinfo("Error", "'Script' not found in 'Mota' section.")
        sys.exit(1)

    core_script = config['Mota']['Script']

    if not os.path.exists(core_script):
        messagebox.showinfo("Error", f"{core_script} not found.")
        sys.exit(1)

    with open(core_script, 'r', encoding='utf-8') as f:
        code = compile(f.read(), core_script, 'exec')
        exec(code, globals())

if __name__ == '__main__':
    main()
