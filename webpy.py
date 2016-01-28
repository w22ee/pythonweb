#use python 2.7 and lpthw.web 模块
import web
urls = (
    '/','index'
)
app = web.application(urls,globals())
class index:
    def GET(self):
        greeting = "greeting!"
        return greeting
if __name__ == "__main__":
    app.run()