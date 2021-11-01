from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <html>
        <form action="/login" method="post">
            <input name="password" type="hidden" value="notcorrectpassword">
            <button>sign In</button>
        </form>
        <!-- Correct Password is OkaKoro -->
    </html>
    """

@app.route("/login", methods=['POST'])
def login():
    data = request.form["password"]
    if (data == "PopOSIsBad"):
        return """
        <img src="https://img.ifunny.co/images/243fbc3362b4824fdc85221fa2520843d6b9b3e0712afbd4cc1cec55cead67bc_1.jpg" alt="">
<img src="https://i.kym-cdn.com/photos/images/original/002/068/730/c9a.jpg" alt="">
<img src="https://i.kym-cdn.com/photos/images/facebook/001/943/392/a22.jpg" alt="">
<img src="https://i.kym-cdn.com/editorials/icons/original/000/002/696/hololive.jpg" alt="">
<img src="https://pbs.twimg.com/media/EXeXDYcUMAYTdm8.jpg:large" alt="">
<img src="https://scontent-sjc3-1.xx.fbcdn.net/v/t1.6435-9/p526x296/130007559_213638176945272_6599088633405354191_n.jpg?_nc_cat=102&ccb=1-5&_nc_sid=8bfeb9&_nc_ohc=BSEg9ZeMc3cAX-5gaqj&_nc_ht=scontent-sjc3-1.xx&oh=2b94ee76aad3c48ff8d4667c5dbc3891&oe=61A5DFD8" alt="">

        """
    if (data=="notcorrectpassword"):
        return "Bruh, do something lamooooooo"
        
    return "bruh' youstupd"
