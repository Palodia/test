import argparse
import torch
def get_args():
    parser = argparse.ArgumentParser(description='Domain generalization')
    parser.add_argument('--a', type=float, default=0.2)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()
    print ( args.a + 1)
    print("CUDA: {}".format(torch.version.cuda))