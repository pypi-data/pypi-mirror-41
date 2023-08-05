'''
Created on Feb 14, 2017

@author: nicolas
'''

from __future__ import print_function

from lemoncheesecake.helpers.console import bold
from lemoncheesecake.helpers.text import ensure_single_line_text
from lemoncheesecake.cli.command import Command
from lemoncheesecake.cli.utils import get_suites_from_project
from lemoncheesecake.filter import add_run_filter_cli_args
from lemoncheesecake.project import load_project
from lemoncheesecake.reporting.console import serialize_metadata


class ShowCommand(Command):
    def get_name(self):
        return "show"
    
    def get_description(self):
        return "Show the test tree"
    
    def add_cli_args(self, cli_parser):
        add_run_filter_cli_args(cli_parser)

        group = cli_parser.add_argument_group("Display")
        group.add_argument("--no-metadata", "-i", action="store_true", help="Hide suite and test metadata")
        group.add_argument("--short", "-s", action="store_true", help="Display suite and test names instead of path")
        group.add_argument("--desc-mode", "-d", action="store_true", help="Display suite and test descriptions instead of path")
        group.add_argument("--flat-mode", "-f", action="store_true", help="Enable flat mode: display all test and suite as path without indentation nor prefix")
        self.add_color_cli_args(group)

    def get_padding(self, depth):
        return " " * (depth * self.indent)

    def get_test_label(self, test, suite):
        if self.show_description:
            return ensure_single_line_text(test.description)
        if self.short:
            return test.name
        return test.path

    def get_suite_label(self, suite):
        if self.show_description:
            return ensure_single_line_text(suite.description)
        if self.short:
            return suite.name
        return suite.path

    def show_test(self, test, suite):
        md = serialize_metadata(test) if self.show_metadata else ""
        if self.flat_mode:
            print("%s%s" % (self.get_test_label(test, suite), " (%s)" % md if md else ""))
        else:
            padding = self.get_padding(suite.hierarchy_depth + 1)
            test_label = self.get_test_label(test, suite)
            print("%s- %s%s" % (padding, test_label, " (%s)" % md if md else ""))
        
    def show_suite(self, suite):
        md = serialize_metadata(suite) if self.show_metadata else ""
        if self.flat_mode:
            print("%s%s" % (bold(self.get_suite_label(suite)), " (%s)" % md if md else ""))
        else:
            padding = self.get_padding(suite.hierarchy_depth)
            suite_label = self.get_suite_label(suite)
            print("%s* %s%s" % (padding, bold(suite_label), " (%s)" % md if md else ""))

        for test in suite.get_tests():
            self.show_test(test, suite)

        for sub_suite in suite.get_suites():
            self.show_suite(sub_suite)
    
    def show_suites(self, suites):
        for suite in suites:
            self.show_suite(suite)

    def run_cmd(self, cli_args):
        self.process_color_cli_args(cli_args)

        self.short = cli_args.short
        self.show_description = cli_args.desc_mode
        self.show_metadata = not cli_args.no_metadata
        self.flat_mode = cli_args.flat_mode
        self.indent = 4

        project = load_project()
        suites = get_suites_from_project(project, cli_args)
        
        self.show_suites(suites)
        
        return 0
