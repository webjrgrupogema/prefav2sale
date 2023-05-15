# -*- coding: utf-8 -*-
# from odoo import http


# class Prefav2sale(http.Controller):
#     @http.route('/prefav2sale/prefav2sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prefav2sale/prefav2sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('prefav2sale.listing', {
#             'root': '/prefav2sale/prefav2sale',
#             'objects': http.request.env['prefav2sale.prefav2sale'].search([]),
#         })

#     @http.route('/prefav2sale/prefav2sale/objects/<model("prefav2sale.prefav2sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prefav2sale.object', {
#             'object': obj
#         })
