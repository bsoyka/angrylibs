from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
from random import shuffle
from string import punctuation

from rich import print
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Confirm, Prompt

from .helpers import (
    display_name,
    get_setting,
    prompt_for_word,
    set_setting,
    settings_file,
    show_directions,
    story_list,
    story_name_from_path,
)


def main():
    try:
        get_setting("opened")
    except KeyError:
        show_directions()
        print()
        set_setting("opened", True)

    story_paths = story_list()
    shuffle(story_paths)
    story_paths = story_paths[:5]

    stories = {
        str(index) + ". " + story_name_from_path(path): path
        for index, path in enumerate(story_paths, start=1)
    }

    for story in stories.keys():
        print(story)

    print()

    story_choice = Prompt.ask(
        "Choose a story", choices=[x.split(".")[0] for x in stories.keys()], default="1"
    )

    story_path = Path(story_paths[int(story_choice) - 1])

    with story_path.open() as file:
        story_template = file.read()

    blanks_dict = dict()
    blanks_counter = Counter()

    for word in story_template.split(" "):
        if "__" in word:
            blank_type = word.split("__")[1]

            if "/" in blank_type:
                blanks_dict[blank_type] = ""
            else:
                blanks_dict[blank_type] = []
                blanks_counter[blank_type] += 1

    keys = list(blanks_dict.keys())
    shuffle(keys)

    for blank in keys:
        if "/" in blank:
            blanks_dict[blank] = prompt_for_word(blank.split("/")[0])
        else:
            for _ in range(blanks_counter[blank]):
                blanks_dict[blank].append(prompt_for_word(blank))

    new_text = ""

    for paragraph in story_template.split("\n"):
        previous_word = ""
        for word in paragraph.split(" "):
            prefix = ""
            suffix = ""

            if "__" in word:
                blank_type = word.split("__")[1]

                try:
                    suffix = word.split("__")[2]
                except:
                    pass

                try:
                    prefix = word.split("__")[0]
                except:
                    pass

                if "/" in blank_type:
                    word = blanks_dict[blank_type]
                else:
                    word = blanks_dict[blank_type].pop()

            if previous_word == "":
                word = word.capitalize()
            new_text += prefix + word + suffix + " "

            previous_word = word

        new_text += "\n"

    new_text = new_text.replace("\\", "\n")

    print(
        Panel(
            Markdown(new_text),
            title="[bold magenta]" + story_name_from_path(story_path),
        )
    )


def reset_settings():
    if Confirm.ask(
        "Are you sure you want to reset all Angry Libs settings?", default=False
    ):
        with settings_file().open("w") as file:
            file.write("{}")

        print("Success!")
    else:
        print("Aborted")


def cli():
    parser = ArgumentParser(
        description="Have a fluffy time by making some slimy choices"
    )
    parser.add_argument("-v", "--version", action="version", version="Angry Libs 2.1.2")
    parser.add_argument("--reset", action="store_true")

    args = parser.parse_args()

    if args.reset:
        reset_settings()
        return

    main()


if __name__ == "__main__":
    cli()
