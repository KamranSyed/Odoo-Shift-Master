# -*- coding: utf-8 -*-
from odoo import http

# class Ksshiftmaster(http.Controller):
#     @http.route('/ksshiftmaster/ksshiftmaster/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ksshiftmaster/ksshiftmaster/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ksshiftmaster.listing', {
#             'root': '/ksshiftmaster/ksshiftmaster',
#             'objects': http.request.env['ksshiftmaster.ksshiftmaster'].search([]),
#         })

#     @http.route('/ksshiftmaster/ksshiftmaster/objects/<model("ksshiftmaster.ksshiftmaster"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ksshiftmaster.object', {
#             'object': obj
#         })