import unittest

from app.components.SquadsComponent import SquadsComponent
from testing.DataSeed import DataSeed


class TestSquadComponent(unittest.TestCase):

    def setUp(self):
        self.component = SquadsComponent()

    def test_maintenance(self):
        name = DataSeed.generate_name("squad{}")
        self.component.create({"name": name})
        entity = self.component.get_by_name(name)
        self.assertTrue(entity)








