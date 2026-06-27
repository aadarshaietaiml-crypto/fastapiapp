from sqlalchemy import Column,Integer,String,Enum,relationship
from database import Base,engine,SessionLocal

class Company(Base):
    _tablename_="companies"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False,index=True)
    email=Column(String,unique=True)
    phone=Column(String,unique=True)
    jobs=relationship("job",back_populates="company")



    