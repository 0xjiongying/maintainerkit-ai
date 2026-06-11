class IssueAnalyzer:
    """
    Analyze GitHub issues and help maintainers
    reduce repetitive triage work.
    """

    def analyze(self, issue_text):

        text = issue_text.lower()

        if any(word in text for word in [
            "error",
            "fail",
            "crash",
            "bug"
        ]):
            category = "bug"
            priority = "medium"

        elif any(word in text for word in [
            "feature",
            "request",
            "add"
        ]):
            category = "feature_request"
            priority = "low"

        else:
            category = "question"
            priority = "normal"


        return {
            "category": category,
            "priority": priority,
            "summary": issue_text[:120],
            "suggested_action":
                "Review issue and assign maintainer response"
        }