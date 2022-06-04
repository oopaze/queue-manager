from argparse import ArgumentParser
import os, platform


def setup():
    os.system("python3 -m pip install virtualenv")
    os.system("python3 -m virtualenv .venv")

    if platform.system() == "Windows":
        os.system("python3 .venv/Scripts/activate_this.py")
    else:
        os.system(". .venv/bin/activate")

    os.system("python -m pip install -r requirements.txt")


def test():
    os.system("python3 -m pytest --verbose")


if __name__ == "__main__":
    parser = ArgumentParser(description="Gerenciador de Fila")
    parser.add_argument("--setup", type=bool, default=False, required=False)
    parser.add_argument("--test", type=bool, default=False, required=False)

    args = parser.parse_args()

    if args.setup:
        setup()

    elif args.test:
        test()
