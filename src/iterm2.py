import os
import osascript

def _apple_script_string_escape(s):
    tmp = repr(s)[1:-1].replace('"', '')
    return repr(tmp)[1:-1].replace('\\', '') # fix this bug


def _iterm_exec(cmd):
    apple_script = '''tell application "iTerm2"
    tell current session of current window
        select split vertically with default profile
        write text "{}"
    end tell
end tell
'''.format(_apple_script_string_escape(cmd))
    osascript.run(apple_script)


def run(command):
    _iterm_exec(command)

#/usr/local/bin/ancyterm -s docker.for.mac.host.internal -p 15111 -t iterm2 -e '/usr/bin/gdb -q  "./character" 734'

def test_run():
    run('ancypwn attach -c "ls"')


if __name__ == '__main__':
    test_run()
