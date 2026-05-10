from app import create_app

# This line MUST be outside of any 'if' blocks
app = create_app()

# You can keep this for local testing, but Vercel ignores it
if __name__ == "__main__":
    app.run(debug=True)
