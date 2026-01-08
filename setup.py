from setuptools import setup

setup(
    name="weather-cli-tool",
    version="1.0",
    description="Lightweight Python CLI tool to get instant weather reports via wttr.in. Supports, multiple languages and cities.",
    py_modules=["main"],
    requires=[
        "requests",
    ],
    entry_points={
		"console_scripts":
		["weather=main:main"]
	},
)
