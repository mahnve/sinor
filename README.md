# Sinor

[![Circle CI](https://circleci.com/gh/mahnve/sinor.svg?style=svg)](https://circleci.com/gh/mahnve/sinor)

Sinor is a simple tool to convert blog content for static websites
written in Python. It can

1. Convert Markdown formatted posts into HTML using Mustache templates.
2. Generate Atom feeds from HTML files
3. Generate link archives from HTML files
4. Convert mustache files to HTML

I wrote Sinor o scratch my own itch as to how I want my own blog to
be built. In general, I have found other tools quite intrusive and
doing too much. Sinor is in itself not enough to build a static
website. You will need a build tool to automate things, I suggest
make.

Sinor does not have any preference on how you organize your
posts, if you use a CSS generation framework or where you should put
static content, should you have it.

## Installation

### Stable

TODO

### Get the latest

```shell
pip install git+git://github.com/mahnve/sinor.git
```

## Convert a Markdown post

```shell
sinor --type single --template template.mustache input.markdown > output.html
```

### Metadata

Sinor expects a few metadata fields in every Markdown file:

* ```date``` - the date the post is published.
* ```title``` - the title of the post.
* ```draft``` (optional) - whether or not the post is to be rendered

#### Example

```Markdown
date: 2014-01-10
title: Agile Smurfing
---

A really good blog post ...
```

### Templates and Metadata

Sinor uses Mustache for templating.

In addition to post data described earlier, Mustache templates are passed a hash of blog metadata:

* ```year``` - The current year
* ```author``` - The blog.author from the ```sinor.toml``` file
* ```blog_title``` - the blog.title from the ```sinor.toml``` file

Example template for single post page:

```mustache
<div class='item-details'>
  <h1 id="post-title" class='post-title'>{{title}}</h1>
  <h2 class='post-info'><time id="post-date">{{date}}</time></h2>
</div>
<div id="post-content" class='item-content'>
  {{{content}}}
</div>
```

## Convert html files to atom feed
```shell
sinor --type feed html1.html html2.html > atom.xml
```

Sinor generates atom feeds from HTML files. In order to extract metadata from the HTML some id's must be declared:

* ```post-date```
* ```post-title```
* ```post-content```

### Example HTML file that can be parsed to atom feed

```html
<header>
  <h1 id="post-title" class='post-title'>Agile Smurfing</h1>
  <h2 class='post-info'><time id="post-date">2014-01-10</time></h2>
</header>
<article id="post-content">
  <p>Recently ... </p
</article>
```

## Convert html files to archive
```
sinor --type archive --template template.mustache html1.html html2.html > output.html
```

Sinor generates archive files just like it does atom feeds - by parsing HTML. The same id's must be declared etc.

### Example template for archive post page:

```Mustache
<ol>
  {{#posts}}
    <li>
      <date>{{date}}</date>
      <a href="{{relative_url}}">{{title}}</a>
    </li>
  {{/posts}}
</ol>
```

## Convert Mustache files

Sinor can convert Mustache files into HTML - and passes the standard metadata described above into the templates.


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
