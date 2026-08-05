import xml.etree.ElementTree as ET


arquivo = r"C:\Users\joao.arruda\Downloads\duimp-26BR00012814793.xml"


root = ET.parse(arquivo).getroot()


for item in root.iter("itens"):

    mercadoria = item.find("mercadoria")

    if mercadoria is not None:

        print("="*50)

        for filho in mercadoria.iter():

            print(
                filho.tag,
                "=>",
                filho.text
            )

        break