"""Testing Conditionals with Low Cards Ex."""

low_card: int = 4
current_card: int = 5

if current_card < low_card:
    low_card = current_card
else:
    print(str(current_card) + " is not the low card")
print("The low card is " + str(low_card))