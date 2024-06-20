import click
from commands._add import add as add_func
from commands._commit import commit as commit_func
from commands._log import log as log_func
from commands._remove import remove as remove_func
from commands._diff import diff as diff_func
from commands._init import init as init_func
from commands._list import list as list_func
from commands._archive import archive as archive_func
from commands._restore import restore as restore_func
from commands._clean import clean as clean_func
from commands._patch import patch as patch_func
from commands._rename import rename as rename_func
from commands._annotate import annotate as annotate_func
from commands._ignore import ignore as ignore_func
from commands._revert import revert as revert_func

@click.group()
def dvc_cli():
    pass

@dvc_cli.command()
@click.argument('file_path')
def add(file_path):
    '''Add a file to the DVC staging area for tracking.'''
    add_func(file_path)

@dvc_cli.command()
@click.argument('message')
def commit(message):
    '''Make a permanent record of changes made to staged files.'''
    commit_func(message)

@dvc_cli.command()
def log():
    '''Show the commit log of the DVC files.'''
    log_func()

@dvc_cli.command()
@click.argument('files', nargs=-1)
def remove(files):
    '''Remove files from the DVC staging area.'''
    remove_func(files)

@dvc_cli.command()
@click.argument('file1')
@click.argument('file2')
def diff(file1, file2):
    '''Show the differences between files in the working directory and the last commit.'''
    diff_func(file1, file2)

@dvc_cli.command()
def init():
    '''Configure the initial setup for DVC.'''
    init_func()

@dvc_cli.command()
def list():
    '''List all the tracked files in the DVC repository.'''
    list_func()

@dvc_cli.command()
@click.argument('file_path')
def archive(file_path):
    '''Create a compressed archive of the DVC repository.'''
    archive_func(file_path)

@dvc_cli.command()
@click.argument('backup_dir')
def restore(backup_dir):
    '''Restore the DVC repository to a previous backup state.'''
    restore_func(backup_dir)

@dvc_cli.command()
def clean():
    '''Clean up unused cache files in the DVC cache directory.'''
    clean_func()

@dvc_cli.command()
@click.argument('patch_file')
@click.argument('target_dir')
def patch(patch_file, target_dir):
    '''Apply a patch file to the target directory.'''
    patch_func(patch_file, target_dir)

@dvc_cli.command()
@click.argument('old_name')
@click.argument('new_name')
def rename(old_name, new_name):
    '''Rename a file or directory tracked by DVC.'''
    rename_func(old_name, new_name)

@dvc_cli.command()
@click.argument('file_path')
def annotate(file_path):
    '''Display annotations for a file tracked by DVC.'''
    annotate_func(file_path)

@dvc_cli.command()
@click.argument('files_or_patterns', nargs=-1)
def ignore(files_or_patterns):
    '''Add files or patterns to the ignore list to exclude them from DVC tracking.'''
    ignore_func(files_or_patterns)

@dvc_cli.command()
@click.argument('file_path')
@click.argument('version')
def revert(file_path, version):
    '''Revert a file tracked by DVC to a specific version.'''
    revert_func(file_path, version)

if __name__ == '__main__':
    dvc_cli()
