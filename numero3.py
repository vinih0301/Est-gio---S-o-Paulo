
import json

dados_faturamento = '''
{
    "dias": [
        {"dia": 1, "faturamento": 1000.0},
        {"dia": 2, "faturamento": 1500.0},
        {"dia": 3, "faturamento": 0.0},
        {"dia": 4, "faturamento": 2000.0},
        {"dia": 5, "faturamento": 500.0},
        {"dia": 6, "faturamento": 800.0},
        {"dia": 7, "faturamento": 0.0},
        {"dia": 8, "faturamento": 2500.0},
        {"dia": 9, "faturamento": 3000.0},
        {"dia": 10, "faturamento": 1000.0}
    ]
}
'''

faturamento_diario = json.loads(dados_faturamento)

def calcula_estatisticas(faturamento_diario):
    valores = [dia["faturamento"] for dia in faturamento_diario["dias"] if dia["faturamento"] > 0]
    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)
    return menor_faturamento, maior_faturamento, dias_acima_media

menor_faturamento, maior_faturamento, dias_acima_media = calcula_estatisticas(faturamento_diario)

print("Menor Faturamento:", menor_faturamento)
print("Maior Faturamento:", maior_faturamento)
print("Dias Acima da Média:", dias_acima_media)