#ifndef STORAGE_H
#define STORAGE_H

#include <stddef.h>

/**
 * @brief NAS 저장소에 저장소에 파일을 바이너리 형태로 저장
 */
int c_save_file(const char* path, const unsigned char* data, size_t size);

/**
 * @brief NAS 저장소에 경로의 파일을 읽어 메모리 주소로 반환
 */
unsigned char* c_read_file(const char* path, size_t* out_size);


/**
 * @brief 사용이 끝난 메모리 버퍼 해제
 */

void c_free_buffer(unsigned char* buffer);

#endif