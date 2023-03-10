# BETTER WAY 4 : C 스타일 형식 문자열을 쓰기보다는 str.format과 f-문자열을 통한 인터폴레이션을 사용하라.

# C스타일 형식 문자열

a = 0b10111011
b = 0xc5f
print('이진수: %d, 십육진수: %d' % (a, b))

'''
문제점
1. 오른 쪽 튜플의 값을 바꾸면 오류가 발생할 수 있음
2. 식을 읽기가 어렵다.
3. 같은 변수를 여러 번 사용한다면 같은 값을 입력해야 해서 실수가 생길 수 있다.
4. 딕셔너리를 사용하면 코드가 복잡해 보인다.
'''

# str.format과 f-string을 사용하여 간단하게 표현
help('FORMATTING') # 함수로 형식 참조
