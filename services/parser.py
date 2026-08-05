from lxml import etree

from models.item import Item
from models.resumo import Resumo

from utils.conversores import numero
from utils.conversores import peso_bruto


class DUIMPParser:

    def __init__(self, arquivo):

        self.tree = etree.parse(arquivo)

        self.root = self.tree.getroot()

    def valor(self, elemento, xpath):

        return elemento.xpath(f"string({xpath})").strip()

    def resumo(self):

        return Resumo(

            numero_duimp=self.root.xpath("string(//numeroDuimp)"),

            data_registro=self.root.xpath("string(//dataRegistroBr)"),

            situacao=self.root.xpath("string(//situacao)"),

            canal=self.root.xpath("string(//canal)"),

            importador=self.root.xpath("string(//importador/nome)"),

            exportador=self.root.xpath("string(//exportador/nome)"),

            fabricante=self.root.xpath("string(//fabricante/nome)"),

            moeda=self.root.xpath("string(//moedaNegociada)"),

            valor_total=numero(
                self.root.xpath(
                    "string(//valorMoedaNegociada)"
                )
            ),

            quantidade_itens=len(
                self.root.xpath("//itens")
            )

        )

    def itens(self):

        lista = []

        for item in self.root.xpath("//itens"):

            quantidade = numero(

                self.valor(
                    item,
                    "mercadoria/quantidadeComercial"
                )

            )

            peso_liquido = numero(

                self.valor(
                    item,
                    "mercadoria/pesoLiquido"
                )

            )

            valor_unitario = numero(

                self.valor(
                    item,
                    "mercadoria/valorUnitarioMoedaNegociada"
                )

            )

            valor_total = numero(

                self.valor(
                    item,
                    "condicaoVenda/valorMoedaNegociada"
                )

            )

            lista.append(

                Item(

                    numero_item=self.valor(
                        item,
                        "identificacao/numeroItem"
                    ),

                    ncm=self.valor(
                        item,
                        "produto/ncm"
                    ),

                    produto=self.valor(
                        item,
                        "produto/codigo"
                    ),

                    descricao=self.valor(
                        item,
                        "produto/descricao"
                    ),

                    descricao_importacao=self.valor(
                        item,
                        "mercadoria/descricao"
                    ),

                    unidade_medida=self.valor(
                        item,
                        "mercadoria/unidadeMedida"
                    ),

                    quantidade=quantidade,

                    peso_liquido=peso_liquido,

                    peso_bruto=peso_bruto(
                        peso_liquido,
                        quantidade
                    ),

                    valor_unitario=valor_unitario,

                    valor_total=valor_total

                )

            )

        return lista