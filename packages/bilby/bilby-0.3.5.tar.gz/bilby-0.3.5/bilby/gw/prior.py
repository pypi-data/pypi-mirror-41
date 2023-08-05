import os

import numpy as np
from scipy.interpolate import UnivariateSpline

from ..core.prior import (PriorDict, Uniform, FromFile, Prior, DeltaFunction,
                          Gaussian, Interped)
from ..core.utils import logger


class UniformComovingVolume(FromFile):

    def __init__(self, minimum=None, maximum=None,
                 name='luminosity distance', latex_label='$d_L$', unit='Mpc'):
        """

        Parameters
        ----------
        minimum: float, optional
            See superclass
        maximum: float, optional
            See superclass
        name: str, optional
            See superclass
        latex_label: str, optional
            See superclass
        """
        file_name = os.path.join(os.path.dirname(__file__), 'prior_files', 'comoving.txt')
        FromFile.__init__(self, file_name=file_name, minimum=minimum, maximum=maximum, name=name,
                          latex_label=latex_label, unit=unit)


class AlignedSpin(Interped):

    def __init__(self, a_prior=Uniform(0, 1), z_prior=Uniform(-1, 1),
                 name=None, latex_label=None, unit=None):
        """
        Prior distribution for the aligned (z) component of the spin.

        This takes prior distributions for the magnitude and cosine of the tilt
        and forms a compound prior.

        This is useful when using aligned-spin only waveform approximants.

        This is an extension of e.g., (A7) of https://arxiv.org/abs/1805.10457.

        Parameters
        ----------
        a_prior: Prior
            Prior distribution for spin magnitude
        z_prior: Prior
            Prior distribution for cosine spin tilt
        name: see superclass
        latex_label: see superclass
        unit: see superclass
        """
        self.a_prior = a_prior
        self.z_prior = z_prior
        chi_min = min(a_prior.maximum * z_prior.minimum,
                      a_prior.minimum * z_prior.maximum)
        chi_max = a_prior.maximum * z_prior.maximum
        xx = np.linspace(chi_min, chi_max, 800)
        aas = np.linspace(a_prior.minimum, a_prior.maximum, 1000)
        yy = [np.trapz(np.nan_to_num(a_prior.prob(aas) / aas *
                                     z_prior.prob(x / aas)), aas) for x in xx]
        Interped.__init__(self, xx=xx, yy=yy, name=name,
                          latex_label=latex_label, unit=unit)


class BBHPriorDict(PriorDict):
    def __init__(self, dictionary=None, filename=None):
        """ Initialises a Prior set for Binary Black holes

        Parameters
        ----------
        dictionary: dict, optional
            See superclass
        filename: str, optional
            See superclass
        """
        if dictionary is None and filename is None:
            filename = os.path.join(os.path.dirname(__file__), 'prior_files', 'binary_black_holes.prior')
            logger.info('No prior given, using default BBH priors in {}.'.format(filename))
        elif filename is not None:
            if not os.path.isfile(filename):
                filename = os.path.join(os.path.dirname(__file__), 'prior_files', filename)
        PriorDict.__init__(self, dictionary=dictionary, filename=filename)

    def test_redundancy(self, key):
        """
        Test whether adding the key would add be redundant.

        Parameters
        ----------
        key: str
            The key to test.

        Return
        ------
        redundant: bool
            Whether the key is redundant or not
        """
        redundant = False
        if key in self:
            logger.debug('{} already in prior'.format(key))
            return redundant
        mass_parameters = {'mass_1', 'mass_2', 'chirp_mass', 'total_mass', 'mass_ratio', 'symmetric_mass_ratio'}
        spin_magnitude_parameters = {'a_1', 'a_2'}
        spin_tilt_1_parameters = {'tilt_1', 'cos_tilt_1'}
        spin_tilt_2_parameters = {'tilt_2', 'cos_tilt_2'}
        spin_azimuth_parameters = {'phi_1', 'phi_2', 'phi_12', 'phi_jl'}
        inclination_parameters = {'iota', 'cos_iota'}
        distance_parameters = {'luminosity_distance', 'comoving_distance', 'redshift'}

        for parameter_set in [mass_parameters, spin_magnitude_parameters, spin_azimuth_parameters]:
            if key in parameter_set:
                if len(parameter_set.intersection(self)) > 2:
                    redundant = True
                    logger.warning('{} in prior. This may lead to unexpected behaviour.'.format(
                        parameter_set.intersection(self)))
                    break
            elif len(parameter_set.intersection(self)) == 2:
                redundant = True
                break
        for parameter_set in [inclination_parameters, distance_parameters, spin_tilt_1_parameters,
                              spin_tilt_2_parameters]:
            if key in parameter_set:
                if len(parameter_set.intersection(self)) > 1:
                    redundant = True
                    logger.warning('{} in prior. This may lead to unexpected behaviour.'.format(
                        parameter_set.intersection(self)))
                    break
                elif len(parameter_set.intersection(self)) == 1:
                    redundant = True
                    break

        return redundant


