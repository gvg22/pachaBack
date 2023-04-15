from psycopg2 import connect, Error

# try:
#     conn = connect(
#         user = 'postgres', 
#         password = 'root0709', 
#         host='127.0.0.1', 
#         port = '5432', 
#         database = 'postgres')
#     cur = conn.cursor()
#     query = 'select version();'
#     cur.execute(query)
#     res = cur.fetchone()
#     print(res)

# except(Exception, Error) as error:
#     print(f"Hubo un error en la conexion {str(error)}")
# finally:
#     cur.close()
#     conn.close()
#     print(f'Se ha cerrado la conexion')

from conexion import conexion
from tabulate import TableFormat, tabulate

conexion = conexion()
query = "Select * from customer LIMIT 10;"
datos = conexion.consultarBDD(query)
header = ['IdCustomer','customerName','IdCountry','IdCity','IdState', 'postalCode', 'IdRegion', 'IdSegment']
print(tabulate(datos, headers=header, tablefmt='fancy_grid'))
# print(datos)
# conexion.ejecutarBDD()