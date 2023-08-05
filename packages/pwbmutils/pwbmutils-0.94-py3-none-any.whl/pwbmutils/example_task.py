"""Contains sample luigi task illustrating the use of PWBMTask.
"""

__author__ = "Nick Janetos"
__copyright__ = "2018 Penn Wharton Budget Model"

import os
from os.path import exists, join

import pandas

import pwbmutils

from pwbmutils.map_target import MapTarget

# pylint: disable=E1101, E1136

class ExampleTask(pwbmutils.PWBMTask):
    """Example task illustrates the use of PWBM task.
    """

    def requires(self):
        """Requires the interface reader.
        """

        return pwbmutils.InterfaceReader(
            interface_info={
                "version": "2018-05-21-21-55-arnon-d43fbc6",
                "interface": "projections",
                "component": "Projections"
            },
            filename="Projections.csv"
        )


    def work(self):
        """Loads the projections then saves them out.
        """

        # load projections
        projections = pandas.read_csv(self.requires().output().path)

        # save to output locationm
        if not exists(self.output().path):
            os.makedirs(self.output().path)

        projections.to_csv(join(self.output().path, "projections.csv"))
