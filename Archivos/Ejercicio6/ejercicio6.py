import pandas as pd
import numpy as np

# Rutas
rutaCECO = r'C:\Users\JefferD\OneDrive - Politécnico Grancolombiano\EngSoftware\BigData\Archivos\Ejercicio6\Data\Dim_CECO.xlsx'
rutaCiudad = r'C:\Users\JefferD\OneDrive - Politécnico Grancolombiano\EngSoftware\BigData\Archivos\Ejercicio6\Data\Dim_Ciudad.xlsx'
rutaCliente = r'C:\Users\JefferD\OneDrive - Politécnico Grancolombiano\EngSoftware\BigData\Archivos\Ejercicio6\Data\Dim_Cliente.xlsx'

# Carga de Archivos
DF_rutaCECO = pd.read_excel(rutaCECO)
DF_rutaCiudad = pd.read_excel(rutaCiudad)
DF_rutaCliente = pd.read_excel(rutaCliente)

#print(DF_rutaCECO)
#print(DF_rutaCiudad)
#print(DF_rutaCliente)

# Agregar Clave CECO
DF_rutaCECO.loc[DF_rutaCECO['Cliente'] <  10, 'Llave'] = 'CECO_0' + DF_rutaCECO['Cliente'].astype(str)
DF_rutaCECO.loc[DF_rutaCECO['Cliente'] >= 10, 'Llave'] = 'CECO_' + DF_rutaCECO['Cliente'].astype(str)
#print(DF_rutaCECO)

# Agregar Clave Ciudad
DF_rutaCiudad.loc[DF_rutaCiudad['Cliente'] <  10, 'Llave'] = 'CECO_0' + DF_rutaCiudad['Cliente'].astype(str)
DF_rutaCiudad.loc[DF_rutaCiudad['Cliente'] >= 10, 'Llave'] = 'CECO_'  + DF_rutaCiudad['Cliente'].astype(str)
print(DF_rutaCiudad)

# Agregar Clave Cliente
DF_rutaCliente.loc[DF_rutaCliente['Cliente'] <  10, 'Llave'] = 'CECO_0' + DF_rutaCliente['Cliente'].astype(str)
DF_rutaCliente.loc[DF_rutaCliente['Cliente'] >= 10, 'Llave'] = 'CECO_'  + DF_rutaCliente['Cliente'].astype(str)
#print(DF_rutaCliente)