def guardar_relatorio(nome_ficheiro, texto):
    """Guarda um relatório de texto em UTF-8."""
    with open(
        nome_ficheiro, "w", encoding="utf-8"
    ) as ficheiro:
        ficheiro.write(texto)


def ler_relatorio(nome_ficheiro):
    """Devolve o texto de um relatório em UTF-8."""
    with open(
        nome_ficheiro, "r", encoding="utf-8"
    ) as ficheiro:
        return ficheiro.read()
