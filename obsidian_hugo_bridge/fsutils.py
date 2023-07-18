import os
import shutil
import time
import glob

def read_md(content):
    frontmatter = []
    body= content
    if content.strip().startswith("---"):
        lines = content.splitlines()
        frontmatter = ["---"]
        idx = 0
        for line in lines[1:]:
            idx = idx+1
            if line == "---":
                frontmatter.append(line)
                break
            else:
                frontmatter.append(line)
        body = "\n".join(lines[idx+1:])
    
    frontmatter = "\n".join(frontmatter)
    return frontmatter, body

def all_files(folder, extention="*"):
    files = list(glob.glob(f'{folder}\\**\\*.{extention}', recursive=True))
    files += list(glob.glob(f'{folder}\\*.{extention}'))
    result = []
    for file in files:
        if os.path.isfile(file):
            result.append(file)
    return result
    return result

def move_file(src, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copy(src, dest)
    
def mutate_file(input_file, func_transforms):
    #read input file
    fin = open(input_file, "rt", encoding="utf-8")
    data = fin.read()
    frontmatter, content = read_md(data)
    for func in func_transforms:
        frontmatter, content = func(frontmatter, content)
    fin.close()
    fin = open(input_file, "wt", encoding="utf-8")
    data = "\n".join([frontmatter, content])
    fin.write(data)
    fin.close()


def cleandir(folder):
    shutil.rmtree(folder, ignore_errors=True)
    time.sleep(0.5)
    os.makedirs(folder, exist_ok=True)
    