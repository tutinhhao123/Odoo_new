from odoo import http


class ElearningSnippet(http.Controller):
    @http.route(['/latest_elearning_courses'], type="json", auth="public", website=True, methods=['POST'])
    def all_courses(self):
        courses = http.request.env['slide.channel'].search_read(
            [('website_published', '=', True)], ['name', 'image_1920', 'id'],
            order='create_date desc', limit=10)


return courses