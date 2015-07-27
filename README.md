# Sinor

[![Circle CI](https://circleci.com/gh/mahnve/sinor.svg?style=svg)](https://circleci.com/gh/mahnve/sinor)

Sinor is a simple tool to convert blog content for static websites
written in Python. It can

1. Convert Markdown formatted posts into HTML using Mustache templates.
2. Generate Atom feeds from HTML files
3. Generate link archives from HTML files
4. Convert mustache files to HTML

I wrote Sinor to scratch my own itch as to how I want my own blog to
be built. In general, I have found other tools quite intrusive and
doing too much. Sinor is in itself not enough to build a static
website. You will need a build tool to automate things, I suggest
make.

Sinor does not have any preference on how you organize your
posts, if you use a CSS generation framework or where you should put
static content, should you have it.

## Installation

### Stable

```shell
pip install sinor
```

### Get the latest

```shell
pip install git+git://github.com/mahnve/sinor.git
```

## Convert a Markdown post

Syntax:

```shell
sinor single --template template.mustache --markdown_content input.markdown > output.html
```

### Metadata

Sinor expects a few metadata fields in every Markdown file:

* ```date``` - the date the post is published. It can also be set to
  'date-rendered' which sets it to the date the page is rendered.
* ```title``` - the title of the post.
* ```draft``` (optional) - whether or not the post is to be rendered

Example:

```Markdown
date: 2014-01-01
title: A Great Post
---

A really good blog post ...
```

### Templates and Metadata

Sinor uses Mustache for templating.

In addition to post data described earlier, Mustache templates are passed a map of blog meta data:

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

## Convert HTML files to atom feed

Syntax:

```shell
sinor feed --html_content html1.html html2.html > atom.xml
```

Sinor generates atom feeds from HTML files. In order to extract meta data from
the HTML some id's must be declared:

* ```post-date```
* ```post-title```
* ```post-content```

URL's are generated from the filepath, using ```blog.url``` and
```build.output_dir``` from the config file.

Example HTML file that can be parsed to atom feed

```html
<header>
  <h1 id="post-title" class='post-title'>Agile Smurfing</h1>
  <h2 class='post-info'><time id="post-date">2014-01-10</time></h2>
</header>
<article id="post-content">
  <p>Recently ... </p
</article>
```

## Convert HTML files to archive

Syntax:

```
sinor archive --limit 5 --template template.mustache --html_content html1.html html2.html > output.html
```

Sinor generates archive files just like it does atom feeds - by parsing
HTML. The same id's must be declared etc. URL's are generated the same way to.

The mustache template is given a map named ```posts``` which is used to generate
the output.

Example template for archive post page:

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

### Tags

Sinor parses tags and provides them to the template along with the posts. Tags
should be available in a list with the id "post-tags", with text content
somewhere in the ```li```'s

Example

```HTML
<ol id="post-tags">
  <li><a href="/tags.html#foo">foo</a></li>
</ol>
```

The resulting tag datastructure looks like this:

```Python
[
  {'name': 'foo', 'posts': [ ... list of posts tagged with foo ... ]}
  {'name': 'bar', 'posts': [ ... list of posts tagged with bar ... ]}
]
```

which is available to a mustache template and can be used like this:

```Mustache
<dl class='vertical-list'>
  {{#tags}}
    <dt id="{{name}}">
      {{name}}
    </dt>
    {{#posts}}
      <dd>
        <date>{{date}}</date>
        <a href="{{relative_url}}">{{title}}</a>
      </dd>
    {{/posts}}
  {{/tags}}
</ol>
```

## Convert Mustache files

Sinor can convert Mustache files into HTML - and passes the standard meta data
described above into the templates.

Example:

```shell
sinor mustache --template foo.mustache > out.html
```

## sinor.toml Config

sinor expects a ```sinor.toml``` file in the directory from which
sinor is called.


Example file:

```toml
[blog]
url="http://www.foo.org"
# Top url to site.

author="Foo Bar"
# Name of the author

title="The Title"
# The title of the site

subtitle="A truly astounding blog"
# Subtitle of the site

date_format="%Y-%m-%d"
# How dates are formatted in metadata

[build]
output_dir="build"
# Top level directory for build output. Note that this is
# used for url generation and does not have anything to do
# where files are stored. That is the job of the build system.

partials_dir="site_src/templates/partials"
# Where to find Mustache partials. Optional, will default to same dir
# as template being rendered if not given

[posts]
base_path="/blog"
# Top level path where to find blog files when generating archives and
# feeds

[feed]
path="/blog/feed"
# URL for the feed file.
```


## Using a Makefile

I personally use a Makefile to generate my blog. In fact, I created
Sinors API by writing the Makefile as I wanted it to look, and then
implemented Sinor to full fill that API.

Example Makefile usage:

```Makefile
POST_SRC_FILES = $(shell find site_src/blog -type f -name '*.markdown')
POST_BUILD_FILES = $(patsubst site_src/blog/%.markdown, $(BUILD_DIR)/blog/%.html, $(POST_SRC_FILES))
TEMPLATE_FILES = $(shell find site_src/templates -iname "*.mustache")
$(BUILD_DIR)/blog/%.html: site_src/blog/%.markdown $(TEMPLATE_FILES)
	@mkdir -p "$(@D)"
    sinor single --template site_src/templates/blog.mustache --markdown_content $< > $@
```

## Future Development

Adding other formats than Markdown is quite easy as long as they
support meta data.
