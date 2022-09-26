from pathlib import Path


def traverse(filepath: Path) -> list:
    result = []
    for d in filepath.iterdir():
        result.append(d)
        result = result + traverse(d)
    return result


if __name__ == '__main__':
    res = traverse(Path('./ch10/test_filesystem'))
    print(res)
