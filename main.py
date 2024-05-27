import customtkinter

# criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x500")

# criar os botões, textos e outros elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("",20))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino")

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=["USD", "BRL", "EUR", "BTC"])
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["USD", "BRL", "EUR", "BTC"])

def converter_moeda():
    print("Converter moeda")

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)


# colocar todos os elementos na tela
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10)
botao_converter.pack(padx=10, pady=10)

# rodar a janela
janela.mainloop()