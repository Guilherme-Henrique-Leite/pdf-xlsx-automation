# PDF to Excel Automation

This project provides a Streamlit application that converts PDF files from ERP systems into Excel format. It allows users to upload PDF files, processes them to extract data, and provides an interface for downloading the converted Excel files.

## Project Structure

- `app.py`: The main Streamlit application code that handles file uploads and data extraction.
- `pdf_to_excel.py`: Contains functions for converting PDF files to Excel and checking if a PDF is scanned.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `.streamlit/config.toml`: Configuration file for Streamlit settings.

## Requirements

To run this application, you need to install the required Python packages. You can do this by running:

```
pip install -r requirements.txt
```

## Running the Application

To start the Streamlit application, navigate to the project directory and run:

```
streamlit run app.py
```

This will launch the application in your default web browser.

## Usage

1. Upload your PDF file using the provided file uploader.
2. The application will analyze the PDF and determine if it is scanned or digital.
3. Once processed, a preview of the extracted data will be displayed.
4. You can download the converted Excel file by clicking the download button.

## License

This project is open-source and available for use and modification.