from yandex_disk_api import YandexDisk


def test_create_folder(token, folder_path):
    ya = YandexDisk(token)
    result = ya.create_folder(folder_path)
    expected = 201
    assert result == expected


def test_create_the_same_folder(token, folder_path):
    ya = YandexDisk(token)
    result = ya.create_folder(folder_path)
    expected = 409
    assert result == expected


def test_create_folder_with_incorrect_folder_path(token):
    ya = YandexDisk(token)
    result = ya.create_folder('//')
    expected = 404
    assert result == expected


def test_create_folder_without_token(folder_path):
    ya = YandexDisk('')
    result = ya.create_folder(folder_path)
    expected = 401
    assert result == expected


def test_create_folder_without_folder_path(token):
    ya = YandexDisk(token)
    result = ya.create_folder('')
    expected = 400
    assert result == expected
