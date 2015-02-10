import markdown
import file_util


def single_meta_data_value(dictionary, key):
    value_list = dictionary.get(key, [''])
    return value_list[0]


def from_file(content_file):
    content = file_util.read_file(content_file)
    return from_string(content)


def from_string(content):
    md_converter = markdown.Markdown(extensions=['codehilite', 'meta'])
    html = md_converter.convert(content)

    meta_data = md_converter.Meta

    return {'content': html,
            'title': single_meta_data_value(meta_data, 'title'),
            'draft': single_meta_data_value(meta_data, 'draft'),
            'date': single_meta_data_value(meta_data, 'date')}
