from fastapi import FastAPI

## intiate the app instance 
app = FastAPI()

## the intial EndPoint(Test Server Connection)
@app.get("/")
def test_server_connection(): 
    return {
        "message": "The server is up and running ✅"
    }