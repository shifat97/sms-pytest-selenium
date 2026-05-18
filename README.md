# Pytest Selenium AI Template

A robust, modern UI automation framework built with **Python**, **Pytest**, and **Selenium**. This template follows the **Page Object Model (POM)** design pattern and includes features like automatic driver management, environment-based configuration, and automated reporting.

## 🚀 Features

- **Page Object Model (POM)**: Clean separation of test logic and UI interactions.
- **Automatic Driver Management**: Uses `webdriver-manager` to handle browser binaries (Chrome & Firefox).
- **Multi-browser Support**: Easily switch between Chrome and Firefox via configuration.
- **Headless Mode**: Support for running tests without a GUI (ideal for CI/CD).
- **Environment Configuration**: Manage settings and secrets using `.env` files.
- **Auto-Screenshots**: Automatically captures screenshots on test failures in `reports/screenshots`.
- **Rich HTML Reports**: Generates detailed test reports using `pytest-html`.
- **Custom Markers**: Organized tests using markers like `@pytest.mark.smoke` and `@pytest.mark.auth`.

## 📋 Prerequisites

- **Python 3.8+**
- **Google Chrome** or **Mozilla Firefox** installed on your machine.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pytest-selenium-ai
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Environment Variables**:
   Copy the example environment file (if provided) or create a `.env` file in the root directory:
   ```bash
   BASE_URL=https://example.com
   BROWSER=chrome
   HEADLESS=true
   TIMEOUT=10
   VALID_EMAIL=user@example.com
   VALID_PASSWORD=Secret123!
   ```

## 🏃 Running Tests

### CLI Quick Reference
```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run only smoke tests
pytest -m smoke

# Run only auth tests verbosely
pytest -m auth -v

# Run specific test file
pytest tests/test_login.py

# Run specific test
pytest tests/test_login.py::TestLogin::test_valid_login_redirects_to_dashboard

# Run headed (not headless) for debugging
HEADLESS=false pytest -m smoke

# Generate HTML report
pytest --html=reports/report.html --self-contained-html
```

### View Reports
After execution, the HTML report is generated at `reports/report.html`. Screenshots for failed tests are stored in `reports/screenshots/`.

## 📂 Project Structure

```text
pytest-selenium-ai/
├── config/             # Configuration management
│   └── config.py       # Reads .env and provides settings
├── pages/              # Page Object Model classes
│   ├── base_page.py    # Common page actions & wrappers
│   ├── login_page.py   # Login page interactions
│   └── dashboard_page.py # Dashboard page interactions
├── tests/              # Test suites
│   ├── test_login.py   # Authentication tests
│   └── test_dashboard.py # Dashboard functionality tests
├── utils/              # Helper functions and utilities
├── reports/            # Generated reports & screenshots (Git ignored)
├── conftest.py         # Pytest fixtures & hooks (driver setup)
├── pytest.ini          # Pytest configuration & markers
├── requirements.txt    # Project dependencies
└── .env                # Local environment secrets (Git ignored)
```

## 🏗️ Adding New Tests

1. **Create a Page Object**: Define new locators and methods in a class under `pages/`, inheriting from `BasePage`.
2. **Write the Test**: Create a new test file in `tests/` or add to an existing one. Use the `driver` fixture.
3. **Use the Page Object**: Instantiate your page object within the test and call its methods.

---

*Happy Testing!* 🧪
