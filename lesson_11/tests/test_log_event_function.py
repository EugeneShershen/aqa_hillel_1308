from pytest import mark

from lesson_11.src.homework_11 import log_event

import os


def read_n_to_last_line(filename, n=1):
    """Returns the nth before last line of a file (n=1 gives last line)"""
    num_newlines = 0
    with open(filename, 'rb') as f:
        try:
            f.seek(-2, os.SEEK_END)
            while num_newlines < n:
                f.seek(-2, os.SEEK_CUR)
                if f.read(1) == b'\n':
                    num_newlines += 1
        except OSError:
            f.seek(0)
        last_line = f.readline().decode()
    return last_line


@mark.parametrize('status_event, log_level', [
    ('success', 'INFO'),
    ('expired', 'WARNING'),
    ('failed', 'ERROR')
])
def test_log_event(status_event, log_level):
    # Arrange
    user_name = 'User'
    expected_result = f"{log_level} - 'Login event - Username: {user_name}, Status: {status_event}'"
    # Act
    log_event(user_name, status_event)
    result = read_n_to_last_line('login_system.log')[26:-2]
    # Assert
    assert result == expected_result
