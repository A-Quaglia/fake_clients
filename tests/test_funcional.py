import pandas as pd
import pytest
from pandas import DataFrame
from pydantic import ValidationError

from src.fakedatager import SchemaCliente, generate_cliente, generate_items


def test_schemacliente_valid():
    cliente = dict(uf= 'MG', nome='Augusto',
    categoria='categoria A', categoria_2='T2', unidades= 3, tamanho=0.35)

    SchemaCliente(**cliente)

def test_schemacliente_validation_error():
    cliente = dict(uf= 'MG', nome=450,
    categoria= 'categoria C', categoria_2= 'T2', unidades= 3, tamanho=0.35)
    
    with pytest.raises(ValidationError):
        SchemaCliente(**cliente)

def test_schemacliente_validation_error_unidades_negativas():
    cliente = dict(uf= 'MG', nome=450,
    categoria= 'categoria B', categoria_2= 'V4', unidades=-3, tamanho=0.35)
    
    with pytest.raises(ValidationError):
        SchemaCliente(**cliente)

def test_schemacliente_validation_error_categoria_nao_valida():
    cliente = dict(uf= 'MG', nome=450,
    categoria= 'categoria Y', categoria_2= 'V4', unidades=-3, tamanho=0.35)
    
    with pytest.raises(ValidationError):
        SchemaCliente(**cliente)
