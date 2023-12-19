import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog

from app import processar_transacoes


def processar_transacoes_gui():
    def abrir_arquivo_entrada():
        arquivo_entrada = filedialog.askopenfilename(title='Selecione o arquivo de entrada',
                                                     filetypes=[('CSV Files', '*.csv')])
        entry_arquivo_entrada.delete(0, tk.END)
        entry_arquivo_entrada.insert(0, arquivo_entrada)

    def abrir_arquivo_saida():
        arquivo_saida = filedialog.asksaveasfilename(title='Selecione o arquivo de saída', defaultextension=".csv",
                                                     filetypes=[('CSV Files', '*.csv')])
        entry_arquivo_saida.delete(0, tk.END)
        entry_arquivo_saida.insert(0, arquivo_saida)

    def processar():
        arquivo_entrada = entry_arquivo_entrada.get()
        arquivo_saida = entry_arquivo_saida.get()
        valor_minimo = entry_valor_minimo.get()

        try:
            valor_minimo = float(valor_minimo)
        except ValueError:
            messagebox.showerror('Erro', 'Valor mínimo inválido. Certifique-se de fornecer um número válido.')
            return

        sucesso, mensagem_erro = processar_transacoes(arquivo_entrada, arquivo_saida, valor_minimo)

        if sucesso:
            messagebox.showinfo('Concluído', f'Transações acima de ${valor_minimo} foram salvas em {arquivo_saida}.')
        else:
            messagebox.showerror('Erro', mensagem_erro)

    root = tk.Tk()
    root.title('Processamento de Transações')

    style = ttk.Style()
    style.theme_use('clam')  # Tema "clam" para garantir compatibilidade

    # Configurações de estilo personalizadas
    style.configure('TFrame', background='#b3fb4f')  # Fundo verde
    style.configure('TLabel', foreground='#000000', background='#b3fb4f')  # Texto preto, fundo verde
    style.configure('TButton', background='#000000', foreground='#ffffff', highlightbackground='#000000',
                    highlightcolor='#000000')  # Botões em preto

    frame = ttk.Frame(root, padding='20')
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(frame, text='Processar Transações', font=('Helvetica', 16, 'bold'), anchor='center', background='#b3fb4f').grid(row=0,
                                                                                                                column=0,
                                                                                                                columnspan=3,
                                                                                                                pady=(
                                                                                                                0, 10))

    ttk.Label(frame, text='Arquivo de Entrada:').grid(row=1, column=0, sticky=tk.W, pady=(5, 5))
    entry_arquivo_entrada = ttk.Entry(frame, width=40)
    entry_arquivo_entrada.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=(5, 5))

    btn_arquivo_entrada = ttk.Button(frame, text='Abrir', command=abrir_arquivo_entrada)
    btn_arquivo_entrada.grid(row=1, column=2, sticky=tk.W, pady=(5, 5))

    ttk.Label(frame, text='Arquivo de Saída:').grid(row=2, column=0, sticky=tk.W, pady=(5, 5))
    entry_arquivo_saida = ttk.Entry(frame, width=40)
    entry_arquivo_saida.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=(5, 5))

    btn_arquivo_saida = ttk.Button(frame, text='Salvar Como', command=abrir_arquivo_saida)
    btn_arquivo_saida.grid(row=2, column=2, sticky=tk.W, pady=(5, 5))

    ttk.Label(frame, text='Valor Mínimo:').grid(row=3, column=0, sticky=tk.W, pady=(5, 5))
    entry_valor_minimo = ttk.Entry(frame, width=10)
    entry_valor_minimo.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=(5, 5))

    btn_processar = ttk.Button(frame, text='Processar', command=processar)
    btn_processar.grid(row=4, column=0, columnspan=3, pady=(10, 0))

    root.mainloop()


processar_transacoes_gui()
