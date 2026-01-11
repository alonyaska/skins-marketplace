from fastapi import UploadFile, APIRouter
import  shutil



router = APIRouter(
    prefix="/images",
    tags=["Loading Image"]
)


@router.post("/skins")
async def  add_skins_image(name:int ,file: UploadFile ):
    with open(f"app/static/images/{name}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
