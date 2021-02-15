from typing import Optional, List
import httpx
import fastapi

from models.location import Location
from models.umbrella_status import UmbrellaStatus

router = fastapi.APIRouter()


@router.get("/api/umbrella", response_model=UmbrellaStatus)
async def need_an_umbrella(location: Location = fastapi.Depends()):
    url = f"https://weather.talkpython.fm/api/weather?city={location.city}&country={location.country}&units=imperial"

    if location.state:
        url += f"&state={location.state}"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        data = resp.json()

    weather = data.get("weather", {})
    category = weather.get("category", "YAYAY")
    forecast = data.get("forecast", {})
    temp = forecast.get("temp", 0.0)

    if category.lower().strip() == "rain":
        bring = True
    else:
        bring = False

    # try:
    #     return UmbrellaStatus(bring_umbrella=bring, temp=temp)
    # except ValidationError as e:
    #     print(e)

    u = UmbrellaStatus(bring_umbrella=bring, temp=temp)
    return u
