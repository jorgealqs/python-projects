# Chrome Selenium Automation

A Python script for automating Chrome browser tasks using Selenium WebDriver.

## 🔧 Requirements

- Python 3.x
- Selenium WebDriver
- Chrome Browser
- ChromeDriver (matching your Chrome version)

## 📥 Installation

1. Install Python dependencies:

    ```bash
        pip install selenium
    ```

2. Download ChromeDriver:
   - Visit [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)
   - Select the version matching your Chrome browser
   - Add the ChromeDriver to your system PATH

## 🚀 Usage

1. Import the script:

    ```python
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    ```

2. Run the script:

    ```bash
    python main.py
    ```

## ⚙️ Configuration

The script includes several Chrome options:

- Disables notifications
- Starts maximized
- Disables automation flags
- Removes "Chrome is being controlled by automated software" message

## 📝 Example

```python
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=chrome_options)
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Contact

For support or queries, please open an issue in the repository.
