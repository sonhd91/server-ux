from odoo import fields, models


class ResUsersLog(models.Model):
    _inherit = "res.users.log"

    create_uid = fields.Many2one("res.users", ondelete="cascade")
