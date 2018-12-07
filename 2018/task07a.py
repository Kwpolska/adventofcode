#!/usr/bin/env python3
from __future__ import annotations
from typing import List
from dataclasses import dataclass, field

with open("input/07.txt") as fh:
    file_data = fh.read().strip()


@dataclass()
class Task:
    name: str
    prerequisites: List[Task] = field(default_factory=list)
    done: bool = False

    def add_prerequisite(self, task: Task) -> None:
        self.prerequisites.append(task)

    def __str__(self) -> str:
        return self.name


def solve(data: str, max_letter: str) -> str:
    tasks = {}
    waiting = []
    done = []
    for tc_int in range(0x41, ord(max_letter) + 1):
        tc = chr(tc_int)
        task = Task(tc)
        tasks[tc] = task
        waiting.append(task)

    for line in data.split('\n'):
        tasks[line[36]].add_prerequisite(tasks[line[5]])

    while waiting:
        for t in waiting:
            possible = True
            for p in t.prerequisites:
                if not p.done:
                    possible = False
                    break
            if possible:
                t.done = True
                done.append(t)
                waiting.remove(t)
                break

    return ''.join(str(t) for t in done)


test_data = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""
test_output = solve(test_data, 'F')
test_expected = "CABDFE"
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data, 'Z'))
