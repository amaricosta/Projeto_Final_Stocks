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


def procurar_por_categoria(produtos, categoria):
    categoria = categoria.strip().casefold()
    encontrados = []

    for produto in produtos:
        if produto.categoria.casefold() == categoria:
            encontrados.append(produto)

    return encontrados


def agrupar_por_categoria(produtos):
    categorias = {}

    for produto in produtos:
        chave = produto.categoria.casefold()

        if chave not in categorias:
            categorias[chave] = {
                "nome": produto.categoria,
                "produtos": 0,
                "unidades": 0,
                "valor": 0.0,
            }
        grupo = categorias[chave]

        grupo["produtos"] += 1
        grupo["unidades"] += produto.quantidade
        grupo["valor"] += produto.valor_em_stock()

    return categorias
