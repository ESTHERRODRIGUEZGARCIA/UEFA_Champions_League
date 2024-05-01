import langchain

# Crear un objeto de conversación
conversation = langchain.Conversation()

# Establecer el contexto inicial (opcional)
conversation.context = "Hola, soy una inteligencia artificial."

while True:
    # Leer la entrada del usuario
    user_input = input(">>> ")

    # Procesar la entrada y generar una respuesta
    response = conversation.process_input(user_input)

    # Mostrar la respuesta
    print(response)

    if user_input.lower() == "hola":
        response = conversation.process_input("Hola! ¿Cómo estás?")
    elif user_input.lower() == "adiós":
        response = conversation.process_input("Adiós! Hasta luego.")
    else:
        response = conversation.process_input(user_input)