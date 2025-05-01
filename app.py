from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Connection to Cloud SQL
conn = pymysql.connect(
    host='34.30.228.26',  # Replace with your Cloud SQL IP
    user='root',
    password='akunwafiq',
    database='products',
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def index():
    with conn.cursor() as cursor:
        cursor.execute("SELECT name, price, image_url FROM product_info")
        products = cursor.fetchall()
    
    # Format the price to Rupiah (e.g., Rp25.000)
    for product in products:
        product['price'] = f"Rp{product['price']:,.0f}"
    
    return render_template('index.html', products=products)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

