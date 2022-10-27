from unittest import TestCase
from singleton import Singleton

class SingletonTestCase(TestCase):
  def setUp(self):
    @Singleton
    class Foo:
      def bar(self):
        return "baz"
    self._class = Foo
  def test_calling_singleton_throws_typeerror(self):
    with self.assertRaises(TypeError):
      self._class()
  def test_multiple_instance_calls_return_same_object(self):
    i1 = self._class.instance()
    i2 = self._class.instance()
    self.assertIs(i1, i2)
  def test_instance_property(self):
    self.assertFalse(hasattr(self._class, "_instance"))
    i = self._class.instance()
    self.assertIs(self._class._instance, i)