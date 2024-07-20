import os
from tkinter import Tk, filedialog
import PyPDF2

def select_folder():
    root = Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter
    folder_selected = filedialog.askdirectory(title="Selecione a pasta com os arquivos PDF")
    root.destroy()
    return folder_selected

def select_save_location():
    root = Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Salvar arquivo combinado como")
    root.destroy()
    return file_path

def merge_pdfs(input_folder, output_path):
    pdf_merger = PyPDF2.PdfMerger()
    
    for item in os.listdir(input_folder):
        if item.endswith('.pdf'):
            file_path = os.path.join(input_folder, item)
            pdf_merger.append(file_path)

    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)

if __name__ == "__main__":
    # Certifique-se de instalar as dependências necessárias
    try:
        import pycryptodome
    except ImportError:
        print("PyCryptodome não está instalado. Instalando agora...")
        os.system('pip install pycryptodome')
    
    input_folder = select_folder()
    if not input_folder:
        print("Nenhuma pasta selecionada. Saindo...")
        exit()

    output_path = select_save_location()
    if not output_path:
        print("Nenhum local de salvamento selecionado. Saindo...")
        exit()

    merge_pdfs(input_folder, output_path)
    print(f"Arquivos PDF mesclados e salvos em: {output_path}")