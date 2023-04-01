import spacy
import parser
import tkinter as tk
from tkinter import ttk

# Load the trained NER model
nlp = spacy.load("C:\\Users\\Farhan Ali Rahmoon\\Desktop\\moonath\\pythonProject")
nlp2 = spacy.load("en_core_web_sm")


def get_asset_name_by_ticker(ticker):
    for asset_name, asset_info in supported_assets.items():
        if asset_info["Ticker"].lower() == ticker.lower():
            return asset_name
    return None


def process_input(input_text):
    doc = nlp(input_text)
    doc2 = nlp2(input_text)
    intents = []
    user_email = None
    journal_number = None
    asset_name = None
    trade_date = ""
    trade_entry = 0
    trade_size = 0
    trade_type = ""

    for ent in doc.ents:
        intents.append(ent.label_)
        if ent.label_ == "ASSET_NAME":
            asset_name = ent.text.capitalize()

    print(intents)

    for ent in doc2.ents:
        if ent.label_ == "DATE":
            trade_date = parser.parse(ent.text).strftime("%Y-%m-%d")
        elif ent.label_ == "MONEY":
            trade_entry = float(ent.text)
        elif ent.label_ == "CARDINAL":
            trade_size = int(ent.text)

    for token in doc2:
        if token.like_email:
            user_email = token.text
        elif token.ent_type_ == "ORDINAL":
            journal_number = word_to_number(token.text)
        elif "short" in str(token).lower():
            trade_type = "Short"
        elif "long" in str(token).lower():
            trade_type = "Long"

    print(f"Date: {trade_date}, Entry: {trade_entry}, Size: {trade_size}, Type: {trade_type}, Asset: {asset_name}")

    if user_email is not None and not has_user_logged_in:
        email_entry.delete(0, tkinter.END)
        email_entry.insert(0, user_email)
        load_data()
    elif "LOGIN" in intents and not has_user_logged_in:
        if email_entry.get() != "":
            load_data()
        else:
            print("Sorry, you haven't provided us with your email.")
    elif "OPEN" in intents and "JOURNAL" in intents:
        if journal_number is not None and has_user_logged_in:
            if journal_number > len(yes_journal_frames) or journal_number < 0:
                print("Sorry, please enter a valid journal number to open.")
            else:
                journal_clicked(journal_number)
        elif not has_user_logged_in:
            print("Sorry, you need to login first before opening a journal.")
        elif journal_number is None:
            for i in range(len(journal_name_labels)):
                if journal_name_labels[i].cget("text").lower() in input_text.lower():
                    journal_number = i + 1
                    journal_clicked(journal_number)

            if journal_number is None:
                print("Sorry, you haven't provided which journal you want to open.")
    elif "OPEN" in intents:
        if "ASSET_NAME" in intents:
            if len(asset_name) < 6:
                asset_name = get_asset_name_by_ticker(asset_name)

            if asset_name in assets_added[current_vertical_line_position - 1]:
                create_trade_log(asset_name, True)
            else:
                print("Sorry, you are trying to open an asset that does not exists in this journal.")
        else:
            print("Sorry, you haven't provided which asset you would like to open.")
    elif "TRADE_ACTION" in intents and asset_name is not None:
        if len(asset_name) < 6:
            asset_name = get_asset_name_by_ticker(asset_name)

        if asset_name in assets_added[current_vertical_line_position - 1]:
            entry_price_entry, exit_price_entry, trade_type_entry, trade_size_entry, profit_loss_label, trade_actions_add, entry_date_entry, exit_date_entry, index = add_trade(assets_added[current_vertical_line_position - 1].index(asset_name), entry_price=trade_entry, entry_date=trade_date, trade_size=trade_size, trade_type=trade_type)
            confirm_trade_entry(entry_price_entry, exit_price_entry, trade_type_entry, trade_size_entry, profit_loss_label, trade_actions_add, entry_date_entry, exit_date_entry, index)
            add_entry(yes_journal_frames_database_ids[current_vertical_line_position - 1], assets_added[current_vertical_line_position - 1][index], entry_price_entry.get(), exit_price_entry.get(), entry_date_entry.get(), exit_date_entry.get(), trade_size_entry.get(), trade_type_entry.get(), profit_loss_label)
        else:
            print("Sorry, you are adding a trade to an asset that does not exists in this journal.")
    else:
        print("Sorry, I can't understand your command.")
