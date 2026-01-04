#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <dirent.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * [NAS 파일 쓰기]
 * Nas 저장소에 파일을 바이너리 형태로 저장하는 함수
 * @param path 저장할 절대 경로
 * @param data 저장할 데이터의 시작 주소
 * @param size 저장할 데이터의 총 크기
 * 성공시 0
 * 실패시 -1
 */
int c_save_file(const char* path, const unsigned char* data, size_t size) {
    FILE *fp = fopen(path, "wb");
    if (fp == NULL){
        perror("NAS Engine Error (fopen)");
        return -1;
    }
    size_t written = fwrite(data, 1, size, fp);

    if(written < size){
        perror("NAS Engine Error (fopen)");
        fclose(fp);
        return -1;
    }
    fclose(fp);
    return 0; 
}

/**
 * [NAS 파일 읽기]
 * 지정된 경로의 파일을 열어 메모리(Heap)에 할당하고 그 주소를 반환합니다.
 * @param path 읽어드릴 위치 pointer
 * @param out_size 파일의 크기(Bytes)를 저장하여 호출자에게 알려줄 포인터 변수
 * 실패시 NULL 
 * 성공시 동적메모리가 시작하는 포인터 위치 반환
 */
unsigned char* c_read_file(const char* path, size_t* out_size){
    
    FILE *fp = fopen(path, "rb");
    if (fp == NULL){
        perror("NAS Engine Error (fopen)");
        return NULL;
    }

    fseek(fp, 0, SEEK_END);
    size_t size = ftell(fp);
    rewind(fp);

    unsigned char* buffer = (unsigned char*)malloc(size);
    if(!buffer){
        fclose(fp);
        return NULL;
    }

    size_t read_size = fread(buffer, 1, size, fp);
    if (read_size < size) {
        free(buffer); 
        fclose(fp);
        return NULL;
    }
    fclose(fp);

    *out_size = size; 

    return buffer;    
}


/**
 * [NAS 메모리 해제]
 * c_read_file에서 할당된 메모리를 안전하게 해제합니다.
 */
void c_free_buffer(unsigned char* buffer) {
    if (buffer != NULL) {
        free(buffer);
    }
}