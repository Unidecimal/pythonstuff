from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from subprocess import check_output
import sys


def _fetch_local_branches():
    shell_result = check_output(["git", "branch"], text=True)
    return [
        branch.strip() for branch in shell_result.split("\n")
        if not branch.startswith("*") and (branch.strip() != "master" or "main")
        ]


def _delete_branch(branch):
    return str(check_output(["git", "branch", "-D", branch], text=True))


def _print_branches():
    for branch in _fetch_local_branches():
        print(branch)


def _parser(args):
    parser = ArgumentParser(
        description = "A skript to purge all your local branches",
        formatter_class=ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("lb", "--list-branches", default=False, action="store_true")



if __name__ == "__main__":
    _print_branches()

# print(delete_branch("mob/applesearchads/handle-old-admin-area"))