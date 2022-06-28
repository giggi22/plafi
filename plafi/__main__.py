import argparse
from . import functions as fc
import os
import sys
sys.tracebacklimit = 0

def main():
    # parser initialization
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        help='possible actions', dest='subparser')

    # PLOT argument
    plot_parser = subparsers.add_parser('plot', help='plot the data')
    plot_parser.add_argument("path", help='path to data to plot', type=str, nargs="?")
    plot_parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")

    # FIT argument
    fit_parser = subparsers.add_parser('fit', help='fit the data')

    # CONSTANTS argument
    constants_parser = subparsers.add_parser('const', help='manage the constants')
    constants_parser.add_argument("-a", "--add", help="add a new constant", action="store_true")
    constants_parser.add_argument("-d", "--delete", help="delete a constant", action="store_true")

    # arguments are converted into an argparser.Namespace object
    args = parser.parse_args()

    # MAIN IF STATEMENTS
    # plot case
    if args.subparser == 'plot':
        path = args.path
        if args.verbose:
            fc.plot_data_verbose()
        else:
            if path == None:
                raise ValueError("A path must be passed")
            elif not os.path.exists(path):
                raise ValueError("The file does not exist")
            else:
                try:
                    data = fc.read_data(path)
                    fc.plot_data(data)
                except:
                    raise ValueError("It was not possible to read the file")

    # fit case
    if args.subparser == 'fit':
        fc.fitting_procedure()

    # const case
    if args.subparser == 'const':
        fc.initialize_constants()
        if args.add:
            fc.add_constant()
        if args.delete:
            fc.delete_constant()
        fc.print_constants()


if __name__ == '__main__':
    main()
