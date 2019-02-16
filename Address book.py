import sqlite3
import time
import os

db = sqlite3.connect("addresses.db")
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS addresses(id integer primary key AUTOINCREMENT, fname TXT, lname TXT, address TXT, phone INT, email TXT)""")


def store():
	fname = input("First name: ")
	lname = input("Last name: ")
	address = input("Address: ")
	phone = input("Phone number: ")
	email = input("Email: ")
	cur.execute("""INSERT INTO addresses VALUES (?, ?, ?, ?, ?, ?)""", (None, fname, lname, address, phone, email))
	db.commit()
	print("Successfully stored everything into database.")
	os.system('pause')
	main()


def search():
	print("Search for name, address, email or phone number")
	s = input("> ")
	cur.execute("""SELECT * FROM addresses WHERE fname or lname or address or phone or email = ?""", (s,))
	result = cur.fetchall()
	print(result)
	os.system('pause')
	main()


def edit():
	print("Type the entry ID you wan't to edit.")
	id = input("Entry ID: ")
	print("1) Change first name")
	print("2) Change Last name")
	print("3) Change Address")
	print("4) Change Phone number")
	print("5) Change Email")
	print("6) Go back")
	choice = input("> ")
	if choice == "1":
		data = input("> ")
		cur.execute("""UPDATE addresses SET fname = ? WHERE id = ?""", (data, id))
		db.commit()
		print("First name changed to: {}".format(data))
		edit()
		
	if choice == "2":
		data = input("> ")
		cur.execute("""UPDATE addresses SET lname = ? WHERE id = ?""", (data, id))
		db.commit()
		print("Last name changed to: {}".format(data))
		edit()
		
	if choice == "3":
		data = input("> ")
		cur.execute("""UPDATE addresses SET address = ? WHERE id = ?""", (data, id))
		db.commit()
		print("Address changed to: {}".format(data))
		edit()
		
	if choice == "4":
		data = input("> ")
		cur.execute("""UPDATE addresses SET phone = ? WHERE id = ?""", (data, id))
		db.commit()
		print("Phone number changed to: {}".format(data))
		edit()
		
	if choice == "5":
		data = input("> ")
		cur.execute("""UPDATE addresses SET email = ? WHERE id = ?""", (data, id))
		db.commit()
		print("Email address changed to: {}".format(data))
		edit()
	if choice == "6":
		main()

def delete():
	print("Please give the ID of the entry you wan't to delete.")
	id = input("> ")
	print("Are you sure you wan't to delete ID {}? (yes or no)".format(id))
	confirm = input("> ")
	if confirm == "yes" or "Yes":
		cur.execute("""DELETE FROM addresses WHERE ID = ?""", id)
		print("Database entry deleted.")
		os.system('pause')
		main()
	else:
		print("Database entry deletion cancelled.")
		time.sleep(3)
		main()

def main():
    print("1) Store.")
    print("2) Search.")
    print("3) Edit")
    print("4) Delete")
    main = input("> ")
    if main == "1":
        store()

    if main == "2":
        search()

    if main == "3":
        edit()

    if main == "4":
        delete()

main()
