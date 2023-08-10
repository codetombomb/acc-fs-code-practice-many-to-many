from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = "recipe"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    category = Column(String, nullable=False)
    instructions = Column(String)
    
    area = Column(String)
    def __repr__(self):
        return "<Recipe " \
            + f"name={self.name}, " \
            + f"category={self.category}, " \
            + f"instructions={self.instructions}, " \
            + f"area={self.area}" \
            + ">"
            
class Ingredient(Base):
    __tablename__ = "ingredient"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    def __repr__(self):
        return "<Recipe " \
            + f"id={self.id}, " \
            + f"name={self.name}" \
            + ">"