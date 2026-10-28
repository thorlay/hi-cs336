"""Approximate a deliberately simplified decoder; see notes/03-transformer-accounting.md."""
import argparse


def positive_int(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vocab-size", type=positive_int, default=32000)
    parser.add_argument("--layers", type=positive_int, default=12)
    parser.add_argument("--d-model", type=positive_int, default=768)
    parser.add_argument("--d-ff", type=positive_int, default=3072)
    parser.add_argument("--tokens", type=positive_int, default=100000000)
    parser.add_argument("--tied", action="store_true")
    args = parser.parse_args()
    embedding = args.vocab_size * args.d_model * (1 if args.tied else 2)
    blocks = args.layers * (4 * args.d_model**2 + 2 * args.d_model * args.d_ff)
    parameters = embedding + blocks
    print("Assumptions: standard MHA, plain two-layer MLP, no bias/norm/position parameters")
    print(f"Approximate parameters: {parameters:,}")
    print(f"BF16 weights only: {parameters * 2 / 2**30:.6f} GiB")
    print(f"Rough training FLOPs (6ND): {6 * parameters * args.tokens:.3e}")
    print("Estimates only; excludes activation memory and sequence-dependent attention FLOPs.")


if __name__ == "__main__":
    main()
