import unittest

from Class_Task.DiaryApplication.Diary import Diary
from Class_Task.DiaryApplication.Entry import Entry


class DiaryTest(unittest.TestCase):

    def test_that_we_have_a_diary_object(self):
        my_diary = Diary("Edmund Udeh", "password")
        self.assertIsNotNone(my_diary)

    def test_that_diary_is_locked(self):
        my_diary = Diary("Edmund Udeh", "password")
        my_diary.locked()
        self.assertTrue(my_diary.get_is_locked())

    def test_you_can_create_entry_in_diary(self):
        my_diary = Diary("Edmund Udeh", "password")
        my_diary.create_entry("God's love", "God is love")
        self.assertEqual(Entry(1, "God's love", "God is love").get_entry(),
                         my_diary.find_entry(1).get_entry())

    def test_you_can_create_multiple_entries_in_diary(self):
        my_diary = Diary("Edmund Udeh", "password2")
        my_diary.create_entry("God's love", "God is love2")
        self.assertEqual(Entry(1, "God's love", "God is love2").get_entry(),
                         my_diary.find_entry(1).get_entry())
        my_diary.create_entry("Love story", "Love is me")
        self.assertEqual(Entry(2, "Love story", "Love is me").get_entry(),
                         my_diary.find_entry(2).get_entry())

    def test_you_can_delete_entry_from_diary(self):
        my_diary = Diary("Edmund Udeh", "password1")
        my_diary.create_entry("God's love", "God is love1")
        self.assertEqual(Entry(1, "God's love", "God is love1").get_entry(),
                         my_diary.find_entry(1).get_entry())
        my_diary.create_entry("Love story", "Love is me")
        self.assertEqual(Entry(2, "Love story", "Love is me").get_entry(),
                         my_diary.find_entry(2).get_entry())
        my_diary.delete_entry(1)
        with self.assertRaises(ValueError):
            my_diary.find_entry(1)

    def test_to_find_entry_by_id(self):
        my_diary = Diary("Edmund Udeh", "password")
        my_diary.create_entry("God's love", "God is love")
        my_diary.create_entry("Love story", "Love is me")
        entry = my_diary.find_entry(2)
        self.assertEqual(Entry(2, "Love story", "Love is me").get_entry(), entry.get_entry())

    def test_to_update_entry_in_diary(self):
        my_diary = Diary("Edmund Udeh", "password")
        my_diary.create_entry("God's love", "God is love")
        self.assertEqual(Entry(1, "God's love", "God is love").get_entry(),
                         my_diary.find_entry(1).get_entry())
        my_diary.create_entry("Love story", "Love is me")
        self.assertEqual(Entry(2, "Love story", "Love is me").get_entry(),
                         my_diary.find_entry(2).get_entry())
        my_diary.update_entry(1, "Make money", "I am a money magnet")
        self.assertEqual(Entry(1, "Make money", "I am a money magnet").get_entry(),
                         my_diary.find_entry(1).get_entry())


if __name__ == '__main__':
    unittest.main()
