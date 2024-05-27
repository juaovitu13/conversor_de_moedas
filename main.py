import customtkinter

# criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x500")

# criar os botões, textos e outros elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("",20))

# colocar todos os elementos na tela
titulo.pack(padx=10, pady=10)

# rodar a janela
janela.mainloop()