from fastapi import FastAPI, File, UploadFile
import PIL.Image
from io import BytesIO
from image2ascii import img2asci

app = FastAPI()
def insert_newlines(string, every=64):
    return '\n'.join(string[i:i+every] for i in range(0, len(string), every))

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")

async def create_upload_file(file: UploadFile = File(...)):
    a=await file.read()
    image=PIL.Image.open(BytesIO(a))
    character, width = img2asci(image)
    print(type(character))
    output={"op":insert_newlines(character, width)}
    return output

