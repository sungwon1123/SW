# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}  # type이 set {}
print(menu, type(menu))

menu = list(menu)  # type을 list로 바꿈 []
print(menu, type(menu))

menu = tuple(menu)  # type을 tuple로 바꿈 tuple은 ()
print(menu, type(menu))

menu = set(menu)  # 다시 set으로
print(menu, type(menu))
