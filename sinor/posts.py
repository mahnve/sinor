from sinor import markdown_content, html_content, file_util
from datetime import date, datetime
import pystache
from sinor.config import config
from os.path import dirname
from pyatom import AtomFeed
from sinor.html_content import from_file
import sys


def render_atom_feed(files):
    feed = AtomFeed(title=config.feed_title(),
                    subtitle=config.feed_subtitle(),
                    feed_url=config.feed_url(),
                    author=config.author(),
                    url=config.feed_url())

    posts = map(from_file, files)
    for post in no_drafts(sorted_posts(posts)):
        try:
            feed.add(title=post['title'],
                     content=post['content'],
                     author=config.author(),
                     url=post['absolute_url'],
                     updated=datetime.strptime(post['date'],
                                               config.blog_date_format()).date())
        except:
            print('Failed adding post {} to feed'.format(post))
            sys.exit(-1)

    return feed.to_string()


def render_post_list(file_names, template, count):
    posts = limit(
        no_drafts(
            sorted_posts(map(html_content.from_file, file_names))), count)
    return render_mustache_page(template, {'posts': posts})


def render_markdown_page(input_file, template_file):
    content = markdown_content.from_file(input_file)
    return render_mustache_page(template_file, content)


def render_mustache_page(template, content={}):
    template = file_util.read_file(template)
    mustache_renderer = pystache.Renderer(search_dirs=partials_dir(template),
                                          file_encoding="utf8")
    return mustache_renderer.render(template, common_data(content))


def sorted_posts(posts):
    return sorted(posts,
                  key=lambda post: post['date'], reverse=True)


def limit(list, count=0):
    if(count < 1):
        count = len(list)
    return list[:count]


def no_drafts(posts):
    return filter(is_not_draft, posts)


def is_not_draft(post):
    if 'status' in post:
        return post['status'] != 'draft'
    else:
        return True


def common_data(to_merge={}):
    return dict({'year': date.today().year,
                 'author': config.author(),
                 'blog_title': config.blog_title()},
                **to_merge)


def partials_dir(file_name):
    if config.build_partials_dir() is '':
        return dirname(file_name)
    else:
        return config.build_partials_dir()
