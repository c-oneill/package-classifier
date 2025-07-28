import unittest
from package_classifier import sort, PackageCategory

class TestPackageClassifier(unittest.TestCase):

    def test_standard_package(self):
        # Not heavy, not bulky
        self.assertEqual(sort(10, 10, 10, 10), PackageCategory.STANDARD)

    def test_heavy_only(self):
        # Heavy (mass ≥ 20), not bulky
        self.assertEqual(sort(10, 10, 10, 25), PackageCategory.SPECIAL)

    def test_bulky_only_by_dimension_width(self):
        # Bulky due to dimension ≥ 150, not heavy
        self.assertEqual(sort(150, 10, 10, 10), PackageCategory.SPECIAL)
        
    def test_bulky_only_by_dimension_height(self):
        # Bulky due to dimension ≥ 150, not heavy
        self.assertEqual(sort(10, 150, 10, 10), PackageCategory.SPECIAL)
        
    def test_bulky_only_by_dimension_length(self):
        # Bulky due to dimension ≥ 150, not heavy
        self.assertEqual(sort(10, 10, 150, 10), PackageCategory.SPECIAL)

    def test_bulky_only_by_volume(self):
        # Bulky due to volume ≥ 1,000,000, not heavy
        self.assertEqual(sort(120, 120, 120, 10), PackageCategory.SPECIAL)
        
    def test_edge_case_volume(self):
        # Exactly at volume threshold
        self.assertEqual(sort(100, 100, 100, 19), PackageCategory.SPECIAL)

    def test_heavy_and_bulky_and_over_dimension(self):
        # Heavy and bulky
        self.assertEqual(sort(151, 200, 300, 30), PackageCategory.REJECTED)
        
    def test_heavy_and_bulky_by_dimension(self):
        # Heavy and bulky by dimension
        self.assertEqual(sort(151, 1, 1, 30), PackageCategory.REJECTED)

    def test_edge_case_mass(self):
        # Exactly at mass threshold
        self.assertEqual(sort(10, 10, 10, 20), PackageCategory.SPECIAL)


if __name__ == "__main__":
    unittest.main()
