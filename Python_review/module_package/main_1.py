#패키지 내부의 모듈을 모두 읽어 들입니다.
from test_package import *

#모듈 내부의 변수를 출력
print(module_a.variable_a)
print(module_b.variable_b)

#main_1.py파일로 패키지를 읽어 들일 떄, __init__.py를 가장 먼저 실행하는 것을 알 수 있음