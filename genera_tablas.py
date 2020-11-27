from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

class Docente(Base):
    __tablename__ = 'docentes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    ciudad = Column(String, nullable=False)
    
    def __repr__(self):
        return "Docente: nombre=%s apellido=%s ciudad:%s" % (
                          self.nombre, 
                          self.apellido, 
                          self.ciudad)

Base.metadata.create_all(engine)
