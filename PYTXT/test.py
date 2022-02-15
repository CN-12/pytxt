# File = open("test.txt", "a")
# File.write(input())
# File.close()
# 이렇게 쓰기 귀찮으니깐 밑에 걸로
with open('test.txt', "w", encoding="utf8") as File: #w는 쓰기 r는 읽기 a는 append ㅇㅋ?
    a = input() #input 받아서 쓰기
    File.write(a) 
with open('test.txt', "r", encoding="utf8") as File:
    print(File) #상태 출력
    for i in File:
        print(i) #하나씩 출력