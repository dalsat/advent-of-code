from __future__ import annotations

from aoc import load_day


__day__ = 7


def part1(data):

    root = FSBuilder().from_commands(data)
    filter_dirs = lambda e:isinstance(e, Directory) and e.size <= 100000
    
    return sum(each.size for each in root.all_children(filter_dirs))


def part2(data):

    root = FSBuilder().from_commands(data)

    target_space = 30_000_000 - (70_000_000 - root.size)
    filter_dirs = lambda e:isinstance(e, Directory) and e.size >= target_space
    return sorted(each.size for each in root.all_children(filter_dirs))[0]


class File:

    def __init__(self, name, size):
        self.name = name
        self._size = size

    @property
    def size(self):
        return self._size

    def tree(self, level=0) -> str:
        return f'{" "*level*2}- {self.name} (file, size={self.size})'

    def all_children(self, where=lambda e: True):
        yield self
    

class Directory(File):
    children: dict[str, File]

    def __init__(self, name) -> None:
        self.name = name
        self.children = {}
    
    def __contains__(self, name: str) -> bool:
        return name in self.children

    def __getitem__(self, name: str) -> File:
        return self.children[name]

    def __setitem__(self, name: str, value: File):
        self.children[name] = value

    def ensure_directory(self, name: str):
        if name not in self.children:
            self.children[name] = Directory(name)
    
    @property
    def size(self) -> int:
        return sum(child.size for child in self.children.values())

    def tree(self, level=0) -> str:
        out = [f'{" "*level*2}- {self.name} (dir) size={self.size}']
        out += [f'{child.tree(level=level+1)}' for child in sorted(self.children.values(), key=lambda e: e.name)]
        return '\n'.join(out)

    def all_children(self, where=lambda e: True):
        if where(self):
            yield self
        for each in self.children.values():
            yield from filter(where, each.all_children())


class FSBuilder:

    def __init__(self) -> None:
        self.root = Directory(name='/')
        self.path: list[Directory] = []

    def execute(self, command: str) -> None:
        match command.split():
            case ['$', 'cd', '/']:
                self.path = []

            case ['$', 'cd', '..']:
                if self.path:
                    self.path.pop()

            case ['$', 'cd', name]:
                self.path.append(self.ensure_directory(name))

            case ['$', 'ls']:
                pass

            case [size, name] if size.isdigit():
                self.ensure_file(name, int(size))

            case ['dir', name]:
                self.ensure_directory(name)

            case _:
                raise ValueError(f'unknown command {command}')

    @property
    def current(self) -> Directory:
        if not self.path:
            return self.root
        return self.path[-1]

    def ensure_directory(self, name: str) -> Directory:
        assert isinstance(self.current, Directory)
        if name not in self.current:
            self.current[name] = Directory(name)
        new_dir = self.current[name]
        assert isinstance(new_dir, Directory)
        return new_dir

    def ensure_file(self, name: str, size: int) -> File:
        assert isinstance(self.current, Directory)
        if name not in self.path:
            self.current[name] = File(name, size)
        new_file = self.current[name]
        assert isinstance(new_file, File)
        return new_file

    @classmethod
    def from_commands(cls, commands: list[str]) -> Directory:
        fsb = cls()
        
        for command in commands:
            fsb.execute(command)
        
        return fsb.root
        
    
data = load_day(__day__)


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
