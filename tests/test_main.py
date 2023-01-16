import requests

api_url = 'http://localhost:8000'


def test_healthcheck():
    response = requests.get(f'{api_url}/__health')
    assert response.status_code == 200


class TestStudents():
    def test_get_empty_staffmember(self):
        response = requests.get(f'{api_url}/v1/staffmembers')
        assert response.status_code == 200
        assert len(response.json()) == 0

    def test_create_staffmember(self):
        body = {"NameStaffMember": "Mac Mie 10", "AgeStaffMember": "24", "RoleStaffMember": "Assistant"}
        response = requests.post(f'{api_url}/v1/staffmembers', json=body)
        assert response.status_code == 200
        assert response.json().get('NameStaffMember') == 'Mac Mie 10'
        assert response.json().get('AgeStaffMember') == '24'
        assert response.json().get('RoleStaffMember') == 'Assistant'
        assert response.json().get('IdStaffMember') == '0'

    def test_get_staffmember_by_id(self):
        response = requests.get(f'{api_url}/v1/staffmembers/0')
        assert response.status_code == 200
        assert response.json().get('NameStaffMember') == 'Mac Mie 10'
        assert response.json().get('AgeStaffMember') == '24'
        assert response.json().get('RoleStaffMember') == 'Assistant'
        assert response.json().get('IdStaffMember') == '0'

    def test_get_not_empty_staffmember(self):
        response = requests.get(f'{api_url}/v1/staffmembers')
        assert response.status_code == 200
        assert len(response.json()) == 1
