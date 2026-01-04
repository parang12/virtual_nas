# 1. 컴파일러 및 옵션 설정
CC = gcc
# -Wall: 경고 메시지 표시, -fPIC: 공유 라이브러리 필수 옵션, -I: 헤더 파일 경로 지정
CFLAGS = -Wall -fPIC -I./include
# -shared: 공유 라이브러리(.so) 생성 옵션
LDFLAGS = -shared

# 2. 타겟 파일 이름 및 경로 설정
TARGET = libstorage.so
SRCS = src/core/storage.c src/core/system_info.c
# 소스 파일(.c) 목록을 이용해 오브젝트 파일(.o) 목록 자동 생성
OBJS = $(SRCS:src/core/%.c=obj/%.o)

# 3. 기본 빌드 규칙
all: $(TARGET)

# 4. 최종 결과물(.so) 생성 규칙
$(TARGET): $(OBJS)
	$(CC) $(LDFLAGS) -o $@ $^

# 5. 중간 결과물(.o) 생성 규칙 (패턴 규칙)
# obj 폴더가 없으면 생성하고 컴파일 진행
obj/%.o: src/core/%.c
	@mkdir -p obj
	$(CC) $(CFLAGS) -c $< -o $@

# 6. 정리 규칙 (생성된 파일 삭제)
clean:
	rm -rf obj $(TARGET)

# .PHONY는 파일 이름과 타겟 이름이 겹치는 것을 방지함
.PHONY: all clean