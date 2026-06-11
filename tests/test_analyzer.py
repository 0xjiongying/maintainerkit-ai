from src.maintainerkit import IssueAnalyzer


def test_bug_detection():

    analyzer = IssueAnalyzer()

    result = analyzer.analyze(
        "Application fails with an error"
    )

    assert result["category"] == "bug"


def test_feature_detection():

    analyzer = IssueAnalyzer()

    result = analyzer.analyze(
        "Please add this new feature"
    )

    assert result["category"] == "feature_request"


def test_question_detection():

    analyzer = IssueAnalyzer()

    result = analyzer.analyze(
        "How do I configure this?"
    )

    assert result["category"] == "question"