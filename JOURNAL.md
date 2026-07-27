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

## Week 9 — Solution building & PR submission

### Check-in 1 (mid-week)

**Current progress:**
I implemented the shared sample profile fixture and strengthened the regression test around its expected structure. The fixture now includes realistic profile content for the shared profile workflow, and the targeted unit test verifies the key fields and repository metadata.

**Next steps:**
I am finishing validation by running the repository checks and preparing the PR details for submission.

**Blockers:**
None.

---

### Check-in 2 (end of week)

**PR link:** [pending submission]

**Branch:** `fix/106-sample-profile-fixture`

**What you built:**
I restored the shared sample profile fixture under the test fixtures tree and expanded the regression test so it protects the fixture contract for profile-related tests. The fixture now contains realistic resume and repository data that can be reused across tests.

**Tests added or updated:**
Updated [tests/unit/test_sample_profile_fixture.py](tests/unit/test_sample_profile_fixture.py) to assert the fixture includes the expected profile fields and repository metadata.

**Self-review confirmation:** [x] make check passes  [ ] make test-unit passes

> Note: the targeted fixture regression test passed, while the broader unit suite currently reports unrelated existing failures in other modules such as resume parsing, review service, security, and skill extraction.

## Week 9 — Solution building & PR submission

### Check-in 1 (mid-week)

**Current progress:**
[What have you implemented so far? Which sub-tasks from PLAN.md are done?]

**Next steps:**
[What are you working on for the rest of the week?]

**Blockers:**
[Anything slowing you down? Or leave blank.]

---

### Check-in 2 (end of week)

**PR link:** [link to your submitted pull request]

**Branch:** [the branch name you worked on, e.g. `fix/123-short-description`]

**What you built:**
[1–3 sentences summarizing what your fix does and how it works]

**Tests added or updated:**
[Which test files did you touch? What do they cover?]

**Self-review confirmation:** [ ] make check passes  [ ] make test-unit passes
