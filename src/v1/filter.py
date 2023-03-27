import re


def extract_information(message: str):
    pattern_general = re.compile(r'(PRINT)\n(GUIA) {1}(\d+)\n(PARA) {1}([a-zA-Z0-9_-]+)\n(.*)$', re.DOTALL)
    pattern_multiples_item = re.compile(r'\* (\w+) ([1-9]\d*)$')

    match = pattern_general.match(message)
    if match:
        list_match = match.groups()
        multiples_item = list_match[5].split("\n")
        for indivual_item in multiples_item:
            match = pattern_multiples_item.match(indivual_item)
            if not match:
                return "REVICE PORFAVOR LAS LINEAS DE:\n* DESCRIPCION_DE_ARTICULO CANTIDAD"
        return list_match, multiples_item
    else:
        return "FORMATO:\nPRINT\nGUIA\nPARA *LUGAR_DE_ENVIO*\n* DESCRIPCION_DE_ARTICULO CANTIDAD"
