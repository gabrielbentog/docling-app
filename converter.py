import os
from docling.document_converter import DocumentConverter

def convert_pdf_to_markdown(input_dir, output_dir):
    # Inicializa o conversor do Docling
    converter = DocumentConverter()

    # Verifica se o diretório de saída existe; se não, cria-o
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Itera sobre os arquivos no diretório de entrada
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.pdf'):
            source_path = os.path.join(input_dir, filename)
            output_filename = f"{os.path.splitext(filename)[0]}.md"
            output_path = os.path.join(output_dir, output_filename)

            try:
                # Converte o documento
                result = converter.convert(source_path)
                # Exporta para Markdown
                markdown_content = result.document.export_to_markdown()
                # Salva o conteúdo convertido no arquivo de saída
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(markdown_content)
                print(f"Arquivo convertido com sucesso: {output_filename}")
            except Exception as e:
                print(f"Erro ao converter {filename}: {e}")

if __name__ == "__main__":
    input_directory = "input"
    output_directory = "output"
    convert_pdf_to_markdown(input_directory, output_directory)
