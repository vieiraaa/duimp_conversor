import pandas as pd


class ExcelExporter:


    def exportar(self, produtos, arquivo):

        dados = []


        for produto in produtos:

            dados.append(
                produto.to_dict()
            )


        df = pd.DataFrame(dados)


        df.to_excel(
            arquivo,
            index=False
        )


        return arquivo