from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def get_hello():
    """ Simply a fastapi endpoint """
    return {'response': 'hello world'}
