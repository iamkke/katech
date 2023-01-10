from fastapi import HTTPException

from api_mycar import MycarAPI

_DB_CAR_OWNER = {
    "12가3456":"홍길동"
}

def _verify(regnum, owner):
    if not regnum or not owner:
        raise HTTPException(status_code=400, detail="parameter must be set")
    if regnum not in _DB_CAR_OWNER: 
        raise HTTPException(status_code=404, detail=f"{regnum} and {owner} is not found")

async def inquiry(regnum, owner):
    _verify(regnum, owner)
    
    mycar = MycarAPI(regnum, owner)
    return await mycar.call_apis()
