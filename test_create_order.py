import requests

BASE_URL = "https://6475add9-c96e-47b3-a1a7-d56346eeb7b8.serverhub.praktikum-services.ru/"

def test_get_order_by_track():

    order_data = {
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "address": "Moscow",
        "metroStation": 4,
        "phone": "+79999999999",
        "rentTime": 5,
        "deliveryDate": "2026-03-10",
        "comment": "Test order",
        "color": ["BLACK"]
    }

    # Создание заказа
    response = requests.post(f"{BASE_URL}/api/v1/orders", json=order_data)

    track = response.json()["track"]

    # Получение заказа по треку
    get_order = requests.get(f"{BASE_URL}/api/v1/orders/track?t={track}")

    # Проверка ответа
    assert get_order.status_code == 200
