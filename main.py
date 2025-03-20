from pathlib import Path
import queue
import time

import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer

import pydub
import openai
from moviepy.video.io.VideoFileClip import VideoFileClip
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

PASTA_TEMP = Path(__file__).parent / 'temp'
PASTA_TEMP.mkdir(exist_ok=True)
ARQUIVO_AUDIO_TEMP = PASTA_TEMP / 'audio.mp3'
ARQUIVO_VIDEO_TEMP = PASTA_TEMP / 'video.mp4'
ARQUIVO_MIC_TEMP = PASTA_TEMP / 'mic.mp3'

client = openai.OpenAI()

def transcreve_audio(caminho_audio, prompt):
    with open(caminho_audio, 'rb') as arquivo_audio:
        transcricao = client.audio.transcriptions.create(
            model='whisper-1',
            language='pt',
            response_format='text',
            file=arquivo_audio,
            prompt=prompt
        )
    return transcricao



if not 'transcricao_mic' in st.session_state:
    st.session_state['transcricao_mic'] = ''

# Transcreve Audio Microfone ===================================================
def adiciona_chunks_de_audio(frames_de_audio, chunk_audio):
    for frame in frames_de_audio:
        sound = pydub.AudioSegment(
            data = frame.to_ndarray().tobytes(),
            sample_width = frame.format.bytes,
            frame_rate = frame.sample_rate,
            channels = len(frame.layout.channels)
        )
        chunk_audio += sound
    return chunk_audio

def transcreve_tab_mic():
    prompt_input = st.text_input('(opcional) Digite o seu prompt', key='input_mic')
    webrtc_ctx = webrtc_streamer(
        key = 'recebe_audio',
        mode=WebRtcMode.SENDONLY,
        audio_receiver_size=1024,
        media_stream_constraints={'video':False, 'audio':True}
    )
    
    if not webrtc_ctx.state.playing:
        st.write(st.session_state['transcricao_mic'])
        return

    container = st.empty()
    container.markdown('Comece a falar...')
    chunk_audio = pydub.AudioSegment.empty()
    tempo_ultima_transcricao = time.time()
    st.session_state['transcricao_mic'] = ''
    while True:
        if webrtc_ctx.audio_receiver:
            try:
                frames_de_audio = webrtc_ctx.audio_receiver.get_frames(timeout=1)
            except queue.Empty:
                time.sleep(0.1)
                continue

            chunk_audio = adiciona_chunks_de_audio(frames_de_audio, chunk_audio)

            agora = time.time()
            if len(chunk_audio) > 0 and agora - tempo_ultima_transcricao > 7:
                tempo_ultima_transcricao = agora
                chunk_audio.export(ARQUIVO_MIC_TEMP)
                transcricao = transcreve_audio(ARQUIVO_MIC_TEMP, prompt_input)
                st.session_state['transcricao_mic'] += transcricao
                container.write(st.session_state['transcricao_mic'])
                chunk_audio = pydub.AudioSegment.empty()
                

        else:
            break

# Transcreve Video ============================================================
def salva_audio_do_video(video_bytes):
    with open(ARQUIVO_VIDEO_TEMP, mode='wb') as video_f:
        video_f.write(video_bytes.read())
    moviepy_video = VideoFileClip(str(ARQUIVO_VIDEO_TEMP))
    moviepy_video.audio.write_audiofile(str(ARQUIVO_AUDIO_TEMP))

def transcreve_tab_video():
    prompt_input = st.text_input('(opcional) Digite o seu prompt', key='input_video')
    arquivo_video = st.file_uploader('Adicione um arquivo de vídeo .mp4', type=['mp4'])

    if not arquivo_video is None:
        salva_audio_do_video(arquivo_video)
        transcricao = transcreve_audio(ARQUIVO_AUDIO_TEMP, prompt_input)
        st.write(transcricao)

# Transcreve Audio ============================================================
def transcreve_tab_audio():
    prompt_input = st.text_input('(opcional) Digite o seu prompt', key='input_audio')
    arquivo_audio = st.file_uploader('Adicione um arquivo de áudio .mp3', type=['mp3'])
    if not arquivo_audio is None:
        transcricao = client.audio.transcriptions.create(
            model='whisper-1',
            language='pt',
            response_format='text',
            file=arquivo_audio,
            prompt=prompt_input
        )
        st.write(transcricao)

# Main ========================================================================
def main():
    st.header('Audio Transcriptor AI🎙️', divider=True)
    st.markdown('#### Transcreva áudio do microfone, de vídeos e de arquivos de áudio')
    tab_mic, tab_video, tab_audio = st.tabs(['Microfone', 'Vídeo', 'Áudio'])
    with tab_mic:
        transcreve_tab_mic()
    with tab_video:
        transcreve_tab_video()
    with tab_audio:
        transcreve_tab_audio()

if __name__ == '__main__':
    main()
