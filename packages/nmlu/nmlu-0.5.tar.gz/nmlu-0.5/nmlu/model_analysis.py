import  pandas as pd
import numpy as np
from concurrent.futures import ProcessPoolExecutor
from treeinterpreter import treeinterpreter as ti


def parallel_trees(m, fn, n_jobs=8):
    return list(ProcessPoolExecutor(n_jobs).map(fn, m.estimators_))


def get_ensamble_preds(model, x):
    """Return separately the predictions done by all the estimators in ensemble.

    Parameters
    ----------
    model
    x

    Returns
    -------
    predictions : ndarray shaped (estimators, n_samples)
    """
    # TODO: figure out how to get the faster version commented below working
    # (AttributeError: Can't pickle local object 'get_ensamble_preds.<locals>.get_preds')
    # def get_preds(t):
    #     return t.predict(x)
    #
    # return np.stack(parallel_trees(model, get_preds))

    # WORKAROUND for large datasets:
    # run code above manually (eg. in script.notebook), then use
    # make_ensemble_preds_with_confidence_table directly instead of get_ensemble_preds_with_confidence

    return np.stack([t.predict(x) for t in model.estimators_])


def make_ensemble_preds_with_confidence_table(df_raw_val, preds, fld, y_fld):
    df = df_raw_val.copy()

    df['pred_std'] = np.std(preds, axis=0)
    df['pred'] = np.mean(preds, axis=0)

    flds = [fld, y_fld, 'pred', 'pred_std']
    tbl = df[flds].groupby(flds[0], as_index=False).mean()

    return tbl


def get_ensemble_preds_with_confidence(
        model, x_val, df_raw_val, fld, y_fld
):
    preds = get_ensamble_preds(model, x_val)
    return make_ensemble_preds_with_confidence_table(df_raw_val, preds, fld, y_fld)


# TODO: confirm this works
def plot_ensemble_regression_preds_with_confidence(
        model, x_val, df_raw_val, fld, y_fld, figsize=None
):
    preds = get_ensamble_preds(model, x_val)
    tbl = make_ensemble_preds_with_confidence_table(df_raw_val, preds, fld, y_fld)
    return tbl.plot(tbl, 'pred', 'barh',
                    xerr='pred_std', alpha=0.6, figsize=figsize)


def rf_feat_importance(model, df):
    return pd.DataFrame(
        {'cols': df.columns, 'imp': model.feature_importances_}
    ).sort_values('imp', ascending=False)


def rf_show_plot_fi(model, df, figsize=(12,7)):
    fi = rf_feat_importance(model, df)
    print(fi)
    fi.plot('cols', 'imp', 'barh', figsize=figsize, legend=False)


def ti_make_readable_contribs(df, cs):
    idxs = np.argsort(cs[:, 0])
    sorted_feats = df.columns[idxs]
    return [o for o in zip(
        sorted_feats,
        df.iloc[0][sorted_feats],
        cs[idxs],
    )]


def ti_make_explained_predictions_data(df, preds, contribs):
    xcontribs = [ti_make_readable_contribs(df, c) for c in contribs]
    preds_dict = [{
        i : p
        for i, p in enumerate(pred)
    } for pred in preds]
    return list(zip(preds_dict, xcontribs))


def rf_predict_with_explanations(model, x):
    preds, biases, contribs = ti.predict(model, x)
    return ti_make_explained_predictions_data(x, preds, contribs)
