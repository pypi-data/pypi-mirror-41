"""
:ref:`chainladder.methods<methods>`.MackChainladder
===================================================

:ref:`MackChainladder<mack>` produces the same IBNR results as the deterministic
approach, but ldf selection happens in a regression framework that allows for
the calculation of prediction errors.  The Mack Chainladder technique is the OG
stochastic method.

"""
import numpy as np
import copy
from chainladder.methods import Chainladder


class MackChainladder(Chainladder):
    """ Basic stochastic chainladder method popularized by Thomas Mack

    Parameters
    ----------
    None

    Attributes
    ----------
    triangle
        returns **X**
    ultimate_
        The ultimate losses per the method
    ibnr_
        The IBNR per the method
    full_expectation_
        The ultimates back-filled to each development period in **X** replacing
        the known data
    full_triangle_
        The ultimates back-filled to each development period in **X** retaining
        the known data
    summary_
        summary of the model
    full_std_err_
        The full standard error
    total_process_risk_
        The total process error
    total_parameter_risk_
        The total parameter error
    mack_std_err_
        The total prediction error by origin period
    total_mack_std_err_
        The total prediction error across all origin periods

    """

    def fit(self, X, y=None, sample_weight=None):
        """Fit the model with X.

        Parameters
        ----------
        X : Triangle-like
            Data to which the model will be applied.
        y : Ignored
        sample_weight : Ignored

        Returns
        -------
        self : object
            Returns the instance itself.
        """
        super().fit(X, y, sample_weight)
        self._mack_recursion('param_risk')
        self._mack_recursion('process_risk')
        self._mack_recursion('total_param_risk')
        return self

    @property
    def full_std_err_(self):
        obj = copy.deepcopy(self.X_)
        tri_array = self.full_triangle_.triangle
        weight_dict = {'regression': 2, 'volume': 1, 'simple': 0}
        val = np.array([weight_dict.get(item.lower(), 2)
                        for item in list(self.average_) + ['volume']])
        for i in [2, 1, 0]:
            val = np.repeat(np.expand_dims(val, 0), tri_array.shape[i], axis=0)
        k, v, o, d = val.shape
        weight = np.sqrt(tri_array[..., :-1]**(2-val))
        weight[weight == 0] = np.nan
        obj.triangle = self.X_.sigma_.triangle / weight
        w = np.concatenate((self.X_.w_, np.ones((k, v, o, 1))*np.nan), axis=3)
        w[np.isnan(w)] = 1
        obj.triangle = np.nan_to_num(obj.triangle) * w
        obj.nan_override = True
        return obj

    @property
    def total_process_risk_(self):
        obj = copy.deepcopy(self.process_risk_)
        obj.triangle = np.sqrt(np.nansum(self.process_risk_.triangle**2, 2))
        obj.triangle = np.expand_dims(obj.triangle, 2)
        obj.odims = ['tot_proc_risk']
        return obj

    def _mack_recursion(self, est):
        obj = copy.deepcopy(self.X_)
        # replace this with nan_x_latest
        nans = np.expand_dims(np.expand_dims(self.X_.nan_triangle(), 0), 0)
        k, v, o, d = self.X_.shape
        nans = nans * np.ones((k, v, o, d))
        nans = np.concatenate((nans, np.ones((k, v, o, 1))*np.nan), 3)
        nans = 1-np.nan_to_num(nans)
        obj.ddims = np.array([str(item) for item in obj.ddims]+['Ult'])
        obj.nan_override = True
        risk_arr = np.zeros((k, v, o, 1))
        if est == 'param_risk':
            obj.triangle = self._get_risk(nans, risk_arr,
                                          obj.std_err_.triangle)
            self.parameter_risk_ = obj
        elif est == 'process_risk':
            obj.triangle = self._get_risk(nans, risk_arr,
                                          self.full_std_err_.triangle)
            self.process_risk_ = obj
        else:
            risk_arr = risk_arr[..., 0:1, :]
            obj.triangle = self._get_tot_param_risk(risk_arr)
            obj.odims = ['Total param risk']
            self.total_parameter_risk_ = obj

    def _get_risk(self, nans, risk_arr, std_err):
        t1_t = (self.full_triangle_.triangle[..., :-1] * std_err)**2
        ldf = self.X_.ldf_.triangle.copy()
        for i in range(self.full_triangle_.shape[3]-1):
            t1 = t1_t[..., i:i+1]
            t2 = (ldf[..., i:i+1] * risk_arr[..., i:i+1])**2
            t_tot = np.sqrt(t1+t2)*nans[..., i+1:i+2]
            risk_arr = np.concatenate((risk_arr, t_tot), 3)
        return risk_arr

    def _get_tot_param_risk(self, risk_arr):
        t1 = self.full_triangle_.triangle[..., :-1] - \
             np.nan_to_num(self.X_.triangle) + \
             np.nan_to_num(self.X_.get_latest_diagonal(False).triangle)
        t1 = np.expand_dims(np.sum(t1*self.X_.std_err_.triangle, 2), 2)
        ldf = np.unique(self.X_.ldf_.triangle, axis=-2)
        for i in range(self.full_triangle_.shape[-1]-1):
            t_tot = np.sqrt((t1[..., i:i+1])**2 + (ldf[..., i:i+1] *
                            risk_arr[..., -1:])**2)
            risk_arr = np.concatenate((risk_arr, t_tot), -1)
        return risk_arr

    @property
    def mack_std_err_(self):
        obj = copy.deepcopy(self.parameter_risk_)
        obj.triangle = np.sqrt(self.parameter_risk_.triangle**2 +
                               self.process_risk_.triangle**2)
        return obj

    @property
    def total_mack_std_err_(self):
        obj = copy.deepcopy(self.X_.latest_diagonal)
        obj.triangle = np.sqrt(self.total_process_risk_.triangle**2 +
                               self.total_parameter_risk_.triangle**2)
        obj.triangle = obj.triangle[..., -1:]
        obj.ddims = ['Total Mack Std Err']
        obj.odims = ['Total']
        return obj

    @property
    def summary_(self):
        obj = copy.deepcopy(self.X_)
        obj.triangle = np.concatenate(
            (self.X_.latest_diagonal.triangle,
             self.ibnr_.triangle,
             self.ultimate_.triangle,
             self.mack_std_err_.triangle[..., -1:]), 3)
        obj.ddims = ['Latest', 'IBNR', 'Ultimate', 'Mack Std Err']
        obj.nan_override = True
        return obj
