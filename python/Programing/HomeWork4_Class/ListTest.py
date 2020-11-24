import unittest
import list
import momento


class Test(unittest.TestCase):
    def setUp(self):
        print("Test", end="")
        self.history = momento.CareTaker()
        self.list = list.LinkedList()
        list.text_start()
        list.LinkedList.read_from_file(self.list)

    def tearDown(self):
        pass

    def test_read_from_file(self):
        print("Read from File in List")
        self.assertIsNotNone(list.LinkedList.read_from_file(self.list))
        self.assertIsNone(list.LinkedList.read_from_file(None))

    def test_add_to_end(self):
        print("Add to End in List")
        self.assertIsNotNone(list.LinkedList.add_to_end(self.list, None))
        self.assertIsNone(list.LinkedList.add_to_end(None, None))
        self.assertIsNotNone(list.LinkedList.add_to_end(self.list, "New"))

    def test_return_len(self):
        print("Return Len in List")
        self.assertIsNotNone(list.LinkedList.return_len(self.list))
        self.assertGreaterEqual(list.LinkedList.return_len(self.list), 0)
        self.assertIsNone(list.LinkedList.return_len(None))

    def test_renew_file(self):
        print("Renew File in List")
        self.assertIsNone(list.LinkedList.renew_file(None))

    def test_add_new_element(self):
        print("Add new Element in List")
        arr = []
        self.assertIsNone(list.LinkedList.add_new_element(None, arr))
        self.assertIsNotNone(list.LinkedList.add_new_element(self.list, None))

    def test_remove_last(self):
        print("Remove Last in List")
        self.assertIsNotNone(list.LinkedList.return_len(self.list))
        self.assertIsNone(list.LinkedList.return_len(None))

    def test_delete_element(self):
        print("Delete Element in List")
        self.assertIsNone(list.LinkedList.delete_element(self.list, "123"))
        self.assertIsNone(list.LinkedList.delete_element(None, "123"))
        self.assertIsNone(list.LinkedList.delete_element(self.list, None))
        x = list.LinkedList.copy_list(self.list)
        x = list.LinkedList.delete_element(x, "114")
        self.assertLess(list.LinkedList.return_len(x), list.LinkedList.return_len(self.list))

    def test_change_element(self):
        print("Change Element in List")
        self.assertIsNotNone(list.LinkedList.change_element(self.list, "114", 1, None))
        self.assertIsNone(list.LinkedList.change_element(self.list, "123", None, "Value"))
        self.assertIsNone(list.LinkedList.change_element(self.list, None, 4, "Value"))
        self.assertIsNone(list.LinkedList.change_element(None, "123", 4, "Value"))

    def test_search_element(self):
        print("Search Element in List")
        self.assertIsNotNone(list.LinkedList.search_element(self.list, "114"))
        self.assertIsNone(list.LinkedList.search_element(None, "123"))
        self.assertIsNone(list.LinkedList.search_element(self.list, None))

    def test_list_move_end(self):
        print("List move to End in List")
        self.assertIsNotNone(list.LinkedList.list_move_end(self.list, 2))
        self.assertIsNone(list.LinkedList.list_move_end(None, 2))
        self.assertIsNone(list.LinkedList.list_move_end(self.list, None))

    def test_sort_by_elements(self):
        print("Sort by Elements in List")
        self.assertIsNone(list.LinkedList.sort_by_elements(self.list, None))
        self.assertIsNotNone(list.LinkedList.sort_by_elements(self.list, 2))
        self.assertIsNone(list.LinkedList.sort_by_elements(self.list, 10))
        self.assertIsNone(list.LinkedList.sort_by_elements(None, None))

    def test_copy_list(self):
        print("Copy List in List")
        self.assertIsNone(list.LinkedList.copy_list(None))
        self.assertIsNotNone(list.LinkedList.copy_list(self.list))

    def test_undo(self):
        print("Undo in List")
        self.assertIsNone(list.LinkedList.undo(None, self.history))
        self.assertIsNone(list.LinkedList.undo(self.list, None))
        self.assertIsNotNone(list.LinkedList.undo(self.list, self.history))

    def test_redo(self):
        print("Redo in List")
        self.assertIsNone(list.LinkedList.redo(None, self.history))
        self.assertIsNone(list.LinkedList.redo(self.list, None))
        self.assertIsNotNone(list.LinkedList.redo(self.list, self.history))


if __name__ == '__main__':
    unittest.main()
