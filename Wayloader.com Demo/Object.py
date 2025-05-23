from flask import Flask, request, render_template_string
import folium

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login with Map</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }}
        body {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: linear-gradient(45deg, #1a2a6c, #b21f1f, #fdbb2d);
            animation: gradientAnimation 6s infinite alternate;
        }}
        @keyframes gradientAnimation {{
            0% {{ background-position: left; }}
            100% {{ background-position: right; }}
        }}
        .container {{
            display: flex;
            width: 80%;
            max-width: 900px;
            height: 500px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            overflow: hidden;
            backdrop-filter: blur(10px);
        }}
        .left, .right {{
            width: 50%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 30px;
            color: white;
        }}
        .left h2 {{
            margin-bottom: 20px;
            font-size: 24px;
        }}
        input, button {{
            width: 90%;
            padding: 12px;
            margin: 10px 0;
            border: none;
            border-radius: 5px;
        }}
        input {{
            background: rgba(255, 255, 255, 0.2);
            color: white;
            outline: none;
        }}
        input::placeholder {{
            color: rgba(255, 255, 255, 0.8);
        }}
        button {{
            background: #ff7f50;
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: 0.3s;
        }}
        button:hover {{
            background: #ff4500;
        }}
        .right iframe {{
            width: 100%;
            height: 100%;
            border: none;
        }}
        /* E-commerce Product Page */
        .product-screen {{
            width: 100%;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: url('https://source.unsplash.com/1200x800/?product,ecommerce') no-repeat center center/cover;
            color: white;
            text-align: center;
            flex-direction: column;
            backdrop-filter: blur(5px);
        }}
        .product-card {{
            background: rgba(0, 0, 0, 0.7);
            padding: 30px;
            border-radius: 10px;
            max-width: 500px;
            width: 90%;
            text-align: center;
        }}
        .product-card h1 {{
            font-size: 28px;
            margin-bottom: 10px;
        }}
        .product-card p {{
            font-size: 18px;
            margin-bottom: 10px;
        }}
        .price {{
            font-size: 24px;
            font-weight: bold;
            color: #ffbb00;
        }}
        .btn {{
            display: inline-block;
            margin-top: 10px;
            padding: 12px 24px;
            background: #ff7f50;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: 0.3s;
        }}
        .btn:hover {{
            background: #ff4500;
        }}
    </style>
</head>
<body>
    {content}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    map_center = [33.6844, 73.0479]  # Default location (Islamabad, PK)
    my_map = folium.Map(location=map_center, zoom_start=12)
    map_html = my_map._repr_html_()

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            return render_template_string(HTML_TEMPLATE.format(content=f"""
                <div class='product-screen'>
                    <div class='product-card'>
                        <h1>Amazing Smartwatch</h1>
                        <p>Experience the best smartwatch with AI features and health tracking.</p>
                        <p class='price'>$199.99</p>
                        <a href='#' class='btn'>Add to Cart</a>
                    </div>
                    <div class='product-card'>
                        <h1>Smartphone</h1>
                        <p>Experience the best smartphone with advanced features and camera.</p>
                        <p class='price'>$999.99</p>
                        <a href='#' class='btn'>Add to Cart</a>
                    </div>
                    <div class='product-card'>
                        <h1>Headphones</h1>
                        <p>Experience the best headphones with noise cancellation and wireless connectivity.</p>
                        <p class='price'>$49.99</p>
                        <a href='#' class='btn'>Add to Cart</a>
                        <link 
                    </div>
                </div>
            """))

    login_form = f"""
        <div class="container">
            <div class="left">
                <h2>Login</h2>
                <form method="POST">
                    <input type="text" name="username" placeholder="Username" required>
                    <input type="password" name="password" placeholder="Password" required>
                    <button type="submit">Login</button>
                </form>
            </div>
            <div class="right">
                {map_html}
            </div>
        </div>
    """
    return render_template_string(HTML_TEMPLATE.format(content=login_form))

if __name__ == '__main__':
    app.run(debug=True)
