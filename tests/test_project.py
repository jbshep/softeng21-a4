from pmgr.project import Project, TaskException
from pathlib import Path
import sys
import pytest
import os

@pytest.fixture
def fix_project():
    proj_name = "clean_house"
    project = Project(proj_name)
    project.add_task("clean")
    project.add_task("vacum")
    project.add_task("dust")
    yield project
    os.remove(project.filepath)
    os.rmdir(Path.cwd() / '.projects')
    
def test_get_task(fix_project):
    tasks = fix_project.get_tasks()
    
    assert tasks == ['clean', 'vacum', 'dust']

def test_remove_task(fix_project):
    textTasks='''clean\ndust\n'''
    fix_project.remove_task("vacum")
    with open(fix_project.filepath) as f:
        test = f.read()
    
    assert textTasks == test

def test_add_task(fix_project):
    textTasks = '''clean\nvacum\ndust\n'''
    with open(fix_project.filepath) as f:
        test = f.read()
        
    assert textTasks == test

def test_add_existing_task(fix_project):
    with pytest.raises(TaskException):
        result = fix_project.add_task('clean')
        
def test_remove_nonexistent_task(fix_project):
    with pytest.raises(TaskException):
        result = fix_project.remove_task("laundry")
