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
            tags = line.replace("tags: ", "")
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
        return frontmatter, content[1:]
    else:
        return frontmatter, content


def remove_slide_markers(frontmatter, contents):
    contents = re.sub(r"\s---\s", "\n", contents)
    return frontmatter, contents


def img_src_absolute(frontmatter, contents):
    contents = re.sub(r"!\[(.*?)\]\(Assets/(.*)\)", "![\\1](/Assets/\\2)\n", contents)
    return frontmatter, contents


def wikilink_src_absolute(frontmatter, contents):
    contents = re.sub(r"!\[\[(.*?)[|?](.*?)\]\]", "![\\1](/\\1)\n", contents)
    return frontmatter, contents


def media_html_embeds(frontmatter, contents):
    link_regex = re.compile(r"!\[(.*?)\]\((.*)\)")
    for m in re.finditer(link_regex, contents):
        if m and "webm" in m.group(2):
            original = contents[m.start() : m.end()]
            audio_tag = f"""<audio controls src="{m.group(2)}"><a href="{m.group(2)}"> Download audio </a></audio>"""
            contents = contents.replace(
                original,
                audio_tag,
            )
    return frontmatter, contents


def youtube_embeds(frontmatter, contents):
    link_regex = re.compile(r"\[(.*?)\]\(https:\/\/.*?\/watch\?v=(.*)\)")
    for m in re.finditer(link_regex, contents):
        if m:
            original = contents[m.start() : m.end()]
            yt_tag = f"""<iframe width="560" height="315" src="https://www.youtube.com/embed/{m.group(2)}"  frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""
            contents = contents.replace(
                original,
                yt_tag,
            )
    return frontmatter, contents


def clean_excalidraw_editlinks(frontmatter, contents):
    contents = re.sub(r"^\%\%(.*)$", "", contents, 0, re.MULTILINE)
    return frontmatter, contents
