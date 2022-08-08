from fastapi import fastAPI
app = fastAPI()

@app.get("/")

def root():
    return {"message": "Hello!"}


