import os
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 경로설정
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
STORAGE_DIR = os.path.join(BASE_DIR, "storage")
TEMPLATES_DIR = os.path.join(BASE_DIR, "src", "web", "templates")

# 
if not os.path.exists(STORAGE_DIR):
    os.makedirs(STORAGE_DIR)

# 3. 템플릿 엔진 설정
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# [GET] 메인 페이지: 파일 목록 보여주기
@app.get("/", response_class=HTMLResponse) #html 응답
async def index(request: Request):
    # storage 폴더에서 파일 리스트 읽기
    files = os.listdir(STORAGE_DIR)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "files": files
    })

# [POST] 파일 업로드 처리
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(STORAGE_DIR, file.filename)
    
    # 파일을 storage 폴더에 저장
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    # 업로드 후 다시 메인 페이지로 이동 (새로고침 효과)
    return RedirectResponse(url="/", status_code=303)