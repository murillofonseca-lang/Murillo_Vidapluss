def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError("altura deve ser maior que zero.")
    return round(peso / (altura ** 2), 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "abaixo do peso"
    elif 18.5 <= imc <25:
        return "peso normal"
    elif 25 <= imc < 30:
        return "sobrepeso"
    elif 30 <= imc <35:
        return "obesidade grau I"
    elif 35 <= imc < 40:
        return "obesidade grau II"
    else:
        return "obesidade grau III"
    