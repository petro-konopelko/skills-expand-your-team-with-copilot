import sys
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from backend.database import initial_activities
from backend.routers.activities import get_activities


class MangaManiacsDatabaseTest(unittest.TestCase):
    def test_manga_maniacs_is_seeded_with_expected_details(self):
        activity = initial_activities["Manga Maniacs"]

        self.assertEqual(
            activity["description"],
            "Embark on epic adventures with unforgettable heroes, rivalries, and hidden powers from the world of Japanese manga and graphic novels.",
        )
        self.assertEqual(activity["max_participants"], 15)
        self.assertEqual(activity["participants"], [])
        self.assertEqual(activity["schedule_details"]["days"], ["Tuesday"])
        self.assertEqual(activity["schedule_details"]["start_time"], "19:00")
        self.assertEqual(activity["schedule_details"]["end_time"], "20:30")

    def test_activity_difficulty_is_optional_and_filter_uses_unspecified_all(self):
        self.assertIn("difficulty", initial_activities["Programming Class"])
        self.assertNotIn("difficulty", initial_activities["Art Club"])

        with patch("backend.routers.activities.activities_collection.find") as find_mock:
            find_mock.side_effect = [
                [{"_id": "Beginner Club", "description": "Intro", "difficulty": "Beginner"}],
                [{"_id": "Open Club", "description": "For everyone"}],
            ]

            beginner_results = get_activities(difficulty="Beginner")
            all_results = get_activities(difficulty="all")

        self.assertEqual(find_mock.call_count, 2)
        self.assertEqual(find_mock.call_args_list[0].args[0], {"difficulty": "Beginner"})
        self.assertEqual(find_mock.call_args_list[1].args[0], {"difficulty": {"$exists": False}})
        self.assertEqual(list(beginner_results.keys()), ["Beginner Club"])
        self.assertEqual(list(all_results.keys()), ["Open Club"])


if __name__ == "__main__":
    unittest.main()
