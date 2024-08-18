# Documentación de la Clase `LeerDatos`

La clase `LeerDatos` está diseñada para leer archivos CSV y cargar su contenido en un `DataFrame` de pandas. A continuación, se detalla su funcionamiento y los métodos disponibles.

## Definición de la Clase

```python
import pandas as pd

class LeerDatos:
    def __init__(self, ruta_completa: str, tipo_archivo: str) -> None:
        self.ruta_completa = ruta_completa
        self.tipo_archivo = tipo_archivo
        self.df = None

    def leer_archivo_csv(self, separador: str = ',') -> pd.DataFrame:
        """
        Lee un archivo CSV y carga su contenido en un DataFrame.

        Parámetros:
        - separador: Caracter utilizado para separar las columnas en el archivo CSV (por defecto ',').

        Retorna:
        - DataFrame con el contenido del archivo CSV.
        """
        if self.tipo_archivo.lower() == 'csv':
            try:
                self.df = pd.read_csv(self.ruta_completa, encoding='utf-8', sep=separador)
            except FileNotFoundError:
                print(f"Error: El archivo en la ruta {self.ruta_completa} no se encuentra.")
                self.df = None
            except pd.errors.EmptyDataError:
                print("Error: El archivo está vacío.")
                self.df = None
            except pd.errors.ParserError:
                print("Error: Error de análisis del archivo CSV.")
                self.df = None
            except Exception as e:
                print(f"Error inesperado: {e}")
                self.df = None
        else:
            print("Error: Tipo de archivo no soportado. Se esperaba 'csv'.")
        return self.df
