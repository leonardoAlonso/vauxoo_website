from odoo import http
from odoo.addons.website_sale.controllers.main import  WebsiteSale


class Academy(http.Controller):

    @http.route('/academy/academy', auth='public', website=True)
    def index(self, **kw):
        teachers = http.request.env['academy.teachers']
        return http.request.render('academy.index', {
            'teachers': teachers.search([])
        })

    @http.route('/academy/<model("academy.teachers"):teacher>', auth='public', website=True)
    def biography(self, teacher):
        return http.request.render('academy.biography', {
            'person': teacher
        })


class WebsiteSaleInh(WebsiteSale):
    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        print("Inherits correctly")
        res = super(WebsiteSaleInh, self).shop(page=page, category=category, search=search, ppg=ppg, **post)
        import ipdb
        #ipdb.set_trace()
        res.qcontext['categories'] = res.qcontext['categories'].sorted(key=lambda r: r.name)
        res.qcontext['search'] = 'ipad'
        return res
