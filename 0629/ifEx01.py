#Ex01 성적평가 프로그램(점수를 입력하는 경우)
score = int(input("Enter your score : "))

if score >= 90:
     print("탁월한 성적입니다.")
elif score >= 80:
     print("우수한 성적입니다.")
elif score >= 70:
     print("보통입니다.")
elif score >= 60:
     print("미흡합니다.")
else:
     print("노력이 필요합니다.")

print("성적평가 프로그램을 사용해 주셔서 감사합니다.")

#Ex02 성적평가 프로그램(학점을 입력하는 경우)
grade = (input("Enter your grade : "))

if grade == "A":
     print("탁월한 성적입니다.")
elif grade == "B":
     print("우수한 성적입니다.")
elif grade == "C":
     print("보통입니다.")
elif grade == "D":
     print("미흡합니다.")
else:
     print("노력이 필요합니다.")

print("성적평가 프로그램을 사용해 주셔서 감사합니다.")
