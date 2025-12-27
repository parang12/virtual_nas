mkdir -p include/core include/web
mkdir -p src/core src/web/templates
mkdir -p storage
mkdir -p obj

touch include/core/storage.htouch include/core/system_info.h

touch src/core/storage.c
touch src/core/system_info.c

touch src/web/app.py
touch src/web/bridge.py
chmod +x setup_project.sh
echo "✅ NAS 프로젝트 구조 생성 완료!"
