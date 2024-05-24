# fiestallm

# Instalación de Ollama y versiones de Llama

## 1.- Instalación de Ollama
'''shell
curl -fsSL https://ollama.com/install.sh | sh
'''

## 2.- Ejecutar el servidor
'''shell
ollama serve
'''

## 3.- Descargar un programa
'''shell
ollama pull tinyllama 
ollama pull llama3
'''

## 4.- Ejecutar el programa
'''shell
ollama run tinyllama (escribir mensaje sin ejecutar el modo chat)
ollama run llama3
ctrl+D (detiene el proceso del modo chat)
'''
