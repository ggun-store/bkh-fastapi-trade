
import datetime
import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()



@app.get("/")
async def main():
        return f"Hello fastapi 날짜 : {datetime.datetime.today()}" 


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)