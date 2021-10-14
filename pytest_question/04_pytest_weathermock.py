# contents of test_app.py, a simple test for our API retrieval
# import requests for the purposes of monkeypatching
import requests
from threading import Thread
import json

# our app.py that includes the get_json() function
# this is the previous code block example
import weatherService

# custom class to be the mock return value
# will override the requests.Response returned from requests.get
class MockResponse:
    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        return {"mock_desc": "mock_rainy"}


def test_TempGetter(monkeypatch):
    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the .json() method.
    def mock_get(*args, **kwargs):
        return MockResponse()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # app.get_json, which contains requests.get, uses the monkeypatch
    result = weatherService.TempGetter("https://fakeurl")
    assert result == {'mock_desc': 'mock_rainy'}