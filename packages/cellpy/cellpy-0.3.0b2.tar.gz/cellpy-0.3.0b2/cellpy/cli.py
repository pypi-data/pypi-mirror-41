import os
import getpass
import click
import pkg_resources
import pathlib

from cellpy.parameters import prmreader
from cellpy.exceptions import ConfigFileNotWritten
import cellpy._version

DEFAULT_FILENAME_START = "_cellpy_prms_"
DEFAULT_FILENAME_END = ".conf"
DEFAULT_FILENAME = DEFAULT_FILENAME_START + "default" + DEFAULT_FILENAME_END
VERSION = cellpy._version.__version__
REPO = "git-repo-name"


def save_prm_file(prm_filename):
    """saves (writes) the prms to file"""
    prmreader._write_prm_file(prm_filename)


def get_package_prm_dir():
    """gets the folder where the cellpy package lives"""
    prm_dir = pkg_resources.resource_filename("cellpy", "parameters")
    return prm_dir


def get_default_config_file_path(init_filename=None):
    """gets the path to the default config-file"""
    prm_dir = get_package_prm_dir()
    if not init_filename:
        init_filename = DEFAULT_FILENAME
    src = os.path.join(prm_dir, init_filename)
    return src


def get_user_dir_and_dst(init_filename):
    """gets the name of the user directory and full prm filepath"""
    user_dir = os.path.abspath(os.path.expanduser("~"))
    dst_dir = user_dir
    dst_file = os.path.join(dst_dir, init_filename)
    return user_dir, dst_file


def get_user_name():
    """get the user name of the current user (cross platform)"""
    return getpass.getuser()


def create_custom_init_filename():
    """creates a custom prms filename"""
    return DEFAULT_FILENAME_START + get_user_name() + DEFAULT_FILENAME_END


def check_if_needed_modules_exists():
    pass


def modify_config_file():
    pass


def create_cellpy_folders():
    pass


@click.group("cellpy")
def cli():
    pass


@click.command()
@click.option(
    '--interactive', '-i',
    is_flag=True,
    default=False, help="Use the newest of the newest (a bit risky)."
)
@click.option(
    '--not-relative', '-nr',
    is_flag=True,
    default=False,
    help="If root-dir is given, put it directly in the root (/) folder"
         " i.e. don't put it in your home directory. Defaults to False. Remark"
         " that if you specifically write a path name instead of selecting the"
         " suggested default, the path you write will be used as is."
)
@click.option(
    '--dry-run', '-dr',
    is_flag=True, default=False,
    help="Run setup in dry mode (only print - do not execute). This is"
         " typically used when developing and testing cellpy. Defaults to"
         " False."
)
@click.option(
    '--reset', '-r',
    is_flag=True, default=False,
    help="Do not suggest path defaults based on your current configuration-file"
)
@click.option(
    '--root-dir', '-d',
    default=None, help="Use custom root dir. If not given, your home directory"
                       " will be used as the top level where cellpy-folders"
                       " will be put. The folder path must follow"
                       " directly after this option (if used). Example:\n"
                       " $ cellpy setup -d 'MyDir'"
)
def setup(interactive, not_relative, dry_run, reset, root_dir):
    """This will help you to setup cellpy."""

    click.echo("[cellpy] setup")

    # generate variables
    init_filename = create_custom_init_filename()
    userdir, dst_file = get_user_dir_and_dst(init_filename)

    if interactive:
        click.echo(" interactive mode ".center(80, "-"))
        _update_paths(root_dir, not not_relative, dry_run=dry_run, reset=reset)
        _write_config_file(
            userdir, dst_file,
            init_filename, dry_run,
        )
        _check()

    else:
        _write_config_file(userdir, dst_file, init_filename, dry_run)
        _check()


