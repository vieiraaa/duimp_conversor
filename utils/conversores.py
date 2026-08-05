from decimal import Decimal


def texto(valor):

    if valor is None:
        return ""

    return str(valor).strip()


def numero(valor):

    if valor is None:
        return 0.0

    valor = str(valor).strip()

    if valor == "":
        return 0.0

    try:

        if "," in valor:

            valor = valor.replace(".", "")
            valor = valor.replace(",", ".")

        return float(valor)

    except:

        return 0.0


def moeda(valor):

    return round(numero(valor), 2)


def peso_bruto(peso_liquido, quantidade):

    return round(peso_liquido * quantidade, 3)