import os

class DUIMPParser:


    def texto(self, elemento, caminho):

        if elemento is None:
            return ""

        encontrado = elemento.find(caminho)

        if encontrado is not None and encontrado.text:
            return encontrado.text.strip()

        return ""



    def numero(self, valor):

        if not valor:
            return 0

        try:

            valor = (
                valor
                .strip()
                .replace(".", "")
                .replace(",", ".")
            )

            return float(valor)

        except:

            return 0



    def buscar(self, elemento, tag):

        if elemento is None:
            return ""

        encontrado = elemento.find(".//" + tag)

        if encontrado is not None and encontrado.text:
            return encontrado.text.strip()

        return ""



    def processar(self, root):

        produtos = []


        for item in root.iter("itens"):


            mercadoria = item.find("mercadoria")
            produto = item.find("produto")


            if mercadoria is None:
                continue



            descricao_importacao = self.texto(
                mercadoria,
                "descricao"
            )


            if descricao_importacao == "":
                continue



            peso_liquido = self.numero(
                self.texto(
                    mercadoria,
                    "pesoLiquido"
                )
            )



            peso_bruto = self.numero(
                self.texto(
                    mercadoria,
                    "pesoBruto"
                )
            )


            # Caso DUIMP não tenha peso bruto
            if peso_bruto == 0:

                peso_bruto = peso_liquido



            valor_brl = self.numero(
                self.buscar(
                    item,
                    "valorBRL"
                )
            )



            dados = {


                "Nº Item":

                    self.texto(
                        item,
                        "identificacao/numeroItem"
                    ),



                "NCM":

                    self.texto(
                        produto,
                        "ncm"
                    ),



                "Produto":

                    self.texto(
                        produto,
                        "denominacao"
                    ),



                "Descrição":

                    self.texto(
                        produto,
                        "descricao"
                    ),



                "Desc. Importação":

                    descricao_importacao,



                "Unidade de Medida":

                    self.texto(
                        mercadoria,
                        "unidadeComercial"
                    ),



                "Qnt Pedido":

                    self.numero(
                        self.texto(
                            mercadoria,
                            "quantidadeComercial"
                        )
                    ),



                "Peso Líq.":

                    peso_liquido,



                "Peso Bruto":

                    peso_bruto,



                "Valor Unitário":

                    self.numero(
                        self.texto(
                            mercadoria,
                            "valorUnitarioMoedaNegociada"
                        )
                    ),



                "Valor Total":

                    valor_brl

            }



            produtos.append(
                Produto(dados)
            )



        return DUIMP(produtos)






class Produto:


    def __init__(self, dados):

        self.dados = dados



    def to_dict(self):

        return self.dados







class DUIMP:


    def __init__(self, produtos):

        self.produtos = produtos



    def resumo(self):


        peso_liquido = sum(
            x.dados["Peso Líq."]
            for x in self.produtos
        )



        peso_bruto = sum(
            x.dados["Peso Bruto"]
            for x in self.produtos
        )



        valor = sum(
            x.dados["Valor Total"]
            for x in self.produtos
        )



        return (

            f"Itens: {len(self.produtos)}\n"

            f"Peso Líquido Total: {peso_liquido:.2f} KG\n"

            f"Peso Bruto Total: {peso_bruto:.2f} KG\n"

            f"Valor Total BRL: R$ {valor:,.2f}"

        )