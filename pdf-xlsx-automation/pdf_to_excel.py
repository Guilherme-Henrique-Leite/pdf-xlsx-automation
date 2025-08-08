import os
import pandas as pd
import camelot
import fitz
import pytesseract
from tempfile import TemporaryDirectory


def pdf_is_scanned(pdf_path):
    """Verifica se o PDF é escaneado (imagem) ou digital (texto)."""
    doc = fitz.open(pdf_path)
    for page in doc:
        if page.get_text().strip():
            return False
    return True


def ocr_pdf_to_text_tables(pdf_path):
    """Converte PDF escaneado em DataFrame usando OCR."""
    data = []
    with TemporaryDirectory() as tmpdir:
        doc = fitz.open(pdf_path)
        for page_num, page in enumerate(doc, start=1):
            pix = page.get_pixmap(dpi=300)
            img_path = os.path.join(tmpdir, f"page_{page_num}.png")
            pix.save(img_path)

            text = pytesseract.image_to_string(img_path, lang="por")
            lines = [line for line in text.split("\n") if line.strip()]
            data.extend([line.split() for line in lines])
    return pd.DataFrame(data)


def extract_tables(pdf_path):
    """Extrai tabelas de PDF digital."""
    tables = camelot.read_pdf(pdf_path, pages="all", flavor="lattice")
    if tables.n == 0:
        tables = camelot.read_pdf(pdf_path, pages="all", flavor="stream")
    return pd.concat([t.df for t in tables], ignore_index=True)


def clean_repeated_headers(df):
    """Remove cabeçalhos repetidos."""
    if df.empty:
        return df
    first_row = df.iloc[0]
    df_clean = df[~(df == first_row).all(axis=1)]
    return df_clean.reset_index(drop=True)


def convert_pdf_to_excel(pdf_path, output_path):
    """Processa qualquer PDF (digital ou escaneado) e salva como Excel."""
    if pdf_is_scanned(pdf_path):
        df = ocr_pdf_to_text_tables(pdf_path)
    else:
        df = extract_tables(pdf_path)

    df = clean_repeated_headers(df)
    df.to_excel(output_path, index=False)
    return df
