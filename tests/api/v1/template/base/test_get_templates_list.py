async def test_get_template_by_id_200(
    test_client,
    create_template,  # noqa: ARG001
    mock_response_get_templates_list_success,
):
    response = await test_client.get("/v1/templates")
    assert response.status_code == 200
    response_data = response.json()
    for template in response_data["response"]:
        template.pop("id")
    assert response_data == mock_response_get_templates_list_success
