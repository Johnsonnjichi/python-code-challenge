from sqlalchemy import Column, Integer, String
from database import Base

# creating a table model
class Students(Base):

    __tablename__ = "students"
    student_id = column(Integer, primary_key = True)
    student_name = column(string(100))