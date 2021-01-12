from fastapi import File, UploadFile, FastAPI, Form, status, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
import base64
import uvicorn
from fastapi.responses import JSONResponse


##importing models
#from models import ImageModel, PotrawaModel
#logging
import logging
logger = logging.getLogger(__name__)

##DB
from motor.motor_asyncio import AsyncIOMotorClient
MONGODB_URI = 'mongodb://piotrek:testtest@cluster0-shard-00-00.obezc.mongodb.net:27017,cluster0-shard-00-01.obezc.mongodb.net:27017,cluster0-shard-00-02.obezc.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-pijk1g-shard-0&authSource=admin&retryWrites=true&w=majority'
MONGODB_DATABASE = 'PRZEPISY'
MONGODB_COLLECTION = 'potrawy'
import uuid
from pydantic import BaseModel, Field

class ImageModel(BaseModel):
    base64: str
    content_type: str
    html: str


class PotrawaModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    kategoria: str = None
    nazwa: str = None
    przepis: str = None
    image: ImageModel
##

app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)
templates = Jinja2Templates(directory='templates/')

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(MONGODB_URI)
    app.mongodb = app.mongodb_client[MONGODB_DATABASE]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()


@app.post("/create", response_description="Dodaj nową potrawe")
async def post_picture(kategoria:str = Form(...),nazwa:str = Form(...),przepis:str = Form(...),file: UploadFile = File(...)):
    contents = await file.read()
    data_uri = base64.b64encode(contents).decode('ascii')
    image = ImageModel(base64=data_uri,content_type=file.content_type,html="data:{1};base64,{0}".format(data_uri,file.content_type))
    potrawa=PotrawaModel(kategoria=kategoria,nazwa=nazwa,przepis=przepis, image=image)
    potrawa = jsonable_encoder(potrawa)
    new_potrawa = await app.mongodb["potrawy"].insert_one(potrawa)
    created_potrawa = await app.mongodb["potrawy"].find_one(
        {"_id": new_potrawa.inserted_id}
    )
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_potrawa)


@app.get("/api/v1/{kategoria}", response_description="Lista potraw po kategorii")
async def list_potrawy(kategoria: str):
    potrawy = []
    for doc in await app.mongodb["potrawy"].find({"kategoria": kategoria}).to_list(length=1000):
        potrawy.append(doc)
    if not potrawy:
        raise HTTPException(status_code=404, detail=f"Dana kategoria: {kategoria} nie istnieje")
    else:
        return potrawy
    
@app.get("/api/v1", response_description="Lista potraw")
async def list_potrawy_all():
        potrawy = []
        for doc in await app.mongodb["potrawy"].find().to_list(length=100):
            potrawy.append(doc)
        return potrawy


@app.get("/")
async def load_page(request: Request):
        return templates.TemplateResponse('index.html', context={'request': request})

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True)