from imc import *
import pytest
def test_calcular_imc():
    assert calcular_imc(70, 1.75) == 22.86
    assert calcular_imc(70, 1.75) == round(70 / (1.75 ** 2), 2) 
    with pytest.raises(ValueError):    
        calcular_imc(70, 0)

def test_classificar_imc():
    assert classificar_imc(17.9) == "abaixo do peso"
    assert classificar_imc(22.0) == "peso normal"
    assert classificar_imc(27.3) == "sobrepeso"
    assert classificar_imc(33.0) == "obesidade grau I"
    assert classificar_imc(37.0) == "obesidade grau II"
    assert classificar_imc(45.0) == "obesidade grau III"

def test_casas():
   assert calcular_imc(80, 1.80) == round(80 / (1.80 ** 2), 2)