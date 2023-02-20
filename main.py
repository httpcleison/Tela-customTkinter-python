import customtkinter #instalar lib: pip install customtkinter

#Janela
app = customtkinter.CTk()
app.geometry("400x300")
app.title("CTk projeto de exemplo")

#Verificar
def Verificar_Login():
    if inpEmail.get() != "" and inpSenha.get() != "": #se as caixas de textos estiverem completas:
        textInfo.configure(text="")
        print("ok")
    elif inpEmail.get() == "" or inpSenha.get() ==  "": #se for alguma caixa de texto estiver vazio:
        textInfo.configure(text="Oops! algo errado, tente novamente.")


#Interface
text1 = customtkinter.CTkLabel(app, text="Faça login para continuar!")
text1.pack(padx=10, pady=10)

#--caixa de texto email
inpEmail = customtkinter.CTkEntry(app, placeholder_text="email")
inpEmail.pack(padx=10, pady=10)

#--caixa de texto senha
inpSenha = customtkinter.CTkEntry(app, placeholder_text="senha", show="*")
inpSenha.pack(padx=10, pady=10)

#--botão de login
button1 = customtkinter.CTkButton(app, text="Login", command=Verificar_Login)
button1.pack(padx=10, pady=10)

#--texto de informação
textInfo = customtkinter.CTkLabel(app, text="")
textInfo.pack(padx=10, pady=10)

text2 = customtkinter.CTkLabel(app, text="Cleison-desenvolvedor", text_color="#47575c")
text2.pack(padx=10, pady=10)

#Tema escuro
customtkinter.set_appearance_mode("Dark")

#Comandos de iniciar
app.mainloop()