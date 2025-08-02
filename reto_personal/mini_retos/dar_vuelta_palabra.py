# Dada una palabra como 'hola' darle vuelta para que diga 'aloh'
palabra = 'hola'
palabra_nueva = ''
for i in palabra:
    palabra_nueva = i + palabra_nueva
print(palabra_nueva)

# Segunda forma
word = 'Python'
new_word = word[::-1]
print(new_word)