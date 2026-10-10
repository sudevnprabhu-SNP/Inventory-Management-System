# 📦 Inventory Management System

**A Python-based inventory application for managing products, tracking stock quantities, and identifying low-stock items.**

A menu-driven console project demonstrating how Python can be used to organize product records and perform everyday inventory operations.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Dependencies-None-2ea44f?style=for-the-badge" alt="No third-party dependencies">
  <img src="https://img.shields.io/badge/Interface-CLI-555555?style=for-the-badge" alt="Command-line interface">
  <img src="https://img.shields.io/badge/Project-Learning%20Project-orange?style=for-the-badge" alt="Learning project">
</p>

---

## 📌 Overview

The **Inventory Management System** provides a simple way to manage product information through an interactive terminal menu.

Users can add products, browse and search records, update product details, adjust stock quantities, and identify items that may need replenishment.

The project focuses on practical Python programming, data structures, record management, and basic inventory tracking.

## ✨ Features

| Feature | Description |
|---|---|
| ➕ Product Registration | Add products and detect duplicate product IDs |
| 📋 Product Listing | View product records and sort them by supported fields |
| 🔎 Product Search | Find products using their IDs |
| ✏️ Record Updates | Modify existing product details |
| 📈 Stock Adjustment | Increase or decrease product quantities |
| 🗑️ Product Deletion | Remove products with confirmation details |
| ⚠️ Low-Stock Detection | Identify products that fall below the configured stock threshold |

## 🛠️ Built With

- **Language:** Python
- **Interface:** Interactive command-line menu
- **Data management:** In-memory product records
- **Dependencies:** Python standard library only

No third-party packages or database installation are required.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or newer recommended
- A terminal or command prompt
- Git, if you want to clone the repository

### 1. Clone the repository

```bash
git clone https://github.com/sudevnprabhu-SNP/Inventory-Management-System.git
```

### 2. Navigate to the project folder

```bash
cd Inventory-Management-System
```

### 3. Start the application

```bash
python3 src/inventory.py
```

If `python3` is not recognized on Windows, try:

```bash
python src/inventory.py
```

Use the numbered menu and follow the prompts to perform inventory operations.

## 🧪 Example Workflow

A typical session could include:

1. Viewing the available products.
2. Searching for a product by its ID.
3. Updating product information.
4. Increasing or decreasing stock quantities.
5. Checking for low-stock items.
6. Deleting a product when it is no longer required.

Sample products are included to help users explore the application.

## 📁 Project Structure

```text
Inventory-Management-System/
├── src/
│   └── inventory.py
├── docs/
│   └── screenshots/
├── README.md
├── requirements.txt
└── LICENSE
```

## 🖥️ Screenshots

Application screenshots can be added here to demonstrate the program in action.

Suggested screenshots:

- Main menu
- Product listing
- Product search or update
- Stock quantity adjustment
- Low-stock report

*Screenshots are not included yet. Add genuine terminal captures after running the application.*

## 💾 Data and Persistence

The application starts with sample product records defined in the source code. Product information and changes are stored in memory while the program is running.

**Important:** Changes are not saved after the application exits.

## ⚠️ Limitations

- **Temporary storage:** Product records are not persisted to a file or database.
- **Basic validation:** Input and stock validation are simplified and may require additional edge-case handling.
- **Console-based interface:** No graphical user interface is currently provided.
- **No external integrations:** Barcode scanners, suppliers, and external inventory services are not connected.

This project is intended for learning and demonstration, not for production inventory, billing, or accounting operations.

## 🎯 Learning Objectives

This project demonstrates practical use of:

- Python dictionaries and data structures
- Functions, loops, and conditional statements
- Creating, reading, updating, and deleting records
- Searching and sorting data
- Input validation and quantity checks
- Basic stock monitoring and threshold-based warnings
- Organizing a Python project for GitHub

## 🔮 Future Improvements

Possible extensions include:

- Saving product records using SQLite
- Adding a graphical interface or web dashboard
- Generating inventory reports
- Supporting product categories and stock movement history
- Adding automated tests and stronger input validation

These are potential future enhancements, not existing features.

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.

Publish this license only if you have the rights to license the code and documentation in the repository. Any third-party materials remain subject to their own terms.

---

<p align="center">
  <i>Built with Python • Focused on Inventory Management • Created as a Learning Project</i>
</p>
