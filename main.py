from pyscript import display, document

def check(e):

    document.getElementById("output").innerHTML = ""

    Members = ["Nathan Ladion", "Carlos Borromeo", "Tyler Sales", "Samantha Lacuesta", "Joaquin Castor"]

    lastname = document.getElementById("Last-Name").value

    firstname = document.getElementById("First-Name").value

    full_name = (firstname + " " + lastname).strip()

    checker = full_name in Members

    statement = [f"Sorry {full_name}, your name is not on the list.",f"Congratulations {full_name}! You are now part of the ICT club."]

    finalstatement = statement[checker]

    display(finalstatement, target="output")