from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"  # nécessaire pour session admin

# ---------------------------
# INITIALISATION BASE
# ---------------------------
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS etudiants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        age INTEGER,
        email TEXT,
        filiere TEXT,
        niveau TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ---------------------------
# ROUTE PRINCIPALE
# ---------------------------
@app.route("/", methods=["GET", "POST"])
def form():

    if request.method == "POST":
        try:
            nom = request.form.get("nom")
            age = int(request.form.get("age"))
            email = request.form.get("email")
            filiere = request.form.get("filiere")
            niveau = request.form.get("niveau")

            # validation âge
            if age < 18 or age > 26:
                return "Erreur : âge doit être entre 18 et 26 ans"

            conn = sqlite3.connect("database.db")
            c = conn.cursor()

            # insertion
            c.execute("""
            INSERT INTO etudiants (nom, age, email, filiere, niveau)
            VALUES (?, ?, ?, ?, ?)
            """, (nom, age, email, filiere, niveau))

            conn.commit()

            # ---------------------------
            # STATISTIQUES
            # ---------------------------
            c.execute("SELECT AVG(age) FROM etudiants")
            age_moyen = c.fetchone()[0] or 0

            c.execute("SELECT filiere, COUNT(*) FROM etudiants GROUP BY filiere")
            filieres = c.fetchall()

            if not filieres:
                filieres = [("Aucune donnée", 1)]

            labels = [f[0] for f in filieres]
            values = [f[1] for f in filieres]

            conn.close()

            # ---------------------------
            # RESULTAT
            # ---------------------------
            return render_template(
                "result.html",
                nom=nom,
                age=age,
                email=email,
                filiere=filiere,
                niveau=niveau,
                age_moyen=age_moyen,
                labels=labels,
                values=values
            )

        except Exception as e:
            return f"Erreur serveur : {e}"

    return render_template("form.html")


# ---------------------------
# LOGIN ADMIN
# ---------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        password = request.form.get("password")

        if password == "yessoh":  # mot de passe admin
            session["admin"] = True
            return redirect("/admin")
        else:
            return "Mot de passe incorrect"

    return render_template("login.html")


# ---------------------------
# PAGE ADMIN
# ---------------------------
@app.route("/admin")
def admin():

    if not session.get("admin"):
        return redirect("/login")

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT * FROM etudiants")
    data = c.fetchall()

    # statistiques admin
    c.execute("SELECT COUNT(*) FROM etudiants")
    total = c.fetchone()[0]

    c.execute("SELECT AVG(age) FROM etudiants")
    age_moyen = c.fetchone()[0] or 0

    conn.close()

    return render_template(
        "admin.html",
        data=data,
        total=total,
        age_moyen=age_moyen
    )


# ---------------------------
# LOGOUT
# ---------------------------
@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/")


# ---------------------------
# LANCEMENT
# ---------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
