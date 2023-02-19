import argparse
from cowsay import cowsay, list_cows

parser = argparse.ArgumentParser()
parser.add_argument('-e', type=str)
parser.add_argument('-T', type=str)
parser.add_argument('-b', action='store_true')
parser.add_argument('-d', action='store_true')
parser.add_argument('-g', action='store_true')
parser.add_argument('-p', action='store_true')
parser.add_argument('-s', action='store_true')
parser.add_argument('-t', action='store_true')
parser.add_argument('-w', action='store_true')
parser.add_argument('-y', action='store_true')

parser.add_argument('message', type=str)
args = parser.parse_args()

params = {}
if args.e is not None:
    params['eyes'] = args.e[:2]
if args.T is not None:
    params['tongue'] = args.T[:2]

args_dict = vars(args)
preset_list = 'bdgpstwy'
for preset in preset_list:
    if args_dict[preset]:
        params['preset'] = preset
        break


params['message'] = args.message
print(cowsay(**params))