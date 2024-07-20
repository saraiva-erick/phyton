import os
from tkinter import Tk, filedialog
import PyPDF2
import fitz  # PyMuPDF
from PIL import Image
import io

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

    temp_path = output_path.replace('.pdf', '_temp.pdf')
    with open(temp_path, 'wb') as output_file:
        pdf_merger.write(output_file)

    return temp_path

def compress_pdf(input_path, output_path):
    # Abrir o documento PDF
    document = fitz.open(input_path)
    
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        
        images = page.get_images(full=True)
        for img in images:
            xref = img[0]
            base_image = document.extract_image(xref)
            image_bytes = base_image["image"]
            
            # Usar PIL para reduzir a qualidade da imagem, converter para preto e branco e reduzir a resolução
            image = Image.open(io.BytesIO(image_bytes)).convert("L")
            
            # Reduzir a resolução da imagem
            new_width = int(image.width * 0.5)
            new_height = int(image.height * 0.5)
            image = image.resize((new_width, new_height), Image.LANCZOS)
            
            with io.BytesIO() as image_buffer:
                image.save(image_buffer, format="JPEG", quality=30)
                new_image_bytes = image_buffer.getvalue()
            
            # Substituir a imagem no PDF
            rect = fitz.Rect(0, 0, new_width, new_height)
            page.insert_image(rect, stream=new_image_bytes)
    
    # Salvar o documento otimizado
    document.save(output_path)
    document.close()
    
if __name__ == "__main__":
    input_folder = select_folder()
    if not input_folder:
        print("Nenhuma pasta selecionada. Saindo...")
        exit()

    output_path = select_save_location()
    if not output_path:
        print("Nenhum local de salvamento selecionado. Saindo...")
        exit()

    temp_pdf_path = merge_pdfs(input_folder, output_path)
    compress_pdf(temp_pdf_path, output_path)
    
    # Remover o arquivo temporário
    os.remove(temp_pdf_path)

    print(f"Arquivos PDF mesclados e comprimidos salvos em: {output_path}")
