async def test_create_template_201(
    test_client,
    mock_request_create_template_success,
    mock_response_create_template_success,
):
    response = await test_client.post("/v1/templates", json=mock_request_create_template_success)
    assert response.status_code == 201
    response_data = response.json()
    response_data["response"].pop("id")
    assert response_data == mock_response_create_template_success


async def test_create_template_409(
    test_client,
    create_template,  # noqa: ARG001
    mock_request_create_template_success,
):
    response = await test_client.post("/v1/templates", json=mock_request_create_template_success)
    assert response.status_code == 409
