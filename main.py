from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from user_agents import parse

app = FastAPI()

@app.get("/track")
async def track_user(request: Request):
    user_agent = request.headers.get("User-Agent")
    ip_address = request.client.host
    # Parse the user agent string to get the OS and browser information
    with open("user_data.txt", "a") as file:
        file.write(f"{ip_address},{user_agent}\n")
    return RedirectResponse(url="https://www.google.com")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
