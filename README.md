# Sinor

[![Circle CI](https://circleci.com/gh/mahnve/sinor.svg?style=svg)](https://circleci.com/gh/mahnve/sinor)

Sinor is a simple tool to convert blog content for static websites
written in Python. It can:

* Convert Markdown formatted posts into HTML using Mustache templates.
* Generate Atom feeds from HTML files
* Generate link archives from HTML files
* Convert mustache files to html

Sinor is built to scratch my own itch as to how I want my own blog to
be built. In general, I have found other tools quite intrusive and
doing too much. Sinor is not enough in itself to build a static
website. You will need a build tool to automate things, I suggest
make.

Sinor does not have any preference on how you organize your
posts, if you use a CSS generation framework or where you should put
static content, should you have it.

## Quickstart

### Convert a Markdown post
```shell
sinor --type single --template template.mustache input.markdown > output.html
```

### Convert html files to atom feed
```shell
sinor --type feed html1.html html2.html > atom.xml
```

### Convert html files to archive
```
sinor --type archive --template template.mustache html1.html html2.html > output.html
```

## sinor.toml Config

sinor expects a ```sinor.toml``` file in the directory from which
sinor is called.


Example file: (All fields are mandatory as of now)

```toml
[blog]
url="http://www.foo.org"
author="Foo Bar"
title="The Title"
subtitle="A truly astounding blog"
date_format="%Y-%m-%d"

[build]
output_dir="build"
templates_dir="site_src/templates"

[posts]
base_path="/blog"

[feed]
path="/blog/feed"
```

## Markdown and Metadata

Sinor expects a few metadata fields in every Markdown file:

* ```date``` - the date the post is published. 
* ```title``` - the title of the post. 
* ```draft``` (optional) - whether or not the post is to be rendered

When rendering a archive, these are wrapped in a list called ```posts```

## Templates and Metadata

In addition to post data, Mustache templates are passed a hash of blog metadata:

* ```year``` - The current year
* ```author``` - The blog.author from the ```sinor.toml``` file
* ```blog_title``` - the blog.title from the ```sinor.toml``` file


## Using a Makefile

I personally use a Makefile to generate my blog. In fact, I created
Sinors API by writing the Makefile as I wanted it to look, and then
implemented Sinor to fullfill that API.

Example Makefile usage:

```Makefile
POST_SRC_FILES = $(shell find site_src/blog -type f -name '*.markdown')
POST_BUILD_FILES = $(patsubst site_src/blog/%.markdown, $(BUILD_DIR)/blog/%.html, $(POST_SRC_FILES))
TEMPLATE_FILES = $(shell find site_src/templates -iname "*.mustache")
$(BUILD_DIR)/blog/%.html: site_src/blog/%.markdown $(TEMPLATE_FILES)
	@mkdir -p "$(@D)"
	sinor --type single --template site_src/templates/blog.mustache $< > $@
```

## Future Development

Adding other formats than Markdown is quite easy as long as they
support metadata. 
