#Ex1: crie um programa para rodar "python main.py --nome (nome)" em que
# o argumento seja obrigatório (ou requerido)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--nome", required=True)
argument = parser.parse_args()