class BBHPriorSet(BBHPriorDict):

    def __init__(self, dictionary=None, filename=None):
        """ DEPRECATED: USE BBHPriorDict INSTEAD"""
        logger.warning("The name 'BBHPriorSet' is deprecated use 'BBHPriorDict' instead")
        super(BBHPriorSet, self).__init__(dictionary, filename)


class BNSPriorDict(PriorDict):

    def __init__(self, dictionary=None, filename=None):
        """ Initialises a Prior set for Binary Neutron Stars

        Parameters
        ----------
        dictionary: dict, optional
            See superclass
        filename: str, optional
            See superclass
        """
        if dictionary is None and filename is None:
            filename = os.path.join(os.path.dirname(__file__), 'prior_files', 'binary_neutron_stars.prior')
            logger.info('No prior given, using default BNS priors in {}.'.format(filename))
        elif filename is not None:
            if not os.path.isfile(filename):
                filename = os.path.join(os.path.dirname(__file__), 'prior_files', filename)
        PriorDict.__init__(self, dictionary=dictionary, filename=filename)

    def test_redundancy(self, key):
        logger.info("Performing redundancy check using BBHPriorDict().test_redundancy")
        bbh_redundancy = BBHPriorDict().test_redundancy(key)
        if bbh_redundancy:
            return True
        redundant = False

        tidal_parameters =\
            {'lambda_1', 'lambda_2', 'lambda_tilde', 'delta_lambda'}

        if key in tidal_parameters:
            if len(tidal_parameters.intersection(self)) > 2:
                redundant = True
                logger.warning('{} in prior. This may lead to unexpected behaviour.'.format(
                    tidal_parameters.intersection(self)))
            elif len(tidal_parameters.intersection(self)) == 2:
                redundant = True
        return redundant


class BNSPriorSet(BNSPriorDict):

    def __init__(self, dictionary=None, filename=None):
        """ DEPRECATED: USE BNSPriorDict INSTEAD"""
        super(BNSPriorSet, self).__init__(dictionary, filename)
        logger.warning("The name 'BNSPriorSet' is deprecated use 'BNSPriorDict' instead")


Prior._default_latex_labels = {
    'mass_1': '$m_1$',
    'mass_2': '$m_2$',
    'total_mass': '$M$',
    'chirp_mass': '$\mathcal{M}$',
    'mass_ratio': '$q$',
    'symmetric_mass_ratio': '$\eta$',
    'a_1': '$a_1$',
    'a_2': '$a_2$',
    'tilt_1': '$\\theta_1$',
    'tilt_2': '$\\theta_2$',
    'cos_tilt_1': '$\cos\\theta_1$',
    'cos_tilt_2': '$\cos\\theta_2$',
    'phi_12': '$\Delta\phi$',
    'phi_jl': '$\phi_{JL}$',
    'luminosity_distance': '$d_L$',
    'dec': '$\mathrm{DEC}$',
    'ra': '$\mathrm{RA}$',
    'iota': '$\iota$',
    'cos_iota': '$\cos\iota$',
    'psi': '$\psi$',
    'phase': '$\phi$',
    'geocent_time': '$t_c$',
    'lambda_1': '$\\Lambda_1$',
    'lambda_2': '$\\Lambda_2$',
    'lambda_tilde': '$\\tilde{\\Lambda}$',
    'delta_lambda': '$\\delta\\Lambda$'}


