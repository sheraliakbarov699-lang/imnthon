from pathlib import Path


def find_log_files(directory: Path) -> list[Path]:
    return sorted(path for path in directory.iterdir() if path.is_file() and path.suffix == ".log")


def print_log_report(directory: Path) -> int:
    log_files = find_log_files(directory)

    if not log_files:
        print(f'"{directory}" katalogida .log fayllari topilmadi.')
        print("Log fayllari soni: 0")
        return 0

    for log_file in log_files:
        print(f"{log_file.name}: {log_file.stat().st_size} bayt")

    print(f"Log fayllari soni: {len(log_files)}")
    return len(log_files)


def main() -> None:
    logs_directory = Path(__file__).resolve().parent / "logs"
    logs_directory.mkdir(exist_ok=True)
    print_log_report(logs_directory)


if __name__ == "__main__":
    main()