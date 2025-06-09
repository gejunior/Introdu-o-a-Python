from datetime import datetime, timedelta

# d = datetime.date(2025, 5, 6)
# print(d) # data específica
# print(d.today())# data atual

tipo_carro = "G"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"Data estimada para carro pequeno: {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"Data estimada para carro médio: {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"Data estimada para carro grande: {data_estimada}")
