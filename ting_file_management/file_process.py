from ting_file_management.file_management import txt_importer


import sys


def process(path_file, queueInstance):
    lines = txt_importer(path_file)
    for item in queueInstance._data:
        if item["nome_do_arquivo"] == path_file:
            return print("Arquivo já existente!")

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    queueInstance.enqueue(data)
    return print(data)


def remove(queueInstance):
    if len(queueInstance) == 0:
        return print("Não há elementos", file=sys.stdout)

    removed_item = queueInstance.dequeue()
    print(f"Arquivo {removed_item['nome_do_arquivo']} removido com sucesso")


def file_metadata(queueInstance, position):
    if position < 0 or position >= len(queueInstance):
        return print("Posição inválida", file=sys.stderr)

    metadata = queueInstance.search(position)
    print(metadata)
