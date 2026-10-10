    # Inventory Management System

    A menu-driven Python console program for managing product and stock records.

    ## Features

    - Add products and detect duplicate product IDs
- View product records sorted by supported fields
- Search products by ID
- Update product details
- Increase or decrease stock quantity
- Delete products with confirmation details
- Check for low-stock items

    ## Requirements

    Uses only the Python standard library; no third-party packages are required.

    - Recommended Python version: Python 3.10 or newer.
    - See [`requirements.txt`](requirements.txt).

    ## Run locally

    1. Install Python 3.
    2. Clone this repository or download it as a ZIP.
    3. Open a terminal in the repository root.
    4. Run:

       ```bash
       python3 src/inventory.py
       ```

    ## Sample usage

    Run the script and use the numbered menu to add, view, search, update, adjust quantity, delete products, or check stock. Sample products are included.

    ## Project structure

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

    ## Screenshots

    Add terminal screenshots here after running the program. Suggested screenshots: product list, stock adjustment, and low-stock check. No screenshots are included because none were provided.

    ## Data and persistence

    The program starts with sample records defined in the source code. Records are maintained in memory during the current run; they are not saved to a database or file.

    ## Limitations

    - Product records are stored in memory and are lost when the program exits.
- Input validation and stock rules are simplified and may need additional edge-case handling.
- There is no database, file-based persistence, GUI, or barcode integration.
- This is a learning project, not a production inventory or accounting system.

    ## License

    This project is distributed under the MIT License. See [`LICENSE`](LICENSE). The license applies to the original project code and documentation authored for this repository; any third-party materials retain their own terms.
