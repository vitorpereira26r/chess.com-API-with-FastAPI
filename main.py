from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter
import requests
import os

from exceptions import ExceptionHandler, exception_handler

load_dotenv()
API_URL = os.getenv("CHESS_API_URL")

HEADERS = {
    'User-Agent': f'username: ${os.getenv("CHESS_USERNAME")}, email: ${os.getenv("CHESS_EMAIL")}'
}

app = FastAPI()


app.add_exception_handler(ExceptionHandler, exception_handler)


api_router = APIRouter(prefix="/api", tags=["api"])


@api_router.get("/player/{username}")
async def player(username: str):
    url = f"{API_URL}/pub/player/{username}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        raise ExceptionHandler(status_code=404, message=f"User {username} not found")


@api_router.get("/player/title/{title}")
async def title(title: str):
    url = f"{API_URL}/pub/titled/{title}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        raise ExceptionHandler(status_code=404, message=f"Title {title} not found")


@api_router.get("/player/stats/{username}")
async def stats(username: str):
    url = f"{API_URL}/pub/player/{username}/stats"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        raise ExceptionHandler(status_code=404, message=f"User {username} not found")


@api_router.get("/player/games/{username}")
async def games(username: str):
    url = f"{API_URL}/pub/player/{username}/games"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        raise ExceptionHandler(status_code=404, message=f"User {username} not found")


@api_router.get("/player/daily/games/{username}")
async def daily(username: str):
    url = f"{API_URL}/pub/player/{username}/games"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        raise ExceptionHandler(status_code=404, message=f"User {username} not found")


@api_router.get("/player/games/archives/{username}")
async def games_archives(username: str):
    url = f"{API_URL}/pub/player/{username}/games/archives"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        raise ExceptionHandler(status_code=404, message=f"User {username} not found")


@api_router.get("/player/games/{username}/{year}/{month}")
async def games_year_month(year: str, month: str, username: str):
    url = f"{API_URL}/pub/player/{username}/games/{year}/{month}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        raise ExceptionHandler(status_code=404, message=f"User {username} not found")


@api_router.get("/player/clubs/{username}")
async def clubs(username: str):
    url = f"{API_URL}/pub/player/{username}/clubs"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        raise ExceptionHandler(status_code=404, message=f"User {username} not found")


@api_router.get("/player/matches/{username}")
async def matches(username: str):
    url = f"{API_URL}/pub/player/{username}/matches"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        raise ExceptionHandler(status_code=404, message=f"User {username} not found")


@api_router.get("/player/tournaments/{username}")
async def matches(username: str):
    url = f"{API_URL}/pub/player/{username}/tournaments"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        raise ExceptionHandler(status_code=404, message=f"User {username} not found")


app.include_router(api_router)
