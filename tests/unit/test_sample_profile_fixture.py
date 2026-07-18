import json
from pathlib import Path


def test_basic_profile_fixture_contains_expected_profile_fields() -> None:
    """Regression test for the missing shared profile fixture.

    Reproduction note: profile-related tests depend on this fixture being
    available at tests/fixtures/sample_profiles/basic_profile.json. Before the
    fixture existed, the suite could not load realistic sample profile data.
    """
    fixture_path = (
        Path(__file__).resolve().parents[1] / "fixtures" / "sample_profiles" / "basic_profile.json"
    )

    assert fixture_path.exists(), "shared sample profile fixture should exist"

    with fixture_path.open(encoding="utf-8") as handle:
        profile = json.load(handle)

    assert profile["github_username"] == "janedoe"
    assert profile["portfolio_url"] == "https://janedoe.dev"
    assert profile["repos"][0]["name"] == "weather-app"
    assert len(profile["repos"]) == 2
