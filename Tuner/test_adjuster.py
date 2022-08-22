import unittest
from adjuster import oscar_calculator, rating_penalizer


class RatingPenalizerTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_when_difference_zero_expect_zero_penalty(self):
        penalty = rating_penalizer(0, 0)
        self.assertEqual(penalty, 0)
        penalty = rating_penalizer(100, 100)
        self.assertEqual(penalty, 0)
        penalty = rating_penalizer(100000, 100000)
        self.assertEqual(penalty, 0)

    def test_when_difference_one_expect_zero_penalty(self):
        penalty = rating_penalizer(0, 1)
        self.assertEqual(penalty, 0)
        penalty = rating_penalizer(100, 101)
        self.assertEqual(penalty, 0)
        penalty = rating_penalizer(100000, 100001)
        self.assertEqual(penalty, 0)

    def test_when_difference_below_treshold_expect_zero_penalty(self):
        penalty = rating_penalizer(0, 99999)
        self.assertEqual(penalty, 0)
        penalty = rating_penalizer(100, 100099)
        self.assertEqual(penalty, 0)
        penalty = rating_penalizer(100000, 199999)
        self.assertEqual(penalty, 0)

    def test_when_difference_is_100000_expect_0_1_penalty(self):
        penalty = rating_penalizer(0, 100000)
        self.assertEqual(penalty, 0.1)
        penalty = rating_penalizer(100, 100100)
        self.assertEqual(penalty, 0.1)
        penalty = rating_penalizer(100000, 200000)
        self.assertEqual(penalty, 0.1)

    def test_when_difference_is_100001_expect_0_1_penalty(self):
        penalty = rating_penalizer(0, 100001)
        self.assertEqual(penalty, 0.1)
        penalty = rating_penalizer(100, 100101)
        self.assertEqual(penalty, 0.1)
        penalty = rating_penalizer(100000, 200001)
        self.assertEqual(penalty, 0.1)

    def test_when_difference_is_199999_expect_0_1_penalty(self):
        penalty = rating_penalizer(0, 199999)
        self.assertEqual(penalty, 0.1)
        penalty = rating_penalizer(100, 200099)
        self.assertEqual(penalty, 0.1)
        penalty = rating_penalizer(100000, 299999)
        self.assertEqual(penalty, 0.1)

    def test_when_difference_is_200000_expect_0_2_penalty(self):
        penalty = rating_penalizer(0, 200000)
        self.assertEqual(penalty, 0.2)
        penalty = rating_penalizer(100, 200100)
        self.assertEqual(penalty, 0.2)
        penalty = rating_penalizer(100000, 300000)
        self.assertEqual(penalty, 0.2)

    def test_when_difference_is_200001_expect_0_2_penalty(self):
        penalty = rating_penalizer(0, 200001)
        self.assertEqual(penalty, 0.2)
        penalty = rating_penalizer(100, 200101)
        self.assertEqual(penalty, 0.2)
        penalty = rating_penalizer(100000, 300001)
        self.assertEqual(penalty, 0.2)


class OscarCalculatorTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_0_oscar(self):
        oscar_adjustment = oscar_calculator(0)
        self.assertEqual(oscar_adjustment, 0)

    def test_1_2_oscars(self):
        oscars = [1, 2]
        for oscar in oscars:
            oscar_adjustment = oscar_calculator(oscar)
            self.assertEqual(oscar_adjustment, 0.3)

    def test_3_5_oscars(self):
        oscars = [3, 4, 5]
        for oscar in oscars:
            oscar_adjustment = oscar_calculator(oscar)
            self.assertEqual(oscar_adjustment, 0.5)

    def test_6_10_oscars(self):
        for oscar in range(6, 11):
            oscar_adjustment = oscar_calculator(oscar)
            self.assertEqual(oscar_adjustment, 1.0)

    def test_over_10_oscars(self):
        oscar_adjustment = oscar_calculator(11)
        self.assertEqual(oscar_adjustment, 1.5)
        oscar_adjustment = oscar_calculator(100)
        self.assertEqual(oscar_adjustment, 1.5)
