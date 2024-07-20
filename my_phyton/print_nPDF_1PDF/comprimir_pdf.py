import os
import fitz  # PyMuPDF
from PIL import Image
import io
from tkinter import Tk, filedialog

def select_pdf_file():
    root = Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")], title="Selecione o arquivo PDF para comprimir")
    root.destroy()
    return file_path

def compress_pdf(input_path):
    # Obter o nome do arquivo sem extensão e o diretório
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(os.path.dirname(input_path), f"{base_name}_comprimido.pdf")
    
    # Abrir o documento PDF
    document = fitz.open(input_path)
    new_document = fitz.open()  # Novo documento PDF
    
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        new_page = new_document.new_page(width=page.rect.width, height=page.rect.height)
        
        # Copiar o conteúdo da página original para a nova página
        new_page.show_pdf_page(new_page.rect, document, page_num)
        
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
            new_page.insert_image(rect, stream=new_image_bytes)
    
    # Salvar o novo documento PDF
    new_document.save(output_path)
    new_document.close()
    document.close()
    
    return output_path

if __name__ == "__main__":
    input_path = select_pdf_file()
    if not input_path:
        print("Nenhum arquivo PDF selecionado. Saindo...")
        exit()

    output_path = compress_pdf(input_path)
    print(f"Arquivo PDF comprimido e salvo em: {output_path}")
