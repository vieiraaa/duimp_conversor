import xml.etree.ElementTree as ET

arquivo = r"C:\Users\joao.arruda\Downloads\duimp-26BR00012814793.xml"

tree = ET.parse(arquivo)
root = tree.getroot()

contador = 0

for item in root.findall(".//itens"):

    texto = ""

    for elem in item.iter():
        if elem.text:
            texto += elem.text + " "

    if "MOTOR DE INDUCAO" in texto:

        print("="*80)
        print("ITEM ENCONTRADO")
        print("="*80)

        for elem in item.iter():
            print(
                "TAG:",
                elem.tag,
                "| VALOR:",
                elem.text
            )

        break