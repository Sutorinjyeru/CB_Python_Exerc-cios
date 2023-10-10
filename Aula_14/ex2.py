#Ex2: Faça um codigo que permita o uso de 2 argparsers ("age", "city")
# se for passado idade/cidade printe na tela o valor. Se não, printe
# "Nenhuma mensagem fornecida.".

import argparse

parser = argparse.ArgumentParser(exit_on_error=False)
parser.add_argument("--age", required=False)
parser.add_argument("--city", required=False)
try:
    argument = parser.parse_args()
except argparse.ArgumentError:
    print('Nenhuma mensagem fornecida.')

