import datetime
#obtem a data e hr atual 
agora= datetime.datetime.now()

# exibe a data no formado dia/mes/ano
print(f"Data:  {agora.day:02d}/{agora.month:02d}/{agora.year}")

# exiba a hora no formato hora.minuto
print(f"Hora:  {agora.hour:02d}:{agora.minute:02d}")