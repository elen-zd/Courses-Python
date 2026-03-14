from sqlalchemy import create_engine
from sqlalchemy import text


class Tables:
    def __init__(self, connection_str):
        self.qa_db = create_engine(connection_str)

    def add_subject(self, title, id):
        connection = self.qa_db.connect()
        sql_add = text("INSERT INTO subject"
                       " (\"subject_title\", \"subject_id\") "
                       "VALUES (:new_title, :new_id)")
        connection.execute(sql_add,
                           {'new_title': title, 'new_id': id})

        connection.commit()
        connection.close()

    def get_max_id_subject(self):
        connection = self.qa_db.connect()
        sql_get = connection.execute(text("SELECT MAX"
                                          " (\"subject_id\") FROM subject"))

        id_sub = sql_get.scalar()
        connection.close()
        return id_sub

    def get_id_subject(self, id):
        connection = self.qa_db.connect()
        sql_get_id = text("SELECT * FROM subject WHERE subject_id = :id")
        result = connection.execute(sql_get_id, {'id': id})
        subject = result.mappings().all()
        connection.close()
        return subject

    def delete_subject(self, id):
        connection = self.qa_db.connect()
        connection.execute(
            text("DELETE FROM subject WHERE subject_id = :id_del"),
            {'id_del': id})

        connection.commit()
        connection.close()

    def update_subject(self, title, id):
        connection = self.qa_db.connect()
        sql_edit = text("update subject "
                        "set subject_title = :new_title"
                        " where subject_id = :id")
        result = connection.execute(sql_edit,
                                    {'new_title': title, 'id': id})

        connection.commit()
        connection.close()
        return result.rowcount

    def get_subjects(self):
        connection = self.qa_db.connect()
        result = connection.execute(text(
            "select * from subject"))
        rows = result.mappings().all()

        connection.close()
        return rows

    def get_students(self):
        connection = self.qa_db.connect()
        result = connection.execute(text(
            "select * from student"))
        rows = result.mappings().all()

        connection.close()
        return rows

    def add_new_student(self, id, level):
        connection = self.qa_db.connect()
        sql_add = text("INSERT INTO student (\"user_id\", \"level\") "
                       "VALUES (:new_user_id, :new_level)")
        connection.execute(sql_add,
                           {'new_user_id': id, 'new_level': level})

        connection.commit()
        connection.close()

    def delete_student(self, id):
        connection = self.qa_db.connect()
        connection.execute(
            text("DELETE FROM student WHERE user_id = :id_delete"),
            {'id_delete': id})

        connection.commit()
        connection.close()

    def get_min_id_student(self):
        connection = self.qa_db.connect()
        sql_get = connection.execute(text("SELECT MIN"
                                          " (\"user_id\") FROM student"))

        id_user = sql_get.scalar()
        connection.close()
        return id_user

    def edited_student(self, level, id):
        connection = self.qa_db.connect()
        sql_edit = text("UPDATE student "
                        "set level = :new_level"
                        " WHERE user_id = :id")
        result = connection.execute(sql_edit,
                                    {'new_level': level, 'id': id})

        connection.commit()
        connection.close()
        return result
