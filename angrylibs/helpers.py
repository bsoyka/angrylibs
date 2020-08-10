from glob import glob
from json import dump, load
from pathlib import Path
from random import choice
from re import search

from click import get_app_dir
from inflect import engine
from rich import print
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt

p = engine()


def display_name(string: str) -> str:
    if string == "verb_ing":
        return "Verb ending in -ing"
    if string == "verb_ed":
        return "Verb ending in -ed"

    return " ".join(string.split("_")).title()


def get_setting(setting: str):
    with settings_file().open() as file:
        settings = load(file)

    return settings[setting]


def prompt_for_word(type_: str) -> str:
    """Prompts the user for a word"""

    if type_ == "plural_noun":
        if "noun" in words_dict().keys():
            random_word = choice(words_dict()["noun"])
        else:
            random_word = None

        return p.plural(Prompt.ask(display_name("noun"), default=random_word))
    else:
        if type_.strip("_AN") in words_dict().keys():
            random_word = choice(words_dict()[type_.strip("_AN")])
        else:
            random_word = None

        user_input = Prompt.ask(display_name(type_.strip("_AN")), default=random_word)

        if "_AN" in type_:
            return p.a(user_input)
        else:
            return user_input


def set_setting(setting: str, value):
    with settings_file().open() as file:
        settings = load(file)

    settings[setting] = value

    with settings_file().open("w") as file:
        dump(settings, file)


def settings_file() -> Path:
    """Gets the path to the Angry Libs settings file"""

    settings_path = Path(get_app_dir(app_name="Angry Libs")) / "settings.json"

    if not settings_path.is_file():
        settings_path.parent.mkdir(parents=True, exist_ok=True)
        with settings_path.open("w") as file:
            file.write("{}")

    return settings_path


def show_directions():
    """Shows the user directions for the program"""

    print(
        Panel(
            Markdown(
                """**Here's how to get started:**

* Pick a story from the random choices given

* Fill in the blanks! Some word types will give you a random default value, which you can use by just pressing Enter!

* Read your story and laugh!"""
            ),
            title="[bold green]WELCOME TO ANGRY LIBS!",
        )
    )


def story_list():
    """Gets a list of story files"""

    return glob(str(Path(__file__).parent / "stories/*.story.txt"))


def story_name_from_path(path: str) -> str:
    """Gets the name of a story from its path"""

    match = search(r"stories[\\/]([a-z\d_]+)\.story\.txt", str(path))

    return display_name(match.groups()[0])


def words_dict() -> dict:
    """Gets the dictionary from words.json"""

    with open(Path(__file__).parent / "words.json") as file:
        return load(file)
