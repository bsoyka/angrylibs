from pytest import mark
from pathlib import Path
from angrylibs.helpers import (
    display_name,
    settings_file,
    story_list,
    story_name_from_path,
    words_dict,
)


@mark.parametrize(
    "test_input,expected",
    [
        ("ALL CAPS", "All Caps"),
        ("hElLO wORlD", "Hello World"),
        ("OnEWoRD", "Oneword"),
        ("underscores_in_this_one", "Underscores In This One"),
        ("verb_ing", "Verb ending in -ing"),
    ],
)
def test_display_name(test_input: str, expected: str):
    assert display_name("heLLo WOrlD") == "Hello World"


def test_settings_file():
    assert isinstance(settings_file(), Path)


def test_story_list():
    stories = story_list()

    assert isinstance(stories, list)

    for item in stories:
        assert isinstance(item, str)
        assert Path(item).is_file()


@mark.parametrize(
    "file_path",
    [
        "stories/story_name.story.txt",
        "~/path/to/stories/story_name.story.txt",
        "stories\\story_name.story.txt",
        "\\backslashes\\to\\stories\\story_name.story.txt",
    ],
)
def test_story_name_from_path(file_path):
    assert story_name_from_path(file_path) == "Story Name"


def test_words_dict():
    words = words_dict()

    assert isinstance(words, dict)

    for key, value in words.items():
        assert isinstance(key, str)
        assert isinstance(value, list)

        for word in value:
            assert isinstance(word, str)
