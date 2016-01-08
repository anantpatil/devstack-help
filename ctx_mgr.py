
import collections
import os
import sys
import pwd
import subprocess
import logging
import contextlib
import six
import shlex 

logging.basicConfig(filename='/opt/stack/example.log',level=logging.DEBUG)
LOG=logging.getLogger("ctx_mgr")

def print_uids():
	print "===="
	print "uid => ", os.getuid()
	print "euid => ", os.geteuid()
	print "gid => ", os.getgid()
	print "egid => ", os.getegid()
	print "===="

class ControlledPrivilegesFailureException(Exception):
    pass


@contextlib.contextmanager
def controlled_privileges(user):
    print "==== BEFORE ===="
    print_uids()
    orig_euid = None 
    try: 
        real = pwd.getpwnam(user)
        if os.geteuid() != real.pw_uid:
            orig_euid = os.geteuid()
            os.seteuid(real.pw_uid)
            LOG.debug("Privileges set for user %s" % user)
    except Exception as e:
        raise ControlledPrivilegesFailureException(e)

    try:
	print "==== BETWEEN ===="
	print_uids()
        yield
    finally:
        if orig_euid is not None:
            try:
                os.seteuid(orig_euid)
                LOG.debug("Original privileges restored.")
            except Exception as e:
                LOG.error("Error restoring privileges %s" % e)
    print "==== AFTER ===="
    print_uids()

Command = collections.namedtuple('Command', 'cmd cwd env')


def _make_subprocs(cmds, stdout_file):

    def chain_popen(p, cmd, out):
        stdin = p.stdout if p else None
        return subprocess.Popen(cmd.cmd, cwd=cmd.cwd, env=cmd.env,
                                stdin=stdin, stdout=out,
                                stderr=subprocess.PIPE)

    cmds, last = cmds[:-1], cmds[-1]
    p = None
    cmd_str = ""
    for cmd in cmds:
        p = chain_popen(p, cmd, subprocess.PIPE)
        cmd_str += six.text_type(cmd) + " | "

    cmd_str += six.text_type(last)
    out = subprocess.PIPE
    if stdout_file is not None:
        # If redirect is specified, use it as stdout of last command
        out = stdout_file
        cmd_str += " > " + stdout_file.name

    p = chain_popen(p, last, out)
    return p, cmd_str


def run_piped(cmds, user='root', stdout_file=None):
    status, stdout, stderr = None, None, None
    try:
        with controlled_privileges(user):
            subproc, cmd_str = _make_subprocs(cmds, stdout_file)
            print("Running command: ", cmd_str)
            if stdout_file is not None:
                status = subproc.wait()
                stderr = subproc.stderr.read()
            else:
                output = subproc.communicate()
                status = subproc.returncode
                stdout = output[0]
                stderr = output[1]
    except ControlledPrivilegesFailureException as e:
        LOG.error("Error setting privileges for user '%s': %s"
                  % (user, e))
        status = 126
        stderr = six.text_type(e)

    if status:
        LOG.debug("Return code of %d after executing: '%s'\n"
                  "stdout: '%s'\n"
                  "stderr: '%s'" % (status, cmd_str, stdout,
                                    stderr))
    return (status, stdout, stderr)


class CommandRunner(object):
    """Helper class to run a command and store the output."""

    def __init__(self, command, shell=False, nextcommand=None):
        self._command = str(command)
        self._shell = shell
        self._next = nextcommand
        self._stdout = None
        self._stderr = None
        self._status = None

    def __str__(self):
        s = "CommandRunner:"
        s += "\n\tcommand: %s" % self._command
        if self._status:
            s += "\n\tstatus: %s" % self.status
        if self._stdout:
            s += "\n\tstdout: %s" % self.stdout
        if self._stderr:
            s += "\n\tstderr: %s" % self.stderr
        return s

    def run(self, user='root', cwd=None, env=None):
        """Run the Command and return the output.

        Returns:
            self
        """
        LOG.debug("Running command: %s" % self._command)

        cmd = self._command

        try:
            with controlled_privileges(user):
                subproc = subprocess.Popen(self._command,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE, cwd=cwd,
                                           env=env, shell=True)
                output = subproc.communicate()
                self._status = subproc.returncode
                self._stdout = output[0]
                self._stderr = output[1]
        except ControlledPrivilegesFailureException as e:
            LOG.error("Error setting privileges for user '%s': %s"
                      % (user, e))
            self._status = 126
            self._stderr = six.text_type(e)

        if self._status:
            LOG.debug("Return code of %d after executing: '%s'\n"
                      "stdout: '%s'\n"
                      "stderr: '%s'" % (self._status, cmd, self._stdout,
                                        self._stderr))
        else:
            print(self._stdout)

        if self._next:
            self._next.run()
        return self

    @property
    def stdout(self):
        return self._stdout

    @property
    def stderr(self):
        return self._stderr

    @property
    def status(self):
        return self._status

'''
c1 = '/tmp/cmdrun.py'
cr=CommandRunner(c1)
cr.run(user='stack')

c2 = 'ls -al /root'
cr=CommandRunner(c2)
cr.run(user='stack')
'''

'''
c2 = 'ls -al /opt/stack'
cr=CommandRunner(c2, shell=True)
cr.run(user='stack')
'''

'''
c2 = 'ls -al /root'
cr=CommandRunner(c2)
cr.run()
'''
'''
url='/opt/stack/devstack-help/example.log.gz'
cmd = ['cat', url]
cr = CommandRunner(cmd)
cmd2 = ['gunzip']
fd = open('/opt/stack/devstack-help/example.log', 'w')
cr.pipe(cmd2, stdout_file=fd)
cr.run(user='stack')
fd.close()
print "STDOUT: ", cr.stdout
print "STDERR: ", cr.stderr
print "exit code: ", cr.status
'''

'''
url='http://tarballs.openstack.org/heat/heat-5.0.0.0b2.tar.gz'
cmd = ['curl', '-s', url]
cr = CommandRunner(cmd)
cmd2 = ['gunzip']
cr.pipe(cmd2)
cmd3= ['tar', '-xvf', '-']
cr.pipe(cmd3)
cr.run(user='stack')
print "STDOUT: ", cr.stdout
print "STDERR: ", cr.stderr
print "exit code: ", cr.status
'''

cmds = []
url='/opt/stack/devstack-help/example.log.gz'
cmd = ['cat', url]
c1 = Command(cmd=cmd, cwd=None, env=None)
cmd2 = ['gunzip']
c2 = Command(cmd=cmd2, cwd=None, env=None)
cmds.append(c1)
cmds.append(c2)
fd = open('/opt/stack/devstack-help/example.log', 'w')
(status, stdout, stderr) = run_piped(cmds, user='stack', stdout_file=fd)
fd.close()
print "STDOUT: ", stdout
print "STDERR: ", stderr
print "exit code: ", status

'''
cmds = []
url = 'http://tarballs.openstack.org/heat/heat-5.0.0.0b2.tar.gz'
cmd1 = ['curl', '-s', url]
cmds.append(Command(cmd=cmd1, cwd=None, env=None))
cmd2 = ['gunzip']
cmds.append(Command(cmd=cmd2, cwd=None, env=None))
cmd3= ['tar', '-xvf', '-']
cmds.append(Command(cmd=cmd3, cwd=None, env=None))
(status, stdout, stderr) = run_piped(cmds, user='stack')
print "STDOUT: ", stdout
print "STDERR: ", stderr
print "exit code: ", status
'''
