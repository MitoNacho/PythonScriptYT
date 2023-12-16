import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, \
    QVBoxLayout, QWidget, QRadioButton, QFileDialog

from pytube import YouTube
from moviepy.editor import VideoFileClip
from PyQt6.QtGui import QIcon

current_directory = os.path.dirname(os.path.abspath(__file__))
download_directory = current_directory

def descargar_youtube():
    def descargar():
        url = entry_url.text()
        try:
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            download_file = video.download(output_path=download_directory, filename='video_descargado.mp4')
            print(f"Archivo descargado en: {download_file}")
            label_info.setText("¡Descarga del video en formato mp4 completada con éxito!")

        except Exception as e:
            label_info.setText(f"Hubo un error al descargar el video: {e}")
    def seleccionar_directorio():
        global download_directory
        download_directory = QFileDialog.getExistingDirectory(window, "Seleccionar carpeta de descarga")
    
    def convertir():
        nombre_video = 'video_descargado.mp4'
        print(f"Ruta del archivo: {os.path.join(download_directory, nombre_video)}")
        eleccion = var
        if eleccion == 1:
            audio_convertido = convertir_video_a_mp3(nombre_video)
            if audio_convertido:
                label_info.setText("¡Conversión a MP3 completada con éxito!")
            else:
                label_info.setText("Hubo un error al convertir a MP3.")
        elif eleccion == 2:
            video_convertido = convertir_video(nombre_video)
            if video_convertido:
                label_info.setText("¡Conversión a MP4 completada con éxito!")
            else:
                label_info.setText("Hubo un error al convertir a MP4.")
        else:
            label_info.setText("Eleccion no válida. Por favor, selecciona una opción válida")

    def convertir_video_a_mp3(video_file):
        try:
            video_path = os.path.join(download_directory, video_file)
            clip = VideoFileClip(video_path)
            audio_file = os.path.join(download_directory, 'audio_extraido.mp3')
            clip.audio.write_audiofile(audio_file, codec='mp3')
            return audio_file
        except Exception as e:
            print("Error al convertir a MP3:", e)
            return None

    def convertir_video(video_file):
        try:
            video_path = os.path.join(download_directory, video_file)
            clip = VideoFileClip(video_path)
            output_file = os.path.join(download_directory, 'video_convertido.mp4')
            clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
            return output_file
        except Exception as e:
            print("Error al convertir el video:", e)
            return None




    app = QApplication([])

    icon_path = os.path.abspath('icon.ico')  # Cambia 'icono.png' al nombre de tu archivo de ícono


    window = QMainWindow()
    window.setWindowTitle("DownTube")
    window.setWindowIcon(QIcon(icon_path))
    central_widget = QWidget()
    window.setCentralWidget(central_widget)
    layout = QVBoxLayout()
    window.resize(300, 250)
    label_url = QLabel("URL del video de YouTube:")
    layout.addWidget(label_url)

    entry_url = QLineEdit()
    layout.addWidget(entry_url)

    btn_descargar = QPushButton("Descargar")
    btn_descargar.clicked.connect(descargar)
    btn_descargar.setStyleSheet("background-color:  #a2d2ff; color: blue;")
    btn_descargar.setStyleSheet("""
        QPushButton {
            background-color: #a2d2ff;
            color: blue;
            border: none;
            padding: 8px;
        }
        QPushButton:hover {
            background-color: #75baff; /* Color cuando se pasa el cursor */
        }
    """)
    layout.addWidget(btn_descargar)

    btn_convertir_mp4 = QLabel("¿Deseas convertir el video a:")
    layout.addWidget(btn_convertir_mp4)

    radio_mp3 = QRadioButton("MP3")
    radio_mp3.clicked.connect(lambda: set_format(1))
    layout.addWidget(radio_mp3)


    btn_convertir = QPushButton("Convertir")
    btn_convertir.clicked.connect(convertir)
    btn_convertir.setStyleSheet("background-color: #a2d2ff; color: blue;")
    btn_convertir.setStyleSheet("""
        QPushButton {
            background-color: #a2d2ff;
            color: blue;
            border: none;
            padding: 8px;
        }
        QPushButton:hover {
            background-color: #75baff; /* Color cuando se pasa el cursor */
        }
    """)
    layout.addWidget(btn_convertir)

    btn_seleccionar_carpeta = QPushButton("Seleccionar ubicación")
    btn_seleccionar_carpeta.clicked.connect(seleccionar_directorio)
    btn_seleccionar_carpeta.setStyleSheet("background-color: #a2d2ff; color: blue;")
    btn_seleccionar_carpeta.setStyleSheet("""
        QPushButton {
            background-color: #a2d2ff;
            color: blue;
            border: none;
            padding: 8px;
        }
        QPushButton:hover {
            background-color: #75baff; /* Color cuando se pasa el cursor */
        }
    """)
    layout.addWidget(btn_seleccionar_carpeta)
    label_info = QLabel("")
    layout.addWidget(label_info)

    def set_format(value):
        global var
        var = value

    central_widget.setLayout(layout)
    window.show()

    app.exec()

descargar_youtube()
