#!/bin/bash
# Make a file po/pot with the current state of files

CWD=$(pwd)

xgettext -d drumst "../src/DrumsT.py" "../src/drumsT_FRAMES/mainwindow.py" \
"../src/drumsT_FRAMES/lessons.py" "../src/drumsT_PANELS/add_lesson.py" \
"../src/drumsT_PANELS/lessons_prospective.py" "../src/drumsT_DIALOGS/infoprg.py" \
"../src/drumsT_DIALOGS/first_time_start.py" "../src/drumsT_DIALOGS/add_student.py" \
"../src/drumsT_DIALOGS/add_school.py" "../src/drumsT_DIALOGS/add_newyear.py" \
"../src/drumsT_SYS/os_filesystem.py" "../src/drumsT_SYS/SQLite_lib.py"
