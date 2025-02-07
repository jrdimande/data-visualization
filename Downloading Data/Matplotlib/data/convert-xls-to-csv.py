import pandas as pd
def converter_xls_para_csv(xls_path, csv_path):
    df = pd.read_excel(xls_path)
    df.to_csv(csv_path, index=False)
    print(f"Arquivo CSV salvo como {csv_path}")

xls_path = "maputo_cidade.xls"
csv_path = "seu_arquivo.csv"

converter_xls_para_csv(xls_path, csv_path)
