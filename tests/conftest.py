#Here we have functions that enable configuration of test run, if keyword isn't provided default is used
def pytest_addoption(parser):
    parser.addoption("--keyword", action="store", default="Malvazija")


def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value = metafunc.config.option.keyword
    if 'keyword' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("keyword", [option_value])
