import re

def clean_csv(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Step 1: replace commas inside quotes with |
    # Regex finds text between "..."
    def replace_commas(match):
        inner = match.group(1)
        inner = inner.replace(",", "|")
        return f'"{inner}"'

    content = re.sub(r'"([^"]*)"', replace_commas, content)

    # Step 2: remove all double quotes
    content = content.replace('"', '')

    # Write the result
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)


# Usage
clean_csv("movies.csv", "movies_cleaned.csv")
