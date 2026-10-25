
import unittest

from password_checker import (
    calculate_entropy,
    score_password,
    generate_password,
)


class TestPasswordChecker(unittest.TestCase):

    def test_empty_password_entropy(self):
        self.assertEqual(calculate_entropy(""), 0)

    def test_password_length(self):
        result = score_password("pass1234")
        self.assertEqual(result["length"], 8)

    def test_common_password_is_weak(self):
        result = score_password("password")
        self.assertEqual(result["verdict"], "Weak")

    def test_long_mixed_password(self):
        result = score_password("River!Cloud7Map#92")
        self.assertGreaterEqual(result["length"], 12)
        self.assertGreaterEqual(result["entropy"], 50)

    def test_score_is_within_range(self):
        result = score_password("Example!Pass123")
        self.assertGreaterEqual(result["score"], 0)
        self.assertLessEqual(result["score"], 100)

    def test_password_generator_length(self):
        generated = generate_password(16)
        self.assertEqual(len(generated), 16)

    def test_generated_password_has_variety(self):
        generated = generate_password(16)
        self.assertTrue(any(c.islower() for c in generated))
        self.assertTrue(any(c.isupper() for c in generated))
        self.assertTrue(any(c.isdigit() for c in generated))
        self.assertTrue(
            any(c in "!@#$%^&*()-_=+?" for c in generated)
        )

    def test_generator_rejects_short_length(self):
        with self.assertRaises(ValueError):
            generate_password(8)


if __name__ == "__main__":
    unittest.main()
