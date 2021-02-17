"""add to read me"""
import sqlite3

import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, insert, ForeignKey

from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///:orm.db', echo = True)
Session = sessionmaker(bind = engine)
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



class Backlog_class(Exception):

    def insert_table_values(self, bid, sub, status,stud_id):
        session = Session()

        insert_query = BacklogDb(bid = bid, sub= sub, status = status, stud_id = stud_id)
        try:
            session.add(insert_query)
            session.commit()
            session.refresh(insert_query)
            session.close()
        except sqlite3.IntegrityError as e:
            print(str(e))
        except sqlalchemy.exc.IntegrityError as e:
            print("Unique constraint failed: backlog id id should be unique")
        else:
            return insert_query.sub

    def delete_record(self, id):
        session = Session()

        rows = session.query(BacklogDb).filter(BacklogDb.bid == id).delete()
        session.commit()
        session.close()

        if rows == 0:
            return -1
        else:
            return rows

    def update_record(self, id, status):
        session = Session()

        rows = session.query(BacklogDb).filter(BacklogDb.bid == id).update({'status': status})
        session.commit()
        session.close()
        return rows

    def display(self):
        session = Session()

        result = session.query(BacklogDb).all()
        print("| Backlog Id | subject | Status | Student id | ")

        for row in result:
            print("|  ",row.bid, "  | ", row.sub, "  | ", row.status, "  | ", row.stud_id, " |")
        session.close()


    def subject_name(self, status):
        session = Session()
        result = session.query(BacklogDb).filter(BacklogDb.status == status)
        subject_name = None
        for row in result:
            print("Backlog Id: ", row.bid, " Subject Name :", row.sub)
            subject_name = row.sub
        session.close()

        return subject_name

    def getChoice(self):
        print("----------Menu-------------------")
        print(" 1. Insert values into Table\n 2. Delete from Table\n "
              "3. Update Student backlog Status\n 4. Display Records\n "
              "5. Show Status wise backlog\n 6. Exit")
        try:
            choice = int(input("Enter your choice"))
        except ValueError:
            print("enter 1 to 6")
        return choice



if __name__=='__main__':

    backlog = Backlog_class()
    choice = backlog.getChoice()
    while choice != 6:

        if choice == 1:
            records=[]

            count = int(input("How many Backlogs you want to enter?"))
            for i in range(0, count, 1):
                bid = int(input("Enter Backlog id : "))
                sub = str(input("Enter Subject name : "))
                status = str(input("Enter Status (Active/Closed) : "))
                stdid = int(input('Enter Student Id : '))
                records.append([bid, sub, status, stdid])

            for i in range(0,len(records)) :

                #print(len(records))
                print(records)
                try:
                    result=backlog.insert_table_values(records[i][0], records[i][1], records[i][2], records[i][3])
                except NameError:
                    print("Error")
                else:
                    print("Inserted Backlog : ", result)

        elif choice == 2:
            try:
                id = int(input("Enter backlog Id to be deleted : "))
            except ValueError:
                print("Insert Valid Id(Interger)")
            else:
                result = backlog.delete_record(id)
                if result == 1:
                    print("deleted")
                else:
                    raise Exception("Record not found!!")

        elif choice == 3:
            # update
            try:
                id = int(input("Enter backlog Id to be updated : "))
                status = input("enter status Active/Closed) : ")

            except ValueError:
                print("Insert Valid values")
            else:
                result = backlog.update_record(id, status)
                if result == 1:
                    print("updated")
                else:
                    raise Exception("Record not found!!")


        elif choice == 4:
            backlog.display()
        elif choice == 5:
            status = (input("Enter status to list backlog : "))
            backlog.subject_name(status)
        else:
            print("Invalid option. Try again!")

        choice = backlog.getChoice()