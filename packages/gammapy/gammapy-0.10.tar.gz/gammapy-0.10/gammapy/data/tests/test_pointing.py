# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function, unicode_literals
from numpy.testing import assert_allclose
from astropy.time import Time
from ...utils.testing import requires_data, assert_time_allclose
from ..pointing import PointingInfo


@requires_data("gammapy-data")
class TestPointingInfo:
    @classmethod
    def setup_class(cls):
        filename = "$GAMMAPY_DATA/tests/hess_event_list.fits"
        cls.pointing_info = PointingInfo.read(filename)

    def test_str(self):
        ss = str(self.pointing_info)
        assert "Pointing info" in ss

    def test_location(self):
        lon, lat, height = self.pointing_info.location.geodetic
        assert_allclose(lon.deg, 16.5002222222222)
        assert_allclose(lat.deg, -23.2717777777778)
        assert_allclose(height.value, 1834.999999999783)

    def test_time_ref(self):
        expected = Time(51910.00074287037, format="mjd", scale="tt")
        assert_time_allclose(self.pointing_info.time_ref, expected)

    def test_table(self):
        assert len(self.pointing_info.table) == 100

    def test_time(self):
        time = self.pointing_info.time
        assert len(time) == 100
        expected = Time(53025.826414166666, format="mjd", scale="tt")
        assert_time_allclose(time[0], expected)

    def test_duration(self):
        duration = self.pointing_info.duration
        assert_allclose(duration.sec, 1586.0000000044238)

    def test_radec(self):
        pos = self.pointing_info.radec[0]
        assert_allclose(pos.ra.deg, 83.633333333333)
        assert_allclose(pos.dec.deg, 24.51444444)
        assert pos.name == "icrs"

    def test_altaz(self):
        pos = self.pointing_info.altaz[0]
        assert_allclose(pos.az.deg, 11.45751357)
        assert_allclose(pos.alt.deg, 41.34088901)
        assert pos.name == "altaz"

    def test_altaz_from_table(self):
        pos = self.pointing_info.altaz_from_table[0]
        assert_allclose(pos.az.deg, 11.20432353385406)
        assert_allclose(pos.alt.deg, 41.37921408774436)
        assert pos.name == "altaz"

    def test_altaz_interpolate(self):
        time = self.pointing_info.time[0]
        pos = self.pointing_info.altaz_interpolate(time)
        assert_allclose(pos.az.deg, 11.45751357)
        assert_allclose(pos.alt.deg, 41.34088901)
        assert pos.name == "altaz"
