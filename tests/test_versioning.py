import unittest

from scripts.bump_version import next_version


class VersionIncrementTests(unittest.TestCase):
    def test_regular_increment(self):
        self.assertEqual(next_version("2.2.7"), "2.2.8")
        self.assertEqual(next_version("2.2.8"), "2.2.9")

    def test_minor_rollover(self):
        self.assertEqual(next_version("2.2.9"), "2.3.0")

    def test_major_rollover(self):
        self.assertEqual(next_version("2.9.9"), "3.0.0")

    def test_major_above_nine(self):
        self.assertEqual(next_version("12.9.9"), "13.0.0")

    def test_invalid_versions(self):
        for version in ("2.2.7.4.9", "2.2.10", "2.10.0", "v2.2.7", "2.2", ""):
            with self.subTest(version=version):
                with self.assertRaises(ValueError):
                    next_version(version)


if __name__ == "__main__":
    unittest.main()
