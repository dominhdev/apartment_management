# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_profile_group = fields.Boolean(default=False)
