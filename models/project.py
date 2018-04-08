from odoo import api, fields, models, tools, _

class ProjectIdea(models.Model):
    _name = "project.idea"

    name = fields.Char('Nom',required=True)