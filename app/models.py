from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .database import Base
from .enums import Estado

class Zona(Base):
    __tablename__ = "zonas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    codigo_postal = Column(String)
    limite_velocidad = Column(Integer)

    patinetes = relationship("Patinete", back_populates="zona")


class Patinete(Base):
    __tablename__ = "patinetes"

    id = Column(Integer, primary_key=True)
    numero_serie = Column(String)
    modelo = Column(String)
    bateria = Column(Float)
    estado = Column(Enum(Estado))

    puntuacion_usuario = Column(Float, nullable=True)  

    zona_id = Column(Integer, ForeignKey("zonas.id"))
    zona = relationship("Zona", back_populates="patinetes")