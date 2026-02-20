import sys
import os
import re

def load_settings():
    settings = {}
    
    with open("settings.py", "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(r'(\w+)\s*=\s*"?(.*?)"?$', line.strip())
            if match:
                key, value = match.groups()
                settings[key] = value

    return settings


def myCvRender():
    if len(sys.argv) != 2:
        print("Usage: python render.py <template_file>")
        return
    if not sys.argv[1].endswith(".template"):
        print("Error: The file must have a .template extension")
        return
    if not os.path.isfile(sys.argv[1]):
        print("Error: The specified file does not exist")
        return
    
    template_file = sys.argv[1]

    with open(template_file, 'r', encoding='utf-8') as file:
        template_content = file.read()
    settings = load_settings()
    rendered_content = template_content.format(
        firstname=settings["firstname"],  
        lastname=settings["lastname"],    
        age=settings["age"],             
        profession=settings["profession"]
    )
    
    output_file = "myCV.html"
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(rendered_content)
    
    print(f"CV successfully created: {output_file}")
    
   

if __name__ == "__main__":
    myCvRender() 