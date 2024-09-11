import unittest
from tilores import TiloresAPI
from langchain_tilores import TiloresTools

class IntegrationTest(unittest.TestCase):
    """
    This is a set of tests run against a specific Tilores instance,
    pre-configured with a fixed schema and fixed test data.

    Before running these tests, obtain a set of API credentials and
    provide them in your environemnt. See also: .envrc.example
    """
    @classmethod
    def setUpClass(cls):
        cls.tilores = TiloresAPI.from_environ()

    def test_dynamic_search_tool(self):
        dynamic_tools = TiloresTools(self.tilores)
        tool = dynamic_tools.search_tool
        self.assertEqual(tool.name, 'tilores_search')
        self.assertEqual(tool.description, 'useful for when you need to search entities on variable parameters')
        self.assertEqual(tool.return_direct, True)
        self.assertListEqual([*tool.args.keys()], self.tilores.search_param_names)

if __name__ == '__main__':
    unittest.main()

