# -*- coding: utf-8 -*-
# © 2019 Mr_T - Tiago Magrini Rigo 

from odoo import api, fields, models, _

class Task(models.Model):
    _inherit = "project.task"

    kanban_state = fields.Selection(inverse='_inverse_state')

    @api.multi
    def _inverse_state(self):
        for obj in self:
            if obj.kanban_state == 'done':
                #set progress 100%
                obj.write({'progress': 100})
            else:
                #set progress 0%
                obj.write({'progress': 0})