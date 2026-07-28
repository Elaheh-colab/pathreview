from ingestion.parsers.resume_parser import ResumeParser

r = ResumeParser()

# Breaking the long string into a multi-line format to pass linting
test_resume = (
    "\n    John Smith\n"
    "    john@example.com\n\n"
    "    Education:\n"
    "    - B.S. Computer Science\n\n"
    "    Skills: Python\n"
)

res = r.parse(test_resume)
print(res.metadata["detected_sections"])
