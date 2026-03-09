from methods.methods import YouGile


url_base = YouGile("https://yougile.com/api-v2/")


def test_create_project_none_title():
    title = ""
    result_project = url_base.create_project(title)
    body = result_project.json()

    assert result_project.status_code == 400
    assert body["message"][0] == "title should not be empty"


def test_get_id_project_wrong_id():
    wrong_id = "1233456"
    get_result = url_base.get_project_id(wrong_id)
    body = get_result.json()

    assert get_result.status_code == 404
    assert body["message"] == "Проект не найден"


def test_edit_project_with_out_key():
    title = "Project"
    create_result = url_base.create_project(title)
    new_id = create_result.json()["id"]
    new_title = "Edited project"
    edit_result = url_base.edit_none_token(new_id, new_title)

    status_code = edit_result["statusCode"]
    message = edit_result["message"]

    assert status_code == 401
    assert message == "Unauthorized"
    url_base.delete_project(new_id)
