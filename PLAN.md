## Solution plan

**Issue:** [Shared test fixture for a sample user profile is missing from `tests/fixtures/`](https://github.com/jamjamgobambam/pathreview/issues/106)

### Understand
What is the root cause of this issue? What behavior is expected vs. actual?

The root cause is that profile-related tests expect a shared sample profile fixture to exist under the test fixtures tree, but the fixture data was not available in a consistent location for the test environment. The expected behavior is that tests can load realistic profile input from a reusable fixture; the actual behavior is that the test setup lacks that data and cannot exercise the profile workflow reliably.

### Map
Which files, functions, or modules are involved?
List the specific files you expect to touch.

- tests/fixtures/sample_profiles/basic_profile.json
- tests/unit/test_sample_profile_fixture.py
- possibly any profile-related test modules that rely on the shared fixture

### Plan
What are the steps to fix this issue?
Break it into 3–5 concrete sub-tasks.

1. Confirm the expected fixture shape and the specific fields profile tests rely on.
2. Add or restore the shared sample profile fixture under the test fixtures directory with realistic content.
3. Add or strengthen a regression test that asserts the fixture exists and contains the expected profile fields.
4. Run the targeted test(s) to verify the fixture is loadable and the profile data is usable.

### Inputs & outputs
What does your fix take as input? What should it produce or change?

The fix takes no runtime input; it provides a static JSON fixture for tests. The output is a reusable sample profile payload that can be loaded by tests and used to exercise profile-related workflows.

### Risks & unknowns
What could go wrong? What are you still unsure about?

The main risk is that different tests may expect slightly different fixture fields or shapes. I am still verifying whether any other profile-related tests depend on additional keys beyond the sample currently covered by the regression test.

### Edge cases
What inputs or states should your fix handle gracefully?

- Empty or partial profile data should still be represented clearly in the fixture structure.
- The fixture should remain valid JSON and be readable by standard test utilities.
- The sample profile should be realistic enough for profile workflow tests without introducing fragile assumptions.
