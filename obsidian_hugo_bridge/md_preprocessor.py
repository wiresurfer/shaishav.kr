import re

def remove_slide_markup(frontmatter, content):
    frontmatter = frontmatter.replace("type: 'Blog'", "type: pages")
    frontmatter = frontmatter.replace("type: Blog", "type: pages")
    return frontmatter, content
        
def split_fm_tags(frontmatter, content):
    fm_lines = frontmatter.splitlines()
    fm_out = []
    for line in fm_lines:
        if "tags: " in line:
            tags = line.replace("tags: ","")
            tag_lines = ["tags: "]
            for tag in tags.split(","):
                tag_lines.append(f"  - {tag.strip()}")
            tag_lines = "\n".join(tag_lines)
            fm_out.append(tag_lines)
        else:
            fm_out.append(line)
    return "\n".join(fm_out), content
            
    
def remove_starting_hyphen(frontmatter, content):
    if content.strip().startswith("-"):
        return frontmatter,content[1:]
    else:
        return frontmatter, content

def remove_slide_markers(frontmatter, contents):
    contents = re.sub(r'\s---\s', '\n', contents)
    return frontmatter, contents
