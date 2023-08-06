"""Builtin Datasets.
"""
from .read_load import read, load
from .preprocessing.utils import cleanup
from anndata import AnnData
import numpy as np
import pandas as pd


def toy_data(n_obs):
    """
    Randomly samples from the Dentate Gyrus dataset.

    Arguments
    ---------
    n_obs: `int`
        Size of the sampled dataset

    Returns
    -------
    Returns `adata` object
    """

    """Random samples from Dentate Gyrus.
    """
    adata = dentategyrus()
    indices = np.random.choice(adata.n_obs, n_obs)
    adata = adata[indices]
    adata.obs_names = np.array(range(adata.n_obs), dtype='str')
    adata.var_names_make_unique()
    return adata


def dentategyrus():
    """Dentate Gyrus dataset from Hochgerner et al. (2018).

    Dentate gyrus is part of the hippocampus involved in learning, episodic memory formation and spatial coding.
    It is measured using 10X Genomics Chromium and described in Hochgerner et al. (2018).
    The data consists of 25,919 genes across 3,396 cells and provides several interesting characteristics.

    Returns
    -------
    Returns `adata` object
    """
    filename = 'data/DentateGyrus/10X43_1.loom'
    url = 'http://pklab.med.harvard.edu/velocyto/DG1/10X43_1.loom'
    adata = read(filename, backup_url=url, cleanup=True, sparse=True, cache=True)
    cleanup(adata, clean='all', keep={'spliced', 'unspliced', 'ambiguous'})

    url_louvain = 'https://github.com/theislab/scvelo_notebooks/raw/master/data/DentateGyrus/DG_clusters.npy'
    url_umap = 'https://github.com/theislab/scvelo_notebooks/raw/master/data/DentateGyrus/DG_umap.npy'

    adata.obs['clusters'] = load('./data/DentateGyrus/DG_clusters.npy', url_louvain)
    adata.obsm['X_umap'] = load('./data/DentateGyrus/DG_umap.npy', url_umap)

    adata.obs['clusters'] = pd.Categorical(adata.obs['clusters'])

    return adata


def forebrain():
    """Developing human forebrain.
    Forebrain tissue of a week 10 embryo, focusing on the glutamatergic neuronal lineage.

    Returns
    -------
    Returns `adata` object
    """
    filename = 'data/ForebrainGlut/hgForebrainGlut.loom'
    url = 'http://pklab.med.harvard.edu/velocyto/hgForebrainGlut/hgForebrainGlut.loom'
    adata = read(filename, backup_url=url, cleanup=True, sparse=True, cache=True)
    adata.var_names_make_unique()
    return adata


def simulation(n_obs=300, n_vars=4, alpha=None, beta=None, gamma=None, alpha_=None, t_max=None,
               noise_model='normal', noise_level=1):
    """Simulation of mRNA metabolism with transcription, splicing and degradation

    Returns
    -------
    Returns `adata` object
    """
    from .tools.dynamical_model_utils import unspliced, spliced, vectorize

    def draw_poisson(n):
        from random import uniform  # draw from poisson
        t = np.cumsum([- .1 * np.log(uniform(0, 1)) for _ in range(n - 1)])
        return np.insert(t, 0, 0)  # prepend t0=0

    def simulate_dynamics(tau, alpha, beta, gamma, u0, s0, noise_model, noise_level):
        ut = unspliced(tau, u0, alpha, beta)
        st = spliced(tau, s0, u0, alpha, beta, gamma)

        if noise_model is 'normal':  # add noise
            ut += np.random.normal(scale=noise_level * np.percentile(ut, 99) / 10, size=len(ut))
            st += np.random.normal(scale=noise_level * np.percentile(st, 99) / 10, size=len(st))
        ut, st = np.clip(ut, 0, None), np.clip(st, 0, None)
        return ut, st

    def simulate_gillespie(alpha, beta, gamma):
        # update rules: transcription (u+1,s), splicing (u-1,s+1), degradation (u,s-1), nothing (u,s)
        update_rule = np.array([[1, 0], [-1, 1], [0, -1], [0, 0]])

        def update(props):
            if np.sum(props) > 0:
                props /= np.sum(props)
            p_cumsum = props.cumsum()
            p = np.random.rand()
            i = 0
            while p > p_cumsum[i]:
                i += 1
            return update_rule[i]

        u, s = np.zeros(len(alpha)), np.zeros(len(alpha))
        for i, alpha_i in enumerate(alpha):
            u_, s_ = (u[i - 1], s[i - 1]) if i > 0 else (0, 0)
            du, ds = update(props=np.array([alpha_i, beta * u_, gamma * s_]))
            u[i], s[i] = (u_ + du, s_ + ds)
        return u, s

    alpha = 5 if alpha is None else alpha
    beta = .5 if beta is None else beta
    gamma = .3 if gamma is None else gamma
    alpha_ = 0 if alpha_ is None else alpha_

    t = draw_poisson(n_obs)
    if t_max is not None:
        t *= t_max / np.max(t)
    t_max = np.max(t)

    # switching time point obtained as fraction of t_max rounded down
    t_ = np.array([np.max(t[t < t_i * t_max]) for t_i in [.4, .7, 1, .1]])

    U = np.zeros(shape=(len(t), n_vars))
    S = np.zeros(shape=(len(t), n_vars))
    for i in range(n_vars):
        tau, alpha_vec, u0_vec, s0_vec = vectorize(t, t_[i], alpha, beta, gamma, alpha_=alpha_, u0=0, s0=0)
        if noise_model is 'gillespie':
            U[:, i], S[:, i] = simulate_gillespie(alpha_vec, beta, gamma)
        else:
            U[:, i], S[:, i] = simulate_dynamics(tau, alpha_vec, beta, gamma, u0_vec, s0_vec, noise_model, noise_level)

    obs = {'true_t': t.round(2)}
    var = {'true_t_': t_[:n_vars],
           'true_alpha': np.ones(n_vars) * alpha,
           'true_beta': np.ones(n_vars) * beta,
           'true_gamma': np.ones(n_vars) * gamma}
    layers = {'unspliced': U, 'spliced': S}

    return AnnData(S, obs, var, layers=layers)
