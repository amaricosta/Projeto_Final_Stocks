from math import isfinite
from modelos import Produto
import consultas


def apresentar_menu():
    print("\nGESTÃO DE STOCKS")
    print("1 — Registar produto")
    print("2 — Listar produtos")
    print("3 — Pesquisar produtos")
    print("4 — Registar entrada de stock")
    print("5 — Registar saída de stock")
    print("6 — Consultar produtos com stock baixo")
    print("7 — Consultar estatísticas")
    print("8 — Guardar relatório de stock")
    print("9 — Ler o último relatório guardado")
    print("0 — Sair")


def main():
    produtos = []

    while True:
        apresentar_menu()
        opcao = input("Opção: ").strip()

        if opcao == "0":
            print("Programa terminado.")
            break

        elif opcao == "1":
            registar_produto(produtos)

        elif opcao == "2":
            mostrar_produtos(produtos)

        elif opcao == "3":
            pesquisar_produtos(produtos)

        elif opcao == "4":
            movimentar_stock(produtos, "entrada")

        elif opcao == "5":
            movimentar_stock(produtos, "saida")

        elif opcao in (
            "6", "7", "8", "9"
        ):
            print("Funcionalidade ainda não implementada.")

        else:
            print("Opção inválida.")


def ler_texto(mensagem):
    """Lê texto não vazio."""
    while True:
        texto = input(mensagem).strip()

        if texto:
            return texto

        print("Preencha este campo com texto não vazio.")


def ler_inteiro(mensagem, minimo):
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("Introduza um número inteiro.")
            continue

        if valor >= minimo:
            return valor

        print(
            f"Introduza um valor igual ou superior a {minimo}."
        )


def ler_preco(mensagem):
    while True:
        texto = input(mensagem).strip().replace(",", ".")

        try:
            valor = float(texto)
        except ValueError:
            print("Introduza um preço válido.")
            continue

        if isfinite(valor) and valor >= 0:
            return round(valor, 2)

        print("O preço deve ser finito e não negativo.")


def registar_produto(produtos):
    codigo = ler_texto("Código: ").upper()

    if consultas.procurar_por_codigo(produtos, codigo) is not None:
        print("Já existe um produto com esse código.")
        return

    nome = ler_texto("Nome: ")
    categoria = ler_texto("Categoria: ")
    quantidade = ler_inteiro("Quantidade inicial: ", 0)
    minimo = ler_inteiro("Stock mínimo: ", 0)
    preco = ler_preco("Preço unitário: ")

    produto = Produto(
        codigo, nome, categoria,
        quantidade, minimo, preco
    )

    produtos.append(produto)

    print("Produto registado.")


def formatar_euros(valor):
    return f"{valor:.2f}".replace(".", ",") + " €"


def descrever_produto(produto):
    preco = formatar_euros(produto.preco_unitario)
    valor = formatar_euros(produto.valor_em_stock())

    return (
        f"{produto.codigo} - {produto.nome} "
        f"({produto.categoria})\n"
        f"Quantidade: {produto.quantidade} | "
        f"Mínimo: {produto.minimo}\n"
        f"Preço unitário: {preco} | Valor em stock: {valor}"
    )


def mostrar_produtos(
    produtos,
    mensagem_vazia="Não existem produtos registados."
):
    if not produtos:
        print(mensagem_vazia)
        return

    for numero, produto in enumerate(produtos, start=1):
        print(f"\n{numero}. {descrever_produto(produto)}")


def pesquisar_produtos(produtos):
    if not produtos:
        print("Não existem produtos registados.")
        return

    print("1 — Código")
    print("2 — Parte do nome")
    print("3 — Categoria")
    print("0 — Voltar")

    opcao = input("Pesquisar por: ").strip()

    if opcao == "0":
        return
    if opcao == "1":
        codigo = ler_texto("Código: ")
        produto = consultas.procurar_por_codigo(produtos, codigo)

        encontrados = []
        if produto is not None:
            encontrados.append(produto)

    elif opcao == "2":
        texto = ler_texto("Parte do nome:")
        encontrados = consultas.procurar_por_nome(produtos, texto)

    elif opcao == "3":
        print("Pesquisa ainda não implementada.")
        return

    else:
        print("Opção inválida.")
        return

    mostrar_produtos(
        encontrados, "Não foram encontrados produtos."
    )


def movimentar_stock(produtos, tipo):
    if not produtos:
        print("Não existem produtos registados.")
        return

    codigo = ler_texto("Código do produto: ")
    produto = consultas.procurar_por_codigo(produtos, codigo)

    if produto is None:
        print("Produto não encontrado.")
        return

    quantidade = ler_inteiro(
        "Quantidade do movimento: ", 1
    )
    if tipo == "entrada":
        aceite = produto.registar_entrada(quantidade)
    else:
        aceite = produto.registar_saida(quantidade)

    if aceite:
        print(
            f"Movimento registado. "
            f"Stock atual: {produto.quantidade}."
        )
    else:
        print(
            "Saída recusada: stock insuficiente. "
            "Quantidade inalterada."
        )


if __name__ == "__main__":
    main()
