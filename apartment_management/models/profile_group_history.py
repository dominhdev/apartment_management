# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class ProfileGroupHistory(models.Model):
    _name = "profile.group.history"
    _description = "Profile Group History"
    _inherit = ['mail.thread']
    _rec_name = 'user_id'
    _order = "id desc"

    function_admin_user_id = fields.Many2one("res.users")
    user_id = fields.Many2one("res.users")
    history_ids = fields.One2many("profile.group.history.line", 'history_id')


class ProfileGroupHistoryLine(models.Model):
    _name = "profile.group.history.line"
    _description = "Profile Group History Line"
    _inherit = ['mail.thread']
    _order = "id desc"

    group_id = fields.Many2one("res.groups")
    history_id = fields.Many2one("profile.group.history", ondelete='cascade')
