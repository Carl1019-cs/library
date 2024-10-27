# -*- coding: utf-8 -*-

from odoo import models, fields


class Book(models.Model):
    _inherit = 'library.book'

    author_id = fields.Many2one('res.partner', String="Author", required=False)
    

