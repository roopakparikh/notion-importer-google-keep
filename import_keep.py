#!/usr/bin/env python
from notion.client import NotionClient
from notion.block import EmbedOrUploadBlock,PageBlock
from parse_html import get_text
from md2notion.upload import upload
import argparse

import os

def import_data(token_v2, parent_page, keep_dir):
    # Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
    client = NotionClient(token_v2)

    page = client.get_block(parent_page)
    print("The parent page  title is:", page.title)
    list_of_files = []
    for (dirpath, dirnames, filenames) in os.walk(keep_dir):
        for filename in filenames:
            if filename.endswith('.html'): 
                list_of_files.append( os.sep.join([dirpath, filename]))

    for html_file in list_of_files:
        newchild = page.children.add_new(PageBlock, title=os.path.basename(html_file))
        with open(get_text(html_file), "r") as mdFile:
            upload(mdFile, newchild)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Import Google Keep Notes into notion")
    parser.add_argument("--token", help="Notion.so token_v2 cookie value")
    parser.add_argument("--page", help="Url of the page to import Google Keep Notes")
    parser.add_argument("--dir", help="Directory where the exported Keep notes are (in .html format)")
    args = parser.parse_args()
    import_data(args.token, args.page, args.dir)