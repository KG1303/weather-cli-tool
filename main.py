import argparse
import requests


def weather_report(city, lang):
    url = f"https://wttr.in/{city}?M_lang={lang}"
    response = requests.get(url).text
    return response


def main():
    parser = argparse.ArgumentParser(description="Weather CLI Tool")
    parser.add_argument(
        "--city", type=str, default="Barcelona", help="City name(default: Barcelona)"
    )
    parser.add_argument(
        "--lang", type=str, default="en", help="Language code(default: en)"
    )
    args = parser.parse_args()
    result = weather_report(args.city, args.lang)
    print(f"Weather in {args.city.capitalize()}")
    print(result)


if __name__ == "__main__":
    main()
