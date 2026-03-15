from sqlalchemy import inspect
from tables.Tables import Tables

connection_string = "postgresql://postgres:3579@localhost:5432/QA Practic"
qa_practice = Tables(connection_string)


def test_db_connection():
    inspector = inspect(qa_practice.qa_db)
    names = inspector.get_table_names()
    print(names)


def test_add_subject():
    title = "Test"
    id = 143
    qa_practice.add_subject(title, id)
    id_sub = qa_practice.get_max_id_subject()

    assert id_sub == 143

    delete = qa_practice.delete_subject(id_sub)
    assert delete is None


def test_update_subject():
    title = "Test"
    id_sub = 111
    qa_practice.add_subject(title, id_sub)
    qa_practice.get_id_subject(id_sub)
    result_before = qa_practice.get_subjects()

    new_title = "New test"
    qa_practice.update_subject(new_title, id_sub)
    result_after = qa_practice.get_subjects()

    qa_practice.delete_subject(id_sub)

    assert result_before[-1]["subject_title"] == title
    assert result_before[-1]["subject_id"] == id_sub
    assert result_after[-1]["subject_title"] == new_title

    found = False
    for subject in result_after:
        if subject["subject_title"] == new_title:
            found = True
            break
    assert found


def test_delete_subject():
    title = "Delete test"
    id = 56
    qa_practice.add_subject(title, id)
    before = qa_practice.get_subjects()

    qa_practice.delete_subject(id)
    after = qa_practice.get_subjects()

    assert len(before) - len(after) == 1


def test_create_student():
    id_user = 1
    level = "Testing"
    qa_practice.add_new_student(id_user, level)
    student = qa_practice.get_min_id_student()

    assert student == id_user

    delete = qa_practice.delete_student(student)
    assert delete is None


def test_edit_student():
    level = "Test"
    id_user = 1
    qa_practice.add_new_student(id_user, level)
    result_before = qa_practice.get_students()

    new_level = "Test level"
    qa_practice.edited_student(new_level, id_user)
    result_after = qa_practice.get_students()

    qa_practice.delete_student(id_user)

    assert result_before[-1]["level"] == level
    assert result_after[-1]["level"] == new_level
    assert result_after[-1]["user_id"] == id_user


def test_delete_student():
    level_student = "Delete test"
    id_user = 0
    qa_practice.add_new_student(id_user, level_student)
    before = qa_practice.get_students()

    qa_practice.delete_student(id_user)
    after = qa_practice.get_students()

    assert len(before) - len(after) == 1
