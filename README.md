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

curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt":"¿por que el cielo es azul?",
  "stream": false
}'

git add . (guarda cualquier cambio que se realize)
git commit -m "UPDATED README" (guarda cambios con un nombre dentro de comillas)
git push -u origin main (sube el codigo de nuestra maquina a github origin(maquina, main(nube)))

https://www.w3schools.com/python/module_requests.asp