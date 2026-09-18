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


def main():
    testar_entrada_valida()
    testar_valor_em_stock()

    print("Todos os testes passaram.")


if __name__ == "__main__":
    main()
