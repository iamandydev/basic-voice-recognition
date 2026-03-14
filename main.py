import speech_recognition as sr
import subprocess
import pyautogui

recognizer = sr.Recognizer()
proceso = None

def ejecutar_comando(comando):
    global proceso
    if "abrir notepad" in comando:
        if proceso is None:
            proceso = subprocess.Popen(["notepad.exe"])
            print("Notepad abierto.")
        else:
            print("Ya hay un Notepad abierto.")
    elif "cerrar notepad" in comando:
        if proceso is not None:
            proceso.terminate()
            proceso = None
            print("Notepad cerrado.")
        else:
            print("No hay un proceso de Notepad abierto.")
    elif "abrir navegador" in comando:
        if proceso is None:
            proceso = subprocess.Popen(["firefox.exe"])
            print("Navegador Firefox abierto.")
        else:
            print("Ya hay un programa abierto.")


def escuchar_comandos():
    with sr.Microphone() as source:
        print("¿En qué te puedo ayudar?")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="es-ES")
        print(f"Comando reconocido: {comando}")
        ejecutar_comando(comando.lower())
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except Exception as e:
        print(f"No se pudo realizar la acción: {e}")

if __name__ == "__main__":
    while True:
        escuchar_comandos()