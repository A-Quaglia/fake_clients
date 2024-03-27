import pandas as pd

from src.fakedatager import SchemaCliente, generate_cliente, generate_items

if __name__ == "__main__":
    _, items = generate_items(130, generate_cliente, SchemaCliente) ## return: error, df
    df = pd.DataFrame([dict(x) for x in items])

    print(df.head())
    df.to_csv('data/rand_df.csv', index=False)
    