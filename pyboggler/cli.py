# -*- coding: utf-8 -*-

"""Console script for pyboggler."""
import sys
import click

from bogglesolver import BoggleSolver
@click.option('--grid', prompt='grid',
              help='.')
@click.command()
def main(grid):
    """Console script for pyboggler."""
    bs = BoggleSolver(grid)
    for w in bs.solve():print w
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
