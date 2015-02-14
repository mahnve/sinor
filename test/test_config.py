from nose.tools import assert_equals
import sinor.config
from mock import Mock


def test_empty_feed_title():
    sinor.config.blog_title = Mock(return_value="foo")
    assert_equals(sinor.config.feed_title(), 'foo')


def test_empty_partials_dir():
    sinor.config.config={'build': {}}
    assert_equals(sinor.config.build_partials_dir(), '')
