from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class ConnectMssql(models.Model):
    _name = "test.allen.mssql"
    _description = 'Connect to MS SQL Server'
    server_name = fields.Char('Server', required=True, help="The server name, could be an IP or a URL")
    database_name = fields.Char('Database name', required=True)
    user_name = fields.Char('User name', required=True)
    password = fields.Char('Password', required=True)
    query = fields.Text('SQL Query/Instruction', required=True,
                        help="A Select statement or an insert/update/delete instruction")
    result = fields.Text('Result')

    #@api.multi odoo13中已內建，不需呼叫
    def execute_query(self, name):
        try:
            import pymssql

            # Connection Parameters
            my_server = self.server_name
            my_user = self.user_name
            my_database = self.database_name
            my_password = self.password
            my_query = self.query

            # Make the connection and execute the query
            conn = pymssql.connect(server=my_server, user=my_user, password=my_password, database=my_database)
            cursor = conn.cursor()
            cursor.execute(my_query)

            # Check whether the query is a select statement or an insert/update/delete instruction
            if my_query.strip().split(" ")[0].lower() == "select":
                rows = cursor.fetchall()
                my_result = ""
                for i in rows:
                    for x in i:
                        my_result += "\t" + str(x)
                    my_result += "\n"

                # Show the result
                self.result = my_result
            else:
                conn.commit()
                self.result = "Statement executed successfully, please check your database or make a select statement."
            conn.close()

        except:
            self.result = "An Error Occurred, please check your parameters!\n" \
                          "And make sure (pymssql) is installed (pip3 install pymssql)."


# class DemoOdooTutorial(models.Model):
#     _name = 'test.allen.mssql' #name的規範用.隔開，不要用其他的，進到DB時會自動變成demo_odoo_tutorial
#     _description = 'Allen Model測試' #單純說明
#     _inherit = ['mail.thread', 'mail.activity.mixin'] # track_visibility  繼承

#     name = fields.Char('Description', required=True)

#     # track_visibility='always' 和 track_visibility='onchange'
#     is_done_track_onchange = fields.Boolean(
#         string='Is Done?', default=False, track_visibility='onchange')
#     name_track_always = fields.Char(string="track_name", track_visibility='always') #Track_visiblity會當資料變更儲存時，作變更紀錄追蹤，沒有繼承mail，寫view時的追蹤會出錯

#     start_datetime = fields.Datetime('Start DateTime', default=fields.Datetime.now())
#     stop_datetime = fields.Datetime('End Datetime', default=fields.Datetime.now())

#     field_onchange_demo = fields.Char('onchange_demo')
#     field_onchange_demo_set = fields.Char('onchange_demo_set', readonly=True)

#     # float digits
#     # field tutorial
#     input_number = fields.Float(string='input number', digits=(10,3)) #digits使用10進位，取到小數點第三位
#     field_compute_demo = fields.Integer(compute="_get_field_compute") # 預設是readonly 僅計算顯示，不會存在DB中，如要存在DB中需要加入store=True

#     _sql_constraints = [ #設定資料庫限制，1.設定欄位限定唯一值2.唯一值欄位名稱3.說明
#         ('name_uniq', 'unique(name)', 'Description must be unique'),
#     ]

#     @api.constrains('start_datetime', 'stop_datetime')
#     def _check_date(self):
#         for data in self:
#             if data.start_datetime > data.stop_datetime:
#                 raise ValidationError(
#                     "data.stop_datetime  > data.start_datetime"
#                 )

#     @api.depends('input_number') #抓取input_number的值去計算
#     def _get_field_compute(self):#為上方_get_field_compute的呼叫
#         for data in self:
#             data.field_compute_demo = data.input_number * 1000

#     @api.onchange('field_onchange_demo')
#     def onchange_demo(self):
#         if self.field_onchange_demo:
#             self.field_onchange_demo_set = 'set {}'.format(self.field_onchange_demo)