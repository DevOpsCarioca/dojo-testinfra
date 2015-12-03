
def test_container_debian_like(SystemInfo):
    assert SystemInfo.distribution == "debian"

def test_python_version(Package):
    python = Package("python2.7")
    assert python.version.startswith("2.7")

def test_python_pip(Package):
    pip = Package("python-pip")
    assert pip.is_installed

def test_folder_app(File):
    assert File("/app").is_directory

def test_gunicorn(Command):
    cmd = Command("pip freeze | grep gunicorn==")
    assert cmd.stdout.startswith("gunicorn")

def test_flask(Command):
    cmd = Command("pip freeze | grep Flask")
    assert cmd.stdout.startswith("Flask")

def test_port(Command):
    cmd = Command("ss -ntpl | grep 8000")
    assert "8000" in cmd.stdout 
