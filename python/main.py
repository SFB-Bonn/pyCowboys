# main app

from utils.args import args
from utils.circle import circle

if __name__ == "__main__":
    prog_args = args()
    this_circle: circle = circle(prog_args.args.number)
    this_circle.high_noon()
    this_circle.report()
