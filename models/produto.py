class Produto:

    def __init__(
        self,
        ncm="",
        descricao="",
        quantidade=0,
        valor_unitario=0.0
    ):

        self.ncm = ncm
        self.descricao = descricao
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario


    def valor_total(self):

        return self.quantidade * self.valor_unitario


    def to_dict(self):

        return {
            "NCM": self.ncm,
            "Descrição": self.descricao,
            "Quantidade": self.quantidade,
            "Valor Unitário": self.valor_unitario,
            "Valor Total": self.valor_total()
        }