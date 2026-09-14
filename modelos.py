class Produto:
    """Representa um produto da loja."""

    def __init__(
        self, codigo, nome, categoria, quantidade, minimo
    ):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.minimo = minimo
