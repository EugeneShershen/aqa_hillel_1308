from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

DATABASE_URL = "postgresql://shershen:sher@localhost/university"
engine = create_engine(DATABASE_URL)

Base = declarative_base()


class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(300), nullable=False, unique=True)

    registration_list = relationship('RegistrationList', back_populates='course')


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)

    registration_list = relationship('RegistrationList', back_populates='student')


class RegistrationList(Base):
    __tablename__ = 'registration_list'

    id_course = Column(Integer, ForeignKey("course.id", ondelete='SET NULL'), primary_key=True)
    id_student = Column(Integer, ForeignKey("student.id", ondelete='SET NULL'), primary_key=True)

    course = relationship('Course', back_populates='registration_list')
    student = relationship('Student', back_populates='registration_list')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
