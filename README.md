# 📄 Docling PDF-to-Markdown Converter

Este projeto é um conversor de documentos que utiliza o [Docling](https://github.com/docling-project/docling) para transformar arquivos **PDF** em arquivos **Markdown (.md)**. Ele foi desenvolvido em Python com foco em escalabilidade, para futuramente suportar outros formatos de arquivos como DOCX, HTML, entre outros.

---

## 🚀 Funcionalidades

- ✅ Conversão automática de arquivos `.pdf` para `.md`
- 📁 Processamento em lote de documentos em uma pasta
- 📂 Estrutura de projeto modular e organizada
- 🔄 Preparado para suportar outros formatos de entrada (como `.docx`, `.html`, etc.)

---

## 📁 Estrutura do Projeto

```
docling_converter/
├── input_files/        # Coloque seus arquivos PDF aqui
├── output_files/       # Arquivos Markdown convertidos serão salvos aqui
└── converter.py        # Script principal de conversão
```

---

## 🥪 Pré-requisitos

Certifique-se de ter o **Python 3.8+** instalado. Em seguida, instale as dependências com:

```bash
pip install docling
```

---

## ⚙️ Como Usar

1. Coloque os arquivos `.pdf` que deseja converter dentro do diretório `input_files/`.
2. Execute o script:

```bash
python converter.py
```

3. Os arquivos `.md` serão gerados automaticamente na pasta `output_files/`.

---

## 🥉 Suporte a Outros Formatos

Para adicionar suporte a outros formatos (como `.docx`, `.html`), edite o trecho abaixo em `converter.py`:

```python
if filename.lower().endswith(('.pdf', '.docx', '.html')):
```

O Docling já possui suporte interno para esses formatos!

---

## 🦹‍♂️ Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar **pull requests**.

---

## 🔧 Tecnologias Utilizadas

- Python
- [Docling](https://pypi.org/project/docling/)

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT**.

---

## ✨ Agradecimentos

- IBM e colaboradores do projeto [Docling](https://github.com/docling-project/docling)
- Comunidade Python

