# Constitution of Kenya RAG
This project provides a Streamlit-powered frontend interface to search and retrieve information from the Constitution of Kenya PDF using advanced AI capabilities powered by Groq and Langchain. Users can ask questions about the constitution and receive real-time answers along with the relevant sources.

## Kenyan Constitution AI Search

This project provides a Streamlit-powered frontend interface to search and retrieve information from the Constitution of Kenya PDF using advanced AI capabilities powered by Groq and Langchain. Users can ask questions about the constitution and receive real-time answers along with the relevant sources.

### 🌟 Features

  * **Interactive Search**: Ask questions in natural language and get instant answers.
  * **AI-Powered Retrieval**: Utilizes Groq for fast inference and Langchain for robust RAG (Retrieval Augmented Generation) capabilities.
  * **Source Attribution**: Provides source references for the generated answers, enhancing transparency and verifiability.
  * **User-Friendly Interface**: Built with Streamlit for an intuitive and easy-to-use experience.

### 🛠️ Technologies Used

  * **Python**: The core programming language for both frontend and backend.
  * **Streamlit**: For building the interactive web application frontend.
  * **Groq**: For fast language model inference (backend).
  * **Langchain**: For orchestrating the RAG pipeline (backend).
  * **Requests**: For communication between the Streamlit frontend and the local backend API.
  * **Jupyter Notebook**: Likely used for data processing, PDF parsing, or backend logic development.

### 📁 Project Structure

  * `app_py.py`: The Streamlit frontend application. This file handles user input, displays results, and communicates with the backend.
  * `kenyanconstitution (1).ipynb`: A Jupyter Notebook likely containing the logic for processing the Kenyan Constitution PDF, setting up the Langchain pipeline, and potentially implementing the backend API that the Streamlit app communicates with.
  * `kenyan_flag.jpg`: An image file used for display in the Streamlit app.

### 🚀 Setup and Installation

To set up and run this project locally, follow these steps:

1.  **Clone the Repository**:

    ```bash
    git clone https://github.com/DorcasBwire/Kenyan_Constitution_RAG.git
    cd Kenyan_Constitution_RAG
    ```

2.  **Install Dependencies**:
    It's recommended to create a virtual environment.

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

    *Note*: A `requirements.txt` file is not provided in the uploaded files. You will need to create one based on the imports in `app_py.py` and the expected backend dependencies (Groq, Langchain, possibly PDF loaders/parsers). A minimal `requirements.txt` would include:

    ```
    streamlit
    requests
    groq
    langchain
  

3.  **Run the Backend (API Service)**:
    The Streamlit app connects to a backend service running on `http://localhost:8000`. You will need to ensure your backend (likely implemented in or derived from `kenyanconstitution (1).ipynb`) is running and listening on this port.

      * If `kenyanconstitution (1).ipynb` contains your backend logic, you'll need to adapt it to run as a Python script (e.g., using Flask, FastAPI, or a simple HTTP server) and start it.
      * Example (conceptual, actual implementation depends on your notebook's backend structure):
        ```bash
        python your_backend_script.py # Assuming you convert your notebook to a Python script
        ```

    Ensure this backend service is active before launching the Streamlit frontend.

4.  **Run the Streamlit Frontend**:
    Once the backend is running, open a new terminal, navigate to the project directory, and run the Streamlit application:

    ```bash
    streamlit run app_py.py
    ```

    This command will open the Streamlit application in your default web browser.

### 🌐 Running in Google Colab

If you prefer to run this project in Google Colab, refer to the detailed instructions provided previously, which include steps for uploading files, installing `streamlit` and `pyngrok`, and exposing the Streamlit app via a public URL. Remember to also run your backend logic within the Colab environment for full functionality.

### 🚀 Usage

1.  Launch the Streamlit application as described in the "Setup and Installation" section.
2.  Enter your question related to the Constitution of Kenya into the text input field.
3.  Click the "Ask" button.
4.  The application will display the answer and a list of sources from the Constitution PDF.

-----

**Disclaimer**: The accuracy of the answers depends on the quality of the underlying PDF document, the Groq model's capabilities, and the Langchain implementation.
