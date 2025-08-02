from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

entrenamiento = ['hola', 'buenos días', 'adiós','hasta luego', 'como estás', 'qué haces', 'gracias', 'quién eres']
respuestas = ['¡Hola!', '¡Buenos días!', '¡Adiós!', '¡Nos vemos!', '¡Estoy muy bien!', '¡Estoy programando!', '¡De nada!', '¡Soy un chat bot!']

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(entrenamiento)

modelo = MultinomialNB()
modelo.fit(x, respuestas)

while True:
    entrada = input('Tú: ')
    if entrada.lower() in ['salir', 'exit']:
        print('Bot: ¡Hasta pronto!')
        break
    entrada_vector = vectorizer.transform([entrada])
    respuesta = modelo.predict(entrada_vector)
    print('Bot:', respuesta[0])
