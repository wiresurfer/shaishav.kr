import subprocess 
    
def pandoc(input_file, output_file, obsidian_root, obsidian_asset_folders):
    options = ['pandoc','-s', '-o', output_file]
    for entry in obsidian_asset_folders:
        options += [
            f'--resource-path="{entry}"',    
        ]
    options += [
        '--lua-filter',
        f"{obsidian_root}\\.obsidian\\plugins\\obsidian-enhancing-export\\lua\\markdown+hugo.lua",
        '-t',
        'commonmark_x-attributes',
        input_file
    ] 
    print(options)  # for debugging
    return subprocess.check_call(options)
        