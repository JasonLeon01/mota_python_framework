import os
import sys
import configparser
from tkinter import Tk, messagebox
import logging

def main():
    root = Tk()
    root.withdraw()
    config = configparser.ConfigParser()
    config.read('mota.ini')
    
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )
    
    os.environ['DEBUG'] = 'True'
    
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
        exec(code, globals(), locals())

if __name__ == '__main__':
    main()
