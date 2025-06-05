import easygui

cards = {
    1: {"Name": "1 Stonelin",
        "Strength": "7" ,
        "Speed": "1",
        "Stealth": "25",
        "Cunning": "15"
    },
    2: {"Name": "2 Vexscream",
        "Strength": "1" ,
        "Speed": "6",
        "Stealth": "21",
        "Cunning": "19"
    },
    3: {"Name": "3 Dawnmirage",
        "Strength": "5" ,
        "Speed": "15",
        "Stealth": "18",
        "Cunning": "22"
    },
    4: {"Name": "4 Blazegolem",
        "Strength": "15" ,
        "Speed": "20",
        "Stealth": "23",
        "Cunning": "6"
    },
    5: {"Name": "5 Websnake",
        "Strength": "7" ,
        "Speed": "15",
        "Stealth": "10",
        "Cunning": "5"
    },
    6: {"Name": "6 Moldvine",
        "Strength": "21" ,
        "Speed": "18",
        "Stealth": "14",
        "Cunning": "5"
    },
    7: {"Name": "7 Vortexwing",
        "Strength": "19" ,
        "Speed": "13",
        "Stealth": "19",
        "Cunning": "2"
    },
    8: {"Name": "8 Rotthing",
        "Strength": "16" ,
        "Speed": "7",
        "Stealth": "4",
        "Cunning": "12"
    },
    9: {"Name": "9 Froststep",
        "Strength": "14" ,
        "Speed": "14",
        "Stealth": "17",
        "Cunning": "4"
    },
    10: {"Name": "10 Wispghoul",
        "Strength": "17" ,
        "Speed": "19",
        "Stealth": "3",
        "Cunning": "2"
    },
}

while True:
    card_list = "\n".join([
        "{}: Strength = {}, Speed = {}, Stealth = {}, Cunning = {}\n".format(
            card["Name"], card["Strength"], card["Speed"],
            card["Stealth"], card["Cunning"]
        ) for card in cards.values()
    ])
    easygui.msgbox("Available Cards:\n\n" + card_list,
                   title="Monster Card Game")

    choice = easygui.buttonbox("Choose an option below:",
                               title="Monster Card Game",
                               choices=["Add", "Search",
                                        "Remove", "Exit"])

    

    if choice == "Add":
        new_card = easygui.multenterbox("Enter new card details:", "Add Card",
                                        ["ID", "Name", "Strength", "Speed",
                                         "Stealth", "Cunning"])
        if new_card:
            card_id = int(new_card[0])
            cards[card_id] = {
                "Name": new_card[1],
                "Strength": int(new_card[2]),
                "Speed": int(new_card[3]),
                "Stealth": int(new_card[4]),
                "Cunning": int(new_card[5])
            }
            while True:
                edit_choice = easygui.buttonbox(
                    "New card added:\n\n" + str(cards[card_id]) +
                    "\n\nDo you wanna edit this card?",
                    title="Monster Card Game",
                    choices=["Edit", "Confirm"]
                )

                if edit_choice == "Edit":
                    updated_card = easygui.multenterbox("Update card details:"
                                                        , "Edit Card",
                                                        ["Name", "Strength",
                                                         "Speed", "Stealth",
                                                         "Cunning"],
                                                        [cards[card_id]["Name"],
                                                         str(cards[card_id]["Strength"]),
                                                         str(cards[card_id]["Speed"]),
                                                         str(cards[card_id]["Stealth"]),
                                                         str(cards[card_id]["Cunning"])])

                    if updated_card:
                        cards[card_id]["Name"] = updated_card[0]
                        cards[card_id]["Strength"] = int(updated_card[1])
                        cards[card_id]["Speed"] = int(updated_card[2])
                        cards[card_id]["Stealth"] = int(updated_card[3])
                        cards[card_id]["Cunning"] = int(updated_card[4])

                elif edit_choice == "Confirm":
                    easygui.msgbox("Card added successfully",
                                   title="Monster Card Game")
                    break



            

    elif choice == "Search":
        search_name = easygui.enterbox("Enter the number and the name of the"
                                       " card to search"
                                       " (First letter need to be capital) :",
                                       title="Monster Card Game")
        if search_name:
            search_name = search_name.strip().lower()
            result = None
            for card in cards.values():
                if card["Name"].lower() == search_name:
                    result = card

            if result:
                easygui.msgbox("Card found:\n{}".format(result),
                               title="Monster Card Game")
            else:
                easygui.msgbox("Card not found",
                               title="Monster Card Game")


                

    elif choice == "Remove":
        remove_id = easygui.enterbox("Enter the ID of the card to remove:",
                                     title="Monster Card Game")
        if remove_id:
            remove_id = int(remove_id)
            if remove_id in cards:
                del cards[remove_id]
                easygui.msgbox("Card removed successfully",
                               title="Monster Card Game")
            else:
                easygui.msgbox("Card ID not found",
                               title="Monster Card Game")
                

    elif choice == "Exit":
        break
