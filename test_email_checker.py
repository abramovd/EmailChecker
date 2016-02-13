import unittest
from email_checker import EmailChecker, MIN_NAME, MIN_DOMAIN,\
                                       MAX_NAME, MAX_DOMAIN

class TestEmailChecker(unittest.TestCase):
    def setUp(self):
        self.checker = EmailChecker()

    def test_one_at_returns_true(self):
        self.assertTrue(self.checker.check_email('example@yandex.ru'))

    def test_several_ats_returns_false(self):
        self.assertFalse(self.checker.check_email('ex@ample@yand@ex.ru'))

    def test_no_ats_returns_false(self):
            self.assertFalse(self.checker.check_email('exampleyandex.ru'))

    def test_domain_length_less_min_returns_false(self):
        self.assertFalse(self.checker.check_email('example@y.'))

    def test_domain_length_in_range_returns_true(self):
        self.assertTrue(self.checker.check_email('example@google.ru'))

    def test_domain_length_more_max_returns_false(self):
        domain = [str(x) for x in range(MAX_DOMAIN + 1)]
        self.assertFalse(self.checker.check_email('example@' + ''.join(domain)))

    def test_name_length_less_min_returns_false(self):
        self.assertFalse(self.checker.check_email('@yandex.ru'))

    def test_name_length_more_max_returns_false(self):
        name = [str(x) for x in range(MAX_NAME + 1)]
        self.assertFalse(self.checker.check_email(''.join(name) + '@yandex.ru'))

    def test_name_length_in_range_returns_true(self):
        name = [str(x) for x in range(MAX_NAME // 2)]
        self.assertTrue(self.checker.check_email(''.join(name) + '@yandex.ru'))

    def test_simple_domain_numbers_letters_returns_true(self):
        self.assertTrue(self.checker.check_email('example@ya2nde_x1.r1u'))

    def test_name_numbers_letters_returns_true(self):
        self.assertTrue(self.checker.check_email('ex.am21_ple@yandex.ru'))

    def test_simple_domain_bad_sybmols_returns_false(self):
        self.assertFalse(self.checker.check_email('example@ya!n:dex1.r1u'))

    def test_simple_domain_with_dashes_returns_false(self):
        self.assertFalse(self.checker.check_email('example@-yandex.ru'))
        self.assertFalse(self.checker.check_email('example@yandex-.ru'))
        self.assertFalse(self.checker.check_email('example@yandex.ru-'))

    def test_composite_domain_without_dashes_returns_true(self):
        self.assertTrue(self.checker.check_email('example@mail.yandex.ru'))

    def test_composite_domain_with_dashes_returns_false(self):
        self.assertFalse(self.checker.check_email('example@mail.-yandex.ru'))
        self.assertFalse(self.checker.check_email('example@mail.-yandex-.ru'))
        self.assertFalse(self.checker.check_email('example@-mail.-yandex.ru-'))

    def test_name_two_dots_returns_false(self):
        self.assertFalse(self.checker.check_email('exa..mple@mail.yandex.ru'))

    def test_name_two_separated_dots_returns_true(self):
        self.assertTrue(self.checker.check_email('exa.mp.le@mail.yandex.ru'))

    def test_name_one_quote_returns_false(self):
        self.assertFalse(self.checker.check_email('exa\"mple@mail.yandex.ru'))

    def test_name_pairs_of_quotes_returns_true(self):
        self.assertTrue(self.checker.check_email('exa"m"ple@mail.yandex.ru'))

    def test_name_symbols_inside_quotes_returns_true(self):
        self.assertTrue(self.checker.check_email('exa\"!m,m:!\"ple@mail.yandex.ru'))

    def test_name_symbols_outside_quotes_returns_false(self):
        self.assertFalse(self.checker.check_email('!e!x!a\"m\"pl,e;@mail.yandex.ru'))

    def test_empty_email_returns_false(self):
        self.assertFalse(self.checker.check_email(''))

if __name__ == '__main__':
    unittest.main()
