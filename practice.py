python = "Python is Amazing"
print(python.lower()) # .lower() 함수는 모든 문자열을 소문자로 바꿔줌.
print(python.upper()) # .upper() 함수는 모든 문자열을 대문자로 바꿔줌.
print(python[0].isupper()) # pytho의 0 = P가 대문자인지 소문자인지 알려줌.
print(len(python)) # len() 함수는 문자열이 몇개인지 세준다. (공백 포함 X)
print(python.replace("Python", "Java")) # .replace() 함수는 ("~","!") ~의 문자를 찾아 !의 문자로 바꿔줌.

index = python.index("n") # 문자열중에 n글자가 몇번째에 있는지 알려줌.
print(index)
index = python.index("n", index + 1) # + 1을 하면 5번째에 있는 n이 아닌 그 다음 n을 찾게된다.
print(index)

print(python.find("n")) # .find() 함수는 몇번째에 있는지 알려준다 하지만 원하는 값이 없을 땐 -1 이 나온다.
print(python.find("Java"))
# print(python.index("Java")) / # .index() 는 find와 달리 오류 발생.

print(python.count("n")) # .count()는 문자열 중에 몇개가 있는지 찾아줌.
