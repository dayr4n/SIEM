from fastapi import APIRouter

router = APIRouter()


@router.post("/agents/register")
def register():
    return {"Agent recieved , thank you we will start the monitorization .."}


@router.post("/agents/dynamic")
def recieve_dynamic(data: dict):
    print(data)
    return {"status": "recieved"}


@router.post("/agents/static")
def recieve_static(data: dict):
    print(data)
    return {"status": "recieved"}
