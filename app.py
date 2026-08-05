from services import XMLReader, DUIMPParser
from services.excel_exporter import ExcelExporter

arquivo = input(
    "Selecione o Caminho do XML DUIMP: "
)

reader = XMLReader()

root = reader.carregar(
    arquivo
)

parser = DUIMPParser()

duimp = parser.processar(
    root
)

print("="*60)
print("RESULTADO DUIMP")
print("="*60)

print(
    duimp.resumo()
)

saida = "DUIMP_EXPORTADO.xlsx"

exportador = ExcelExporter()

exportador.exportar(
    duimp.produtos,
    saida
)

print()
print("Excel gerado:")
print(saida)