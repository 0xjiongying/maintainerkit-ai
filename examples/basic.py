from src.maintainerkit import IssueAnalyzer


analyzer = IssueAnalyzer()


issue = """
Installation fails after upgrading the package.
The terminal shows dependency errors.
"""


result = analyzer.analyze(issue)


print("Category:", result["category"])
print("Priority:", result["priority"])
print("Summary:", result["summary"])
print("Action:", result["suggested_action"])