# News Research Tool

The News Research Tool is a Streamlit-based application that allows users to input URLs of news articles, process these articles, and then ask questions about the content. The tool uses OpenAI's language model to provide answers and relevant sources from the processed articles.

## Features

- **URL Input**: Users can input up to three news article URLs for processing.
- **Text Processing**: The tool loads, splits, and embeds the text from the provided URLs.
- **Question Answering**: Users can ask questions about the content of the articles, and the tool will provide answers using OpenAI's language model.
- **FAISS Indexing**: The tool uses FAISS for efficient similarity search and storing of embeddings.

## Installation

### Prerequisites

- Python 3.8 or higher
- Streamlit
- OpenAI API key
- FAISS
- dotenv

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/news-research-tool.git
    cd news-research-tool
    ```

2. **Install the Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

4. **Run the Application**:
    ```bash
    streamlit run main.py
    ```

## Usage

1. **Input URLs**:
    - Open the application in your browser.
    - Enter up to three news article URLs in the sidebar and click "Process URLs".

2. **Ask Questions**:
    - After the URLs are processed, enter your question in the main input box and press Enter.
    - The application will display the answer along with the sources.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.
