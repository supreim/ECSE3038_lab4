from datetime import date, datetime
import os
from fastapi import FastAPI, HTTPException, status
import motor.motor_asyncio
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from pymongo import ReturnDocument




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

#print(os.getenv('db'))
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.4.0")

db = client.get_database("Profile")
user_collection = db.get_collection("User")
tanks_collection = db.get_collection("Tanks")


@app.get("/profile/",status_code=status.HTTP_200_OK)
async def get_profile():
     tanks:Profile = await user_collection.find_one()
     tanks["_id"] = str(tanks["_id"])
     return tanks

@app.post("/profile/", 
        response_description="Add new User",
 	    response_model=Profile,
	    status_code=status.HTTP_201_CREATED,
	    response_model_by_alias=False,)
async def create_profile(user: Profile):
    if len(await user_collection.find().to_list()) > 0:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User already created")
    
    new_user = await user_collection.insert_one(user.model_dump(by_alias=True, exclude=["id"]))
    created_user = await user_collection.find_one({"_id": new_user.inserted_id})
    created_user["_id"] = str(created_user["_id"])
    return created_user

@app.get("/tank/", status_code=status.HTTP_200_OK)
async def create_item():
    tanks:Tank = await tanks_collection.find().to_list()
    
    for (i,tank) in enumerate(tanks):
        tanks[i]["_id"] = str(tanks[i]["_id"])
    return tanks


@app.post("/tank/", status_code=status.HTTP_201_CREATED)
async def create_item(tank: Tank):

    if len(await user_collection.find().to_list()) == 0:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No profile has been created")
    if not (tank.location and tank.lat and tank.long):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Missing data")

    new_tank = await tanks_collection.insert_one(tank.model_dump(by_alias=True, exclude=["id"]))
    created_tank = await tanks_collection.find_one({"_id": new_tank.inserted_id})
    created_tank["_id"] = str(created_tank["_id"])

    await user_collection.update_one({},{"$set": {"last_updated":str(datetime.now())}})

    
    return created_tank

@app.patch("/tank/{id}",status_code=status.HTTP_201_CREATED)
async def create_item(id:str, tank: UpdateTank):
    tank = await tanks_collection.find_one_and_update({"_id":id},{"$set":tank},return_document = ReturnDocument.AFTER)
    return tank

@app.delete("/tank/{id}")
async def create_item(id:str):
    return