def _update_paths(custom_dir=None, relative_home=True,
                  reset=False, dry_run=False, default_dir="cellpy_data"):

    h = pathlib.Path.home()
    if custom_dir:
        if relative_home:
            h = h / custom_dir
        else:
            h = custom_dir
    if not reset:
        outdatadir = pathlib.Path(prmreader.prms.Paths.outdatadir)
        rawdatadir = pathlib.Path(prmreader.prms.Paths.rawdatadir)
        cellpydatadir = pathlib.Path(prmreader.prms.Paths.cellpydatadir)
        filelogdir = pathlib.Path(prmreader.prms.Paths.filelogdir)
        db_path = pathlib.Path(prmreader.prms.Paths.db_path)
        db_filename = prmreader.prms.Paths.db_filename
    else:
        outdatadir = "out"
        rawdatadir = "raw"
        cellpydatadir = "cellpyfiles"
        filelogdir = "logs"
        db_path = "db"
        db_filename = "cellpy_db.xlsx"
        if not custom_dir:
            h = h / default_dir

    outdatadir = h / outdatadir
    rawdatadir = h / rawdatadir
    cellpydatadir = h / cellpydatadir
    filelogdir = h / filelogdir
    db_path = h / db_path

    outdatadir = _ask_about_path(
        "where to output processed data and results",
        outdatadir,
    )

    rawdatadir = _ask_about_path(
        "where your raw data are located",
        rawdatadir,
    )

    cellpydatadir = _ask_about_path(
        "where to put cellpy-files",
        cellpydatadir,
    )

    filelogdir = _ask_about_path(
        "where to dump the log-files",
        filelogdir,
    )

    db_path = _ask_about_path(
        "what folder your db file lives in",
        db_path,
    )

    db_filename = _ask_about_name(
        "the name of your db-file",
        db_filename,
    )

    # update folders based on suggestions
    for d in [outdatadir, rawdatadir, cellpydatadir, filelogdir, db_path]:
        if not dry_run:
            _create_dir(d)
        else:
            click.echo(f" -> creating {d}")

    # update config-file based on suggestions
    prmreader.prms.Paths.outdatadir = str(outdatadir)
    prmreader.prms.Paths.rawdatadir = str(rawdatadir)
    prmreader.prms.Paths.cellpydatadir = str(cellpydatadir)
    prmreader.prms.Paths.filelogdir = str(filelogdir)
    prmreader.prms.Paths.db_path = str(db_path)
    prmreader.prms.Paths.db_filename = str(db_filename)


def _ask_about_path(q, p):
    click.echo(f"[cellpy] input {q}:\n[cellpy] [{p}]")
    new_path = input("[cellpy] >>> ").strip()
    if not new_path:
        new_path = p
    return pathlib.Path(new_path)


def _ask_about_name(q, n):
    click.echo(f"[cellpy] input {q}:\n[cellpy] [{n}]")
    new_name = input("[cellpy] >>> ").strip()
    if not new_name:
        new_name = n
    return new_name


def _create_dir(path, confirm=True, parents=True, exist_ok=True):
    o = path.resolve()
    if not o.is_dir():
        o_parent = o.parent
        create_dir = True
        if confirm:
            if not o_parent.is_dir():
                create_dir = input(
                    f"[cellpy] {o_parent} does not exist. Create it [y]/n ?"
                )
                if not create_dir:
                    create_dir = True
                elif create_dir in ["y", "Y"]:
                    create_dir = True
                else:
                    create_dir = False

        if create_dir:
            o.mkdir(parents=parents, exist_ok=exist_ok)
        else:
            click.echo(f"[cellpy] Could not create {o}")
    return o


def _check():
    click.echo(" checking ".center(80, "-"))
    click.echo("[cellpy] Checking is not implemented yet!")
    click.echo("[cellpy] Hint if you run into problems!")
    click.echo("A typical source of error is that you are"
               " missing drivers for MS Access.")


def _write_config_file(userdir, dst_file, init_filename, dry_run):
    click.echo(" update configuration ".center(80, "-"))
    click.echo("[cellpy] Writing configurations to user directory:")
    click.echo(f"\n         {userdir}\n")

    if os.path.isfile(dst_file):
        click.echo("[cellpy] File already exists!")
        click.echo(
            "[cellpy] Keeping most of the old configuration parameters"
        )
    try:
        if dry_run:
            click.echo(
                f"*** dry-run: skipping actual saving of {dst_file} ***",
                color="red",
            )
        else:
            save_prm_file(dst_file)

    except ConfigFileNotWritten:
        click.echo("[cellpy] Something went wrong! Could not write the file")
        click.echo(
            "[cellpy] Trying to write a file"
            + f"called {DEFAULT_FILENAME} instead")

        try:
            userdir, dst_file = get_user_dir_and_dst(init_filename)
            if dry_run:
                click.echo(
                    f"*** dry-run: skipping actual saving of {dst_file} ***",
                    color="red",
                )
            else:
                save_prm_file(dst_file)

        except ConfigFileNotWritten:
            _txt = "[cellpy] No, that did not work either.\n"
            _txt += "[cellpy] Well, guess you have to talk to the developers."
            click.echo(_txt)
    else:
        click.echo(
            f"[cellpy] Configuration file written!")
        click.echo(
            f"[cellpy] OK! Now you can edit it. For example by "
            f"issuing \n\n         [your-favourite-editor] {init_filename}\n")


