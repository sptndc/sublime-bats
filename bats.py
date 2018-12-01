import os

import sublime
import sublime_plugin


def file_executable(file):
    return os.path.exists(file) and os.access(file, os.X_OK)


# See https://stackoverflow.com/a/9877856
def which(cmd):
    path = os.environ['PATH']
    for p in path.split(os.path.pathsep):
        p = os.path.join(p, cmd)
        if file_executable(p):
            return p


class Bats():
    def __init__(self, window):
        self.window = window
        self.view = window.active_view()
        if not self.view:
            raise ValueError('view not found')

    def run(self, working_dir=None, file=None):
        self.window.run_command('exec', {'kill': True})

        env = {}
        cmd = []

        try:
            if not working_dir:
                working_dir = os.path.dirname(self.view.file_name())
                if not working_dir:
                    raise ValueError('working directory not found')

            if not os.path.isdir(working_dir):
                raise ValueError('working directory does not exist or is not a valid directory')

            if env is None:
                env = os.environ.copy()

            bats_executable = self.get_bats_executable()
            cmd.append(bats_executable)

            file = self.view.file_name()
            if not file:
                raise ValueError('test file \'%s\' not found' % file)

            cmd.append(file)

        except ValueError as e:
            sublime.status_message('Bats: {}'.format(e))
            print('Bats: {}'.format(e))
            return
        except Exception as e:
            sublime.status_message('Bats: {}'.format(e))
            print('Bats: \'{}\''.format(e))
            raise e

        self.window.run_command('exec', {
            'cmd': cmd,
            'env': env,
            'quiet': True,
            'shell': False,
            'word_wrap': False,
            'working_dir': working_dir
        })

    def cancel(self):
        self.window.run_command('exec', {'kill': True})

    def get_bats_executable(self):
        bats_executable = which('bats')
        if bats_executable:
            return bats_executable
        else:
            raise ValueError('bats not found')


class BatsTestCommand(sublime_plugin.WindowCommand):

    def run(self):
        Bats(self.window).run()


class BatsTestCancelCommand(sublime_plugin.WindowCommand):

    def run(self):
        Bats(self.window).cancel()
