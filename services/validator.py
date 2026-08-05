class Validator:


    def validar_produto(self, produto):

        erros=[]

        if not produto.ncm:
            erros.append(
                "Produto não contém NCM"
            )

        if not produto.descricao:
            erros.append(
                "Produto não contém descrição"
            )

        return erros