import random
from enum import Enum
from typing import Callable, List, Tuple

from faker import Faker
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


def generate_cliente():
    """
    Gera cliente aleatório

    Returns:
        dict: Um dicionário representando um cliente aleatório com as seguintes chaves:
            - 'uf': Estado de residência do cliente (string).
            - 'nome': Nome do cliente (string).
            - 'categoria': Categoria do cliente (string).
            - 'categoria_2': Categoria adicional do cliente (string).
            - 'unidades': Número de unidades relacionadas ao cliente (inteiro).
            - 'tamanho': Tamanho do cliente (float).
    """
    cliente = dict(
        uf=fake.estado()[0],
        nome= fake.name(),
        categoria= random.choice(list(Categoria)).value,
        categoria_2= random.choice(list(Categoria2)).value,
        unidades= random.randrange(1, 6),
        tamanho= random.uniform(0, 12),
    )
    return cliente

def generate_items(nrows: int, generator: Callable, schema: None | BaseModel = None) -> Tuple[List, List]:
    """
    Gera lista de itens utilizando um gerador (generator) e que pode ser validado por um schema (BaseModel)

    Args:
        nrows (int): número de items a serem gerados
        generator (Callable): gerador de item
        schema (None | BaseModel, optional): esquema a ser usado para validação dos dados gerados, se None -> skip validation. Defaults to None.

    Returns:
        Tuple[List, List]: Lista contendo os erros (validação esquema incorreta) e lista de resultados (items gerados)
    """
    error = []
    rows = []
    for i in range(nrows):
        row = generate_cliente()

        if schema:
            try:
                row = SchemaCliente(**row)
            except ValidationError as e:
                error.append(e)

        rows.append(row)

    return error, rows

