from nose.tools import assert_equals
from sinor import posts
from sinor.config import config
from mock import Mock


def test_draft():
    a = {'a': 1}
    b = {'draft': 1}
    assert_equals(posts.no_drafts([a, b]), [a])


def test_limit_count():
    a = [0, 1, 2, 3, 4, 5]
    assert_equals([0, 1, 2], posts.limit(a, 3))


def test_limit_negative_count():
    a = [0, 1, 2]
    assert_equals(a, posts.limit(a, -1))


def test_default_partial_dir():
    config.build_partials_dir = Mock(return_value='')
    assert_equals(posts.partials_dir("/foo/bar.mustache"), "/foo")


def test_selects_config_partial_dir():
    config.build_partials_dir = Mock(return_value="/bar")
    assert_equals(posts.partials_dir("/foo/bar.mustache"), "/bar")
