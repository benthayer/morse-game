ansi_cursor_up = '\x1b[1A'
ansi_cursor_left = '\x1b[1D'
ansi_cursor_right = '\x1b[1C'
ansi_clear_line = "\x1b[2K"
ansi_clear_cursor = "\x1b[0K"

ansi_save_pos = "\x1b[s"
ansi_restore_pos = "\x1b[u"


def control_print(seq):
    print(seq, end="")


def cursor_up():
    control_print(ansi_cursor_up)


def cursor_left():
    control_print(ansi_cursor_left)


def cursor_right():
    control_print(ansi_cursor_right)


def clear_line():
    control_print(ansi_clear_line)


def clear_cursor():
    control_print(ansi_clear_cursor)


def save_pos():
    control_print(ansi_save_pos)


def restore_pos():
    control_print(ansi_restore_pos)
