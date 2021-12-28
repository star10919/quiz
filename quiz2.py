lines: list = []
f = open('C://Users/ypolaris/Desktop/quiz/quiz/data/quiz2.txt', mode='r')
print(f.read())
# file = f.readlines
# print(type(file))

list_ = []
cal = 1
for i in f.readlines():
      if i % 3 == 0:
            cal = i[0] * i
            
      elif i % 10 == 0:
            cal = i[0] - i
            
      # elif :
            
      else:
            cal = i[0] + i
      list_.append(cal)
   
      
print(list_)
f.close()

# TODO: 
# 위 코드는 'data/quiz2.txt'의 텍스트를 줄 단위로 읽어들이는 코드입니다.
# 아래 조건에 맞추어 정답을 계산하세요.

# 조건 1. 
#  두번째 라인에서 마지막 라인까지의 숫자를 읽어들여
# 조건 2. 
#  직전 라인에서 계산된 최종 값에(첫번째 라인은 계산하지 않음) 
#   - 3의 배수면 곱하기
#   - 10의 배수면 빼기
#   - 소수면 나누기
#   - 그 외의 값은 더하기
#  를 한 결과 값(정답)을 'data/quiz2.txt'에 저장해 주세요.
#  조건 3, 
#   단, 정답은 결과 파일의 첫번째 줄에 위치해야 합니다.

# 제약 조건 
#   모듈 또는 라이브러리를 추가로 로드하지 않습니다. 
#   파이썬 코드 파일을 추가로 생성하지 않습니다. 
#   상단 코드는 하단의 코드로 결과를 확인할 수 있는 한 마음껏 수정하셔도 됩니다.

# {코드 작성 시작} 

        
      



# {코드 작성 완료}

f = open('C://Users/ypolaris/Desktop/quiz/quiz/data/quiz2.txt', mode='r')
print(f.read())
f.close()