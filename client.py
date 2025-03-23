from langserve import RemoteRunnable

chain_remota = RemoteRunnable("http://localhost:8000/tradutor")
texto = chain_remota.invoke({"idioma": "italiano", "texto": "Estou estudando programação hoje!"})
print(texto)