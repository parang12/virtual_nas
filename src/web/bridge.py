import ctypes
import os


# 라이브러리 경로 설정 
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lib_path = os.path.join(os.getcwd(), "libstorage.so")
lib = ctypes.CDLL(lib_path) 


# C 함수 시그니처 함수 규격 정의
lib.c_save_file.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]
lib.c_save_file.restype = ctypes.c_int

lib.c_read_file.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)]
lib.c_read_file.restype = ctypes.POINTER(ctypes.c_ubyte)

lib.c_free_buffer.argtypes = [ctypes.POINTER(ctypes.c_ubyte)]
lib.c_free_buffer.restype = None

def save_file(path:str, data: bytes) -> int:
    """파일 저장 함수

    ** C 엔진을 사용하여 파일을 읽어 bytes로 반환합니다. ** 

    Args:
        path (str): 저장할 파일 경로
        data (bytes): 저장할 파일 데이터
    """

    size = ctypes.c_size_t(len(data))
    result = lib.c_save_file(path.encode('utf-8'), data, size) 
    return result == 0


def read_file(path:str) -> bytes:
    """파일 읽기 함수

    ** C 엔진을 사용하여 파일을 읽어 bytes로 반환합니다. ** 

    Args:
        path (str): 읽을 파일 경로

    Returns:
        bytes: 읽은 파일 데이터
    """
    size = ctypes.c_size_t()

    ptr = lib.c_read_file(path.encode('utf-8'), ctypes.byref(size))
    if not ptr:
        return None
    
    try:
        data = ctypes.string_at(ptr, size.value)
        return data
    finally:
        lib.c_free_buffer(ptr)