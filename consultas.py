def procurar_por_codigo(produtos, codigo):
    codigo = codigo.strip().upper()

    for produto in produtos:
        if produto.codigo == codigo:
            return produto

    return None


def procurar_por_nome(produtos, texto):
    encontrados = []
    texto = texto.strip().upper()

    for produto in produtos:
        if texto in produto.nome.upper():
            encontrados.append(produto)
    return encontrados


def selecionar_stock_baixo(produtos):
    produtos_stock_baixo = []

    for produto in produtos:
        if produto.stock_baixo() is True:
            produtos_stock_baixo.append(produto)
    return produtos_stock_baixo
