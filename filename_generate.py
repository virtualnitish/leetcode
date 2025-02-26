def convert_title(title):
    parts = title.split(". ", 1)
    if len(parts) != 2:
        raise ValueError("Invalid title format. Expected format is 'number. title'")
    
    number = parts[0].zfill(4)
    text = parts[1].strip().lower().replace(" ", "_")
    filename = f"{number}.{text}.md"
    return filename

if __name__ == "__main__":
    print("Enter the title to convert (or type 'exit' to quit)")
    print("Sample input: 1. Two Sum", end="\n\n")
    while True:
        try:
            title = input("Title: ")
            if title.lower() == 'exit':
                break
            
            filename = convert_title(title)
            print(f"{filename}",end="\n\n")
        
        except ValueError as e:
            print(e)
