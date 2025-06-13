
# 🔐 MyPass – Password Manager

MyPass is a graphical password manager built with Python and Tkinter that allows you to generate secure passwords and save your website login credentials. Data is stored locally in a CSV file, and a companion script (`fetch_data.py`) helps in viewing saved data.

---

## 📌 Features

- 🔐 Strong password generation with letters, numbers, and symbols
- 💾 Save website, email, and password data locally
- ⚠️ Input validation for empty fields and password length
- 📊 View saved passwords using `fetch_data.py`
- 🖼️ Simple GUI with a custom logo image

---

## 🗂️ Project Structure

```
MyPass/
├── main.py             # Main GUI application
├── fetch_data.py       # Script to read and display saved credentials
├── data.csv            # CSV file storing passwords
├── logo.png            # Logo used in GUI
└── README.md           # Project documentation
```

---

## 🖥️ Getting Started

### 🔧 Prerequisites

- Python 3.7 or higher
- Required package:
  - `pandas`

Install the required package using:

```bash
pip install pandas
```

---

## ⚙️ Installation & Running

### Clone the repository

```bash
git clone https://github.com/mithildabhi/MyPass.git
cd MyPass
```

### Run the Password Manager GUI

```bash
python main.py
```

### View Saved Data

To display the saved login credentials:

```bash
python fetch_data.py
```

This will read the `data.csv` file and display the first 10 entries using pandas.

---

## 📸 Screenshot

[![Screenshot 2025-05-24 150211.](![image](https://github.com/mithildabhi/Password-Manager/blob/main/Screenshot%202025-05-24%20150211.png))]

---

## ✏️ How to Use

1. Run `main.py`.
2. Fill in the **Website**, **Email/Username**, and click **Generate Password** to auto-generate a secure password.
3. Click **Add** to save the entry to `data.csv`.
4. Use `fetch_data.py` to view entries.

📝 *Empty fields are not allowed, and passwords must be at least 8 characters long.*

---

## 🛠️ Notes

- All data is saved in `data.csv` in the format:
  ```
  website,email,password
  ```
- The GUI reads `logo.png` for branding. Make sure it exists in the same directory as `main.py`.

---

## 📤 Pull & Contribution Guide

Want to contribute? Follow these steps:

1. Fork the repository
2. Create your branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request



---

## 👤 Author

Developed by [Mithil Dabhi]
