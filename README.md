# Audio Transcriptor AI 🎙️

Aplicação web desenvolvida com Streamlit para transcrever áudio, microfone e vídeos usando o modelo **Whisper de código aberto (Open Source)** rodando 100% localmente no seu computador. Sem limites de tamanho de upload, sem cobranças de API na nuvem!

## 📋 Funcionalidades

- **Processamento 100% Local**: O app usa o modelo fornecido gratuitamente pela OpenAI e processa os dados no seu próprio hardware. Nada é enviado para a nuvem.
- **Suporte a Arquivos Gigantes**: Limite de upload aumentado para 2 GB, usando otimização de RAM por *chunks* para não travar o computador.
- **Transcrição de Microfone**: Grave e transcreva áudio em tempo real diretamente do seu microfone.
- **Transcrição de Vídeo**: Faça upload de arquivos `.mp4` (mesmo aqueles pesados com mais de 200MB) e transcreva o áudio.
- **Transcrição de Áudio**: Faça upload de arquivos `.mp3` para transcrição.

## 🚀 Tecnologias

- **Streamlit**: Interface web.
- **Whisper (openai-whisper)**: Inteligência artificial que roda nativa na sua máquina.
- **MoviePy & PyDub**: Manipulação local e salvamento do áudio/vídeo em chunks pesados.

---

## 💻 Requisitos do PC (Hardware)

Como a aplicação roda a transcrição de IA na sua própria máquina local, seu computador precisa ter o mínimo de força para fazer o processamento:

- **Sistema Operacional**: Windows, Linux, ou macOS.
- **Memória RAM**: Recomendado **8 GB no mínimo**, sendo **16 GB ou mais o ideal**.
- **Processador (CPU)**: Processadores modernos de no mínimo 4 Núcleos.
- **Placa de Vídeo (GPU)**: O PC vai conseguir usar sua CPU perfeitamente, mas se você possuir uma Placa de Vídeo Dedicada da NVIDIA, o tempo de carregamento e as transcrições serão aceleradas em até 10x mais.

## 📝 Requisitos de Sistema (Software)

- **Python**: Versão 3.8 a 3.12 Recomendado.
- **FFmpeg**: O arquivo executável precisará estar no sistema (atualmente acompanhado através do `ffmpeg.exe` no projeto) ou instalado nativamente.
- **Nenhuma Chave API**: Você não precisa mais pagar ou utilizar keys da OpenAI!

---

## 📦 Instalação e Testes

1. Clone o repositório ou faça o download da pasta:
```bash
git clone https://github.com/fbressa/audioTranscriptor.git
cd audioTranscriptor
```

2. Instale as bibliotecas necessárias para uso do Whisper Local:
```bash
pip install -r requirements.txt
```
> *Nota: O processo pode demorar alguns minutos dependendo de quão rápido for sua internet para baixar a biblioteca do PyTorch, utilizada pelo modelo de IA.*

3. Execute a aplicação do Streamlit:
```bash
streamlit run main.py
```

## 🎯 Como Usar 

1. Acesse o IP que aparecerá no seu terminal `http://localhost:8501`.
2. O aplicativo deve baixar o modelo `base` do Whisper automaticamente a primeira vez que você rodar a transcrição.
3. **Na aba de Microfone**: Clique no botão para começar a capturar a sua fala em tempo real.
4. **Na aba de Vídeo / Áudio**: Arraste e solte o arquivo desejado na área indicada. Não se preocupe mais com arquivos passando o limite de 200MB! O app salvará tudo na pasta `temp/` rodando pouco a pouco.

## 🔧 Pasta Temp()
O sistema gerencia arquivos dividindo e salvando blocos da leitura diretamente na sua pasta `temp/` otimizando sua memória de página RAM.

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT. Autor Original: **fbressa**.