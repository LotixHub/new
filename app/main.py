from fastapi import FastAPI

app = FastAPI(title="FinalRound AI - Ultimate")

@app.get("/")
async def read_root() -> dict[str, str]:
    """
    Health check endpoint.

    Returns `{"health": "ok"}` if the service is running.
    """
    return {"health": "ok"}