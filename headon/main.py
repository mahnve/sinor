#!/usr/bin/env python

__author__ = 'mahnve'

import feed
import argparse
import posts

if(__name__ == "__main__"):
    parser = argparse.ArgumentParser(description="Parse generator args")
    parser.add_argument("--type",
                        help="'single', 'feed' or 'archive'",
                        default="single")

    parser.add_argument("--template",
                        help="Mustache template file")

    parser.add_argument("markdown_files",
                        nargs='*',
                        help="Markdown file")
    args = parser.parse_args()
    if args.type == 'single':
        print(posts.render_markdown_page(args.markdown_files[0],
                                         args.template).encode('utf_8'))
    else:
        if args.type == 'feed':
            print(feed.render_atom_feed(args.markdown_files).encode('utf_8'))
        else:
            if args.type == 'archive':
                print(posts.render_post_list(args.markdown_files,
                                             args.template).encode('utf_8'))
            else:
                if args.type == 'mustache':
                    print(posts.render_mustache_page(args.template,
                                                     {'year': '2015'}).encode('utf_8'))
