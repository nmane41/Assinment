import sqlite3
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, insert, ForeignKey

from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///:orm.db', echo = True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class StudentDb(Base):
   __tablename__ = 'student'
   id = Column(Integer, primary_key=True)

   name = Column(String)
   lastname = Column(String)
   standard = Column(Integer)


class BacklogDb(Base):
    __tablename__ = 'backlog'
    bid = Column(Integer, primary_key=True)
    sub = Column(String)
    status = Column(String)
    stud_id = Column(Integer, ForeignKey('student.id'))
    student = relationship("StudentDb", back_populates="backlog")


StudentDb.backlog = relationship("BacklogDb", order_by = BacklogDb.bid, back_populates="student")
Base.metadata.create_all(engine)


class Student(Exception):

    def insert_table_values(self, id, name, lastname, standard):
        session = Session()

        insert_query = StudentDb(id=id, name= name, lastname = lastname, standard = standard)
        try:
            session.add(insert_query)
            session.commit()
            session.refresh(insert_query)
            session.close()
        except sqlite3.IntegrityError as e:
            print(str(e))
        except sqlalchemy.exc.IntegrityError as e:
            print("Unique constraint failed: student id should be unique")

        else:
            return insert_query.name

    def delete_record(self, id):
        session = Session()

        rows = session.query(StudentDb).filter(StudentDb.id == id).delete()
        session.commit()
        session.close()

        if rows == 0:
            return -1
        else:
            return rows

    def update_record(self, id, standard):
        session = Session()

        rows = session.query(StudentDb).filter(StudentDb.id == id).update({'standard': standard})
        session.commit()
        session.close()
        return rows

    def display(self):
        session = Session()

        result = session.query(StudentDb).all()
        print("| Student Id | Name | Lastname | Standard | ")

        for row in result:
            print("|  ",row.id, "  | ", row.name, "  | ", row.lastname,  " |", row.standard, " |")
        session.close()


    def subject_name(self,sid):
        session = Session()
        result = session.query(BacklogDb).filter(BacklogDb.stud_id == sid)
        subject_name = None
        for row in result:
            print("Backlog Id : ", row.bid, " Subject Name : ", row.sub, " Status : ", row.status)
            subject_name = row.sub
        session.close()

        return subject_name

    def getChoice(self):
        print("----------Menu-------------------")
        print(" 1. Insert values into Table\n 2. Delete from Table\n "
              "3. Update Student Standard\n 4. Display Records\n "
              "5. Show backlogs of a student\n 6. Exit")
        try:
            choice = int(input("Enter your choice"))
        except ValueError:
            print("enter 1 to 6")
        else:
            return choice




if __name__ == '__main__':

    std = Student()
    choice = std.getChoice()
    while choice != 6:

        if choice == 1:
            records=[]

            count = int(input("How many Students you want to enter?"))
            for i in range(0, count, 1):
                id = int(input("Enter id : "))
                name = str(input("Enter student name : "))
                lastname = str(input("Enter Last name : "))



                standard =int(input('Student standard'))
                try:
                    records.append([id, name, lastname, standard])
                except NameError:
                    print("Insert proper data")

            for i in range(0,len(records)) :

                #print(len(records))
                print(records)
                try:
                    result=std.insert_table_values(records[i][0], records[i][1], records[i][2], records[i][3])
                except NameError:
                    print("Error")
                else:
                    print("Inserted Student",result)

        elif choice == 2:
            try:
                id = int(input("Enter Student Id to be deleted : "))
            except ValueError:
                print("Insert Valid Id(Interger)")
            else:
                result = std.delete_record(id)
                if result == 1:
                    print("Deleted")
                else:
                    raise Exception("Record not found!!")

        elif choice == 3:
            # update
            try:
                id = int(input("Enter Employee Id to be updated : "))
                strd = int(input("Enter new standard"))

            except ValueError:
                print("Insert Valid values")
            else:
                result = std.update_record(id, strd)
                if result == 1:
                    print("Updated")
                else:
                    raise Exception("Record not found!!")


        elif choice == 4:
            std.display()
        elif choice == 5:
            sid=int(input("Enter student id whose backlog you want : "))
            std.subject_name(sid)
        else:
            print("Invalid option. Try again!")

        choice = std.getChoice()