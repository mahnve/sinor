from nose.tools import assert_equals
from sinor import posts
from sinor.config import config
from mock import Mock
from data_builder import MarkdownPostBuilder


def test_draft():
    draft = MarkdownPostBuilder().with_status('draft').build()
    published = MarkdownPostBuilder().with_status('published').build()
    assert_equals(posts.no_drafts([draft, published]), [published])


def test_limit_count():
    a = b = c = d = MarkdownPostBuilder().build()
    plist = [a, b, c, d]
    assert_equals([a, b], posts.limit(plist, 2))


def test_limit_negative_count():
    a = b = c = d = MarkdownPostBuilder().build()
    post_list = [a, b, c, d]
    assert_equals(post_list, posts.limit(post_list, -1))


def test_default_partial_dir():
    config.build_partials_dir = Mock(return_value='')
    assert_equals(posts.partials_dir("/foo/bar.mustache"), "/foo")


def test_selects_config_partial_dir():
    config.build_partials_dir = Mock(return_value="/bar")
    assert_equals(posts.partials_dir("/foo/bar.mustache"), "/bar")


def test_build_tags_list():
    a = {'tags': ['foo', 'bar'], 'relative_url': '/url-1'}
    b = {'tags': ['foo'], 'relative_url': '/url-2'}

    assert_equals(posts.build_tag_tree([a, b]),
                  {'foo': ['/url-1', '/url-2'], 'bar': ['/url-1']})
