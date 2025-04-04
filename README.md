# Document Summarization

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

**Document Summarization** is a lightweight Python web application that provides automatic summarization of long-form text documents using basic NLP techniques. Built with Flask, it features a simple interface to paste or upload content and receive a concise summary.

## 🚀 Features

- 📄 **Multi-File Support** – Upload and process Word, PDF, and PPTX files.
- ✂️ **Text Summarization** – Quickly distill long texts into brief summaries.
- 🌐 **Web Interface** – Clean and minimal front end for ease of use.
- ⚙️ **Modular Structure** – Easy to modify, extend, and understand.
- ☁️ **Ready for Deployment** – Includes support files for Heroku and similar platforms.

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Nwwar/Document-Summarization.git
cd Document-Summarization
```

### 2. (Optional) Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🧠 Usage

### Run the App Locally

```bash
python app.py
```


### Interface

- Paste or type in a block of text.
- Click **Summarize**.
- View the generated summary below.

## 🗂 Project Structure

```
Document-Summarization/
├── app.py              # Main Flask application
├── utils.py            # Summarization logic and helper functions
├── templates/          # HTML templates (e.g., index.html)
├── requirements.txt    # Python dependencies
├── runtime.txt         # Runtime version (for Heroku)
├── Procfile            # Deployment configuration
├── .slugignore         # Optional deployment ignores
└── LICENSE             # Apache License 2.0
```

## 🛠 Customization

- **Summarization Logic**: You can tweak `utils.py` to improve or modify the algorithm.
- **UI Styling**: Edit `templates/index.html` for layout and CSS changes.
- **Deployment**: With `Procfile` and `runtime.txt`, deploy to [Heroku](https://www.heroku.com/) in minutes.

## 📄 License

This project is licensed under the **Apache License 2.0**.  
See the [LICENSE](LICENSE) file for full license text.

## 🤝 Contributing

Pull requests are welcome!  
Open an issue to discuss major changes or ideas.

## 🙋‍♂️ Questions?

Feel free to reach out by opening an issue in the repository.
