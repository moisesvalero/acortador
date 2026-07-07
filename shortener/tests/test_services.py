from django.test import TestCase

from shortener.services import (
    base62_encode,
    generate_short_code,
    hash_ip,
)


class Base62EncodeTests(TestCase):
    def test_zero(self):
        self.assertEqual(base62_encode(0), "0")

    def test_ten(self):
        self.assertEqual(base62_encode(10), "a")

    def test_sixty_one(self):
        self.assertEqual(base62_encode(61), "Z")

    def test_sixty_two(self):
        self.assertEqual(base62_encode(62), "10")

    def test_large_number(self):
        result = base62_encode(1000000)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 3)

    def test_small_number(self):
        result = base62_encode(5)
        self.assertEqual(result, "5")


class GenerateShortCodeTests(TestCase):
    def test_minimum_length(self):
        for i in range(1, 100):
            code = generate_short_code(i)
            self.assertGreaterEqual(len(code), 6)

    def test_no_collision_in_range(self):
        codes = {generate_short_code(i) for i in range(1, 1000)}
        self.assertEqual(len(codes), 999)

    def test_different_ids_different_codes(self):
        code1 = generate_short_code(1)
        code2 = generate_short_code(2)
        self.assertNotEqual(code1, code2)

    def test_consistent_for_same_id(self):
        code1 = generate_short_code(42)
        code2 = generate_short_code(42)
        self.assertEqual(code1, code2)

    def test_rejects_all_zero(self):
        code = generate_short_code(1)
        self.assertNotEqual(code, "000000")


class HashIpTests(TestCase):
    def test_returns_hex_string(self):
        result = hash_ip("127.0.0.1")
        self.assertEqual(len(result), 64)
        self.assertTrue(all(c in "0123456789abcdef" for c in result))

    def test_deterministic(self):
        self.assertEqual(hash_ip("192.168.1.1"), hash_ip("192.168.1.1"))

    def test_different_ips_different_hashes(self):
        self.assertNotEqual(hash_ip("127.0.0.1"), hash_ip("192.168.1.1"))
