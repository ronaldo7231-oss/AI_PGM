scores = [78, 85, 92, 68, 95, 88, 74] # 리스트 설정
#1.1 평균점수를 계산하시오
average = sum(scores) / len(scores) #average라는 변수 설정 및 scores 내부의 데이터의 합을 scores 데이터의 갯수 (len()은 리스트의 길이를 나타내고, 이것은 리스트 내부 데이터의 개수와 같다)로 나눔
print("평균 점수 : ",average)

#1.2 최고점과 최저점을 출력하시오
highest = max(scores)# highest, lowest라는 변수 설정 및 max,min함수 사용
lowest = min(scores)
print("최고점 :", highest)
print("최저점 :", lowest)

#1.3 80점 이상만 새로운 리스트 생성
eighty_scores=[]#새로운 list 설정
for score in scores: #list내부의 데이터를 score라고 정의
    if score >=80:#그 값이 80이상이라면
        eighty_scores.append(score)#새로운 list에 score값을 추가하라

print("80점 이상 : ", eighty_scores)

#1.4 평균 이상인 학생 수 출력
count = 0#새로운 변수 count 생성

for score in scores:
    if score >= average:#score 값이 1.1에서 정의한 평균값보다 크다면
        count +=1#count변수의 갯수를 1 증가시킨다

print("평균 이상 학생 수 : ",count)