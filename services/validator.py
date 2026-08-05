class Validator:


    def validar_produto(self, produto):

        erros=[]


        if not produto.ncm:
            erros.append(
                "Produto sem NCM"
            )


        if not produto.descricao:
            erros.append(
                "Produto sem descrição"
            )


        return erros