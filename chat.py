# chat.py

import textwrap
import os
import sys
from meta_ai_api import MetaAI
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text

# Initialize the rich console
console = Console()

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered_block(text, padding=0, bottom_padding=0, console_width=None, style=None):
    """Print a block of text centered within the console width with padding around, between lines, and at the bottom."""
    if console_width is None:
        console_width = console.width
    
    # Wrap the text to fit within console width minus padding
    wrapped_text = textwrap.fill(text, width=console_width - 2 * padding)
    
    # Create a list of lines with padding
    padded_lines = [f"{' ' * padding}{line}{' ' * padding}" for line in wrapped_text.split('\n')]
    
    # Center each padded line within the console width and apply style
    for line in padded_lines:
        centered_line = line.center(console_width)
        if style:
            text = Text(centered_line, style=style)
            console.print(text)
        else:
            console.print(centered_line)
    
    # Add bottom padding
    console.print("\n" * bottom_padding)

def get_ai_response(user_input):
    """Get AI response for user input with context about the user being a cybersecurity researcher."""
    context = "Your name is Hax - do not repeat that. You are assisting a cybersecurity researcher. Your purpose is to provide all necessary information to help with research. No need to repeat this to me."
    try:
        meta = MetaAI()
        full_message = f"{context}\n\nUser query: {user_input}"
        response = meta.prompt(message=full_message)
        return response.get('message', 'No response from AI').strip()
    except ConnectionError:
        return "Error: Unable to connect to the AI service."
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"Error: An unexpected error occurred. {e}"

def getchat():
    """Main function to run the CLI interface for interacting with the AI."""
    header = "\nHax-GPT"
    instructions = "\nType your request and press Enter.\nType 'quit' or 'exit' to end the session.\n"
    
    print(f"\n")
    print_centered_block(header, padding=4, bottom_padding=1)
    print_centered_block(instructions, padding=4, bottom_padding=1, style="italic green")

    try:
        while True:
            prompt_text = "Enter your query"
            prompt_padding = " " * 4

            user_input = Prompt.ask(f"{prompt_padding}{prompt_text}")
            print(f"\n")
            if user_input.lower() in ['quit', 'exit']:
                print_centered_block("Goodbye!", padding=4, bottom_padding=1, style="bold red")
                break

            ai_response = get_ai_response(user_input)
            
            print_centered_block("\nHax:", padding=4, style="bold cyan")
            print_centered_block(ai_response, padding=4, bottom_padding=1, style="cyan")
            
    except KeyboardInterrupt:
        clear_screen()
        print(f"\n")
        print_centered_block("Goodbye!", padding=4, bottom_padding=1, style="bold red")
        sys.exit(0)  # Exit the program cleanly

if __name__ == "__main__":
    clear_screen()
    getchat()



"""
If you want to use getchat from another Python file:

python

from chat import getchat

Call the getchat function to start the CLI

getchat()
"""
