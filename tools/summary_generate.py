import os
import re

def parse_md_file(filepath):
    """Extracts problem number and title from the first line of a markdown file."""
    try:
        with open(filepath, 'r') as f:
            first_line = f.readline().strip()
            # Match "# Number. Title"
            match = re.match(r"^#\s*(\d+)\.\s*(.*)", first_line)
            if match:
                return match.group(1), match.group(2)
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
    return None, None

def generate_summary():
    python_dir = "python"
    if not os.path.exists(python_dir):
        print("Python directory not found.")
        return

    problems = []
    for filename in os.listdir(python_dir):
        if filename.endswith(".md") and filename != "template.md":
            filepath = os.path.join(python_dir, filename)
            num, title = parse_md_file(filepath)
            if num and title:
                problems.append({
                    "number": int(num),
                    "title": title,
                    "filename": filename,
                    "path": f"python/{filename}"
                })

    # Sort problems by number
    problems.sort(key=lambda x: x["number"])

    # Build the table
    table = [
        "## Solved Problems",
        "",
        "| # | Title | Solution |",
        "|---|-------|----------|"
    ]
    for p in problems:
        table.append(f"| {p['number']} | {p['title']} | [Solution]({p['path']}) |")
    
    return "\n".join(table)

def update_readme(summary_table):
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print("README.md not found.")
        return

    with open(readme_path, 'r') as f:
        content = f.read()

    # Look for the Solved Problems section or insert before Good Starting Points
    section_marker = "## Solved Problems"
    end_marker = "## Good Starting Points"
    
    if section_marker in content:
        # Replace existing section
        pattern = re.compile(rf"{section_marker}.*?(?={end_marker})", re.DOTALL)
        new_content = pattern.sub(summary_table + "\n\n", content)
    else:
        # Insert before Good Starting Points
        new_content = content.replace(end_marker, summary_table + "\n\n" + end_marker)

    with open(readme_path, 'w') as f:
        f.write(new_content)
    print("README.md updated with solved problems table.")

def check_files():
    """Identifies files that don't match the expected naming or header format."""
    python_dir = "python"
    if not os.path.exists(python_dir):
        return

    print("Checking files in 'python/' for consistency...")
    issues = 0
    for filename in os.listdir(python_dir):
        if not filename.endswith(".md") or filename in ["template.md", "README.md"]:
            continue
        
        # Check filename format NNNN.description.md
        if not re.match(r"^\d{4}\..*\.md$", filename):
            print(f"  [Filename] {filename} does not match NNNN.description.md")
            issues += 1
            
        # Check header format # Number. Title
        filepath = os.path.join(python_dir, filename)
        num, title = parse_md_file(filepath)
        if not num or not title:
            print(f"  [Header]   {filename} has missing or invalid '# Number. Title' header")
            issues += 1
            
    if issues == 0:
        print("All files look good!")
    else:
        print(f"Found {issues} consistency issues.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--check":
        check_files()
    else:
        table = generate_summary()
        if table:
            update_readme(table)
