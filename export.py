import sqlite3, csv
con = sqlite3.connect("data/agri.db")
cur = con.execute("SELECT * FROM parcelles")
with open("data/parcelles.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow([c[0] for c in cur.description])
    w.writerows(cur)
print("OK")