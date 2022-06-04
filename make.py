from argparse import ArgumentParser
import os


def start():
    os.system("python -m pip install virtualenv")
    os.system("python -m virtualenv .venv")
    os.system("python .venv/Scripts/activate_this.py")
    os.system("python -m pip install -r requirements.txt")


def test():
    os.system("python -m pytest --verbose")


if __name__ == "__main__":
    parser = ArgumentParser(description="Gerenciador de Fila")
    parser.add_argument("start", type=bool, default=False, required=False)
    parser.add_argument("test", type=bool, default=False, required=False)

    args = parser.parse_args()

    if args.start:
        start()

    elif args.test:
        test()
