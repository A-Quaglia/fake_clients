# [Gerador de dados fakes validados por Schema](https://github.com/A-Quaglia/fakedatagen)
## Fakedatagen
- [github](https://github.com/A-Quaglia/fakedatagen)

Gerador de dados fakes que podem ser validados por um Schema (`pydantic.BaseModel`).

**`generate_items`**
::: src.fakedatagen.generate_items

### Example
#### Schema (validador) - **SchemaCliente**
::: src.fakedatagen.SchemaCliente
#### Generator - **generate_cliente**
::: src.fakedatagen.generate_cliente
#### Utilizar gerador com validação
Gerar n item; validar; criar pandas.DataFrame e salvar em csv:
``` python
    import pandas as pd

    from src.fakedatagen import SchemaCliente, generate_cliente, generate_items

    if __name__ == "__main__":
        _, items = generate_items(130, generate_cliente, SchemaCliente) ## return: error, df
        df = pd.DataFrame([dict(x) for x in items])

        print(df.head())
        df.to_csv('data/rand_df.csv', index=False)
    
```