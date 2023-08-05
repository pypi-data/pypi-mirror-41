"""
Pytest-dash plugin
------------------
Main entry point for pytest

- Hooks definitions
- Plugin config container
- Plugin selenium driver
- Fixtures imports
"""
import pytest

from selenium import webdriver

from pytest_dash.behaviors import DashBehaviorTestFile
from pytest_dash.errors import InvalidDriverError
from pytest_dash.application_runners import DashThreaded, DashSubprocess

_driver_map = {
    'Chrome': webdriver.Chrome,
    'Firefox': webdriver.Firefox,
    'Remote': webdriver.Remote,
    'Safari': webdriver.Safari,
    'Opera': webdriver.Opera,
    'PhantomJS': webdriver.PhantomJS,
    'Edge': webdriver.Edge,
    'Ie': webdriver.Ie,
}


def _create_config(parser, key, _help=None):
    # Create an option for pytest command line and ini
    parser.addoption('--{}'.format(key), help=_help)
    parser.addini(key, help=_help)


def _get_config(config, key, default=None):
    opt = config.getoption(key)
    ini = config.getini(key)
    return opt or ini or default


###############################################################################
# Plugin hooks.
###############################################################################


# pylint: disable=missing-docstring
def pytest_addoption(parser):
    # Add options to the pytest parser, either on the commandline or ini
    # TODO add more options for the selenium driver.
    _create_config(parser, 'webdriver', 'Name of the selenium driver to use')


# pylint: disable=too-few-public-methods
class DashPlugin(object):
    """Global plugin configuration and driver container"""

    def __init__(self):
        self.driver = None
        self.config = None
        self.behaviors = {}

    # pylint: disable=missing-docstring
    def pytest_configure(self, config):
        self.config = config
        # Called once before the tests are run
        # Get and configure global objects for the plugin to use.
        # TODO get all the options and map a global dict.
        driver_name = _get_config(config, 'webdriver')

        if driver_name not in _driver_map:
            raise InvalidDriverError(
                '{} is not a valid webdriver value.\n'
                'Valid drivers {}'.format(driver_name, _driver_map.keys())
            )

        self.driver = _driver_map.get(driver_name)()

        # pylint: disable=invalid-name, no-self-argument
        class _AddBehavior:
            def __init__(
                    s, syntax, kind='value', inline=True, meta=False,
                    tree=False
            ):
                s.syntax = syntax
                s.kind = kind
                s.inline = inline
                s.meta = meta
                s.tree = tree
                s.handler = None

            def __call__(s, fun):
                name = getattr(fun, '__name__')
                s.handler = fun
                self.behaviors[name] = s

        config.hook.pytest_add_behaviors(add_behavior=_AddBehavior)

    # pylint: disable=unused-argument, missing-docstring
    def pytest_unconfigure(self, config):
        # Quit the selenium driver once all tests are cleared.
        self.driver.quit()

    # pylint: disable=inconsistent-return-statements, missing-docstring
    def pytest_collect_file(self, parent, path):
        if path.ext == ".yml" and path.basename.startswith("test"):
            return DashBehaviorTestFile(path, parent, self)


_plugin = DashPlugin()


@pytest.mark.tryfirst
def pytest_addhooks(pluginmanager):
    # https://github.com/pytest-dev/pytest-xdist/blob/974bd566c599dc6a9ea291838c6f226197208b46/xdist/plugin.py#L67
    # avoid warnings with pytest-2.8
    from pytest_dash import new_hooks
    method = getattr(pluginmanager, "add_hookspecs", None)
    if method is None:
        method = pluginmanager.addhooks
    method(new_hooks)


@pytest.mark.tryfirst
def pytest_configure(config):
    config.pluginmanager.register(_plugin)


###############################################################################
# Fixtures
###############################################################################


@pytest.fixture
def dash_threaded():
    """
    Start a local dash server in a new thread. Stop the server in teardown.

    :return:
    """

    with DashThreaded(_plugin.driver) as starter:
        yield starter


@pytest.fixture
def dash_subprocess():
    """
    Start a Dash server with subprocess.Popen and waitress-serve.
    No instance is returned from this fixture.

    :return:
    """
    with DashSubprocess(_plugin.driver) as starter:
        yield starter
