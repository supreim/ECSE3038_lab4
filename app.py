import os
from bson import ObjectId
from fastapi import FastAPI
import motor.motor_asyncio
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


class Profile(BaseModel):
    id: str | None=None
    last_updated: str | None=None
    username: str
    color: str
    role: str

class Tank(BaseModel):
    id: str | None=None
    location: str
    lat: str
    long: str

class UpdateTank(BaseModel):
    location: str | None=None
    lat: str | None=None
    long: str | None=None



app = FastAPI()


origins = [ "https://ecse3038-lab3-tester.netlify.app" ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('db_url'))

db = client.get_database("tutorial4")
people_collection = db.get_collection("Profile")


@app.get("/profile/")
async def create_item():
    return

@app.post("/profile/")
async def create_item(profile: Profile):
    return

@app.get("/tank/")
async def create_item():
    return

@app.post("/tank/")
async def create_item(tank: Tank):
    return

@app.patch("/tank/{id}")
async def create_item(id:str, tank: UpdateTank):
    return

@app.delete("/tank/{id}")
async def create_item(id:str):
    return

