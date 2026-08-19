# RUN:   python -m pytest
# It operates relative to the directory where you execute the command


from fastapi.testclient import TestClient
from src.main import app  # Here the context of the file is relative 
# to what was passed when running the command 'pytest'

client = TestClient(app)

def test_read_root():
    """ testing a fastapi endpoint """ 
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {'response':'hello world'}
