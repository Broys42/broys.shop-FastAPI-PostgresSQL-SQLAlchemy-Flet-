import asyncio
from fastapi.responses import HTMLResponse
import fastapi_users
import uvicorn
from contextlib import asynccontextmanager
from src.auth.auth import auth_backend
from src.auth.manager import get_user_manager
from src.auth.schemas import UserCreate, UserRead
from src.database.database import User
import flet as ft
import flet.fastapi as flet_fastapi
from ui.view import View
from fastapi import Depends, FastAPI, Request
from fastapi_users import FastAPIUsers
from fastapi.middleware.cors import CORSMiddleware
from src.routers.headphones import headphones_router
from src.viewmodel.viewmodel import ViewModel
from src.model.model import Model


@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()

app = FastAPI(lifespan=lifespan)
parser_product_id = FastAPI(lifespan=lifespan)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(headphones_router)

current_superuser = fastapi_users.current_user(active=True, superuser=True)

@app.get("/protected-route")
def protected_route(user: User = Depends(current_superuser)):
    return f"Hello, {user.email}"

model = Model()
viewmodel = ViewModel(model)
view = View(viewmodel)

app.mount("/", flet_fastapi.app(view.main))
