`#!/usr/bin/env bash

if [[ $# -ne 1 ]]; then
    printf 'Usage: %s <process-name>\n' "$0" >&2
    exit 2
fi

process_name=$1

if pids=$(pgrep -x "$process_name"); then
    printf 'Process "%s" is running. PID(s):\n%s\n' "$process_name" "$pids"
else
    result=$?
    if [[ $result -eq 1 ]]; then
        printf 'Process "%s" is not running.\n' "$process_name"
    else
        printf 'Error: pgrep failed while checking "%s" (exit status %d).\n' "$process_name" "$result" >&2
        exit "$result"
    fi
fi