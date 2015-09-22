from sinor import markdown_content
from datetime import date
from nose.tools import assert_equals


def test_gets_title():
    assert_equals(markdown_content.from_string(
        "title: hej \n date: 2014-10-01 \n\n Hej")['title'],
        "hej")


def test_gets_date():
    assert_equals(markdown_content.from_string(
        "title: hej \n date: 2014-10-01 \n\n Hej")['date'],
        "2014-10-01")


def test_gets_render_time_date():
    assert_equals(
        markdown_content.from_string(
            "title: hej \n date: date-rendered \n\n Hej")['date'],
        date.today().strftime('%Y-%m-%d'))


def test_gets_content():
    assert_equals(markdown_content.from_string(
        "title: hej \n date: 2014-10-01 \n\n Hej")['content'],
        "<p>Hej</p>")


def test_gets_draft():
    assert_equals(markdown_content.from_string(
        "title: hej \n date: 2014-10-01 \ntags: foo\n      bar\ndraft: true\n\n Hej")['status'],
        "draft")


def test_gets_tags():
    assert_equals(markdown_content.from_string(
        "title: hej\ndate: 2014-10-01\ntags: foo\n      bar\ndraft: true")['tags'],
        ['foo', 'bar'])


def test_gets_og_image():
    assert_equals(markdown_content.from_string(
        "title: hej\ndate: 2014-10-01\nog_image: /foo.png", 'http://foo.com')['og_image'],
        "http://foo.com/foo.png"
    )


def test_og_image_with_full_url():
    assert_equals(markdown_content.from_string(
        "title: hej\ndate: 2014-10-01\nog_image: http://foo.com/foo.png", 'http://foo.com')['og_image'],
        "http://foo.com/foo.png"
    )
