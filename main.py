import web
from web.contrib.template import render_jinja

urls = ("/", "hello", "/categories", "categories", "/payments", "payments")
app = web.application(urls, globals())

render = render_jinja(
    "templates",
    encoding="utf-8",
)


categories_list = []
payments_list = []


class hello:
    def GET(self):
        return render.index(
            categories=categories_list,
            payments=payments_list,
        )


class categories:
    def POST(self):
        input_string = web.data()
        key, value = input_string.decode("utf-8").split("=")
        result_dict = {key: value}

        categories_list.append(result_dict["category"])
        return web.redirect("/")


class payments:
    def POST(self):
        input_string = web.data()
        pairs = input_string.decode("utf-8").split("&")

        result_dict = {}
        for pair in pairs:
            key, value = pair.split("=")
            result_dict[key] = value

        payments_list.append(result_dict)
        return web.redirect("/")


if __name__ == "__main__":
    app.run()
