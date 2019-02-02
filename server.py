from flask import Flask, request

app = Flask(__name__)
default_port = 5000
default_host = "0.0.0.0"


class TmpView:
    @classmethod
    def create_with_param(cls, args):
        return cls()

    def __init__(self):
        self.msg = 'Hello!'
        self.status = 200

    def return_content(self):
        return self.msg, self.status


def data_(form):
    obj = form.create_with_param(request.args)
    return obj.return_content()


@app.route('/', methods=['GET'])
def ret_word_data():
    return data_(TmpView)


if __name__ == '__main__':
    app.run(port=default_port, host=default_host)
