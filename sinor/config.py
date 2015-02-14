import toml


def load_toml_file():
    try:
        return toml.load('sinor.toml')
    except IOError:
        print("Could not load sinor.toml file, expect a rough ride from here on")


def blog_url():
    return config['blog']['url']


def feed_url():
    return blog_url() + feed_path()


def feed_path():
    return config['feed']['path']


def blog_title():
    return config['blog']['title']


def blog_date_format():
    return config['blog']['date_format']


def feed_title():
    try:
        return config['feed']['title']
    except (KeyError, TypeError):
        return blog_title()


def feed_subtitle():
    try:
        return config['feed']['subtitle']
    except KeyError:
        return blog_subtitle()


def blog_subtitle():
    return config['blog']['subtitle']


def author():
    return config['blog']['author']


def posts_base_path():
    return config['posts']['base_path']


def build_output_dir():
    return config['build']['output_dir']


def build_partials_dir():
    return config['build']['partials_dir']


config = load_toml_file()
