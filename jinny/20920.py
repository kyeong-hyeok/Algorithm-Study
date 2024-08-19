# 7 4
# apple
# ant
# sand
# apple
# append
# sand
# sand


# 1.자주
# 2.길수록
# 3.알파벳
# 4. m길이 이상

import sys


n,m = map(int, input().split())
word = {}
for i in range(n):
    word_str = sys.stdin.readline().strip()
     
    if len(word_str) >= m :
        if word_str in word:
            word[word_str] +=1
        else :  
            word[word_str] =1
    else :
        continue;

#print(word)
sorted_word = sorted(word.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))
#print(sorted_word)

for key in sorted_word:
    print(key[0])


