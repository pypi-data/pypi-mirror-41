from .. import settings
from .utils import is_categorical, update_axes, set_label, set_title, default_basis, default_color, default_color_map, \
    default_size, interpret_colorkey, get_components, set_colorbar, savefig_or_show, make_unique_list, show_linear_fit
from .docs import doc_scatter, doc_params

from matplotlib import rcParams
import matplotlib.pyplot as pl
import numpy as np
from scipy.sparse import issparse


@doc_params(scatter=doc_scatter)
def scatter(adata, x=None, y=None, basis=None, vkey=None, color=None, use_raw=None, layer=None, color_map=None,
            colorbar=True, palette=None, size=None, alpha=None, perc=None, sort_order=True, groups=None,
            components=None, projection='2d', legend_loc='none', legend_fontsize=None, legend_fontweight=None,
            right_margin=None, left_margin=None, xlabel=None, ylabel=None, title=None, fontsize=None, figsize=None,
            dpi=None, frameon=None, show=True, save=None, ax=None, zorder=None, ncols=None, **kwargs):
    """\
    Scatter plot along observations or variables axes.

    Arguments
    ---------
    adata: :class:`~anndata.AnnData`
        Annotated data matrix.
    x: `str`, `np.ndarray` or `None` (default: `None`)
        x coordinate
    y: `str`, `np.ndarray` or `None` (default: `None`)
        y coordinate
    {scatter}

    Returns
    -------
        If `show==False` a `matplotlib.Axis`
    """
    scatter_kwargs = {"use_raw": use_raw, "sort_order": sort_order, "alpha": alpha, "components": components,
                      "projection": projection, "legend_loc": legend_loc, "groups": groups, "palette": palette,
                      "legend_fontsize": legend_fontsize, "legend_fontweight": legend_fontweight,
                      "right_margin": right_margin, "left_margin": left_margin, "show": False, "save": None}

    colors, layers, bases = make_unique_list(color, allow_array=True), make_unique_list(layer), make_unique_list(basis)
    multikey = colors if len(colors) > 1 else layers if len(layers) > 1 else bases if len(bases) > 1 else None
    if multikey is not None:
        if isinstance(title, (list, tuple)): title *= int(np.ceil(len(multikey) / len(title)))
        ncols = len(multikey) if ncols is None else min(len(multikey), ncols)
        nrows = int(np.ceil(len(multikey) / ncols))
        figsize = rcParams['figure.figsize'] if figsize is None else figsize
        for i, gs in enumerate(
                pl.GridSpec(nrows, ncols, pl.figure(None, (figsize[0] * ncols, figsize[1] * nrows), dpi=dpi))):
            if i < len(multikey):
                scatter(adata, x=x, y=y, size=size, xlabel=xlabel, ylabel=ylabel, color_map=color_map,
                        colorbar=colorbar, perc=perc, frameon=frameon, ax=pl.subplot(gs), zorder=zorder,
                        color=colors[i] if len(colors) > 1 else color,
                        layer=layers[i] if len(layers) > 1 else layer,
                        basis=bases[i] if len(bases) > 1 else basis,
                        title=title[i] if isinstance(title, (list, tuple)) else title, **scatter_kwargs, **kwargs)
        savefig_or_show('' if basis is None else basis, dpi=dpi, save=save, show=show)
        if not show: return ax

    else:
        color, layer, basis = colors[0], layers[0], bases[0]
        color = default_color(adata) if color is None else color
        color_map = default_color_map(adata, color) if color_map is None else color_map
        frameon = frameon if frameon is not None else settings._frameon

        is_embedding = ((x is None) | (y is None)) and basis not in adata.var_names
        basis = default_basis(adata) if basis is None and is_embedding else basis
        size = default_size(adata) if size is None else size

        if projection == '3d':
            from mpl_toolkits.mplot3d import Axes3D
            ax = pl.figure(None, figsize, dpi=dpi).gca(projection=projection) if ax is None else ax
        else:
            ax = pl.figure(None, figsize, dpi=dpi).gca() if ax is None else ax

        if is_categorical(adata, color) and is_embedding:
            from scanpy.api.pl import scatter as scatter_
            ax = scatter_(adata, basis=basis, color=color, color_map=color_map, size=size, frameon=frameon, ax=ax,
                          title=title, **scatter_kwargs, **kwargs)

        else:
            if basis in adata.var_names:
                x = adata[:, basis].layers['spliced'] if use_raw else adata[:, basis].layers['Ms']
                y = adata[:, basis].layers['unspliced'] if use_raw else adata[:, basis].layers['Mu']
                x, y = x.A if issparse(x) else x, y.A if issparse(y) else y
                xlabel, ylabel = 'spliced', 'unspliced'
                title = basis if title is None else title

            elif is_embedding:
                X_emb = adata.obsm['X_' + basis][:, get_components(components, basis)]
                x, y = X_emb[:, 0], X_emb[:, 1]

            elif isinstance(x, str) and isinstance(y, str) and x in adata.var_names and y in adata.var_names:
                x = adata[:, x].layers[layer] if layer in adata.layers.keys() else adata[:, x].X
                y = adata[:, y].layers[layer] if layer in adata.layers.keys() else adata[:, y].X

            c = interpret_colorkey(adata, basis, color, perc) if basis in adata.var_names and color in adata.layers.keys() \
                else interpret_colorkey(adata, color, layer, perc)

            if layer is not None and 'velocity' in layer and isinstance(color, str) and color in adata.var_names:
                ub = np.percentile(np.abs(c), 98)
                kwargs.update({"vmin": -ub, "vmax": ub})
            if layer is not None and ('spliced' in layer or 'Ms' in layer or 'Mu' in layer) \
                    and isinstance(color, str) and color in adata.var_names:
                ub = np.percentile(c, 98)
                kwargs.update({"vmax": ub})

            if groups is not None or (not isinstance(c, str) and not isinstance(c[0], str) and any(np.isnan(c))):
                zorder = 0 if zorder is None else zorder
                ax = scatter(adata, basis=basis, color='lightgrey', ax=ax, zorder=zorder, **scatter_kwargs)
                zorder += 1

            pl.scatter(x, y, c=c, cmap=color_map, s=size, alpha=alpha, edgecolors='none', marker='.', zorder=zorder, **kwargs)

            set_label(xlabel, ylabel, fontsize, basis)
            set_title(title, layer, color, fontsize)
            ax = update_axes(ax, fontsize, is_embedding, frameon)

            if basis in adata.var_names:
                show_linear_fit(adata, basis, vkey, x)

                from .simulation import show_full_dynamics
                if 'true_alpha' in adata.var.keys():
                    show_full_dynamics(adata, basis)
                if 'fit_alpha' in adata.var.keys():
                    show_full_dynamics(adata, basis, 'fit')

            if colorbar and not is_categorical(adata, color): set_colorbar(ax)

        savefig_or_show('' if basis is None else basis, dpi=dpi, save=save, show=show)
        if not show: return ax