from argparse import ArgumentParser
from .laboratory import Laboratory
import yaml


def process():
    parser = ArgumentParser()
    parser.add_argument('yaml_file')
    parser.add_argument('--reactions', action='store_true')
    args = parser.parse_args()

    yaml_shelves = yaml.load(open(args.yaml_file))
    shelves = Laboratory(yaml_shelves)
    result = shelves.run_full_experiment()

    if args.reactions:
        print(result[2])
    else:
        print("lower: {} \nupper: {}".format(result[0], result[1]))
        result_yml = open("result.yml", "w")
        yaml.dump({"lower": result[0], "upper": result[1]}, result_yml)
        result_yml.close()


if __name__ == "__main__":
    process()
