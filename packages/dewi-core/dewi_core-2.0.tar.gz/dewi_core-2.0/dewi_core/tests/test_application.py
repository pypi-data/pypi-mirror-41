# Copyright 2015-2018 Laszlo Attila Toth
# Distributed under the terms of the GNU Lesser General Public License v3

import argparse

import dewi_core.testcase
from dewi_core.application import MainApplication
from dewi_core.command import Command
from dewi_core.context_managers import redirect_outputs
from dewi_core.loader.context import Context
from dewi_core.loader.loader import PluginLoader


class FakeCommand(Command):
    name = 'fake'
    description = 'A fake command for tests'
    arguments = None

    def __init__(self):
        FakeCommand.arguments = None

    def register_arguments(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument('arguments', nargs='*')

    def run(self, args: argparse.Namespace) -> int:
        arguments = args.arguments

        if arguments and arguments[0] == 'ERROR':
            raise RuntimeError("Fake Command Error")

        FakeCommand.arguments = list(arguments)
        return 42


class FakePluginLoader(PluginLoader):
    def __init__(self, command):
        # super() is not wanted to call here, its interface is overridden
        self.loaded = []
        self.command = command

    def load(self, plugins):
        context = Context()

        self.loaded.extend(plugins)

        context.commands.register_class(self.command)

        return context


class TestMainApplication(dewi_core.testcase.TestCase):
    def set_up(self):
        self.command = FakeCommand()
        self.loader = FakePluginLoader(FakeCommand)
        self.application = MainApplication(self.loader, 'myprogram')

    def _invoke_application(self, args, *, expected_exit_value=1):
        with self.assert_raises(SystemExit) as context:
            self.application.run(args)

        self.assert_equal(expected_exit_value, context.exception.code)

    def _invoke_application_redirected(self, *args, **kwargs):
        with redirect_outputs() as redirection:
            self._invoke_application(*args, **kwargs)

        return redirection

    def test_help_option(self):
        redirect = self._invoke_application_redirected(['-h'], expected_exit_value=0)
        self.assert_in('myprogram [options] [command [command-args]]', redirect.stdout.getvalue())
        self.assert_equal('', redirect.stderr.getvalue())

        self.assert_equal(set(), set(self.loader.loaded))

    def test_loading_plugins_requires_a_command_to_run(self):
        redirect = self._invoke_application_redirected(['-p', 'test'], expected_exit_value=None)
        self.assert_equal('', redirect.stderr.getvalue())
        self.assert_in('Available Myprogram Commands.\n', redirect.stdout.getvalue())

        self.assert_equal({'test'}, set(self.loader.loaded))

    def test_command_run_method_is_called(self):
        redirect = self._invoke_application_redirected(
            ['-p', 'test', 'fake', 'something', 'another'],
            expected_exit_value=42)
        self.assert_equal('', redirect.stdout.getvalue())
        self.assert_equal('', redirect.stderr.getvalue())
        self.assert_equal(['something', 'another'], FakeCommand.arguments)
        self.assert_equal({'test'}, set(self.loader.loaded))

    def test_command_run_method_exception_is_handled(self):
        redirect = self._invoke_application_redirected(
            ['-p', 'test', 'fake', 'ERROR'],
            expected_exit_value=1)
        self.assert_equal('', redirect.stdout.getvalue())
        self.assert_in('Fake Command Error', redirect.stderr.getvalue())

    def test_unknown_command(self):
        """
        Test that the output is something like the following,
        without checking the exact space character count between the command name (fake)
        and the description (- A fake command for tests).

        ---8<---
        ERROR: The command 'unknown-name' is not known.

        Available commands and aliases:
        fake                             - A fake command for tests
        --->8---
        """

        redirect = self._invoke_application_redirected(
            ['-p', 'test', 'unknown-name'],
            expected_exit_value=1)
        self.assert_equal('', redirect.stderr.getvalue())

        output = redirect.stdout.getvalue()
        self.assert_in("ERROR: The command 'unknown-name' is not known.\n", output)
        self.assert_in("Similar names - firstly based on command name length:\n", output)
        self.assert_in(" list-all ", output)

    def test_run_help_of_command(self):
        redirect = self._invoke_application_redirected(
            ['-p', 'test', 'fake', '-h'],
            expected_exit_value=0)
        self.assert_in('myprogram fake [-h]', redirect.stdout.getvalue())
        self.assert_equal('', redirect.stderr.getvalue())
        self.assert_equal({'test'}, set(self.loader.loaded))
