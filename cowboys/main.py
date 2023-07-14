# main app

from utils.args import args
from utils.circle import circle

if __name__ == "__main__":
    ''' Simulate circle of cowboys that shoot themselves at high noon
    each cowboy has 10 LP and can fire a shot to their direct neighbor
    each shot can reduce LP by 1-5 integer
    takes number of cowboys as input '''
    prog_args = args()
    this_circle: circle = circle(prog_args.args.number)
    this_circle.high_noon()
    this_circle.report()
