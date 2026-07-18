## Week 7 — Issue selection

**Issue link:** https://github.com/jamjamgobambam/pathreview/issues/106

**Issue title:** Shared test fixture for a sample user profile is missing from `tests/fixtures/`

**Tier:** [x] Tier 1  [ ] Tier 2  [ ] Tier 3

**Problem summary:**
The repository was missing a sample profile fixture that integration and other tests rely on when exercising the profile-related workflow. Without that fixture, the test environment could not provide realistic sample data, which caused missing-data issues during test setup. A successful fix restores the fixture with realistic profile content so tests can run with consistent sample input.

**Scope reasoning:**
This issue is a good first contribution because it is limited to the test data layer rather than core application behavior. The fix is small, low-risk, and easy to verify with a focused regression test. It also helps restore existing test coverage without requiring invasive changes across multiple modules.

**Branch name:** fix/106-sample-profile-fixture

**Setup confirmation:** [x] App runs locally at localhost:5173

**Cohort ledger:** [ ] Issue added to cohort ledger (pending the course-provided ledger link)

## Week 8 — Reproduction & solution planning

**Reproduction commit link:** https://github.com/vdynak/pathreview/commit/135d58b

**Reproduction summary:**
I reproduced the issue by running the targeted regression test for the sample profile fixture and confirming the fixture path is expected by profile-related tests. The test environment now records that expectation explicitly so the missing shared fixture issue is documented and reproducible.

**PLAN.md link:** https://github.com/vdynak/pathreview/blob/fix/106-sample-profile-fixture/PLAN.md

**Walkthrough video (recommended):** N/A

**Blockers or open questions:**
No blockers at this stage; I will continue into Week 9 with the fixture implementation and verification.
