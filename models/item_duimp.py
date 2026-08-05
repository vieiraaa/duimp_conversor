class ItemDUIMP:


    def __init__(self):

        self.numero_item = ""

        self.ncm = ""

        self.descricao = ""

        self.peso_liquido = 0.0

        self.exportador = ""

        self.fabricante = ""

        self.pais_origem = ""

        self.valor_moeda = 0.0

        self.valor_brl = 0.0

    def to_dict(self):

        return {

            "Item": self.numero_item,
            "NCM": self.ncm,
            "Descrição": self.descricao,
            "Peso Líquido": self.peso_liquido,
            "Exportador": self.exportador,
            "Fabricante": self.fabricante,
            "País Origem": self.pais_origem,
            "Valor Moeda": self.valor_moeda,
            "Valor BRL": self.valor_brl

        }
    