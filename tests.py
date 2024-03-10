import unittest
from get_score import get_score


class TestGetScore(unittest.TestCase):

    def test_get_score_when_offset_exists(self):
        # Проверка, что функция возвращает правильный счет, если offset
        # существует
        game_stamps = [
            {"offset": 1, "score": {"home": 2, "away": 1}},
            {"offset": 2, "score": {"home": 0, "away": 0}},
            {"offset": 3, "score": {"home": 3, "away": 1}}
        ]
        home_score, away_score = get_score(game_stamps, 2)
        self.assertEqual(home_score, 0)
        self.assertEqual(away_score, 0)

    def test_get_score_when_offset_does_not_exist(self):
        # Проверка, что функция возвращает None, если offset не существует
        game_stamps = [
            {"offset": 1, "score": {"home": 2, "away": 1}},
            {"offset": 3, "score": {"home": 3, "away": 1}}
        ]
        result = get_score(game_stamps, 2)
        self.assertIsNone(result)

    def test_get_score_when_empty_game_stamps(self):
        # Проверка, что функция возвращает None, если game_stamps пуст
        game_stamps = []
        result = get_score(game_stamps, 2)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
