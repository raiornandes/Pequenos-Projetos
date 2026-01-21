import csv
import random
from datetime import datetime, timedelta

# Configurações
random.seed(42)  # Para resultados consistentes
total_reviews = 40

# Dados fictícios
usuarios = [f"user_{i:03d}" for i in range(1, 21)]  # 20 usuários
produtos = [
    "Smartphone XYZ", "Tablet ABC", "Fone de Ouvido Bluetooth", 
    "Smartwatch Pro", "Câmera Digital 4K", "Notebook Gamer"
]

comentarios_positivos = [
    "Produto excelente! Entrega rápida.",
    "Atendeu todas as minhas expectativas.",
    "Qualidade impressionante pelo preço.",
    "Recomendo para todos!",
    "Veio bem embalado e sem defeitos.",
]

comentarios_negativos = [
    "Veio com atraso e avariado.",
    "Qualidade inferior ao esperado.",
    "Não recomendo. Problemas de funcionamento.",
    "Suporte técnico não resolveu meu problema.",
    "Produto chegou incompleto.",
]

comentarios_neutros = [
    "Produto razoável, mas pode melhorar.",
    "Entrega dentro do prazo, mas o produto é básico.",
    "Nem bom nem ruim.",
    "Funciona, mas não é tão durável.",
]

# Gerar datas aleatórias nos últimos 3 meses
datas = []
hoje = datetime.now()
for _ in range(total_reviews):
    dias_aleatorios = random.randint(1, 90)
    data = hoje - timedelta(days=dias_aleatorios)
    datas.append(data.strftime("%Y-%m-%d"))

# Gerar reviews
reviews = []
for i in range(total_reviews):
    usuario = random.choice(usuarios)
    produto = random.choice(produtos)
    avaliacao = random.choices([1, 2, 3, 4, 5], weights=[0.1, 0.2, 0.3, 0.3, 0.7])[0]  # Viés para notas altas
    
    if avaliacao >= 4:
        comentario = random.choice(comentarios_positivos)
    elif avaliacao <= 2:
        comentario = random.choice(comentarios_negativos)
    else:
        comentario = random.choice(comentarios_neutros)
    
    reviews.append([
        usuario,
        produto,
        avaliacao,
        comentario,
        datas[i]
    ])

# Escrever arquivo CSV
with open('reviews_ficticios.csv', 'w', newline='', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(['usuario_id', 'produto', 'avaliacao', 'comentario', 'data'])
    writer.writerows(reviews)

print("Arquivo gerado com sucesso!")