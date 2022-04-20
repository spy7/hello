from src.compare import Compare


class TestCompare:
    TITLE = "Hello, world!"

    def test_diff_with_same_message(self):
        compare = Compare(self.TITLE, self.TITLE)
        assert compare.diff() == 0

    def test_diff_with_different_message(self):
        compare = Compare(self.TITLE, "Ants")
        assert compare.diff() == 100

    def test_diff_with_similar_message(self):
        compare = Compare(self.TITLE, "Hello")
        assert int(compare.diff()) == 25
