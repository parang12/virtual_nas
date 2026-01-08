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


