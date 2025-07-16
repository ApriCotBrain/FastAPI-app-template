import uuid


async def test_get_template_by_id_200(
    test_client,
    create_template,
    mock_response_get_template_by_id_success,
):
    response = await test_client.get(f"/v1/templates/{create_template}")
    assert response.status_code == 200
    response_data = response.json()
    response_data["response"].pop("id")
    assert response_data == mock_response_get_template_by_id_success


async def test_get_template_by_id_404(test_client):
    response = await test_client.get(f"/v1/templates/{uuid.uuid4()}")
    assert response.status_code == 404
