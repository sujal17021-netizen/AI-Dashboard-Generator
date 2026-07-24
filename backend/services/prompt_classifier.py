import re


AUTO_KEYWORDS = [
    "generate dashboard",
    "create dashboard",
    "make dashboard",
    "dashboard",
    "build dashboard",
    "visualize data",
    "analyse data",
    "analyze data",
    "overview",
    "summary",
]


def classify_prompt(prompt: str):

    prompt = prompt.lower().strip()

    prompt = re.sub(r"\s+", " ", prompt)

    for keyword in AUTO_KEYWORDS:
        if keyword in prompt:
            return "AUTO"

    return "CUSTOM"