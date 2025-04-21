import os
from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify, url_for, g
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def home():
    user_id = session.get("user_id")
    rows = db.execute(
        "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0", user_id)

    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0].get("cash", 0)

    holdings = []
    for row in rows:
        quote = lookup(row["symbol"])
        if quote is None:
            continue
        total_value = quote["price"] * row["total_shares"]
        print(
            f"Symbol: {row['symbol']}, Total Shares: {row['total_shares']}, Price: {quote['price']}, Total Value: {total_value}")
        holdings.append({
            "symbol": row["symbol"],
            "companyName": quote["name"],
            "shares": row["total_shares"],
            "price": quote["price"],
            "total_value": total_value
        })

    grand_total = cash + sum([holding["total_value"] for holding in holdings])
    return render_template("index.html", holdings=holdings, cash=cash, grand_total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        try:
            user_id = session["user_id"]
            rows = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
            cash_before = rows[0]["cash"]
            print(f"Cash before: {cash_before}")

            symbol = request.form.get("symbol")
            print(f"Symbol: {symbol}")
            if not symbol or lookup(symbol) is None:
                return apology("invalid symbol", 400)

            quote = lookup(symbol)
            print(f"Quote: {quote}")

            shares = request.form.get("shares")
            print(f"Shares: {shares}")
            if not shares or not shares.isdigit() or int(shares) <= 0:
                return apology("invalid shares", 400)

            total_cost = quote["price"] * int(shares)
            print(f"Total cost: {total_cost}")

            if cash_before < total_cost:
                return apology("can't afford", 400)

            db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, user_id)
            db.execute("INSERT INTO transactions (user_id, symbol, shares, price, transacted) VALUES (?,?,?,?,?)",
                       user_id, symbol, int(shares), quote["price"], datetime.now())
            return redirect("/")

        except Exception as e:
            print(f"Error: {e}")
            return apology("internal server error", 500)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    user_id = session["user_id"]
    transactions = db.execute(
        "SELECT symbol, shares, price, transacted FROM transactions WHERE user_id = ? ORDER BY transacted DESC", user_id)

    # Calculate the grand total
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    transaction_totals = [round(transaction["shares"] * transaction["price"], 2)
                          for transaction in transactions]
    grand_total = round(cash + sum(transaction_totals), 2)

    return render_template("history.html", transactions=transactions, grand_total=grand_total, cash=cash)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        if quote is None:
            return apology("invalid symbol", 400)
        quote["price"] = f"{quote['price']:.2f}"
        return render_template("quoted.html", quote=quote)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            return apology("must provide username and password", 400)

        if password != confirmation:
            return apology("passwords do not match", 400)

        try:
            user_id = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                                 username, generate_password_hash(password))

        session["user_id"] = user_id
        return redirect("/")

    return render_template("register.html")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol or not shares.isdigit() or int(shares) <= 0:
            return apology("must provide a valid symbol and shares", 400)

        rows = db.execute(
            "SELECT SUM(shares) as total_shares FROM transactions WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)
        if len(rows) != 1 or rows[0]["total_shares"] < int(shares):
            return apology("not enough shares", 400)

        quote = lookup(symbol)
        sale_value = quote["price"] * int(shares)

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", sale_value, session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, transacted) VALUES (?,?, ?, ?, ?)",
                   session["user_id"], symbol, -int(shares), quote["price"], datetime.now())

        return redirect("/")

    else:
        stocks = db.execute(
            "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0", session["user_id"])
        print(stocks)  # Debug print statement
        return render_template("sell.html", stocks=stocks)


@app.route("/password", methods=["GET", "POST"])
def passwordchange():
    if request.method == "POST":
        # Get form data
        current_password = request.form.get("current_password")
        new_password = request.form.get("new_password")
        confirmation = request.form.get("confirmation")

        # Get the current user's data
        user_id = session["user_id"]
        user = db.execute("SELECT * FROM users WHERE id = ?", user_id)[0]

        # Verify current password
        if not check_password_hash(user["hash"], current_password):
            return apology("invalid current password", 400)

        # Check if new password and confirmation match
        if new_password != confirmation:
            return apology("new passwords do not match", 400)

        # Update the password in the database
        db.execute("UPDATE users SET hash = ? WHERE id = ?",
                   generate_password_hash(new_password), user_id)

        return redirect("/")

    return render_template("password.html")
