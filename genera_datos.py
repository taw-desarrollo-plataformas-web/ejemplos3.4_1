from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Docente

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Docente 
docente1 = Docente(nombre="Tony", apellido="García", \
        ciudad="Loja")

docente2 = Docente(nombre="Luis", apellido="Borrero", \
        ciudad="Loja")

docente3 = Docente(nombre="Ana", apellido="Salcedo", \
        ciudad="Zamora")

docente4 = Docente(nombre="Monica", apellido="Valenzuela", \
        ciudad="Zamora")

# se agrega los objetos
# a la sesión
# a la espera de un commit
# para agregar un registro a la base de 
# datos
session.add(docente1)
session.add(docente2)
session.add(docente3)
session.add(docente4)

# se confirma las transacciones
session.commit()
