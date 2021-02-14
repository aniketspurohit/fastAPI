import fastapi
import uvicorn

from views import home
from apis import weather_api

api = fastapi.FastAPI()

# Add routers from different folders
def configure():
    api.include_router(home.router)
    api.include_router(weather_api.router)


configure()
if __name__ == "__main__":
    uvicorn.run(api, debug = True)
