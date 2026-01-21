caminho = "C:/Users/rafael.silva/Desktop/Alura/Especialista_IA/docs/resumos_emails.txt"
novo_caminho = "C:/Users/rafael.silva/Desktop/Alura/Especialista_IA/docs/novo_resumos_emails.txt"

leitura = []
with open (caminho, "r", encoding="utf-8") as arq:
        leitura = [linha.strip() for linha in arq]


with open(novo_caminho, "w", encoding="utf-8") as newarq:
        resultado = "\n".join(leitura)
        newarq.write(resultado)