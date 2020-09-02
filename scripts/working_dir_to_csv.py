import json
import pathlib

import click
import pandas as pd


from runtools.spec import ItemSpec, get_all_specs

@click.command()
@click.argument('working_dirpath')
@click.argument('output_fpath')
def main(working_dirpath, output_fpath):

    dirpath = pathlib.Path(working_dirpath)

    specs = get_all_specs(dirpath)
    spec_reprs = [spec.__repr__() for spec in specs]
    assert len(spec_reprs) == len(set(spec_reprs)), "Duplicate spec"

    fpath_iter = dirpath.rglob("*.json")

    def df_from_fpath(fpath):
        with open(fpath) as fh:
            metadata = json.load(fh)

        data_fname = metadata['data_fname']

        return pd.read_csv(dirpath/data_fname, index_col=0)

    merged_df = pd.concat([df_from_fpath(fpath) for fpath in fpath_iter])

    merged_df.to_csv(output_fpath, index=False, float_format="%.4f")



if __name__ == "__main__":
    main()
    


