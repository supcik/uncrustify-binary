import argparse
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def main():
    parser = argparse.ArgumentParser(
        prog="Builder",
    )
    parser.add_argument("version")
    args = parser.parse_args()

    env = Environment(
        loader=FileSystemLoader("templates"),
    )

    files = [
        {
            "path": f"binaries/uncrustify-macos-x86_64-{ args.version }",
            "name": f"uncrustify-macos-x86_64-{ args.version }",
        },
        {
            "path": f"binaries/uncrustify-macos-arm64-{ args.version }",
            "name": f"uncrustify-macos-arm64-{ args.version }",
        },
        {
            "path": f"binaries/uncrustify-macos-universal-{ args.version }",
            "name": f"uncrustify-macos-universal-{ args.version }",
        },
    ]
    (Path("website") / "binaries").mkdir(parents=True, exist_ok=True)

    template = env.get_template("index.html")
    with open(Path("website") / "index.html", "w") as f:
        f.write(template.render(version=args.version, files=files))


if __name__ == "__main__":
    main()
