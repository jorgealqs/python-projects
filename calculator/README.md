# 📌 Calculator Documentation (CreativeTech)

## 📖 Overview
This is a **modern calculator** built with **PyQt6**. It features a graphical interface with a **custom stylesheet** (`styles.qss`) and supports basic arithmetic operations.

---

## 📂 Project Structure
```
calculator_project/
│── main.py       # Main Python file (GUI logic)
│── styles.qss    # Custom styles for the calculator
│── venv/         # Virtual environment (optional)
│── requirements.txt # Dependencies
```

---

## 🚀 Installation & Setup

### 1️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

---

## 📜 Code Explanation

### 🔹 `Calculator` Class
This class defines the calculator GUI and its functionality.

#### 🔹 `__init__()` - Constructor
- Sets up the **window title, size, and styles**.
- Calls `load_styles()` to apply **QSS styling**.
- Calls `create_ui()` to build the **interface**.

#### 🔹 `load_styles()` - Load Stylesheet
- Reads and applies styles from `styles.qss` using `setStyleSheet()`.

#### 🔹 `create_ui()` - Create UI Components
- Creates a **QLineEdit** for the display.  
- Uses **QGridLayout** to arrange buttons dynamically.  
- Each button has a **custom object name** for styling.

#### 🔹 `on_button_click()` - Button Click Handling
- If `=` is pressed, evaluates the **mathematical expression**.
- If `C` is pressed, it **clears** the display.
- Otherwise, it **appends** the button text to the display.

---

## 🎨 Styling with `styles.qss`
You can define custom styles using QSS (similar to CSS). Example:
```css
QWidget {
    background-color: #2c3e50;
}

QPushButton {
    background-color: #34495e;
    color: white;
    border-radius: 5px;
    font-size: 18px;
}
```

---

## 💡 Running the Calculator
Run the Python script with:
```sh
python main.py
```

This will launch a **modern, responsive calculator GUI**. 🎉🚀****