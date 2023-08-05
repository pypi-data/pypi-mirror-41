'''
Created on Feb 14, 2017

@author: nicolas
'''

from __future__ import print_function

from lemoncheesecake.helpers.console import print_table, bold
from lemoncheesecake.cli.command import Command
from lemoncheesecake.testtree import flatten_tests
from lemoncheesecake.project import load_project


class FixturesCommand(Command):
    def get_name(self):
        return "fixtures"

    def get_description(self):
        return "Show the fixtures available in the project"

    def add_cli_args(self, cli_parser):
        group = cli_parser.add_argument_group("Display")
        self.add_color_cli_args(group)
        group.add_argument("--verbose", "-v", action="store_true", help="Show extra fixture information")

    def show_fixtures(self, scope, fixtures, used_by_tests, used_by_fixtures, verbose):
        lines = []
        ordered_fixtures = sorted(
            fixtures,
            key=lambda f: used_by_fixtures.get(f.name, 0) + used_by_tests.get(f.name, 0),
            reverse=True
        )
        for fixt in ordered_fixtures:
            lines.append([
                bold(fixt.name), ", ".join(fixt.params or "-"),
                used_by_fixtures.get(fixt.name, 0), used_by_tests.get(fixt.name, 0)
            ])
        print_table("Fixture with scope %s" % bold(scope), ["Fixture", "Dependencies", "Used by fixtures", "Used by tests"], lines)

    def run_cmd(self, cli_args):
        self.process_color_cli_args(cli_args)

        project = load_project()
        suites = project.get_suites()
        fixtures = project.get_fixtures()

        fixtures_by_scope = {}
        for fixt in fixtures:
            if fixt.scope in fixtures_by_scope:
                fixtures_by_scope[fixt.scope].append(fixt)
            else:
                fixtures_by_scope[fixt.scope] = [fixt]

        used_by_tests = {}
        for test in flatten_tests(suites):
            for fixt_name in test.get_fixtures():
                used_by_tests[fixt_name] = used_by_tests.get(fixt_name, 0) + 1

        used_by_fixtures = {}
        for fixt in fixtures:
            for param in fixt.params:
                used_by_fixtures[param] = used_by_fixtures.get(param, 0) + 1

        for scope in "session_prerun", "session", "suite", "test":
            self.show_fixtures(scope, fixtures_by_scope.get(scope, []), used_by_tests, used_by_fixtures, cli_args.verbose)
            print()

        return 0