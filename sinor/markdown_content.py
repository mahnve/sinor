import markdown
from sinor import file_util, config
from datetime import date


def from_file(content_file):
    content = file_util.read_file(content_file)
    return from_string(content)


def get_date(meta_data):
    set_value = _single_meta_data_value(meta_data, 'date')
    if set_value == 'date-rendered':
        return date.today().strftime("%Y-%m-%d")
    else:
        return set_value


def from_string(content):
    md_converter = markdown.Markdown(extensions=['codehilite', 'meta'])
    html = md_converter.convert(content)

    meta_data = md_converter.Meta

    return {'content': html,
            'title': _single_meta_data_value(meta_data, 'title'),
            'status': _draft_status(meta_data),
            'date': get_date(meta_data),
            'tags': meta_data.get('tags', ['']),
            'og_image': _get_og_image(meta_data)}


def _single_meta_data_value(dictionary, key, default=None):
    value_list = dictionary.get(key, [default])
    if value_list == [None]:
        raise KeyError(
            "Could not find key '{}' in dict '{}'".format(key,
                                                          dictionary))
    return value_list[0]


def _draft_status(meta_data):
    if _single_meta_data_value(meta_data,
                               'draft',
                               'false') in ('true',
                                            'True'):
        return 'draft'
    else:
        return 'published'
