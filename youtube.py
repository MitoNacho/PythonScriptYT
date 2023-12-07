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
url_youtube = 'https://www.youtube.com/watch?v=JFoQBSMpPEw'  # SUSTITUIR POR LA URL DE LA DESCARGA SIN CARACTERES ESPECIALES (DA ERROR)

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

# Nombre del video descargado
nombre_video = 'video_descargado'  # !!!! Reemplaza con el nombre del video descargado YA DEBERIA ESTAR CON ESE NOMBRE !!!!

# Convertir el video a formato MP3
audio_convertido = convertir_video_a_mp3(nombre_video)

if audio_convertido:
    print("¡Conversión a MP3 completada con éxito!")
else:
    print("Hubo un error al convertir a MP3.")






# Si quieres descargar el video en formato mp4 sustituye desde la linea 26 hasta el final

'''

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
nombre_video = 'video_descargado.mp4'  # Reemplaza con el nombre del video descargado

# Convertir el video a otro formato (ejemplo: MP4)
video_convertido = convertir_video(nombre_video)

if video_convertido:
    print("¡Conversión del video completada con éxito!")
else:
    print("Hubo un error al convertir el video.") 
    
    
    '''