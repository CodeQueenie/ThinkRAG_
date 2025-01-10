# Enhancements_for_ThinkRAG: 

1) TODO PROMPT: BULK Automated Upload Functionality
    Add functions to automatically do a BULK upload and indexing of files all PDFs from a parent-folder directory, and all the PDFs in any subdirectories.  Iterately load and index all the documents in all subdirectories. Use the code in the "frontend\KB_File.py" file as a template for this.  Use all the same default settings that are given in the KB_File.py.  Add the necessary functionality to do this iteratively.  Add a horizontal line at the bottom of the current page that loads files.  

    ### Copilot Clarifying Questions: 

    Q1. Do you want the function to be triggered automatically when the application starts, or should it be triggered by a user action (e.g., clicking a button)?

    Q2. Should the indexed documents be displayed in the Streamlit app, or is the indexing process only for backend processing?

    Q1. Answer: 
        NO, we DO NOT want the functions for the "Bulk Loading of Assets" process to be triggered automatically. The User MUST initiate the bulk upload process.  Provide a Upload Folder component that allows the user to select the parent folder.  

    Q2. Answer: 
        We want the indexing process to be shown with a progress bar, and then display all the assets that were loaded during the process.  

        VERY IMPORTANT: This bulk upload process must be fault-tolerant with good fine-grained logging to a time-stamped file named "knowledge_base_upload_{datetime}.log", with try-except block error-handling with informative messages, so that debugging is easier.  Any processing errors for specific books or web pages that cannot be loaded, parsed and indexed MUST NOT stop the load and index process.  Make sure the application  recovers gracefully and moves to the next asset, until assets have been process.  
        
        Save a "Final Asset Loading Status Report" named "KB_Asset_Loading_Status_Report_{datetime}.md" in a time-stamped file.  Display the same text for the loading results in a text block in a collapsible container below the "Bulk Loading Assets" section.  

## ***<<< RICH & NICOLE LEFT OFF HERE !! >>> ***

#### TODO: FIX "Manage Knowledge Base" to update teh dataframe displaying all assets in library.

    Try Replacing: 
    state.py    with    state_new_TBD.py 
    KB_File.py  with    KB_File_2_debug-and-replace-KB_File.py
    app.py      with    app_new.py

Put "Load Files" section of the KB_File.py indexing page into an expandable container.  

# Main Page (currently named app.py)
    Add an expandable Streamlit container directly underneath the main page logo and in the container show the table with the current library of indexed content.  

    Add configuration to always run the Streamlit app in wide mode.

    Rename the app.py in the project root to ThinkRAG_main.py

# PERFORMANCE IMPROOVEMENTS: 
    Add caching for all user interface operations that can benefit form it 
    add caching for all LLM loading operations so it does not reload data unnecessarily.

# COSMETIC CHANGES TO IMPROVE USABILITY: 

    Rename the pages under "Knowledge Base" in the side bar as follows: 
        Files ==> Load Files
        Web ==> Load Web Pages
        Manage ==> Manage Content

    Make the fonts larger in the sidebar for the names of groups of functions: 

        **Application**
            Query
        **Knowledge Base**
            File
            Web
            Manage
        **Model & Tool**
            LLM
            Embed
            Rerank
            Storage
        **Settings**
            Advanced

# LONG-TERM CHAT MEMORY (ACROSS SESSIONS)
    The Streamlit app currently loses the chat session conversation everytime streamlit is restarted.  

