# Tradutor de Texto com IA - Estudo

## Sobre o Projeto

Este é um projeto de estudo e teste que visa explorar o uso do modelo GPT-4o da OpenAI para realizar traduções automáticas entre diferentes idiomas. A aplicação foi construída utilizando **FastAPI** para criar uma API rápida e eficiente, e a biblioteca **LangChain** para facilitar a integração com o modelo de linguagem da OpenAI.

### Objetivo

O principal objetivo deste projeto é aprender a trabalhar com modelos de linguagem como o GPT-4o, além de entender como construir APIs com **FastAPI** e integrar tudo de maneira simples e eficiente. A ideia é criar um sistema que traduza qualquer texto fornecido pelo usuário para o idioma desejado.

## Tecnologias Usadas

- **FastAPI**: Framework moderno e rápido para construção de APIs.
- **OpenAI GPT-4o**: Utilizado para realizar as traduções de texto de forma precisa.
- **LangChain**: Biblioteca que facilita a criação de fluxos com modelos de linguagem como o GPT.
- **Uvicorn**: Servidor ASGI para rodar a aplicação.

## Como Rodar o Projeto

### Passo 1: Clone o Repositório

Primeiro, faça o clone deste repositório para a sua máquina:

```bash
git clone https://github.com/RayssaGM21/langchain-translate.git
cd tradutor-ia
```

### Passo 2: Instale as Dependências

```bash
pip install -r requirements.txt
```

### Passo 3: Configuração do Arquivo.env
```.env
OPENAI_API_KEY = chave_api
```

### Passo 4: Rode a Aplicação
```bash
uvicorn main:app --reload
```

Agora, uma API estará disponível em http://localhost:8000.

## Como usar a API

A aplicação oferece uma API RESTful para traduzir textos. Você pode fazer uma requisição POSTpara o endpoint `/tradutor` com o seguinte formato:

### Exemplo de Requisição
```json
{
  "idioma": "ingles",
  "texto": "Estou aprendendo LangChain!"
}
```

## Teste Remoto

Além de rodar localmente, você pode integrar este serviço em outros sistemas, por exemplo, com a seguinte implementação remota:


``` python
from langserve import RemoteRunnable

chain_remota = RemoteRunnable("http://localhost:8000/tradutor")

texto = chain_remota.invoke({"idioma": "italiano", "texto": "Estou estudando programação hoje!"})

print(texto)
```

Também é possível realizar testes pela interface gráfica acessando a seguinte url: http://localhost:8000/tradutor/playground/

## Créditos

Este projeto foi inspirado e baseado no vídeo tutorial encontrado no YouTube. Agradecemos ao criador do conteúdo pela excelente explicação!

**Vídeo:** [Langchain - Crie sua Inteligência Artificial LLM](https://www.youtube.com/watch?v=7L0MnVu1KEo)
