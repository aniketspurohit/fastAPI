from typing import Optional
import fastapi

router = fastapi.APIRouter()


@router.get("/api/umbrella")
def need_an_umbrella(city: str, state: Optional[str] = None):
    return {"city": city}
