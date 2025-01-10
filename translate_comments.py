import os
import re
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Define the directory to scan
directory = "."

# Define a function to detect Chinese characters
def contains_chinese(text):
    return re.search(r'[\u4e00-\u9fff]', text)

# Define a function to translate text
def translate_text(text):
    try:
        translated = translator.translate(text, src='zh-cn', dest='en')
        return translated.text
    except Exception as e:
        print(f"Error translating text: {e}")
        return text

# Walk through the directory
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            # Translate comments
            new_lines = []
            for line in lines:
                if contains_chinese(line):
                    comment_match = re.match(r'(\s*#\s*)(.*)', line)
                    if comment_match:
                        comment_prefix = comment_match.group(1)
                        comment_text = comment_match.group(2)
                        translated_text = translate_text(comment_text)
                        new_lines.append(f"{comment_prefix}{translated_text}\n")
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)

            # Write the translated comments back to the file
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)

print("Translation complete.")