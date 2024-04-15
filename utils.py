import pandas as pd
    
def string_to_df(text: str) -> pd.DataFrame:
    """
        Transforma texto en un DataFrame de Pandas

        Args:
            text (str):

        Authors:
            - Alvaro Muñoz

        Created:
            - 14/04/2024

        Returns:
            pd.DataFrame: DataFrame con el contenido ingresado
    """
    
    lineas = text.strip().split("\n")
    datos = [dict(zip(lineas[0].split(), linea.split()[1:])) for linea in lineas[1:]]
    df = pd.DataFrame(datos)
    print(df)

    return df