# Юрий Буров, 41-я когорта - Финальный проект. Инженер по тестированию плюс.
import data
import order_requests


def test_get_order_by_track():

    # создаем заказ
    response = order_requests.create_order(data.ORDER_DATA)
    assert response.status_code == 201

    track = response.json()["track"]

    # получаем заказ по треку
    response = order_requests.get_order_by_track(track)

    assert response.status_code == 200