@click.command()
@click.option(
    '--version', '-v', is_flag=True, help="Print version information."
)
@click.option(
    '--configloc', '-l', is_flag=True,
    help='Print full path to the config file.'
)
@click.option(
    '--params', '-p', is_flag=True, help='Dump all parameters to screen.'
)
@click.option(
    '--check', '-c', is_flag=True, help='Do a sanity check to see if things'
                                        ' works as they should.'
)
def info(version, configloc, params, check):
    complete_info = True

    if check:
        complete_info = False
        _check()

    if version:
        complete_info = False
        _version()

    if configloc:
        complete_info = False
        _configloc()

    if params:
        complete_info = False
        _dump_params()

    if complete_info:
        _version()
        _configloc()


@click.command()
@click.option(
    '--tests', '-t', is_flag=True, help="Download test-files from repo."
)
@click.option(
    '--examples', '-e', is_flag=True, help="Download example-files from repo."
)
@click.option(
    '--clone', '-c', is_flag=True, help="Clone the full repo."
)
@click.option(
    '--directory', '-d', default=None, help="Save into custom directory DIR"
)
def pull(tests, examples, clone, directory):
    if directory is not None:
        click.echo(f"[cellpy] Custom directory: {directory}")
    if clone:
        _clone_repo(directory)
    else:
        if tests:
            _pull_tests(directory)
        if examples:
            _pull_examples(directory)


@click.command()
@click.option(
    '--journal', '-j', is_flag=True,
    help="Run a batch job defined in the given journal-file"
)
@click.option(
    '--debug', '-d', is_flag=True, help="Run in debug mode."
)
@click.option(
    '--silent', '-s', is_flag=True,
    help="Run in silent (i.e. no-plotting) mode."
)
@click.argument('file_name')
def run(journal, debug, silent, file_name):
    print("RUNNING".center(80, "*"))
    if not file_name:
        click.echo("[cellpy] No filename provided.")
        return
    txt = f"[cellpy] The plan is that this cmd will run a batch run\n"
    txt += f"[cellpy] journal: {journal}\n"

    if debug:
        txt += "[cellpy] debug mode on"

    if silent:
        txt += "[cellpy] silent mode on"

    txt += "[cellpy]\n"
    click.echo(txt)

    if journal:
        _run_journal(file_name, debug, silent)

    else:
        _run(file_name, debug, silent)


def _run_journal(file_name, debug, silent):
    print(f"running journal {file_name}")
    print(f" --debug [{debug}]")
    print(f" --silent [{silent}]")


def _run(file_name, debug, silent):
    print(f"running {file_name}")
    print(f" --debug [{debug}]")
    print(f" --silent [{silent}]")


def _clone_repo(directory):
    txt = "[cellpy] The plan is that this "
    txt += "[cellpy] cmd will pull (clone) the cellpy repo.\n"
    txt += "[cellpy] For now it only prins the link to the git-hub\n"
    txt += "[cellpy] repository:\n"
    txt += "[cellpy]\n"
    txt += "[cellpy] https://github.com/jepegit/cellpy.git\n"
    txt += "[cellpy]\n"
    click.echo(txt)


def _pull_tests(directory):
    txt = "[cellpy] The plan is that this cmd will run some tests.\n"
    txt += "[cellpy] For now it only prins the link to the git-hub\n"
    txt += "[cellpy] repository:\n"
    txt += "[cellpy]\n"
    txt += "[cellpy] https://github.com/jepegit/cellpy.git\n"
    txt += "[cellpy]\n"
    click.echo(txt)


def _pull_examples(directory):
    txt = "[cellpy] The plan is that this cmd will download examples.\n"
    txt += "[cellpy] For now it only prins the link to the git-hub\n"
    txt += "[cellpy] repository:\n"
    txt += "[cellpy]\n"
    txt += "[cellpy] https://github.com/jepegit/cellpy.git\n"
    txt += "[cellpy]\n"
    click.echo(txt)


def _version():
    txt = "[cellpy] version: " + str(VERSION)
    click.echo(txt)


def _configloc():
    config_file_name = prmreader._get_prm_file()
    click.echo("[cellpy] ->%s\n" % config_file_name)
    if not os.path.isfile(config_file_name):
        click.echo("[cellpy] File does not exist!")


def _dump_params():
    click.echo("[cellpy] Dumping parameters to screen:\n")
    prmreader.info()


cli.add_command(setup)
cli.add_command(info)
cli.add_command(pull)
cli.add_command(run)


def _main():
    file_name = create_custom_init_filename()
    print(file_name)
    user_directory, destination_file_name = get_user_dir_and_dst(file_name)
    print(user_directory)
    print(destination_file_name)
    print("trying to save it")
    save_prm_file(destination_file_name + "_dummy")

    print(" Testing setup ".center(80, "="))
    #setup(["--interactive", "--root-dir", "new_cellpy_data"])
    setup(["--interactive", "--reset"])


if __name__ == "__main__":
    print("\n\n", " RUNNING MAIN ".center(80, "*"), "\n")
    _main()

