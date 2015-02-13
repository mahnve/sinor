from sinor import markdown_content
from nose.tools import assert_equals


def test_gets_title():
    assert_equals(markdown_content.from_string(
        "title: hej \n date: 2014-10-01 \n--- Hej")['title'],
                  "hej")


def test_gets_date():
    assert_equals(markdown_content.from_string(
        "title: hej \n date: 2014-10-01 \n--- Hej")['date'],
                  "2014-10-01")
