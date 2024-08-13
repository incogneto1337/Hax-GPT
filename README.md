---

# Hax-GPT

UNDER CONSTRUCTION 🚧 

Hax-GPT is a command-line interface (CLI) tool designed to assist cybersecurity researchers by providing AI-driven responses. The tool leverages the MetaAI API to interact with users and deliver relevant information based on their queries.

## Features

- **Clear Terminal Screen**: Provides a clean slate for user interaction.
- **Centered Output**: Ensures text is presented in a clean, readable format.
- **AI Integration**: Uses MetaAI to provide insightful responses to user queries.
- **Session Management**: Allows users to start and end their session easily.

## Installation

Ensure you have the required dependencies installed. You can use `pip` to install them:

```bash
pip install rich meta_ai_api
```

## Usage

To start the Hax-GPT CLI interface, simply run the following command:

```bash
python chat.py
```

### Commands

- **Enter your query**: Type your question or request and press Enter.
- **Type 'quit' or 'exit'**: End the session and exit the CLI.

## Code Overview

### `chat.py`

- **clear_screen()**: Clears the terminal screen based on the operating system.
- **print_centered_block(text, padding, bottom_padding, console_width, style)**: Prints a block of text centered within the console width with optional padding and style.
- **get_ai_response(user_input)**: Retrieves a response from the MetaAI service using the provided user input.
- **getchat()**: Main function to handle the CLI interaction with the AI.

### Example Usage

If you want to use the `getchat` function from another Python file, you can import it and call it as follows:

```python
from chat import getchat

getchat()
```

## Error Handling

- **ConnectionError**: Catches connection issues with the MetaAI service.
- **ValueError**: Handles value errors that may occur.
- **Exception**: Catches all other unexpected errors.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to enhance the functionality or fix any bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
