#!/usr/bin/env Python3


def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_pipeline(iterable):
    for item in take(3, distinct(iterable)):
        print(item)

if __name__ == '__main__':
    fixture = [2, 4, 4, 6, 8, 10, 2, 6]
    run_pipeline(fixture)
