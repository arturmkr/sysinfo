from fastapi import FastAPI, Request, Query
from fastapi.responses import RedirectResponse
import datetime

app = FastAPI()


@app.get("/info")
async def track_user(request: Request, ref_code: str = Query(None), dst: str = Query(None)):
    user_agent = request.headers.get("User-Agent")
    ip_address = request.client.host
    current_time = datetime.datetime.now()
    with open("user_data.txt", "a") as file:
        file.write(
            f"time:{current_time.time()}, ref_code:{ref_code}, dst:{dst}, ip:{ip_address}, agent:{user_agent}\n")
    return RedirectResponse(url=dst)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)
