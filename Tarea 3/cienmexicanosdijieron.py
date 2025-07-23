PREGUNTAS = [
    ("¿Colón descubrió América?", True),
    ("¿La independencia de México fue en el año 1810?", True),
    ("¿The Doors fue un grupo de rock estadounidense?", True),
]


def solicitar_respuesta(pregunta: str) -> bool:
    while True:
        entrada = input(f"{pregunta} (Si/No): ").strip().lower()
        if entrada in ('si', 'no'):
            return entrada == 'si'
        print("Respuesta inválida. Ingresa 'Si' o 'No'.")


def juego_preguntas() -> None:
    print("=== Juego de Preguntas Si/No ===")

    for texto, respuesta_correcta in PREGUNTAS:
        respuesta_usuario = solicitar_respuesta(texto)
        if respuesta_usuario != respuesta_correcta:
            print("\nRespuesta incorrecta. ¡Fin del juego!")
            return

    print("\n¡Felicidades! Has contestado correctamente las tres preguntas y ganas el juego!")

juego_preguntas()
