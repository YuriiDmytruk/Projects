import unittest
import Class


class Test(unittest.TestCase):
    def setUp(self):
        print("Test : ", end="")
        self.check_class = Class.Department("123", "Title", None, "+380(87)457-14-87", "345234", "67457",
                                            "www.Workers.com")
        self.fields_arr = ["id", "title", "director_name", "phone_number", "monthly_budget", "yearly_budget",
                           "website_url"]

    def tearDown(self):
        pass

    def test_get_value(self):
        print("Get Value in Department")
        # Success
        self.assertEqual(Class.Department.get_value(self.check_class, 0), "123")
        self.assertEqual(Class.Department.get_value(self.check_class, 2), "None")
        self.assertEqual(Class.Department.get_value(self.check_class, 6), "www.Workers.com")
        # Fail
        self.assertIsNone(Class.Department.get_value(self.check_class, -1))
        self.assertIsNone(Class.Department.get_value(self.check_class, 7))
        self.assertIsNone(Class.Department.get_value(self.check_class, None))
        self.assertIsNone(Class.Department.get_value(None, 1))

    def test_set_value(self):
        print("Set Value in Department")
        # Success
        self.assertEqual(Class.Department.get_value(Class.Department.set_value(self.check_class, "New", 1), 1), "New")
        self.assertEqual(Class.Department.get_value(Class.Department.set_value(self.check_class, "New", 2), 2), "New")
        # Fail
        self.assertIsNone(Class.Department.get_value(Class.Department.set_value(self.check_class, "New", -1), 5))
        self.assertIsNone(Class.Department.get_value(Class.Department.set_value(self.check_class, "New", 7), 1))
        self.assertIsNone(Class.Department.get_value(Class.Department.set_value(None, "New", 1), 1))
        self.assertIsNotNone(Class.Department.get_value(Class.Department.set_value(self.check_class, None, 1), 1))
        self.assertIsNone(Class.Department.get_value(Class.Department.set_value(self.check_class, "New", None), 1))

    def test_create_new_elem(self):
        print("Create new Element in Department")
        # Success
        arr = [[], [1, None, 3, None], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
        self.assertEqual(Class.Department.get_value(Class.Department.create_new_elem(self.check_class, arr[0]), 5),
                         "None")
        self.assertEqual(Class.Department.get_value(Class.Department.create_new_elem(self.check_class, arr[1]), 2),
                         "None")
        self.assertEqual(Class.Department.get_value(Class.Department.create_new_elem(self.check_class, arr[1]), 5),
                         "None")
        self.assertEqual(Class.Department.get_value(Class.Department.create_new_elem(self.check_class, arr[2]), 5),
                         "6")
        # Fail
        self.assertIsNotNone(Class.Department.create_new_elem(self.check_class, arr[0]))
        self.assertIsNotNone(Class.Department.create_new_elem(self.check_class, arr[1]))
        self.assertIsNotNone(Class.Department.create_new_elem(self.check_class, arr[2]))
        self.assertIsNone(Class.Department.create_new_elem(self.check_class, None))
        self.assertIsNone(Class.Department.create_new_elem(None, arr[2]))

    def test_number_of_fields(self):
        print("Number of Fields in Department")
        self.assertIsNotNone(Class.Department.number_of_fields(self.check_class))
        self.assertGreater(Class.Department.number_of_fields(self.check_class), 0)
        self.assertIsNone(Class.Department.number_of_fields(None))

    def test_get_value_by_name(self):
        print("Get Value by Name in Department")
        # Success
        self.assertEqual(Class.Department.get_value_by_name(self.check_class, "id"), "123")
        self.assertEqual(Class.Department.get_value_by_name(self.check_class, "director_name"), "None")
        self.assertEqual(Class.Department.get_value_by_name(self.check_class, "website_url"), "www.Workers.com")
        # Fail
        self.assertIsNone(Class.Department.get_value_by_name(self.check_class, "asdfasdf"))
        self.assertIsNone(Class.Department.get_value_by_name(self.check_class, None))
        self.assertIsNone(Class.Department.get_value_by_name(None, "asdfasdf"))

    def test_set_value_by_name(self):
        print("Set Value by Name in Department")
        # Success
        self.assertEqual(Class.Department.get_value(Class.Department.set_value_by_name(self.check_class, "New",
                                                                                       "title"), 1), "New")
        self.assertEqual(Class.Department.get_value(Class.Department.set_value_by_name(self.check_class, "New",
                                                                                       "director_name"), 2), "New")
        # Fail
        self.assertIsNone(Class.Department.get_value(Class.Department.set_value_by_name(self.check_class, "New",
                                                                                        None), 6))
        self.assertIsNotNone(Class.Department.get_value(Class.Department.set_value_by_name(self.check_class, None,
                                                                                        "director_name"), 1))
        self.assertIsNone(Class.Department.get_value(Class.Department.set_value_by_name(None, "New", "title"), 1))


if __name__ == '__main__':
    unittest.main()