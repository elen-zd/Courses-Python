from methods.methods import YouGile


url_base = YouGile("https://yougile.com/api-v2/")


def test_create_project():
    title = "Create"
    result_project = url_base.create_project(title)
    new_id = result_project.json()["id"]

    assert result_project.json()["id"] is not None
    assert result_project.status_code == 201
    url_base.delete_project(new_id)


def test_get_id_project():
    title = "get id"
    create_result = url_base.create_project(title)
    new_id = create_result.json()["id"]

    get_result = url_base.get_project_id(new_id)

    assert get_result.status_code == 200
    assert get_result.json()["id"] == new_id
    assert get_result.json()["title"] == title
    url_base.delete_project(new_id)


def test_edit_project():
    title = "Project"
    create_result = url_base.create_project(title)
    new_id = create_result.json()["id"]
    new_title = "Edited project"
    edit_result = url_base.egit_project(new_id, new_title)

    assert edit_result.json()["id"] == new_id
    assert edit_result.status_code == 200
    url_base.delete_project(new_id)


def test_all_projects():
    response = url_base.all_projects()
    projects = response.json()

    assert response.status_code == 200
    assert len(projects) > 0
