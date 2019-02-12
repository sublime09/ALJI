import os

def main():
    print("Running setup for SchoasticPull...")
    geckoDriver = which("geckodriver.exe")
    print("Local search for geckodriver found:", geckoDriver)
    if geckoDriver is None:
        print("Could not find geckodriver.exe!!!")
        print("Download geckodriver from here:")
        print("https://github.com/mozilla/geckodriver/releases/tag/v0.9.0")
        print("Then add .exe file to your system PATH or virtualenv")
        return 1
    print("SchoasticPull setup is done!")

def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file
    return None


if __name__ == '__main__':
    main()
