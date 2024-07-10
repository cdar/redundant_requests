from time import sleep

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
def get_config():
    print("test")
    sleep(20)

    count = 4
    result = 0
    for i in range(0, 200_000_000 * count + 1, 1):
        result += i

    print("done")


if __name__ == "__main__":
    kwargs = {"app": "main:app", "host": "0.0.0.0", "port": 8004, "workers": 1}

    uvicorn.run(**kwargs)

