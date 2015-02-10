from nose.tools import assert_equals
import headon.config
from mock import Mock


def test_empty_feed_title():
    headon.config.blog_title = Mock(return_value="foo")
    assert_equals(headon.config.feed_title(), 'foo')
