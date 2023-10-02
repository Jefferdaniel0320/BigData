import pandas as pd
import numpy as np
ruta = r'C:\Users\JefferD\OneDrive - Politécnico Grancolombiano\EngSoftware\BigData\Archivos\Hotel.xlsx'
DF_Enero = pd.read_excel(ruta, sheet_name='Enero')
DF_Febrero = pd.read_excel(ruta, sheet_name='Febrero')
DF_Marzo = pd.read_excel(ruta, sheet_name='Marzo')

DF_Enero[['Mes']]='Enero'
DF_Febrero[['Mes']]='Febrero'
DF_Marzo[['Mes']]='Marzo'

DF_Final = pd.concat([DF_Enero,DF_Febrero,DF_Marzo])

valor = 120000

DF_Final['Ingreso']=valor*DF_Final['Huespedes']*DF_Final['Noches']
DF_Final = DF_Final.reset_index(drop=True)
DF_Final['Comision']=np.where(DF_Final['Reserva']=='Airbnb',0.03,0.1)
DF_Final['Costo']=DF_Final['Ingreso']*DF_Final['Comision']
DF_Final['Utilidad']=DF_Final['Ingreso']-DF_Final['Costo']
Total_Personas = DF_Final['Huespedes'].sum()
Total_Noches = DF_Final['Noches'].sum()
Prom_Per_Noche = Total_Personas/Total_Noches

print(DF_Final)
print("--------------------------------------------------------------------------------")
print(f'Total Personas: {Total_Personas}')
print(f'Total Noches: {Total_Noches}')
print(f'Promedio de Personas por noche: {round(Prom_Per_Noche,2)} Personas')
print("--------------------------------------------------------------------------------")