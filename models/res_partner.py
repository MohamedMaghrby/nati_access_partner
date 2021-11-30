from odoo import api, fields, models,_
from odoo.exceptions import ValidationError
import re
import phonenumbers



class ResPartner(models.Model):
    _inherit = "res.partner"
    userc_id = fields.Many2one('res.users', string='Owner', default=lambda self: self.env.uid)
    message_partner_ids = fields.Many2many(compute_sudo=True)
