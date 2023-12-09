import tkinter as tk
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
current_directory = os.path.dirname(os.path.abspath(__file__))
download_directory = current_directory
# Función para descargar el video de YouTube
def descargar_youtube():
    def descargar():
        url = entry_url.get()
        try:
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            download_file = video.download(output_path=current_directory, filename='video_descargado.mp4')
            print(f"Archivo descargado en: {download_file}")
            label_info.config(text="¡Descarga del video en formato mp4 completada con éxito!")

        except Exception as e:
            label_info.config(text=f"Hubo un error al descargar el video: {e}")
        
    def convertir():
                    nombre_video = 'video_descargado.mp4'  # Reemplazar con el nombre del video descargado
                    print(f"Ruta del archivo: {os.path.join(current_directory, nombre_video)}")
                    eleccion = var.get()
                    if eleccion == 1:
                        # Convertir el video a formato MP3
                        audio_convertido = convertir_video_a_mp3(nombre_video)
                        if audio_convertido:
                            label_info.config(text="¡Conversión a MP3 completada con éxito!")
                        else:
                            label_info.config(text="Hubo un error al convertir a MP3.")
                    elif eleccion == 2:
                        # Convertir el video a formato MP4
                        video_convertido = convertir_video(nombre_video)
                        if video_convertido:
                            label_info.config(text="¡Conversión a MP4 completada con éxito!")
                        else:
                            label_info.config(text="Hubo un error al convertir a MP4.")
                    else:
                        label_info.config(text="Eleccion no válida. Por favor, selecciona 'MP3' o 'MP4'.")

                # Función para convertir el video a formato MP3
    def convertir_video_a_mp3(video_file):
                    try:
                        video_path = os.path.join(current_directory, video_file)
                        clip = VideoFileClip(video_path)
                        audio_file = os.path.join(current_directory, 'audio_extraido.mp3')
                        clip.audio.write_audiofile(audio_file, codec='mp3')
                        return audio_file
                    except Exception as e:
                        print("Error al convertir a MP3:", e)
                        return None

                # Función para convertir el video a formato MP4
    def convertir_video(video_file):
                    try:
                        video_path = os.path.join(current_directory, video_file)
                        clip = VideoFileClip(video_path)
                        output_file = os.path.join(current_directory, 'video_convertido.mp4')
                        clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
                        return output_file
                    except Exception as e:
                        print("Error al convertir el video:", e)
                        return None
        

            # Configuración de la ventana
    root = tk.Tk()
    root.title("Descargar y Convertir Video de YouTube")
    root.configure(bg="#f0f0f0")  # Cambiar el color de fondo
    label_url = tk.Label(root, text="URL del video de YouTube:", bg="#f0f0f0")  # Fondo del label
    label_url.pack()                    

    entry_url = tk.Entry(root)
    entry_url.pack(pady=5)

    btn_descargar = tk.Button(root, text="Descargar", command=descargar, bg="#0077b6", fg="white")
    btn_descargar.pack(pady=10)


    btn_convertir_mp4 = tk.Label(root, text="¿Deseas convertir el video a:")
    btn_convertir_mp4.pack(pady=10)

    var = tk.IntVar()

    radio_mp3 = tk.Radiobutton(root, text="MP3", variable=var, value=1)
    radio_mp3.pack()

    radio_mp4 = tk.Radiobutton(root, text="MP4", variable=var, value=2)
    radio_mp4.pack_forget()

    btn_convertir_mp4 = tk.Button(root, text="Convertir", command=convertir, bg="#0077b6", fg="white")
    btn_convertir_mp4.pack(pady=10)
    label_info = tk.Label(root, text="")
    label_info.pack()

    root.mainloop()
        # Iniciar la interfaz
descargar_youtube()