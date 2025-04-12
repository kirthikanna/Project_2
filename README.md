#  MINI-PROJECT-02: OrangeHRM Automation Framework

##  Project Title
**Automated Testing for OrangeHRM Demo Web Application using Python Selenium, Pytest, and Page Object Model (POM)**

## Project URL
 [OrangeHRM Demo Site](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)

---

## 🎯 Test Objective

This project aims to build a robust **Python Selenium automation framework** for validating the functionality of the **OrangeHRM demo CRM web application**. It simulates user actions, verifies results with assertions, and generates automated reports.

The framework includes:
- **Data-Driven Testing Framework (DDTF)** using Excel
- **Page Object Model (POM)** with **OOP principles**
- **Explicit Waits** for synchronization
- **Pytest-based HTML reporting**
- Positive and Negative test coverage
- **Keyword Driven + Hybrid Testing** style

---

##  Tools & Technologies

| Technology      | Description                                     |
|----------------|-------------------------------------------------|
| Python          | Programming Language                            |
| Selenium        | Web automation                                  |
| Pytest          | Testing Framework                               |
| POM             | Page Object Model for test structure            |
| DDT             | Data-Driven Testing via Excel                   |
| OpenPyXL        | Excel file interaction                          |
| HTML Report     | Pytest HTML plugin                              |
| Explicit Wait   | WebDriverWait + Expected Conditions             |
---
## Test Case ID	Description
TC-01	 Data-Driven Login Test (Positive/Negative) from Excel and verify using Cookies.
TC-02	 Verify Home URL is accessible.
TC-03	 Validate visibility of username & password input fields.
TC-04	 Post-login menu options visibility and clickability check (Admin, PIM, Leave, etc).
TC-05	 Create new user and validate login for the new user.
TC-06	 Verify new user record in Admin user list.
