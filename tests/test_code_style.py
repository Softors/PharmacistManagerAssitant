import pycodestyle


def test_code_style():
    style = pycodestyle.StyleGuide(config_file='setup.cfg')
    result = style.check_files(['pma', 'tests'])
    assert result.total_errors == 0
