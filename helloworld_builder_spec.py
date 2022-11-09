from unittest import TestCase
from helloworld_builder import HelloWorldBuilder

class BuilderTestCase(TestCase):
  def setUp(self):
    self.builder = HelloWorldBuilder._decorated()

  def test_only_uses_first_character(self):
    self.builder.add_char("foo")
    self.assertListEqual(self.builder._chars, ["f"])
    self.assertEqual(self.builder.build(), "f")

  def test_concats_given_values(self):
    self.builder.add_char("a")
    self.builder.add_char("b")
    self.builder.add_char("c")
    self.builder.add_char("d")
    self.builder.add_char("e")
    self.builder.add_char("f")
    self.builder.add_char("g")

    self.assertEqual(self.builder.build(), "abcdefg")

  def test_non_string_gives_typeerror(self):
    with self.assertRaises(TypeError):
      self.builder.add_char(42)