from fastapi import FastAPI

app = FastAPI(
    title="HockeyLab API",
    description="API for NHL schedules, statistics, and game predictions.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to HockeyLab!",
        "status": "API is running",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}