#6.1 (Вариант 1)
text = "Hello, World!"
print(text[0])
print(text[-1])
print(text[7:12])

#6.2
text = input("Введите строку: ")
if len(text) % 2 == 0:
    print(text.upper())
else:
    print(text.lower())

#6.3
text = input("Введите строку: ")
lower_chars = "aeiou"
upper_chars = "AEIOU"
lower_count = 0
upper_count = 0

for char in text:
    if char in lower_chars:
        lower_count += 1
    elif char in upper_chars:
        upper_count += 1

print(f"Строчных гласных: {lower_count}")
print(f"Заглавных гласных: {upper_count}")

#6.4
text = input("Введите строку: ")
result = ''
for i in range(len(text)):
    if i == 0 or text[i] != text[i-1]:
        result += text[i]
print(result)

#6.5
text1 = input("Введите первое слово: ")
text2 = input("Введите второе слово: ")

if len(text1) != len(text2):
    print(False)
else:
    is_anagram = True
    temp_text2 = text2
    for char in text1:
        found = False
        for i in range(len(temp_text2)):
            if temp_text2[i] == char:
                temp_text2 = temp_text2[:i] + temp_text2[i+1:]
                found = True
                break
        if not found:
            is_anagram = False
            break
    print(is_anagram)