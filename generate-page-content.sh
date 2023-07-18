# rm -rf /home/tempuser/Desktop/wiresurfer.github.io/content/pages
# logseq-export --graphPath /home/tempuser/Desktop/notes/ -blogFolder /home/tempuser/Desktop/wiresurfer.github.io/content/pages/  --assetsRelativePath ../static  --webAssetsPathPrefix /static --unquotedProperties 'date,categories,tags,ShowToc,TocOpen'
pandoc --resource-path="C:\Users\admin\OneDrive\obsidian-notes\Notes\Work\OKS"  ^
--resource-path="C:\Users\admin\OneDrive\obsidian-notes\Assets\media" ^
--lua-filter="C:\Users\admin\OneDrive\obsidian-notes\.obsidian\plugins\obsidian-enhancing-export\lua\markdown+hugo.lua"  ^
-s -o C:\Users\admin\Desktop\development\wiresurfer.github.io\content\pages\OKS KT Session.md ^
-t commonmark_x-attributes  ^
"C:\Users\admin\OneDrive\obsidian-notes\Notes\Work\OKS\OKS KT Session.md"