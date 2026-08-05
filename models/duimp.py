class DUIMP:


    def __init__(
        self,
        numero="",
        importador=""
    ):

        self.numero = numero
        self.importador = importador

        self.produtos = []

        self.exportador = ""
        self.fabricante = ""

        self.incoterm = ""

        self.moeda = ""

        self.metodo_valoracao = ""

        self.valor_brl = 0

        self.numero_rof = ""

        self.cobertura_cambial = ""

        self.peso_total = 0



    def adicionar_produto(self, produto):

        self.produtos.append(
            produto
        )



    def calcular_totais(self):

        self.peso_total = sum(
            item.peso_liquido
            for item in self.produtos
        )



    def resumo(self):

        return {

            "Número DUIMP":
                self.numero,

            "Importador":
                self.importador,

            "Exportador":
                self.exportador,

            "Quantidade Itens":
                len(self.produtos),

            "Peso Total":
                self.peso_total,

            "Incoterm":
                self.incoterm,

            "Moeda":
                self.moeda,

            "Valor BRL":
                self.valor_brl
        }