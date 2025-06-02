# 🖼️ Image Summary Web App (BLIP Model)

This is a simple Flask-based web application that generates a **text summary** (caption) for an uploaded image using the **BLIP** (Bootstrapped Language Image Pretraining) model from Hugging Face. It can describe the content of images using natural language.

---

## 🔍 Features

- Upload any image and get an AI-generated caption
- Uses `Salesforce/blip-image-captioning-base` model
- Fast and lightweight
- Simple and clean user interface
- Runs on both **CPU** and **GPU**

---

## 🧠 Tech Stack

| Layer      | Technology                           |
|------------|--------------------------------------|
| Backend    | Flask (Python)                       |
| Model      | Hugging Face `blip-image-captioning` |
| Frontend   | HTML, CSS, Bootstrap                 |
| Libraries  | `transformers`, `torch`, `Pillow`    |

---

## 🚀 Getting Started

### 📦 1. Clone the Repository

```bash
git clone https://github.com/yourusername/image-summary-blip-app.git
cd image-summary-blip-app
```

### 🛠️ 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 📥 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note**: The model will automatically be downloaded when you run the app for the first time.

---

## 🔧 Project Structure

```
image-summary-blip-app/
├── app.py                     # Flask app code
├── requirements.txt           # Python dependencies
├── templates/
│   └── index.html             # Frontend page
├── static/
│   └── uploads/               # Uploaded images
```

---

### ▶️ 4. Run the App

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 📸 Example

**Uploaded Image**: children playing cricket  
**Generated Summary**:  
> "a young boy in a white uniform" *(example output)*

> *Note: For more accurate summaries, consider switching to the larger BLIP model or ViT-GPT2.*

---

## 🛠 Future Enhancements

- Add better image understanding models (BLIP-2, ViT-GPT2, Kosmos-2)
- Allow voice playback of the generated summary
- Enable batch image captioning
- Add multi-language support

---
