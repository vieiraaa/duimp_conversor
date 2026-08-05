import xml.etree.ElementTree as ET


class XMLReader:


    def carregar(self, caminho):

        try:

            tree = ET.parse(caminho)

            root = tree.getroot()

            return root


        except Exception as erro:

            raise Exception(
                f"Erro lendo XML: {erro}"
            )