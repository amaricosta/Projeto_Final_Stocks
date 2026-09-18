from math import isclose
from modelos import Produto
from consultas import procurar_por_nome


def testar_entrada_valida():
    produto = Produto(
        "T001", "Caderno", "Papelaria",
        10, 3, 2.50
    )

    aceite = produto.registar_entrada(4)

    assert aceite is True
    assert produto.quantidade == 14
    assert produto.preco_unitario == 2.50


def testar_valor_em_stock():
    produto = Produto(
        "T002", "Caneta", "Papelaria",
        3, 1, 0.10
    )

    assert isclose(
        produto.valor_em_stock(), 0.30, abs_tol=1e-9
    )

    produto.registar_entrada(2)

    assert isclose(
        produto.valor_em_stock(), 0.50, abs_tol=1e-9
    )


# Parte C - Testes do Programa


def testar_saida_superior_stock():
    produto = Produto("T003", "Borracha", "Papelaria", 10, 5, 0.30)

    aceite = produto.registar_saida(12)

    assert aceite is False
    assert produto.quantidade == 10


def testar_saida_igual_stock():
    produto = Produto("T004", "Fita Cola", "Papelaria", 5, 2, 2.50)

    aceite = produto.registar_saida(5)

    assert aceite is True
    assert produto.quantidade == 0


def testar_quantidade_igual_minimo():
    produto = Produto("T005", "Rato", "Informática", 10, 10, 9.8)

    resultado = produto.stock_baixo()

    assert resultado is False
    assert produto.quantidade == 10


def testar_pesquisa_por_parte_do_nome():
    produtos = [
        Produto("T001", "Rato", "Informática", 10, 10, 9.8),
        Produto("T002", "Caneta", "Papelaria", 3, 1, 0.10),
        Produto("T003", "Borracha", "Papelaria", 10, 5, 0.30),
        Produto("T004", "Fita Cola", "Papelaria", 5, 2, 2.50),
        Produto("T005", "Borracha Colorida", "Papelaria", 10, 3, 0.50)
    ]

    encontrados = procurar_por_nome(produtos, "boRrAChA")

    assert encontrados == [produtos[2], produtos[4]]


def testar_pesquisa_sem_correspondencia():
    produtos = [
        Produto("T001", "Rato", "Informática", 10, 10, 9.8),
        Produto("T002", "Caneta", "Papelaria", 3, 1, 0.10),
        Produto("T003", "Borracha", "Papelaria", 10, 5, 0.30),
        Produto("T004", "Fita Cola", "Papelaria", 5, 2, 2.50)
    ]

    encontrados = procurar_por_nome(produtos, "Tesoura")

    assert encontrados == []


def main():
    testar_entrada_valida()
    testar_valor_em_stock()
    testar_saida_superior_stock()
    testar_saida_igual_stock()
    testar_quantidade_igual_minimo()
    testar_pesquisa_por_parte_do_nome()
    testar_pesquisa_sem_correspondencia()

    print("Todos os testes passaram.")


if __name__ == "__main__":
    main()
