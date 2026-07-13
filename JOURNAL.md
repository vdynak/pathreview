## Week 7 — Issue selection

**Issue link:** https://github.com/jamjamgobambam/pathreview/issues/106

**Issue title:** Shared test fixture for a sample user profile is missing from `tests/fixtures/`

**Tier:** [x] Tier 1  [ ] Tier 2  [ ] Tier 3

**Problem summary:**
The repository was missing a sample profile fixture that integration and other tests rely on when exercising the profile-related workflow. Without that fixture, the test environment could not provide realistic sample data, which caused missing-data issues during test setup. A successful fix restores the fixture with realistic profile content so tests can run with consistent sample input.

**Branch name:** fix/106-sample-profile-fixture

**Setup confirmation:** [x] App runs locally at localhost:5173

**Cohort ledger:** [ ] Issue added to cohort ledger
