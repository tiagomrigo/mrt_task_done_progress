# -*- coding: utf-8 -*-
{
    'name': 'Task Done Log Hours Progress 100%',
    'version': '12.0.1.0.0',
    'category': 'Addon',
    'sequence': 1,
    'summary': "Set task's log hours progress 100% when a project task is set Done",
    'description': "Module which sets the progress to 100% when a project task is set as Done in kanban state. If you don't want to manually add worked hours to a task when it's completed, but simply have it's progress set to 100%.",
    'author': 'Tiago Magrini Rigo',
    'website': '',
    'depends': ['base','project', 'hr_timesheet'],
    'data': [
    ],
    'images':['static/description/task_list_cover.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'qweb': [],
}
