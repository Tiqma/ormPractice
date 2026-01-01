"""Tests for seed"""

from tests.base import BaseTestCase
from app.seed import load_colors_from_json
import os

class SeedTestCase(BaseTestCase):
    def test_load_colors(self):
        path = os.path.join(os.path.dirname(__file__), "..", "colors.json")
        added = load_colors_from_json(path)
        self.assertEqual(added, 5)
