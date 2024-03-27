import random
from enum import Enum
from typing import Callable, List, Tuple

import pandas as pd
from faker import Faker
from pandas import DataFrame
from pydantic import BaseModel, Field, ValidationError, field_validator

fake = Faker('pt_BR')


class Categoria(str, Enum):
    cat_a = 'categoria A'
    cat_b = 'categoria B'
    cat_c = 'categoria C'


class Categoria2(str, Enum):
    cat_t = 'T2'
    cat_t2 = 'T2'
    cat_t3 = 'T3'
    cat_v4 = 'V4'
    cat_v5 = 'V5'


class SchemaCliente(BaseModel):
    """
    Esquema para representar um cliente.

    Attributes:
        uf (str): Estado de residência do cliente.
        nome (str): Nome do cliente.
        categoria (List[Categoria]): Lista de categorias do cliente.
        categoria_2 (List[Categoria2]): Lista de categorias adicionais do cliente.
        unidades (int, opcional): Número de unidades relacionadas ao cliente (por padrão 0).
        tamanho (float, opcional): Tamanho do cliente, deve estar entre 0 e 20 (por padrão 0).

    """
    uf: str
    nome: str
    categoria: str
    categoria_2: str
    unidades: int = Field(ge=0)
    tamanho: float =  Field(ge=0, le=20)

    @field_validator('categoria')
    def validar_categoria(categoria):
        categorias = set(item.value for item in Categoria)
        if categoria in categorias:
            return categoria
        else: 
            raise Exception("categoria não definida")
        
    @field_validator('categoria_2')
    def validar_categoria_2(categoria):
        categorias = set(item.value for item in Categoria2)
        if categoria in categorias:
            return categoria
        else: 
            raise Exception("categoria_2 não definida")


