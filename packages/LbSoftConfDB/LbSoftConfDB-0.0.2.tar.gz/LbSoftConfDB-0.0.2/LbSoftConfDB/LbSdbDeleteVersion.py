#!/usr/bin/env python
"""
Script to update links to project version nodes

"""
import logging
import sys

from LbCommon.Script import Script
from LbSoftConfDB.SoftConfDB import SoftConfDB


class LbSdbDeleteVersion(Script):
    """ Delete information about a project / version """

    def defineOpts(self):
        """ Script specific options """
        parser = self.parser
        parser.add_option("-d",
                          dest = "debug",
                          action = "store_true",
                          help = "Display debug output")

    def main(self):
        """ Main method for bootstrap and parsing the options.
        It invokes the appropriate method and  """
        self.log = logging.getLogger()
        opts = self.options
        args = self.args
        if opts.debug:
            self.log.setLevel(logging.DEBUG)
        else:
            self.log.setLevel(logging.WARNING)
        if len(args) < 2 :
            self.log.error("Not enough arguments")
            sys.exit(1)
        else :
            project   = args[0].upper()
            version   = args[1]

            # Connect to the ConfDB to update the platform
            self.mConfDB = SoftConfDB()
            self.mConfDB.deletePV(project, version)


def main():
    sUsage = """%prog project version  """
    s = LbSdbDeleteVersion(usage=sUsage)
    sys.exit(s.run())


if __name__=='__main__':
    main()
