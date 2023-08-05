import os
import gzip
import io
import anndata
import pandas as pd
from typing import Optional, Iterable, Tuple, Mapping

from pypairs import utils


def leng15(
        mode: Optional[str] = 'all',
        gene_sub: Optional[Iterable[int]] = None
) -> Iterable[Iterable[float]]:
    """Single cell RNA-seq data of human hESCs to evaluate Oscope [Leng15]_

    Total 213 H1 single cells and 247 H1-Fucci single cells were sequenced.
    The 213 H1 cells were used to evaluate Oscope in identifying oscillatory genes.
    The H1-Fucci cells were used to confirm the cell cycle gene cluster identified
    by Oscope in the H1 hESCs.
    Normalized expected counts are provided in GSE64016_H1andFUCCI_normalized_EC.csv.gz

    Reference
    ---------
        GEO-Dataset: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE64016

    Parameters
    ----------
    mode
        sample selection mode:
            - 'all' for all samples, default
            - 'sorted' for all samples with known cell cycle (G2, S or G1)
            - 'unsorted' for all samples with unknown cell cycle (H1)
    gene_sub
        Index based array of subsetted genes

    Returns
    -------
    adata : :class:`~anndata.AnnData`
        Annotated data matrix containing the normalized gene counts
    """
    filename = os.path.join(os.path.dirname(__file__), 'GSE64016_H1andFUCCI_normalized_EC.csv.gz')

    with gzip.open(filename, 'r') as fin:
        x = pd.read_csv(io.TextIOWrapper(fin, newline=""))

    x.set_index("Unnamed: 0", inplace=True)

    if mode == 'sorted':
        x.drop(list(x.filter(regex='H1_')), axis=1, inplace=True)
    elif mode == 'unsorted':
        x.drop(list(x.filter(regex='^(H1_)')), axis=1, inplace=True)
    elif mode == 'all' or mode is None:
        pass
    else:
        raise NotImplementedError("valid options for mode are 'all', 'sorted' or 'unsorted'")

    if gene_sub:
        x = x.iloc[gene_sub, :]

    x = x.transpose()

    adata = anndata.AnnData(
        x.values,
        obs={
            "category":
                ["G2M" if s.split("_")[0] == "G2" else s.split("_")[0] for s in list(x.index)]
        }
    )

    adata.var_names = list(x.columns)
    adata.obs_names = list(x.index)

    return adata


def default_cc_marker(
        dataset: Optional[str] = 'leng15'
) -> Mapping[str, Iterable[Tuple[str,str]]]:
    """Cell cycle marker pairs derived from [Leng15]_ with the default :func:`~pypairs.pairs.sandbag` settings.

    For description of the dataset see :func:`~pypairs.datasets.leng15`.

    Parameters
    ----------
    dataset
        placeholder. only options currently 'leng15'. Everything else with raise a :class:`~NotImplementedError`

    Returns
    -------
        Mapping from category `['G1','G2M','S']` to list of gene "marker pairs" `[('Gene1', 'Gene2'), ..]`.

    """
    if dataset == 'leng15':
        filename = os.path.join(os.path.dirname(__file__), 'leng15_default_markers.json')

        return utils.read_dict_from_json(filename)
    else:
        raise NotImplementedError("Dataset not yet available")
        # Maybe more to come...
