#r=[]
#def say(name):
 #   print(f"안녕 {name}")
 ##   return r

#r=say("현호")


#def bigger(a, b):
#    if a<b:
 #       return b
 #   else:
 #       return a
    
#print(bigger(3,8))
##print(bigger(10,2))

#def average(scores):
    
#print(average([80, 90, 100]))
#print(average([117, 80, 203]))

#score={"지현호":117, "민수": 80}
#score["영희"] = 203
#score["민수"] = 95
#print(score)
#print(len(score))
#print("민수" in score)

score = {"지현호":117, "민수":95, "영희":203}

for name in score:
    print(name, score[name])

for name, point in score.items():
    print(f"{name}: {point}")

score = {"지현호": 117, "민수": 95}
print(score.items())

words = "apple banana apple".split()
print(words)
count={}
for w in words:
    count[w]=count.get(w,0)+1 #+1이 있어야 빈 장부 카운트에 하나씩 채워지면서 숫자 세짐
    #count[w]에 값이 생기면 자동으로 짝이 지어짐
print(count)

#연습 문제
text = input()
list(text)
ct={}
for w in text:
    ct[w]=ct.get(w,0)+1
print(ct)


