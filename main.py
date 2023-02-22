from fastapi.middleware.cors import CORSMiddleware
from typing import Union

import uvicorn
from fastapi import FastAPI, File
from pydantic import BaseModel
from starlette.responses import FileResponse

import utils
from common_func import start, end

app = FastAPI()


origins = [
    "http://localhost:4200",
    "http://10.1.10.36:4300",
    "http://10.1.20.44:88"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/import_file/")
def import_file(excel_file: bytes = File()):
    data = {}
    # file_name = Path(ex)
    working_days = utils.handle_get_data_from_file(
        start=start, end=end
    )
    data_file = utils.handle_open_file(excel_file=excel_file, working_days=working_days, data=data)

    utils.handle_export_file(data_file)

    # response = FileResponse(
    #     path=out_file, media_type='application/octet-stream', filename=out_file
    # )
    response = {
        "meta": {
            "code": 200,
            "message": "SUCCESS"
        },
        "data": None
    }
    return response


@app.get('/download_file/')
def download_file():
    file_path = "TimeSheet.xlsx"
    return FileResponse(path=file_path, filename=file_path)


if __name__ == "__main__":
    uvicorn.run(app, host="10.1.20.44", port=8000)


# application/vnd.openxmlformats-officedocument.spreadsheetml.sheet