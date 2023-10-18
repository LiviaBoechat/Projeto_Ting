
def exists_word(word, queueInstance):
    results = []

    for data in queueInstance._data:
        occurrences_found = find_line(word, data["linhas_do_arquivo"])
        if occurrences_found:
            result = {
                "palavra": word,
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias": occurrences_found
            }
            results.append(result)
    return results


def find_line(word, lines):
    occurrences = []
    line_position = 1

    for line in lines:
        if word.lower() in line.lower():
            occurrence = {"linha": line_position}
            occurrences.append(occurrence)
        line_position += 1

    return occurrences


def search_by_word(word, queueInstance):
    occurrences = []

    for data in queueInstance._data:
        occurrences_found = find_line(word, data["linhas_do_arquivo"])
        if occurrences_found:
            result = {
                "palavra": word,
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias": {
                    "linha": occurrences_found,
                    "conteudo": data["linhas_do_arquivo"]
                }
            }
            occurrences.append(result)

    return occurrences
