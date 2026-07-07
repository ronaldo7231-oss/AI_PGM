from datetime import datetime
import asyncio
import edge_tts

Voice = "ko-KR-SunHiNeural"

# 경기결과입력받는곳
place=input("경기가열린곳은? ")
time=input("경기가열린시간은? ")
opponent=input("상대팀은? ")
while True:
    goals = input("손흥민은 몇 골을 넣었나요? ")
    aids = input("도움은 몇 개인가요? ")
    score_me = input("손흥민팀이 넣은 골 수는? ")

    if int(goals) + int(aids) <= int(score_me):
        break

    print("\n잘못 입력했습니다.")
    print("골 + 도움의 합은 팀 득점보다 클 수 없습니다.")
    print("다시 입력해주세요.\n")

score_you=input("상대팀이넣은골수는? ")
# 기사작성하는곳
news = "[프리미어리그 속보 (" + datetime.now().strftime("%Y-%m-%d %H:%M") + ")]\n"
news=news+"손흥민선수는 "+place+"에서 "+time+"에 열린 경기에 출전하였습니다.\n"
news=news+"상대팀은 "+opponent+"입니다. "
if score_me>score_you:
    news=news+"손흥민 선수의팀이 "+score_me+"골을 넣어"+score_you+"골을 넣은 상대팀을 이겼습니다. \n"
elif score_me<score_you:
    news=news+"손흥민 선수의팀이 "+score_me+"골을 넣어"+score_you+"골을 넣은 상대팀에게 졌습니다. \n"
else:
    news=news+"두팀은 "+score_me+"대 "+score_you+"로 비겼습니다. \n"
if int(goals)>0 and int(aids)>0:
    news=news+"손흥민선수는 "+goals+"골에 도움"+aids+"개로 승리를 크게 이끌었습니다. \n"
elif int(goals)>0 and int(aids)==0:
    news=news+"손흥민선수는 "+goals+"골로 승리를 이끌었습니다. \n"
elif int(goals)==0 and int(aids)>0:
    news=news+"손흥민선수는 골은 없지만 도움 "+aids+"개로 승리하는데 공헌하였습니다. \n"
else:
    news=news+"아쉽게도 이번 경기에서 손홍민의 발끝은 침묵을 지켰습니다. \n"
print(news)
Text=news
async def main():
    communicate = edge_tts.Communicate(Text, Voice)
    await communicate.save("news.mp3")
    
asyncio.run(main())
import os

asyncio.run(main())

os.system("start news.mp3")