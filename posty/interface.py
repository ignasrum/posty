from argparse import ArgumentParser
from argparse import Action
import sys

from posty import version
from posty.posty import Posty
from posty.verifier import Verifier


def version_info():
    """
    Returns string containing version information.

    Returns
    -------
    message : str
        Message containing version information.

    """
    message = f'Version: {version.__version__}'
    message += f'\nLast modified: {version.__last_modified__}'
    return message

class VersionAction(Action):
    """
    Called when '-v' or '--version' flags are given.

    """
    def __call__(self, parser, namespace, values, option_string=None):
        """
        The print_version function is called when parser is ran with the '-v' or '--version' flags.

        Parameters
        ----------
        parser : argparse.ArgumentParser
            The object which contains this action.
        namespace : argparse.Namespace
            The argparse.Namespace object returned by parse_args().
        values : list
            The command-line arguments with any type conversion applied.
        option_string : string
            The option string which was used to invoke this action.

        Returns
        -------
        None

        """
        print(version_info())
        parser.exit()

def main():
    """
    Main function for user interface. Parses arguments and starts a pipeline if one is selected.

    Returns
    -------
    None

    """
    parser = ArgumentParser(
        prog='posty',
        description='posty: a CLI API platform',
        usage='posty [options]'
    )
    parser.add_argument(
        'environment',
        type=str,
        help='str: path to environment json file (required)'
    )
    parser.add_argument(
        'request',
        type=str,
        help='str: path to request json file (required)'
    )
    parser.add_argument(
        '-v',
        '--version',
        action=VersionAction,
        nargs=0,
        help='flag: print version'
    )
    args, unknown_args = parser.parse_known_args()

    print(f"Running Posty {version.__version__} ...")
    posty = Posty()
    env = posty.load_json(args.environment)
    req = posty.load_json(args.request)
    result = Verifier().verify_request(req)
    if result == 1: sys.exit(1)
    req = posty.populate_dict_from_env(req, env)
    posty.execute_json_request(req, env)