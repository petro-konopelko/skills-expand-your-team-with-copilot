import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from backend.database import initial_activities


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


if __name__ == "__main__":
    unittest.main()
