from amazon import app 
from pyngrok import ngrok

if __name__ == '__main__':
    public_url = ngrok.connect(5000)
    print("URL pública:", public_url)
    app.run()
