from argparse import ArgumentParser

from server import run_server
from client import run_client


if __name__ == "__main__":
    parser = ArgumentParser(description="Gerenciador de Fila")
    parser.add_argument("--as-server", type=bool, default=False)

    args = parser.parse_args()

    if args.as_server:
        run_server()
    else:
        run_client()
