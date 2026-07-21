## Week 7 — Issue selection

**Issue link:** https://github.com/ascherj/pathreview/issues/147
**Issue title:** Resume section detection fails on text with leading whitespace
**Tier:** [x] Tier 1  [ ] Tier 2  [ ] Tier 3 

**Problem summary:**
The `_detect_sections()` function within `resume_parser.py` currently relies on regular expressions anchored exactly to the start of a line (e.g., `^Experience`). When resumes are extracted from PDFs, they often retain leading whitespace or indentation, causing these strict patterns to fail and return an empty `detected_sections` list. A successful fix will update the matching logic to tolerate leading whitespace, allowing the ingestion pipeline to correctly identify and extract key resume sections regardless of standard indentation.

**Branch name:** fix/147-resume-section-whitespace

**Setup confirmation:** [x] App runs locally at localhost:5173
**Cohort ledger:** [x] Issue added to cohort ledger

**Selection reasoning ("Is this right for me?" checklist):**

*   **Part 1 - Understanding the Issue:** I can clearly explain that the `ingestion` pipeline currently fails to detect resume sections when text contains leading whitespace because of strict regex anchors. A successful fix will modify these patterns to tolerate indentation, ensuring the sections are correctly extracted.
*   **Part 2 - Tier Fit:** As a Tier 1 bug labeled as a "good first issue," this is a highly realistic match. It provides a localized, self-contained entry point into the codebase while directly aligning with core backend development and data engineering workflows. 
*   **Codebase Readiness:** I have located the `_detect_sections()` function within `resume_parser.py` and reviewed the specific failing tests in `tests/unit/test_resume_parser.py`. Because the logic centers around regular expressions and string processing, I have enough context to safely plan the fix without needing to understand the entire multi-service architecture.
*   **Scope and Time:** The scope is confined to one or two files, which easily fits the 3–6 hour time estimate for Tier 1 issues across Weeks 8–9. There are no open blockers or dependencies preventing me from starting.