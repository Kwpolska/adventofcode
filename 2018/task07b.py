#!/usr/bin/env python3
from __future__ import annotations
import typing
from typing import List, Dict, Optional
from dataclasses import dataclass, field

with open("input/07.txt") as fh:
    file_data = fh.read().strip()


@dataclass()
class Task:
    name: str
    shift: int
    duration: int = -1
    prerequisites: List[Task] = field(default_factory=list)
    done: bool = False

    def __post_init__(self) -> None:
        self.duration = ord(self.name) - 0x40 + self.shift

    def add_prerequisite(self, task: Task) -> None:
        self.prerequisites.append(task)

    def __str__(self) -> str:
        return self.name


@dataclass()
class Worker:
    task: Optional[Task] = None
    time_remaining: int = 0

    def __str__(self) -> str:
        return f"[{self.task}, {self.time_remaining}]"


def solve(data: str, max_letter: str, shift: int, workers_count: int) -> int:
    tasks: Dict[str, Task] = {}
    waiting: List[Task] = []
    done: List[Task] = []
    workers = [Worker() for _ in range(workers_count)]
    for tc_int in range(0x41, ord(max_letter) + 1):
        tc = chr(tc_int)
        task = Task(tc, shift)
        tasks[tc] = task
        waiting.append(task)

    for line in data.split('\n'):
        tasks[line[36]].add_prerequisite(tasks[line[5]])

    time = 0
    while len(done) != ord(max_letter) - 0x40:
        candidates = []
        for t in waiting:
            possible = True
            for p in t.prerequisites:
                if not p.done:
                    possible = False
                    break
            if possible:
                candidates.append(t)

        for w in workers:
            if not w.task and candidates:
                w.task = candidates.pop()
                w.time_remaining = w.task.duration
                waiting.remove(w.task)

        for w in workers:
            w.time_remaining -= 1
            if w.task and w.time_remaining == 0:
                w.task.done = True
                w.task = None
                done.append(typing.cast(Task, w.task))
        print(time, ' '.join(str(i) for i in workers))
        time += 1

    return time


test_data = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""
test_output = solve(test_data, 'F', 0, 2)
test_expected = 15
print(test_output, test_expected)
assert test_output == test_expected
print(solve(file_data, 'Z', 60, 5))
