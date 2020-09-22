from odoo import http


class DemoOdoo(http.Controller):

    @http.route('/demo/allen', auth='user')  #路徑，auth判斷需登入才可看
    def list(self, **kwargs):
        obj = http.request.env['demo.odoo.tutorial'] #使用的model
        objs = obj.search([])
        return http.request.render(
            'demo_odoo_tutorial.demo_allen_template',{'objs': objs}) #指定到demo_odoo_tutorial(controllers資料夾上層資料夾名稱)下template的ID為demo_odoo_template的頁面
            #在這裡是指到views/demo_odoo_template.xml內，丟過去時命名為'objs'，template的承接也要用'objs'來接
            #設定好後，就會從機台網址+route名稱的網站路徑上看到，ex:localhost:8096/demo/demo
