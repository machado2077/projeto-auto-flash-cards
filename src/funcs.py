import os, json, shelve


def get_from_txt(file="frases.txt"):
    """
        Função que obtém frases de um arquivo .txt. Essa obtenção se dá orientada ao caractere de quebra de linha \\n. A função também realiza tratamento de espaços em branco a cada frase obtida e, se houver no arquivo apenas espaços em branco, o retorno será uma lista vazia.

        Keyword Arguments:
            file {str} -- nome do arquivo que contém as frases. 
            (default: {'frases.txt'})

        Returns:
            list -- lista contendo as frases obtidas do arquivo."""
    while True:
        if os.path.isfile(file) and str(file).endswith(".txt"):
            with open(file, "r") as f:
                phrases = [
                    line.strip() for line in f.read().split("\n") if line.strip() != ""
                ]
                return phrases
        else:
            print(f'\n\n"{file}" não é um arquivo ou um path de arquivo válido.')
            file = input(
                "\nInsira um arquivo existente no mesmo path da VENV ou insira um path de arquivo válido: "
            )


def get_imgs_name(folder_path):
    if not os.path.isdir(folder_path):
        print(f'"{folder_path}" não é um diretório.')
    files = []
    for file in os.listdir(folder_path):
        if file.endswith(".png") or file.endswith(".jpg"):
            files.append(os.path.join(folder_path, file))
    return files


def remove_imgs(folder_path):
    if not os.path.isdir(folder_path):
        print(f'"{folder_path}" não é um diretório.')
    for file in os.listdir(folder_path):
        if file.endswith(".png") or file.endswith(".jpg"):
            os.unlink(os.path.join(folder_path, file))


def remove_imgs_list(imgs_list):
    for img_path in imgs_list:
        if os.path.isfile(img_path) and (
            img_path.endswith(".png") or img_path.endswith(".jpg")
        ):
            os.unlink(img_path)


def text_source_back(source, source_before):
    with open(source, "w") as src:
        for phrse in source_before:
            src.write(f"{phrse}\n")


def db_cards_back(source, key, source_before):
    with shelve.open(source) as db:
        db[key] = source_before

