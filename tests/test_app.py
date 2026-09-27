from src.app import welcome

def test_welcome():
    assert welcome() == "Welcome to the Collaborative Software Workflow!"
