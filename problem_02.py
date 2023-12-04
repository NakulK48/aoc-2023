from __future__ import annotations

from dataclasses import dataclass
import utils


@dataclass
class GameRound:
    red: int = 0
    blue: int = 0
    green: int = 0

    @staticmethod
    def from_str(section: str):
        colours = section.split(", ")
        raw = {}
        for colour_str in colours:
            num, col = colour_str.split()
            raw[col] = int(num)
        return GameRound(**raw)


@dataclass
class ParsedLine:
    game_id: int
    game_rounds: list[GameRound]

    @staticmethod
    def from_str(line: str):
        id_str, rounds = line.split(": ")
        game_id = int(id_str.split()[1])
        game_rounds = []
        for section in rounds.split("; "):
            game_rounds.append(GameRound.from_str(section))
        return ParsedLine(game_id, game_rounds)

    def power(self) -> int:
        max_reds = max(round.red for round in self.game_rounds)
        max_blues = max(round.blue for round in self.game_rounds)
        max_greens = max(round.green for round in self.game_rounds)
        return max_reds * max_blues * max_greens


def part_a():
    lines = utils.get_lines(2)
    result = 0
    for line in lines:
        parsed = ParsedLine.from_str(line)
        for round in parsed.game_rounds:
            if round.red > 12 or round.green > 13 or round.blue > 14:
                break
        else:
            result += parsed.game_id
    return result


def part_b():
    lines = utils.get_lines(2)
    return sum(ParsedLine.from_str(line).power() for line in lines)


print(part_b())
