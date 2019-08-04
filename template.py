#!/usr/bin/env python

# standard Python libraries
import time

# third party Python libraries

# custom Python libraries

# testing notes


class ClassName:
    """Class description"""
    def __init__(self, arg1):
        """Iniitialize ClassName class object."""
        self.arg1 = arg1

    def function_name(self):
        return None




########################################################################
########################################################################

def get_timestamp():
    return time.strftime("%Y%m%d_%H%M%S")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Program description here"
    )
    # boolean option arg
    parser.add_argument(
        "-s",
        dest="arg_name",
        action="store_true",
        help="option description",
    )
    # input arg
    parser.add_argument(
        "-s",
        dest="arg_name2",
        action="store",
        type=str,
        default='default value',
        help="option description",
    )

    # if not os.path.exists(args.google_dorks):
    #     print("[!] Specify a valid file containing Google dorks with -g")
    #     sys.exit(0)

    # if args.delay < 0:
    #     print("[!] Delay must be greater than 0")
    #     sys.exit(0)

    args = parser.parse_args()

    print(f"Initiation timestamp: {get_timestamp()}")

    ClassName(**vars(args))

    print(f"Completion timestamp: {get_timestamp()}")

    print("Done!")


# with open("DOC.txt") as fp:
#     return random.choice(fp.readlines()).strip()
