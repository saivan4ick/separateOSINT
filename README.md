# separateOSINT

### separateOSINT - Various tools for finding anything in the open internet (OSINT world)

separateOSINT is an interesting project and a tool for searching for mentions of a brand or anything else online.  Where is the brand mentioned? separateOSINT can help.  It searches for as many references as you specify.

## Key Features & Benefits

*   **OSINT Toolkit:** Collection of tools for open-source intelligence gathering.
*   **Brand Monitoring:** Helps track mentions of brands across the internet.
*   **Phone Number OSINT:** Includes phone number information gathering capabilities.
*   **Customizable Search:**  Allows users to specify the number of references to search for.

## Prerequisites & Dependencies

Before you begin, ensure you have the following installed:

*   **Python:** Version 3.6 or higher is recommended.
*   **pip:** Python package installer.

The project also relies on the following Python libraries:

*   `requests`: For making HTTP requests.
*   `BeautifulSoup4`: For parsing HTML and XML.
*   `googlesearch-python`: For performing Google searches.
*   `phonenumbers`: For parsing, formatting, and validating phone numbers.
*   `rich`: For rich text and beautiful formatting in the terminal.

## Installation & Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/saivan4ick/separateOSINT.git
    cd separateOSINT
    ```

2.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    This command will install all the necessary libraries listed in the `requirements.txt` file.

## Usage Examples

To run the main script:

```bash
python separateOSINT.py
```

This will start the main application, allowing you to search for brand mentions or perform other OSINT tasks.

To use the phone number OSINT tool:

```bash
python phone.py
```

This will run the `phone.py` script, allowing you to enter a phone number and retrieve information about it.

## Configuration Options

There are no specific configuration files for this project.  The main configurations, such as the number of search results, are defined within the Python scripts. You can modify the code directly to adjust these settings.

## Contributing Guidelines

Contributions are welcome! Here's how you can contribute:

1.  **Fork the repository.**
2.  **Create a new branch** for your feature or bug fix.
3.  **Make your changes** and commit them with clear, descriptive commit messages.
4.  **Submit a pull request** to the main branch of the original repository.

Please ensure that your code follows the project's coding style and includes appropriate documentation.

## License Information

This project is licensed under the **Other** license. The specific terms of the license are outlined in the `COPYRIGHT` file.

## Acknowledgments

*   Thanks to the developers of the Python libraries used in this project.
*   Special thanks to the OSINT community for inspiration and valuable resources.

## Platform Support

| Platform                                                                                                             | Support |
| -------------------------------------------------------------------------------------------------------------------- | :-----: |
| <img src="icons/Linux.png" width="5%" alt="Linux"/> GNU/Linux                                                         |   ✅   |
| <img src="icons/Windows.png" width="5%" alt="Windows"/> Windows                                                       |   ✅   |
| <img src="icons/macOS.png" width="5%" alt="macOS"/> macOS                                                             |   ✅   |
| <img src="icons/Android.png" width="5%" alt="Android"/> Android                                                       |   ✅   |
| <img src="icons/IOS.png" width="5%" alt="IOS"/> IOS                                                                   |   ✅   |
| <img src="icons/WSL.png" width="5%" alt="WSL"/> WSL (Windows Subsystem for Linux)                                     |   ✅   |
