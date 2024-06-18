def converter_para_12h(hora, minuto):
    periodo = "AM" if hora < 12 else "PM"
    hora12 = hora if hora <= 12 else hora - 12
    return hora12, minuto, periodo

# Exemplo de uso:
# hora24 = int(input("Digite a hora (formato 24h): "))
# minuto = int(input("Digite os minutos: "))
# hora12, minuto, periodo = converter_para_12h(hora24, minuto)
# print(f"{hora24}:{minuto} é {hora12}:{minuto} {periodo}")
