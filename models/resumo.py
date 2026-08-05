from dataclasses import dataclass


@dataclass
class Resumo:

    numero_duimp: str

    data_registro: str

    situacao: str

    canal: str

    importador: str

    exportador: str

    fabricante: str

    moeda: str

    valor_total: float

    quantidade_itens: int