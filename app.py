import os
from bson import ObjectId
from fastapi import FastAPI, status
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

db = client.get_database("Profile")
user_collection = db.get_collection("User")
tanks_collection = db.get_collection("Tanks")


@app.get("/profile/")
async def get_profile():
    #created_profile = await user_collection.find_one({"_id": })
    return

@app.post("/profile/", 
        response_description="Add new student",
 	    response_model=Profile,
	    status_code=status.HTTP_201_CREATED,
	    response_model_by_alias=False,)
async def create_profile(profile: Profile):
    new_user = await user_collection.insert_one(profile.model_dump(by_alias=True, exclude=["id"]))
    #created_profile = await user_collection.find_one({"_id": new_user.inserted_id})
    return profile.model_dump(by_alias=True, exclude=["id"])

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

