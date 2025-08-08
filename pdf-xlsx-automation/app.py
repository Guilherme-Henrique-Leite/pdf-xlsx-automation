import os
import streamlit as st
from tempfile import TemporaryDirectory
from pdf_to_excel import convert_pdf_to_excel, pdf_is_scanned
import time

st.set_page_config(page_title="PDF → Excel ERP", page_icon="📄")

st.title("📄 Conversor PDF ERP → Excel")
uploaded_file = st.file_uploader("Envie seu PDF do ERP", type=["pdf"])

today = time.strftime("%d/%m/%Y", time.localtime())

if uploaded_file:
    with TemporaryDirectory() as tmpdir:
        pdf_path = os.path.join(tmpdir, uploaded_file.name)
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.read())

        st.info("📄 Analisando PDF...")
        if pdf_is_scanned(pdf_path):
            st.warning("O PDF é escaneado — usando OCR, isso pode levar um pouco mais de tempo.")
        else:
            st.success("O PDF é digital — extraindo tabelas diretamente.")

        output_path = os.path.join(tmpdir, "resultado.xlsx")
        df = convert_pdf_to_excel(pdf_path, output_path)

        st.subheader("Pré-visualização dos dados extraídos")
        st.dataframe(df.head(50))

        with open(output_path, "rb") as excel_file:
            st.download_button(
                label="📥 Baixar Excel",
                data=excel_file,
                file_name=f"relatorio_{today}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        st.success("✅ Conversão concluída!")