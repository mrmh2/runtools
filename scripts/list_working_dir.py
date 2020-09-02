import json
import pathlib

import click
import pandas as pd

from runtools.spec import item_spec_from_fpath


@click.command()
@click.argument("working_dirpath")
def main(working_dirpath):

    dirpath = pathlib.Path(working_dirpath)
    fpath_iter = dirpath.rglob("*.json")

    specs = [item_spec_from_fpath(fpath) for fpath in fpath_iter]

    # spec_template = "{genotype}_{n}"
    # spec_template = "{n}"
    reprs = [spec.__repr__() for spec in specs]
    print('\n'.join(sorted(reprs)))
        


if __name__ == "__main__":
    main()
