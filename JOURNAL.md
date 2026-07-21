## Week 7 — Issue selection

**Issue link:** https://github.com/ascherj/pathreview/issues/147
**Issue title:** Resume section detection fails on text with leading whitespace
**Tier:** [x] Tier 1  [ ] Tier 2  [ ] Tier 3 

**Problem summary:**
The `_detect_sections()` function within `resume_parser.py` currently relies on regular expressions anchored exactly to the start of a line (e.g., `^Experience`). When resumes are extracted from PDFs, they often retain leading whitespace or indentation, causing these strict patterns to fail and return an empty `detected_sections` list. A successful fix will update the matching logic to tolerate leading whitespace, allowing the ingestion pipeline to correctly identify and extract key resume sections regardless of standard indentation.

**Branch name:** fix/147-resume-section-whitespace

**Setup confirmation:** [x] App runs locally at localhost:5173
**Cohort ledger:** [x] Issue added to cohort ledger