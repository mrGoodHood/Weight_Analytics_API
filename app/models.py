from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class RespondentData(Base):
    __tablename__ = "respondents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String)
    respondent = Column(Integer)
    sex = Column(Integer)
    weight = Column(Float)
