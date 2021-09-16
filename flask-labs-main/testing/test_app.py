from ragtime import create_app

def test_app_creation():
    app = create_app('testing')
    assert app