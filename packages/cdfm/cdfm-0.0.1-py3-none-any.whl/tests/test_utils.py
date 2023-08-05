# -*- coding: utf-8 -*-
"""Testing utility functions.
"""
from os.path import abspath, dirname, join
import pytest
import pandas as pd
import numpy as np
from cdfm.config import DTYPE
from cdfm.consts import LABEL, QID, EID, CID, FEATURES, PROXIMITIES
from cdfm.data import CDFMRow
from cdfm.testing import is_equal_rows
from cdfm.utils import load_cdfmdata, build_cdfmdata, make_map, extract_unique_ids


class TestUtils():
    """Testing utility functions in utils.
    """

    def setup_method(self, method) -> None:
        """Setup testing context.
        """
        self.dataset = [
            CDFMRow(0.5, 'a', 'x', ['y', 'z'], np.array([1.0, 2.0, 3.0], dtype=DTYPE), None),
            CDFMRow(-.5, 'a', 'y', ['x', 'z'], np.array([1.0, 2.0, 3.0], dtype=DTYPE), None),
            CDFMRow(0.0, 'a', 'z', ['x', 'y'], np.array([1.0, 2.0, 3.0], dtype=DTYPE), None),
        ]
        self.data_dir = join(dirname(abspath(__file__)), 'resources')

    def teardown_method(self, method) -> None:
        """Clean up testing context.
        """

    def test_load_cdfmdata(self) -> None:
        """Testing dataset.load_data

        Test Cases:
            - types and values in columns.
            - dtypes for FEATURES and PROXIMITIES columns.
        """
        data_path = join(self.data_dir, 'sample_features.txt')
        df = load_cdfmdata(data_path, ndim=4)
        expected_df = pd.DataFrame([
            (0.5, '1', 'x', np.array([0.1, -.2, 0.3, 0.0], dtype=DTYPE)),
            (0.0, '1', 'y', np.array([-.1, 0.2, 0.0, 0.4], dtype=DTYPE)),
            (-.5, '1', 'z', np.array([0.0, -.2, 0.3, -.4], dtype=DTYPE)),
            (0.5, '2', 'y', np.array([0.1, -.2, 0.3, 0.0], dtype=DTYPE)),
            (0.0, '2', 'z', np.array([-.1, 0.2, 0.0, 0.4], dtype=DTYPE)),
            (-.5, '2', 'w', np.array([0.0, -.2, 0.3, -.4], dtype=DTYPE)),
        ], columns=(LABEL, QID, EID, FEATURES))
        assert pd.testing.assert_frame_equal(df, expected_df) is None
        assert isinstance(df.iloc[0, 3], np.ndarray)

    def test_load_proximities(self) -> None:
        """Testing dataset.load_data

        Test Cases:
            - types and values in columns.
            - dtypes for FEATURES and PROXIMITIES columns.
        """
        data_path = join(self.data_dir, 'sample_proximities.txt')
        df = load_cdfmdata(data_path, ndim=2, mode='proximity')
        expected_df = pd.DataFrame([
            ('1', 'x', 'y', np.array([1, 1], dtype=DTYPE)),
            ('1', 'x', 'z', np.array([2, 2], dtype=DTYPE)),
            ('1', 'y', 'x', np.array([3, 3], dtype=DTYPE)),
            ('1', 'y', 'z', np.array([4, 4], dtype=DTYPE)),
            ('1', 'z', 'x', np.array([5, 5], dtype=DTYPE)),
            ('1', 'z', 'y', np.array([6, 6], dtype=DTYPE)),
            ('2', 'y', 'z', np.array([7, 7], dtype=DTYPE)),
            ('2', 'y', 'w', np.array([8, 8], dtype=DTYPE)),
            ('2', 'z', 'y', np.array([9, 9], dtype=DTYPE)),
            ('2', 'z', 'w', np.array([1, 1], dtype=DTYPE)),
            ('2', 'w', 'y', np.array([2, 2], dtype=DTYPE)),
            ('2', 'w', 'z', np.array([3, 3], dtype=DTYPE)),
        ], columns=(QID, EID, CID, PROXIMITIES))
        assert pd.testing.assert_frame_equal(df, expected_df) is None
        assert isinstance(df.iloc[0, 3], np.ndarray)

    def test_build_cdfmdata(self) -> None:
        feat_path = join(self.data_dir, 'sample_features.txt')
        features = load_cdfmdata(feat_path, 4)
        # not using proximities
        data1 = build_cdfmdata(features)
        expected1 = [
            CDFMRow(0.5, '1', 'x', ['y', 'z'], np.array([0.1, -.2, 0.3, 0.0], dtype=DTYPE), None),
            CDFMRow(0.0, '1', 'y', ['x', 'z'], np.array([-.1, 0.2, 0.0, 0.4], dtype=DTYPE), None),
            CDFMRow(-.5, '1', 'z', ['x', 'y'], np.array([0.0, -.2, 0.3, -.4], dtype=DTYPE), None),
            CDFMRow(0.5, '2', 'y', ['z', 'w'], np.array([0.1, -.2, 0.3, 0.0], dtype=DTYPE), None),
            CDFMRow(0.0, '2', 'z', ['y', 'w'], np.array([-.1, 0.2, 0.0, 0.4], dtype=DTYPE), None),
            CDFMRow(-.5, '2', 'w', ['y', 'z'], np.array([0.0, -.2, 0.3, -.4], dtype=DTYPE), None),
        ]
        for this, that in zip(data1, expected1):
            assert is_equal_rows(this, that)

    def test_build_cdfmdata_with_proximities(self) -> None:
        feat_path = join(self.data_dir, 'sample_features.txt')
        prox_path = join(self.data_dir, 'sample_proximities.txt')
        features = load_cdfmdata(feat_path, 16)
        proximities = load_cdfmdata(prox_path, 2, mode='proximity')
        try:
            res = build_cdfmdata(features, proximities)
        except KeyError:
            pytest.fail('failed to build dataset...')

    def test_extract_unique_ids(self) -> None:
        unique_ids = extract_unique_ids(self.dataset)
        expected = {'x', 'y', 'z'}
        assert unique_ids == expected

    def test_make_map(self) -> None:
        unique_ids = extract_unique_ids(self.dataset)
        mapper = make_map(unique_ids)
        assert set(mapper.keys()) == {'x', 'y', 'z'}
        assert set(mapper.values()) == {0, 1, 2}
