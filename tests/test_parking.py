import json


def test_slots(app, client):
    res = client.get('/slots?slot=3')
    assert res.status_code == 200
    expected = {"slot": "3", "vechicle_plate_num": "AS-9529XZ"}
    assert expected == json.loads(res.get_data(as_text=True))


def test_park(app, client):

    data = {"vechicle_number": "AS-9531XZ"}

    headers = {'Content-Type': 'application/json'}

    res = client.post('/park', data=json.dumps(data), headers=headers)
    assert res.status_code == 200
    expected = {'assigned_slot': 4,
                'vechicle_num': 'AS-9531XZ'}
    assert expected == json.loads(res.get_data(as_text=True))


def test_unpark(app, client):
    data = {"vechicle_number": "AS-9531XZ"}

    headers = {'Content-Type': 'application/json'}

    res = client.post('/unpark', data=json.dumps(data), headers=headers)
    assert res.status_code == 200
    expected = {'slot': 4,
                'vechicle_num': 'AS-9531XZ',
                'status': 'successfully removed'}
    assert expected == json.loads(res.get_data(as_text=True))

