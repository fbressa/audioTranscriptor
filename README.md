# Audio Transcriptor AI 🎙️

Aplicação web desenvolvida com Streamlit para transcrever áudio em tempo real usando a API Whisper da OpenAI.

## 📋 Funcionalidades

- **Transcrição de Microfone**: Grave e transcreva áudio em tempo real diretamente do seu microfone
- **Transcrição de Vídeo**: Faça upload de arquivos .mp4 e extraia/transcreva o áudio
- **Transcrição de Áudio**: Faça upload de arquivos .mp3 para transcrição
- **Suporte a Prompts**: Adicione prompts opcionais para melhorar a qualidade da transcrição

## 🚀 Tecnologias

- **Streamlit**: Interface web interativa
- **OpenAI Whisper**: Modelo de transcrição de áudio
- **streamlit-webrtc**: Captura de áudio em tempo real
- **MoviePy**: Processamento de vídeo
- **PyDub**: Manipulação de áudio

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/fbressa/audioTranscriptor.git
cd audioTranscriptor
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure a chave da API OpenAI:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione sua chave da API:
```
OPENAI_API_KEY=sua_chave_api_aqui
```

## 🎯 Como Usar

1. Execute a aplicação:
```bash
streamlit run main.py
```

2. Acesse a aplicação no navegador (geralmente em `http://localhost:8501`)

3. Escolha uma das abas:
   - **Microfone**: Clique para começar a gravar e falar
   - **Vídeo**: Faça upload de um arquivo .mp4
   - **Áudio**: Faça upload de um arquivo .mp3

4. (Opcional) Adicione um prompt para melhorar a transcrição

## 📝 Requisitos

- Python 3.7+
- Chave de API da OpenAI
- Microfone (para a funcionalidade de gravação em tempo real)

## 🔧 Configuração

O projeto cria automaticamente uma pasta `temp/` para armazenar arquivos temporários durante o processamento.

## ⚙️ Variáveis de Ambiente

Crie um arquivo `.env` com as seguintes variáveis:

```env
OPENAI_API_KEY=sua_chave_api_aqui
```

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 👤 Autor

**fbressa**

## 🤝 Contribuições

Contribuições, issues e feature requests são bem-vindos!