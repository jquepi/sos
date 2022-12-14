# This file is part of the sos project: https://github.com/sosreport/sos
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.

from sos.report.plugins import Plugin, IndependentPlugin


class SkipVersions(Plugin, IndependentPlugin):
    """Collect the fake version files from the test suite, to ensure proper
    skipping of version files
    """

    plugin_name = 'skip_versions'
    short_desc = 'fake plugin to test skipping version files via the IP parser'

    def setup(self):
        self.add_copy_spec([
            '/tmp/sos-test-version.txt',
            '/tmp/sos-test-version-noskip'
        ])
