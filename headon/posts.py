import markdown_content
import html_content
import file_util
from datetime import date
import pystache
import config


def render_post_list(file_names, template, count=0):
    posts = no_drafts(sorted_posts(map(html_content.from_file, file_names)))
    if(count > 0):
        posts = posts[:count]
    return render_mustache_page(template, {'posts': posts})


def render_markdown_page(input_file, template_file):
    content = markdown_content.from_file(input_file)
    return render_mustache_page(template_file, content)


def render_mustache_page(template, content):
    template = file_util.read_file(template)
    mustache_renderer = pystache.Renderer(search_dirs=config.build_templates_dir(),
                                          file_encoding="utf8")
    return mustache_renderer.render(template, common_data(content))


def sorted_posts(posts):
    return sorted(posts,
                  key=lambda post: post['date'], reverse=True)


def no_drafts(posts):
    return filter(lambda post: 'draft' not in post, posts)


def common_data(to_merge={}):
    return dict({'year': date.today().year,
                 'author': config.author(),
                 'blog_title': config.blog_title()},
                **to_merge)
