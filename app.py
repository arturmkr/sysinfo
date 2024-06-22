import logging

from fastapi import FastAPI, Request, Query
from fastapi.responses import RedirectResponse
import datetime
import uvicorn

logging.basicConfig(level=logging.INFO)

app = FastAPI()


@app.get("/info")
async def track_user(request: Request, ref_code: str = Query(None), dst: str = Query(None)):
    user_agent = request.headers.get("User-Agent")
    ip_address = request.client.host
    current_time = datetime.datetime.now()
    with open("user_data.txt", "a") as file:
        client_info = f"time:{current_time.time()}, ref_code:{ref_code}, dst:{dst}, ip:{ip_address}, agent:{user_agent}"
        logging.info(f"Client info {client_info}")
        file.write(f"{client_info}\n")
    return RedirectResponse(url=dst)


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=80)
