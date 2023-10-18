import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            print("Formato inválido", file=sys.stderr)
            return []

        with open(path_file, "r") as file:
            lines = file.read().split("\n")
            return lines
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []


# testes


path_to_txt = "caminho/do/arquivo.txt"
lines = txt_importer(path_to_txt)
print(lines)
