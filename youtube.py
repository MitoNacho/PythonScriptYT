from pytube import YouTube
from moviepy.editor import VideoFileClip
# Función para descargar el video de YouTube
def descargar_youtube(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(filename='video_descargado')

        return 'video_descargado.mp4'
    except Exception as e:
        print("Error al descargar el video:", e)
        return None

# URL del video de YouTube
url_youtube = input("Por favor, ingresa la URL del video de YouTube: ")  # SUSTITUIR POR LA URL DE LA DESCARGA SIN CARACTERES ESPECIALES (DA ERROR)

# Descargar el video
video_descargado = descargar_youtube(url_youtube)

if video_descargado:
    print("¡Descarga del video completada con éxito!")
else:
    print("Hubo un error al descargar el video de YouTube.")

def convertir_video_a_mp3(video_file):
    try:
        clip = VideoFileClip(video_file)
        audio_file = 'audio_extraido.mp3'
        clip.audio.write_audiofile(audio_file, codec='mp3')

        return audio_file
    except Exception as e:
        print("Error al convertir a MP3:", e)
        return None


def convertir_video(video_file, output_format='mp4'):
    try:
        clip = VideoFileClip(video_file)
        output_file = 'video_convertido.' + output_format
        clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
        return output_file
    except Exception as e:
        print("Error al convertir el video:", e)
        return None


# Nombre del video descargado
nombre_video = 'video_descargado'  # !!!! Reemplaza con el nombre del video descargado YA DEBERIA ESTAR CON ESE NOMBRE !!!!

# Simulación de elección del usuario después de la descarga
eleccion_usuario = input("¿Deseas convertir el video a MP3 o MP4? (Ingresa 'mp3' o 'mp4'): ")

# Proceso basado en la elección del usuario
if eleccion_usuario.lower() == 'mp3':
    # Convertir el video a formato MP3
    audio_convertido = convertir_video_a_mp3(nombre_video)

    if audio_convertido:
        print("¡Conversión a MP3 completada con éxito!")
    else:
        print("Hubo un error al convertir a MP3.")
elif eleccion_usuario.lower() == 'mp4':
    # Convertir el video a formato MP4
    video_convertido = convertir_video(nombre_video)

    if video_convertido:
        print("¡Conversión a MP4 completada con éxito!")
    else:
        print("Hubo un error al convertir a MP4.")
else:
    print("Eleccion no válida. Por favor, ingresa 'mp3' o 'mp4'.")





