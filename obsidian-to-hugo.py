import os
import sys
from obsidian_hugo_bridge.fsutils import move_file, mutate_file, cleandir, all_files
import obsidian_hugo_bridge.md_preprocessor as md_preprocessor
from obsidian_hugo_bridge.pandoc import pandoc


def convert_to_hugo(root_dir):
    pass


class ObsidianHugoExporter:
    OBSIDIAN_ROOT = r".\\obsidian-notes"
    OBSIDIAN_CONTENT_ROOT = f"{OBSIDIAN_ROOT}\\Notes\Work"

    OBSIDIAN_ASSET_FOLDERS = [
        f"{OBSIDIAN_ROOT}\\Writing\\Assets",
        # f"{OBSIDIAN_ROOT}\\Assets\\Excalidraw",
        f"{OBSIDIAN_ROOT}\\Assets",
        # f"{OBSIDIAN_ROOT}\\Notes\\Work\\OKS"
    ]

    HUGO_ROOT = r".\\wiresurfer.github.io"
    HUGO_CONTENT_FOLDER = f"{HUGO_ROOT}\\content\\pages"
    HUGO_ASSET_ROOT = f"{HUGO_ROOT}\\assets"

    STAGING_DIR = f"{HUGO_ROOT}\\.build"

    def __init__(self, content_root) -> None:
        assert content_root
        self.OBSIDIAN_CONTENT_ROOT = f"{self.OBSIDIAN_ROOT}{content_root}"
        super().__init__()

    def assets_folder(self):
        return [
            f"{self.OBSIDIAN_CONTENT_ROOT}\\Assets",
        ]

    def start(
        self,
    ):
        print("Moving Assets")
        self.move_assets()
        print(f"Cleaning Staging Dir {self.STAGING_DIR}")
        cleandir(self.STAGING_DIR)
        print(f"Staging Markdown Files to {self.STAGING_DIR}")
        self.get_blog_posts()
        print(f"Cleaning Hugo Content Folder {self.HUGO_CONTENT_FOLDER}")
        cleandir(self.HUGO_CONTENT_FOLDER)
        print(f"Pandoc Converion Starts")
        self.convert_to_hugo()

    def move_assets(self):
        for dir in self.assets_folder():
            for file in all_files(dir):
                src = file
                dir = eval("f'{dir}'")
                dest = file.replace(
                    f"{self.OBSIDIAN_CONTENT_ROOT}\\Assets", self.HUGO_ASSET_ROOT
                )
                print(src, dest)
                move_file(src, dest)

    def get_blog_posts(self):
        print(self.OBSIDIAN_CONTENT_ROOT)
        print(self.STAGING_DIR)
        assert os.path.isdir(self.STAGING_DIR)
        root_dir = self.OBSIDIAN_CONTENT_ROOT

        for name in all_files(self.OBSIDIAN_CONTENT_ROOT, "md"):
            src = name
            dest = name.replace(root_dir, self.STAGING_DIR)
            move_file(src, dest)
        pass

    def convert_to_hugo(self):
        root_dir = self.STAGING_DIR
        output_dir = self.HUGO_CONTENT_FOLDER
        for input_md in all_files(root_dir, "md"):
            if "excalidraw.md" in input_md:
                continue
            filename = os.path.basename(input_md)
            output_md = f"{output_dir}\\{filename}"

            self.preprocess_md(input_md)
            pandoc(input_md, output_md, self.OBSIDIAN_ROOT, self.OBSIDIAN_ASSET_FOLDERS)

    def preprocess_md(self, input_file):
        mutate_file(
            input_file,
            [
                md_preprocessor.remove_slide_markup,
                md_preprocessor.img_src_absolute,
                md_preprocessor.wikilink_src_absolute,
                md_preprocessor.clean_excalidraw_editlinks,
                md_preprocessor.remove_starting_hyphen,
                md_preprocessor.split_fm_tags,
                md_preprocessor.remove_slide_markers,
                md_preprocessor.media_html_embeds,
                md_preprocessor.youtube_embeds,
            ],
        )


ROOT = sys.argv[1] if sys.argv[1] else "\\Writing\\Blog"
converter = ObsidianHugoExporter(content_root=ROOT)
converter.start()
