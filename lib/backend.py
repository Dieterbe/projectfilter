import os,sys

def debug(msg):
    if debug_enabled:
        print "DEBUG: %s" % msg

def critical(msg):
    sys.stderr.write("CRITICAL: %s\n" % msg)
    sys.exit(2)

def warning(msg):
    print "WARNING: %s" % msg

def list_projectdirs(maindirectories):
    for maindir in maindirectories:
        try:
            for projectdir in get_entries_directories(maindir):
                debug("> %s/%s" % (maindir, projectdir))
                yield os.path.join(maindir, projectdir)
        except OSError, e:
            critical("No such directory: %s" % maindir)

def get_entries_directories(dir):
    for name in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, name)):
            yield name

def run_cmd(args):
    from subprocess import Popen, PIPE
    try:
        popen = Popen (args, stdout=PIPE, stderr=PIPE)
        streams = popen.communicate()
        if popen.returncode > 0:
            critical("Could not run command: %s. Exit code: %i - CWD: %s. Stderr: %s", args, popen.returncode, os.getcwd(), streams[1].strip())
        return streams
    except Exception, e:
        critical(e)
