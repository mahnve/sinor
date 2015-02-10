from nose.tools import assert_equals
import headon.posts


def test_draft():
    a = {'a': 1}
    b = {'draft': 1}
    assert_equals(headon.posts.no_drafts([a, b]), [a])
