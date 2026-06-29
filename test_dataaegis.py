# test_dataaegis.py
"""
Tests for DataAegis module.
"""

import unittest
from dataaegis import DataAegis

class TestDataAegis(unittest.TestCase):
    """Test cases for DataAegis class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataAegis()
        self.assertIsInstance(instance, DataAegis)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataAegis()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
