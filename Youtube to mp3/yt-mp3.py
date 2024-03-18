from pytube import YouTube
from moviepy.editor import *

def download_video_as_mp3(youtube_url, save_path='.', filename='downloaded_video'):
    
    try:
        
        yt = YouTube(youtube_url)
        video = yt.streams.filter(only_audio=True).first()
        download_path = video.download(output_path=save_path, filename=filename + '.mp4')

        
        clip = AudioFileClip(download_path)
        clip.write_audiofile(download_path.replace('.mp4', '.mp3'))

        
        os.remove(download_path)
        
        print(f"Le fichier MP3 a été sauvegardé : {download_path.replace('.mp4', '.mp3')}")

    except Exception as e:
        print("Une erreur est survenue :", e)

youtube_url = 'https://www.youtube.com/watch?v=example'
download_video_as_mp3(youtube_url)
