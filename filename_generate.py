import subprocess
import shutil

def check_copyq():
    return shutil.which("copyq") is not None

def convert_title(title):
    parts = title.split(". ", 1)
    if len(parts) != 2:
        raise ValueError("Invalid title format. Expected format is 'number. title'")
    
    number = parts[0].zfill(4)
    text = parts[1].strip().lower().replace(" ", "_")
    filename = f"{number}.{text}.md"
    return filename

def copy_to_clipboard(text):
    try:
        subprocess.run(["copyq", "add", text], check=True)
        print("Filename copied to clipboard.",end="\n\n")
    except subprocess.CalledProcessError:
        print("Failed to copy to clipboard. Make sure CopyQ is running.")

if __name__ == "__main__":
    if not check_copyq():
        print("CopyQ is not installed on your machine. Please install CopyQ to use clipboard functionality.")
        exit(1)
    
    print("Enter the title to convert (or type 'exit' to quit)")
    print("Sample input: 1. Two Sum", end="\n\n")
    while True:
        try:
            title = input("Title: ")
            if title.lower() == 'exit':
                break
            
            filename = convert_title(title)
            print(f"{filename}", end="\n")
            copy_to_clipboard(filename)
        
        except ValueError as e:
            print(e)
