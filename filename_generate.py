import argparse

def convert_title(title):
    # Split the title into the number and the text
    parts = title.split(". ", 1)
    if len(parts) != 2:
        raise ValueError("Invalid title format. Expected format is 'number. title'")
    
    # Get the number and format it as four digits
    number = parts[0].zfill(4)
    
    # Convert the text to lowercase and replace spaces with underscores
    text = parts[1].strip().lower().replace(" ", "_")
    
    # Combine the number and text with the '.md' extension
    filename = f"{number}.{text}.md"
    return filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a title to a filename.")
    parser.add_argument("--title", required=True, help="The title to convert, e.g., '1. Two Sum'")
    
    args = parser.parse_args()
    title = args.title
    
    try:
        filename = convert_title(title)
        print(filename)
    except ValueError as e:
        print(e)
