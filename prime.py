# 課題で提示されたタスクを実行するコードを以下に記述しなさい。
# タスクごとにセルを分けて記述してください。
#%%
# Task 1. 素数リストprime_numbersの作成と出力

# 素数リストの作成
prime_numbers = []
i = 2
while len(prime_numbers) < 100:
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        prime_numbers.append(i)
    i += 1
# %%
5+3
# %%
prime_numbers
# %%
# prime_numbersの要素を出力
for i in range(len(prime_numbers)):
    if i % 10 == 9:
        print(prime_numbers[i])
    else:
        print(prime_numbers[i],end=' ')

# %%
# enumerateを使う方法
# こちらのほうがPythonicで格好いいですね
for i,v in enumerate(prime_numbers):
    if i % 10 == 9:
        print(v)
    else:
        print(v,end=' ')

# %%
# Task 2. prime_numbersの要素を逆順に出力

# prime_numbersを逆順にしたリストを作成
rev = prime_numbers[::-1]
for i in range(len(rev)):
    if i % 10 == 9:
        print(rev[i])
    else:
        print(rev[i],end=' ')

# %%
# Task 3. prime_numbersの要素のうち偶数番目のものを出力

# 偶数番目の素数からなるリストを作成
even = prime_numbers[1::2]
for i in range(len(even)):
    if i % 10 == 9:
        print(even[i])
    else:
        print(even[i],end=' ')

# %%
# Task 4. prime_numbersの要素のうちスーパー素数を出力

j = 0
for i in range(len(prime_numbers)):
    if i+1 in prime_numbers:
        j += 1
        if j % 5 == 0:
            print(prime_numbers[i])
        else:
            print(prime_numbers[i],end=' ')

# %%
# 先にスーパー素数のリストを作るのでも良いと思います
# ここでは少し高度な内包表記を使ってみました
super_prime = [p for i,p in enumerate(prime_numbers) if i+1 in prime_numbers]
for i,p in enumerate(super_prime):
    if i % 5 == 4:
        print(p)
    else:
        print(p,end=' ')

# %%
# 学生さんが考えたエレガントな別回答です
# whileの条件式にprime_numbers[i]<100を持ってくるのがとっても賢いです

i = 0
while prime_numbers[i] < 100:
    if i % 5 == 4:
        print(prime_numbers[prime_numbers[i]-1])
    else:
        print(prime_numbers[prime_numbers[i]-1],end=' ')
    i += 1
# %%
