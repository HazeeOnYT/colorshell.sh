import os

def change_shell_colors(background_color, text_color):
    # Define ANSI color codes
    colors = {
        'black': '0',
        'red': '1',
        'green': '2',
        'yellow': '3',
        'blue': '4',
        'magenta': '5',
        'cyan': '6',
        'white': '7'
    }
    
    # Validate input
    if background_color < 0 or background_color > 7:
        print("Background color should be between 0 and 7.")
        return
    if text_color < 0 or text_color > 7:
        print("Text color should be between 0 and 7.")
        return
    
    # Set ANSI escape sequence for changing shell colors
    bg_code = colors.get('black')
    fg_code = colors.get('white')
    if background_color in colors:
        bg_code = colors.get(background_color)
    if text_color in colors:
        fg_code = colors.get(text_color)
    
    # Construct the command to change shell colors
    command = f"printf '\\033]11;#{bg_code}{fg_code}\\007'"
    
    # Execute the command in shell
    os.system(command)

if __name__ == "__main__":
    # Example usage
    background = int(input("Enter background color (0-7): "))
    text = int(input("Enter text color (0-7): "))
    change_shell_colors(background, text)
