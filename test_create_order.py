# Юрий Буров, 41-я когорта - Финальный проект. Инженер по тестированию плюс.
import requests
from config import BASE_URL
from data import ORDER_DATA


def test_get_order_by_track():

    # Создание заказа
    response = requests.post(f"{BASE_URL}/api/v1/orders", json=ORDER_DATA)
    assert response.status_code == 201

    # Получаем трек заказа
    track = response.json()["track"]

    # Получение заказа по треку
    get_order_url = f"{BASE_URL}/api/v1/orders/track"
    get_order = requests.get(f"{BASE_URL}/api/v1/orders/track", params={"t": track})

    # Проверка ответа
    assert get_order.status_code == 200
