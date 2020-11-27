from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

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

# Obtener todos los registros de 
# la entidad docentes 
docentes = session.query(Docente).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de Docentes")
for s in docentes:
    print("%s" % (s))
    print("---------")

# Eliminar datos o registros de los docentes
# que tiene como apellido "Valenzuela"
docentes_eliminar = session.query(Docente).filter(Docente.apellido=="Valenzuela")\
        .all()

for d in docentes_eliminar:
    # se agrega a la sesión los elementos que
    # se quiere eliminar, a través de
    # session.delete()
    session.delete(d) 

# se confirma las transacciones
session.commit()

# Obtener todos los registros de 
# la entidad docentes 
docentes = session.query(Docente).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de Docentes luego de eliminar")
for s in docentes:
    print("%s" % (s))
    print("---------")

