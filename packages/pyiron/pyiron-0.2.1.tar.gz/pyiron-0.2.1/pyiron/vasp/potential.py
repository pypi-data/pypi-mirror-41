# coding: utf-8
# Copyright (c) Max-Planck-Institut für Eisenforschung GmbH - Computational Materials Design (CM) Department
# Distributed under the terms of "New BSD License", see the LICENSE file.

import pandas
from pyiron.atomistics.job.potentials import PotentialAbstract

__author__ = "Jan Janssen"
__copyright__ = "Copyright 2019, Max-Planck-Institut für Eisenforschung GmbH - " \
                "Computational Materials Design (CM) Department"
__version__ = "1.0"
__maintainer__ = "Jan Janssen"
__email__ = "janssen@mpie.de"
__status__ = "development"
__date__ = "Sep 1, 2017"


class VaspPotentialAbstract(PotentialAbstract):
    """

    Args:
        potential_df:
        default_df:
        selected_atoms:
    """
    def __init__(self, potential_df=None, default_df=None, selected_atoms=None):
        if potential_df is None:
            potential_df = self._get_potential_df(plugin_name='vasp',
                                                  file_name_lst={'potentials_vasp.csv'},
                                                  backward_compatibility_name='vasppotentials')
        super(VaspPotentialAbstract, self).__init__(potential_df=potential_df, default_df=default_df,
                                                    selected_atoms=selected_atoms)

    def default(self):
        if self._default_df is not None:
            return pandas.concat(
                [self._potential_df[(self._potential_df['Name'] == self._default_df.loc[atom].values[0])] for atom in
                 self._selected_atoms])
        return None

    def find_default(self, element):
        if isinstance(element, set):
            element = element
        elif isinstance(element, list):
            element = set(element)
        elif isinstance(element, str):
            element = set([element])
        else:
            raise TypeError('Only, str, list and set supported!')
        element_lst = list(element)
        if self._default_df is not None:
            merged_lst = list(set(self._selected_atoms + element_lst))
            return pandas.concat(
                [self._potential_df[(self._potential_df['Name'] == self._default_df.loc[atom].values[0])] for atom in
                 merged_lst])
        return None

    def find(self, element):
        if isinstance(element, set):
            element = element
        elif isinstance(element, list):
            element = set(element)
        elif isinstance(element, str):
            element = set([element])
        else:
            raise TypeError('Only, str, list and set supported!')
        element_lst = list(element)
        merged_lst = list(set(self._selected_atoms + element_lst))
        return pandas.concat([super(VaspPotentialAbstract, self).find({atom}) for atom in merged_lst])

    def list(self):
        return pandas.concat([super(VaspPotentialAbstract, self).find({atom}) for atom in self._selected_atoms])

    def __getitem__(self, item):
        selected_atoms = self._selected_atoms + [item]
        return VaspPotentialAbstract(potential_df=self._potential_df, default_df=self._default_df,
                                     selected_atoms=selected_atoms)


class VaspPotentialFile(VaspPotentialAbstract):
    """
    The Potential class is derived from the PotentialAbstract class, but instead of loading the potentials from a list,
    the potentials are loaded from a file.

    Args:
        xc (str): Exchange correlation functional ['PBE', 'LDA']
    """
    def __init__(self, xc=None):
        potential_df = self._get_potential_df(plugin_name='vasp',
                                              file_name_lst={'potentials_vasp.csv'},
                                              backward_compatibility_name='vasppotentials')
        if xc == "PBE":
            default_df = self._get_potential_default_df(plugin_name='vasp',
                                                        file_name_lst={'potentials_vasp_pbe_default.csv'},
                                                        backward_compatibility_name='defaultvasppbe')
            potential_df = potential_df[(potential_df['Model'] == 'gga-pbe')]
        elif xc == "GGA":
            default_df = self._get_potential_default_df(plugin_name='vasp',
                                                        file_name_lst={'potentials_vasp_pbe_default.csv'},
                                                        backward_compatibility_name='defaultvasppbe')
            potential_df = potential_df[(potential_df['Model'] == 'gga-pbe')]
        elif xc == "LDA":
            default_df = self._get_potential_default_df(plugin_name='vasp',
                                                        file_name_lst={'potentials_vasp_lda_default.csv'},
                                                        backward_compatibility_name='defaultvasplda')
            potential_df = potential_df[(potential_df['Model'] == 'lda')]
        else:
            raise ValueError('The exchange correlation functional has to be set and it can either be "LDA" or "PBE"')
        super(VaspPotentialFile, self).__init__(potential_df=potential_df, default_df=default_df, selected_atoms=[])

    def add_new_element(self, parent_element, new_element):
        """
        Adding a new user defined element with a different POTCAR file. It is assumed that the file exists

        Args:
            parent_element (str): Parent element
            new_element (str): Name of the new element (the name of the folder where the new POTCAR file exists

        """
        ds = self.find_default(element=parent_element)
        ds["Species"].values[0][0] = new_element
        path_list = ds["Filename"].values[0][0].split("/")
        path_list[-2] = new_element
        name_list = ds["Name"].values[0].split("-")
        name_list[0] = new_element
        ds["Name"].values[0] = "-".join(name_list)
        ds["Filename"].values[0][0] = "/".join(path_list)
        self._potential_df = self._potential_df.append(ds)
        ds = pandas.Series()
        ds.name = new_element
        ds["Name"] = "-".join(name_list)
        self._default_df = self._default_df.append(ds)


class VaspPotential(object):
    """
    The Potential class is derived from the PotentialAbstract class, but instead of loading the potentials from a list,
    the potentials are loaded from a file.

    Args:
        path (str): path to the potential list
    """

    def __init__(self):
        self.pbe = VaspPotentialFile(xc="PBE")
        self.lda = VaspPotentialFile(xc="LDA")