class CalibrationPriorDict(PriorDict):

    def __init__(self, dictionary=None, filename=None):
        """ Initialises a Prior set for Binary Black holes

        Parameters
        ----------
        dictionary: dict, optional
            See superclass
        filename: str, optional
            See superclass
        """
        if dictionary is None and filename is not None:
            filename = os.path.join(os.path.dirname(__file__),
                                    'prior_files', filename)
        PriorDict.__init__(self, dictionary=dictionary, filename=filename)
        self.source = None

    def to_file(self, outdir, label):
        """
        Write the prior to file. This includes information about the source if
        possible.

        Parameters
        ----------
        outdir: str
            Output directory.
        label: str
            Label for prior.
        """
        PriorDict.to_file(self, outdir=outdir, label=label)
        if self.source is not None:
            prior_file = os.path.join(outdir, "{}.prior".format(label))
            with open(prior_file, "a") as outfile:
                outfile.write("# prior source file is {}".format(self.source))

    @staticmethod
    def from_envelope_file(envelope_file, minimum_frequency,
                           maximum_frequency, n_nodes, label):
        """
        Load in the calibration envelope.

        This is a text file with columns:
            frequency median-amplitude median-phase -1-sigma-amplitude
            -1-sigma-phase +1-sigma-amplitude +1-sigma-phase

        Parameters
        ----------
        envelope_file: str
            Name of file to read in.
        minimum_frequency: float
            Minimum frequency for the spline.
        maximum_frequency: float
            Minimum frequency for the spline.
        n_nodes: int
            Number of nodes for the spline.
        label: str
            Label for the names of the parameters, e.g., recalib_H1_

        Returns
        -------
        prior: PriorDict
            Priors for the relevant parameters.
            This includes the frequencies of the nodes which are _not_ sampled.
        """
        calibration_data = np.genfromtxt(envelope_file).T
        frequency_array = calibration_data[0]
        amplitude_median = 1 - calibration_data[1]
        phase_median = calibration_data[2]
        amplitude_sigma = (calibration_data[4] - calibration_data[2]) / 2
        phase_sigma = (calibration_data[5] - calibration_data[3]) / 2

        nodes = np.logspace(np.log10(minimum_frequency),
                            np.log10(maximum_frequency), n_nodes)

        amplitude_mean_nodes =\
            UnivariateSpline(frequency_array, amplitude_median)(nodes)
        amplitude_sigma_nodes =\
            UnivariateSpline(frequency_array, amplitude_sigma)(nodes)
        phase_mean_nodes =\
            UnivariateSpline(frequency_array, phase_median)(nodes)
        phase_sigma_nodes =\
            UnivariateSpline(frequency_array, phase_sigma)(nodes)

        prior = CalibrationPriorDict()
        for ii in range(n_nodes):
            name = "recalib_{}_amplitude_{}".format(label, ii)
            latex_label = "$A^{}_{}$".format(label, ii)
            prior[name] = Gaussian(mu=amplitude_mean_nodes[ii],
                                   sigma=amplitude_sigma_nodes[ii],
                                   name=name, latex_label=latex_label)
        for ii in range(n_nodes):
            name = "recalib_{}_phase_{}".format(label, ii)
            latex_label = "$\\phi^{}_{}$".format(label, ii)
            prior[name] = Gaussian(mu=phase_mean_nodes[ii],
                                   sigma=phase_sigma_nodes[ii],
                                   name=name, latex_label=latex_label)
        for ii in range(n_nodes):
            name = "recalib_{}_frequency_{}".format(label, ii)
            latex_label = "$f^{}_{}$".format(label, ii)
            prior[name] = DeltaFunction(peak=nodes[ii], name=name,
                                        latex_label=latex_label)
        prior.source = os.path.abspath(envelope_file)
        return prior

    @staticmethod
    def constant_uncertainty_spline(
            amplitude_sigma, phase_sigma, minimum_frequency, maximum_frequency,
            n_nodes, label):
        """
        Make prior assuming constant in frequency calibration uncertainty.

        This assumes Gaussian fluctuations about 0.

        Parameters
        ----------
        amplitude_sigma: float
            Uncertainty in the amplitude.
        phase_sigma: float
            Uncertainty in the phase.
        minimum_frequency: float
            Minimum frequency for the spline.
        maximum_frequency: float
            Minimum frequency for the spline.
        n_nodes: int
            Number of nodes for the spline.
        label: str
            Label for the names of the parameters, e.g., recalib_H1_

        Returns
        -------
        prior: PriorDict
            Priors for the relevant parameters.
            This includes the frequencies of the nodes which are _not_ sampled.
        """
        nodes = np.logspace(np.log10(minimum_frequency),
                            np.log10(maximum_frequency), n_nodes)

        amplitude_mean_nodes = [0] * n_nodes
        amplitude_sigma_nodes = [amplitude_sigma] * n_nodes
        phase_mean_nodes = [0] * n_nodes
        phase_sigma_nodes = [phase_sigma] * n_nodes

        prior = CalibrationPriorDict()
        for ii in range(n_nodes):
            name = "recalib_{}_amplitude_{}".format(label, ii)
            latex_label = "$A^{}_{}$".format(label, ii)
            prior[name] = Gaussian(mu=amplitude_mean_nodes[ii],
                                   sigma=amplitude_sigma_nodes[ii],
                                   name=name, latex_label=latex_label)
        for ii in range(n_nodes):
            name = "recalib_{}_phase_{}".format(label, ii)
            latex_label = "$\\phi^{}_{}$".format(label, ii)
            prior[name] = Gaussian(mu=phase_mean_nodes[ii],
                                   sigma=phase_sigma_nodes[ii],
                                   name=name, latex_label=latex_label)
        for ii in range(n_nodes):
            name = "recalib_{}_frequency_{}".format(label, ii)
            latex_label = "$f^{}_{}$".format(label, ii)
            prior[name] = DeltaFunction(peak=nodes[ii], name=name,
                                        latex_label=latex_label)

        return prior


class CalibrationPriorSet(CalibrationPriorDict):

    def __init__(self, dictionary=None, filename=None):
        """ DEPRECATED: USE BNSPriorDict INSTEAD"""
        super(CalibrationPriorSet, self).__init__(dictionary, filename)
        logger.warning("The name 'CalibrationPriorSet' is deprecated use 'CalibrationPriorDict' instead")
