import pandas as pd

class LeerDatos:
    def __init__(self, ruta_completa: str, tipo_archivo: str) -> None:
        self.ruta_completa = ruta_completa
        self.tipo_archivo = tipo_archivo
        self.df = None

    def read_DataFrame(self,datos):
        self.df = pd.DataFrame(datos)

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

    def filtrar_tabla(self,nombre_columna,lista_validacion=None,presentes=True,filtrar_vacios=False):
        """
        Realiza una validación cruzada en el DataFrame basado en una lista de valores, una columna específica,
        y/o campos vacíos.

        Este método filtra el DataFrame según los valores especificados en `lista_validacion` 
        para la columna `nombre_columna`. Dependiendo del parámetro `presentes`, se puede 
        filtrar para mantener solo las filas con valores presentes en `lista_validacion` 
        o eliminar dichas filas. También puede filtrar campos vacíos.

        Args:
            nombre_columna (str): El nombre de la columna en el DataFrame para realizar la validación cruzada.
            lista_validacion (list, optional): Una lista de valores a validar en la columna especificada. 
                                            Por defecto es None.
            presentes (bool, optional): Si es True, mantiene las filas con valores presentes en 
                                        `lista_validacion`. Si es False, elimina las filas con 
                                        valores presentes en `lista_validacion`. El valor 
                                        predeterminado es True.
            filtrar_vacios (bool, optional): Si es True, filtra los campos vacíos (NaN). El valor 
                                            predeterminado es False.

        Returns:
            pd.DataFrame: El DataFrame filtrado según los criterios especificados.
        
        Example:
            >>> df = pd.DataFrame({
            ...     'A': [1, 2, 3, 4, 5],
            ...     'B': ['a', 'b', 'c', 'd', 'e']
            ... })
            >>> mi_clase = MiClase(df)
            >>> resultado = mi_clase.validacion_cruzada('A', [2, 4], presentes=True)
            >>> print(resultado)
            A  B
            1  2  b
            3  4  d
        """
        datos = self.df.copy()
        
        if filtrar_vacios:
            if presentes:
                filtro = datos[nombre_columna].notna()
            else:
                filtro = datos[nombre_columna].isna()
        else:
            if lista_validacion is None:
                raise ValueError("Debe proporcionar una lista de validación o habilitar el filtrado de vacíos.")
            
            if presentes:
                filtro = datos[nombre_columna].isin(lista_validacion)
            else:
                filtro = ~datos[nombre_columna].isin(lista_validacion)
        
        resultado = datos[filtro]
        self.df = resultado
        return self.df
    

class AnalisisExploratorio:
    def __init__(self,df:pd.DataFrame) -> None:
        self.df = pd.DataFrame(df)

    def informacion_Dataset(self):
        print(f'Informacion sobre el DataFrame:')
        print(self.df.info())
        print('\n')
    
    def estadistiva_descriptiva(self) -> None:
        print('Informacion sobre medidas de tendencia central')
        return self.df.describe()

    def cantidad_valores(self) -> None:
        print(f'Cantidad de valores')
        print(self.df.count())
        print('\n')

    def Filtro_nulos(self) -> None:
        print(f'Cantidad de valores nulos por columna:')
        nulos_por_columna = self.df.isnull().sum()
        print(nulos_por_columna)
        print(f'\nTotal de valores nulos en el DataFrame: {nulos_por_columna.sum()}')


    