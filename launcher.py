import os
import sys
import configparser

def main():
    config = configparser.ConfigParser()
    config.read('mota.ini')

    if 'Mota' not in config:
        print("Error: 'Mota' section not found in mota.ini.")
        sys.exit(1)

    if 'Script' not in config['Mota']:
        print("Error: 'Script' not found in 'Mota' section.")
        sys.exit(1)

    core_script = config['Mota']['Script']

    if not os.path.exists(core_script):
        print(f"Error: {core_script} not found.")
        sys.exit(1)

    with open(core_script, 'r') as f:
        code = compile(f.read(), core_script, 'exec')
        exec(code, globals())

if __name__ == '__main__':
    main()
