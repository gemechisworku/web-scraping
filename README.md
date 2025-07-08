# 🕵️‍♂️ OA Web Scraper Dashboard

This is a Streamlit-based web application that scrapes contact and search form data from the **Ordem dos Advogados (OA)** Portugal website. It allows users to extract, view, and export data from several OA pages, all from a user-friendly interface.

---

## 🚀 Features

- 🔗 **Scrape Data from OA Pages**:
  - Conselho Geral Contacts
  - Lawyer Search Page
  - Law Firm Search Page

- 📊 **View Data**:
  - Automatically formats output as tables or lists based on content.

- ⬇️ **Download Options**:
  - Export individual page data as CSV
  - Export all scraped data as a single Excel file with separate sheets

- 🧭 **Tabbed UI**:
  - Clean navigation between sources using Streamlit tabs

- 🧑‍💻 **Modular Codebase**:
  - Scraping logic is separated from UI for better maintainability

- 🧾 **Footer Credits**:
  - App includes a custom footer with developer attribution

---

## 🗂 Project Structure

```plaintext
web-scraping/
├── scripts/
│   ├── app.py
│   ├── scraper.py
├── requirements.txt
└── README.md
```
## 📦 Requirements
```plaintext
streamlit
pandas
beautifulsoup4
requests
openpyxl
```
## 🛠 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/oa-web-scraper-dashboard.git
   cd oa-web-scraper-dashboard
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
    ```
3. Run the Streamlit app:
    ```bash
    streamlit run scripts/app.py
    ```
## 📖 Usage

1. Open your web browser and go to `http://localhost:8501`.
2. Use the tabs to navigate between different scraping options.
3. Follow the on-screen instructions to scrape data from the OA website.
4. View the scraped data in the app and use the download options to export it.

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

