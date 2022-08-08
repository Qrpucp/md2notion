from socket import SO_RCVBUF
from notion.client import NotionClient
from notion.block import PageBlock
from md2notion_master.upload import upload, convert, uploadBlock
from md2notion_master.NotionPyRenderer import NotionPyRenderer, addLatexExtension
import re

client = NotionClient(
    token_v2="a7b0734a7f2628d6646d749a00d7ebfbe0bbe37df0d4b1babfff5b1a09145d94216396b895a19e13cf5c870c7f7a1bda4c3eacab999d9f87cb0597b0f0e2689d5e2d69a7a23e7028800051e919cb")
page = client.get_block(
    "https://www.notion.so/test2-8a2416f436af4645b44134f7d4b186c4")

file_path = "E:\Lab\PID Control"
file_name = "PID Control"

# enable while network environment is good
enable_pictures = 1

with open(file_path + "\\" + file_name + ".md", "r", encoding="utf-8") as mdFile:

    print("find markdown file.")

    newPage = page.children.add_new(PageBlock, title=file_name)
    markdown_lines = mdFile.readlines()
    new_markdown_lines = markdown_lines.copy()

    interline_latex_flag = 0
    insert_nums = 0

    for index, line in enumerate(markdown_lines):
        # deal with picture may encounter 429 error
        if enable_pictures == 0:
            if "![]" in line:
                del new_markdown_lines[index + insert_nums]
                insert_nums -= 1
        else:
            # typora html image format
            if "<img" in line:
                pic_name = ''.join(re.findall('src="(.*?)"', line))
                del new_markdown_lines[index + insert_nums]
                new_markdown_lines.insert(index, "![](" + pic_name + ")\n")
        # deal with interline latex
        if "$$\n" in line:
            if interline_latex_flag == 0:
                new_markdown_lines.insert(index + insert_nums, '\n')
                insert_nums += 1
                interline_latex_flag = 1
            else:
                new_markdown_lines.insert(index + insert_nums + 1, '\n')
                insert_nums += 1
                interline_latex_flag = 0

    print("uploading...")

    rendered = convert(new_markdown_lines, addLatexExtension(NotionPyRenderer))
    for blockDescriptor in rendered:
        uploadBlock(blockDescriptor, newPage, mdFile.name)

    print("upload completed.")
