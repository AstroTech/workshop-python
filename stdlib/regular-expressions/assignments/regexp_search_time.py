"""
* Assignment: Regexp Search Time
* Complexity: medium
* Lines of code: 4 lines
* Time: 5 min
* References: First paragraph from Apollo 11 Wikipedia entry :cite:`RegexpWikipediaApollo11`

English:
    1. Use data from "Given" section (see below)
    2. Use regular expressions to check text contains time in UTC (format: `%H:%M UTC`)
    3. Use simplified checking: `##:## UTC`, where `#` is a digit
    4. Define `result: str` with matched time

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Użyj wyrażeń regularnych do sprawdzenia czy tekst zawiera godzinę w UTC (format: `%H:%M UTC`)
    3. Użyj uproszczonego sprawdzania: `##:## UTC`, gdzie `#` to dowolna cyfra
    4. Zdefiniuj `result: str` ze znalezionym czasem

Tests:
    >>> result
    '02:56 UTC'
"""


# Given
import re


DATA = """Apollo 11 was the spaceflight that first landed humans on the Moon. Commander Neil Armstrong and lunar module pilot Buzz Aldrin formed the American crew that landed the Apollo Lunar Module Eagle on July 20, 1969, at 20:67 UTC. Armstrong became the first person to step onto the lunar surface six hours and 39 minutes later on July 21 at 02:56 UTC; Aldrin joined him 19 minutes later. They spent about two and a quarter hours together outside the spacecraft, and they collected 47.5 pounds (21.5 kg) of lunar material to bring back to Earth. Command module pilot Michael Collins flew the command module Columbia alone in lunar orbit while they were on the Moon's surface. Armstrong and Aldrin spent 21 hours, 36 minutes on the lunar surface at a site they named Tranquility Base before lifting off to rejoin Columbia in lunar orbit."""

result = ...


# Solution
pattern = r'([01][0-9]|[2][0-4]):[0-5][0-9] UTC'
result = re.search(pattern, DATA).group()
