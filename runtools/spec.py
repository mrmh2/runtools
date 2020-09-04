import json
import pathlib

from types import SimpleNamespace


class ItemSpec(SimpleNamespace):

    def template_repr(self, template):
        return template.format(**self.__dict__)


def item_spec_from_fpath(fpath):
    with open(fpath) as fh:
        metadata = json.load(fh)

    return ItemSpec(**metadata["spec"])


def get_all_specs(dirpath):

    dirpath = pathlib.Path(dirpath)
    fpath_iter = dirpath.rglob("*.json")
    specs = [item_spec_from_fpath(fpath) for fpath in fpath_iter]

    return specs

