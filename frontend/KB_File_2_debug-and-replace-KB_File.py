import os
import logging
from datetime import datetime
import pandas as st
import streamlit as st
from server.utils.file import save_uploaded_file, get_save_dir
from server.stores.strage_context import STORAGE_CONTEXT

def process_file(file_path):
    """Process and index the file"""
    # Placeholder for the actual file processing logic
    # For example, you can add code to read the PDF and index its content
    logging.info(f"Processing file: {file_path}")
    # Add your file processing logic here

def bulk_upload(parent_folder):
    """Function to handle bulk upload of files from a parent folder and its subdirectories"""
    log_filename = f"knowledge_base_upload_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(filename=log_filename, level=logging.INFO)
    status_report = []

    total_files = sum([len(files) for r, d, files in os.walk(parent_folder) if any(f.endswith(".pdf") for f in files)])
    progress = 0

    for root, _, files in os.walk(parent_folder):
        for file in files:
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                try:
                    process_file(file_path)  # Process and index the file
                    status_report.append({
                        "file_name": file,
                        "file_type": "PDF",
                        "file_size": os.path.getsize(file_path),
                        "upload_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    logging.info(f"Successfully processed {file_path}")
                except Exception as e:
                    logging.error(f"Error processing {file_path}: {e}")
                progress += 1
                st.progress(progress / total_files)

    report_filename = f"KB_Asset_Loading_Status_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    with open(report_filename, "w") as report_file:
        report_file.write("| File Name | File Type | File Size | Upload Date |\n")
        report_file.write("|-----------|-----------|-----------|-------------|\n")
        for entry in status_report:
            report_file.write(f"| {entry['file_name']} | {entry['file_type']} | {entry['file_size']} | {entry['upload_date']} |\n")

    return report_filename

def handle_file():
    """Function to handle single file upload"""
    st.header("Load Files")
    st.caption("Load Files like PDF, DOCX, TXT, etc. to create a knowledge base index.")
    
    with st.form("my-form", clear_on_submit=True):
        st.session_state.selected_files = st.file_uploader("Upload files: ", accept_multiple_files=True, label_visibility="hidden")
        submitted = st.form_submit_button(
            "Load",
            help="Click here to load it after you select a file.",
        )
        if len(st.session_state.selected_files) > 0 and submitted:
            print("Starting to upload files...")
            print(st.session_state.selected_files)
            for selected_file in st.session_state.selected_files:
                with st.spinner(f"Uploading {selected_file.name}..."):
                    save_dir = get_save_dir()
                    save_uploaded_file(selected_file, save_dir)
                    st.session_state.uploaded_files.append({"name": selected_file.name, "type": selected_file.type, "size": selected_file.size})
                    # Update the doc_store with the new fileimport os
import logging
from datetime import datetime
import pandas as st
import streamlit as st
from server.utils.file import save_uploaded_file, get_save_dir
from server.stores.strage_context import STORAGE_CONTEXT

def process_file(file_path):
    """Process and index the file"""
    # Placeholder for the actual file processing logic
    # For example, you can add code to read the PDF and index its content
    logging.info(f"Processing file: {file_path}")
    # Add your file processing logic here

def bulk_upload(parent_folder):
    """Function to handle bulk upload of files from a parent folder and its subdirectories"""
    log_filename = f"knowledge_base_upload_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(filename=log_filename, level=logging.INFO)
    status_report = []

    total_files = sum([len(files) for r, d, files in os.walk(parent_folder) if any(f.endswith(".pdf") for f in files)])
    progress = 0

    for root, _, files in os.walk(parent_folder):
        for file in files:
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                try:
                    process_file(file_path)  # Process and index the file
                    status_report.append({
                        "file_name": file,
                        "file_type": "PDF",
                        "file_size": os.path.getsize(file_path),
                        "upload_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    logging.info(f"Successfully processed {file_path}")
                except Exception as e:
                    logging.error(f"Error processing {file_path}: {e}")
                progress += 1
                st.progress(progress / total_files)

    report_filename = f"KB_Asset_Loading_Status_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    with open(report_filename, "w") as report_file:
        report_file.write("| File Name | File Type | File Size | Upload Date |\n")
        report_file.write("|-----------|-----------|-----------|-------------|\n")
        for entry in status_report:
            report_file.write(f"| {entry['file_name']} | {entry['file_type']} | {entry['file_size']} | {entry['upload_date']} |\n")

    return report_filename

def handle_file():
    """Function to handle single file upload"""
    st.header("Load Files")
    st.caption("Load Files like PDF, DOCX, TXT, etc. to create a knowledge base index.")
    
    with st.form("my-form", clear_on_submit=True):
        st.session_state.selected_files = st.file_uploader("Upload files: ", accept_multiple_files=True, label_visibility="hidden")
        submitted = st.form_submit_button(
            "Load",
            help="Click here to load it after you select a file.",
        )
        if len(st.session_state.selected_files) > 0 and submitted:
            print("Starting to upload files...")
            print(st.session_state.selected_files)
            for selected_file in st.session_state.selected_files:
                with st.spinner(f"Uploading {selected_file.name}..."):
                    save_dir = get_save_dir()
                    save_uploaded_file(selected_file, save_dir)
                    st.session_state.uploaded_files.append({"name": selected_file.name, "type": selected_file.type, "size": selected_file.size})
                    # Update the doc_store with the new file