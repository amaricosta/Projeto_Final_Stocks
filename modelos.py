class Produto:
    """Representa um produto da loja."""

    def __init__(
        self, codigo, nome, categoria, quantidade, minimo, preco_unitario
    ):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.minimo = minimo
        self.preco_unitario = preco_unitario


def valor_em_stock(self):
    # Devolve o valor do stock ao preço de referência.
    return self.quantidade * self.preco_unitario
