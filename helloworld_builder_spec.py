from unittest import TestCase
from helloworld_builder import HelloWorldBuilder

class BuilderTestCase(TestCase):
  def setUp(self):
    self.builder = HelloWorldBuilder._decorated()

  def test_only_uses_first_character(self):
    self.builder.add_char("foo")
    self.assertListEqual(self.builder._chars, ["f"])
    self.assertEqual(self.builder.build(), "f")