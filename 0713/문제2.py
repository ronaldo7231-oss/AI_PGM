# NumPy와 Pandas 라이브러리 불러오기
import numpy as np
import pandas as pd

# NumPy 배열 생성
data = np.array([
    [85, 90, 88],
    [70, 80, 75],
    [95, 98, 100],
    [60, 72, 68]
])

# 학생 이름 지정
students = ["짱구", "철수", "훈이", "맹구"]

# DataFrame 생성 (학생 이름을 인덱스로 지정)
df = pd.DataFrame(
    data,
    index=students,
    columns=["국어", "영어", "수학"]
)

# 학생별 평균 계산 (소수점 첫째 자리까지 반올림)
df["평균"] = df.mean(axis=1).round(1)

# 평균이 가장 높은 학생 찾기
best_student = df["평균"].idxmax()

# 결과 출력
print("===== 전체 학생 성적 =====\n")
print(df)

print("===== 평균이 가장 높은 학생 =====\n")
print(df.loc[[best_student]])

