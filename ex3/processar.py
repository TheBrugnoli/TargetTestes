import json
import xml.etree.ElementTree as ET
import os

# Função para processar dados JSON
def processar_json(caminho_arquivo):
    if not os.path.isfile(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")
    with open(caminho_arquivo, 'r') as file:
        dados = json.load(file)
    valores = [item['valor'] for item in dados if item['valor'] > 0]
    return valores

# Função para calcular menor valor, maior valor e dias com faturamento acima da média
def calcular_faturamento(valores):
    if not valores:
        return None, None, 0
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_media = len([valor for valor in valores if valor > media_mensal])
    
    return menor_valor, maior_valor, dias_acima_media

# Caminhos dos arquivos
caminho_json = 'C:/Development/ProjectPython2024/testeTarget/ex3/dados.json'

# Ler e processar os arquivos
try:
    valores_json = processar_json(caminho_json)
    
    # Calcular e exibir os resultados
    print("Dados JSON:")
    menor_valor_json, maior_valor_json, dias_acima_media_json = calcular_faturamento(valores_json)
    print(f"Menor valor: {menor_valor_json}")
    print(f"Maior valor: {maior_valor_json}")
    print(f"Número de dias acima da média: {dias_acima_media_json}")
    
except FileNotFoundError as e:
    print(e)