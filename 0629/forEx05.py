#Ex03. 1부터 100까지의 수 중에 6의 배수들의 합을 출력하는 프로그램
hap = 0
for i in range(1,101):
    if i %6==0:
        hap +=i
print(hap)