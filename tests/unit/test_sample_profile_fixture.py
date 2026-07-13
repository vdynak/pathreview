import json
from pathlib import Path


def test_basic_profile_fixture_contains_expected_profile_fields() -> None:
    fixture_path = (
        Path(__file__).resolve().parents[1] / "fixtures" / "sample_profiles" / "basic_profile.json"
    )

    with fixture_path.open(encoding="utf-8") as handle:
        profile = json.load(handle)

    assert profile["github_username"] == "janedoe"
    assert profile["portfolio_url"] == "https://janedoe.dev"
    assert profile["repos"][0]["name"] == "weather-app"
    assert len(profile["repos"]) == 2
