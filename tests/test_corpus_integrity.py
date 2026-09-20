"""Integrity/measurement regression checks for book evidence."""
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from analyze_corpus import load_corpus, lexical_tokens


class CorpusIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest, cls.verses = load_corpus()

    def test_numbered_boundaries(self):
        self.assertEqual((self.verses[0]['surah'], self.verses[0]['verse']), (1, 1))
        self.assertEqual((self.verses[-1]['surah'], self.verses[-1]['verse']), (114, 6))
        self.assertEqual(len({(v['surah'], v['verse']) for v in self.verses}), 6236)

    def test_asr_against_hand_count(self):
        verses = [v for v in self.verses if v['surah'] == 103]
        self.assertEqual([v['lexical_tokens'] for v in verses], [1, 4, 9])

    def test_signs_are_not_words(self):
        self.assertEqual(len(lexical_tokens('ۚ ۩ ۞')), 0)
        self.assertEqual(len(lexical_tokens('قُلْ ۚ هُوَ')), 2)

    def test_attached_clitic_is_one_orthographic_token(self):
        self.assertEqual(len(lexical_tokens('وَتَوَاصَوْا۟')), 1)

    def test_basmala_policy(self):
        first_asr = next(v for v in self.verses if (v['surah'], v['verse']) == (103, 1))
        first_fatiha = self.verses[0]
        self.assertEqual(first_asr['lexical_tokens'], 1)
        self.assertEqual(first_fatiha['lexical_tokens'], 4)


if __name__ == '__main__':
    unittest.main()
