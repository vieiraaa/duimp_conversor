from dataclasses import dataclass


@dataclass
class Item:

    numero_item: str

    ncm: str

    produto: str

    descricao: str

    descricao_importacao: str

    unidade_medida: str

    quantidade: float

    peso_liquido: float

    peso_bruto: float

    valor_unitario: float

    valor_total: float