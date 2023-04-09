from public.input_processing import create_input_processing
import spacy

# Register the custom component factory globally
spacy.Language.factory("input_processing", func=create_input_processing)

# Load the trained NER model
nlp = spacy.load("C:\\Users\\Farhan Ali Rahmoon\\Desktop\\moonath\\pythonProject")


def process_input(input_text):
    doc = nlp(input_text)
    intents = doc._.intents

    if doc._.user_email is not None and not has_user_logged_in:
        email_entry.delete(0, tkinter.END)
        email_entry.insert(0, doc._.user_email)
        load_data()
    elif "LOGIN" in intents and not has_user_logged_in:
        if email_entry.get() != "":
            load_data()
        else:
            print("Sorry, you haven't provided us with your email.")
    elif "OPEN" in intents and "JOURNAL" in intents:
        if doc._.journal_number is not None and has_user_logged_in:
            if doc._.journal_number > len(yes_journal_frames) or doc._.journal_number < 0:
                print("Sorry, please enter a valid journal number to open.")
            else:
                journal_clicked(doc._.journal_number)
        elif not has_user_logged_in:
            print("Sorry, you need to login first before opening a journal.")
        elif doc._.journal_number is None:
            for i in range(len(journal_name_labels)):
                if journal_name_labels[i].cget("text").lower() in input_text.lower():
                    doc._.journal_number = i + 1
                    journal_clicked(doc._.journal_number)

            if doc._.journal_number is None:
                print("Sorry, you haven't provided which journal you want to open.")
    elif "OPEN" in intents:
        if "ASSET_NAME" in intents:
            if len(doc._.asset_name) < 6:
                doc._.asset_name = get_asset_name_by_ticker(doc._.asset_name)

            if doc._.asset_name in assets_added[current_vertical_line_position - 1]:
                create_trade_log(doc._.asset_name, True)
            else:
                print("Sorry, you are trying to open an asset that does not exists in this journal.")
        else:
            print("Sorry, you haven't provided which asset you would like to open.")
    elif "TRADE_ACTION" in intents and doc._.asset_name is not None:
        if len(doc._.asset_name) < 6:
            asset_name = get_asset_name_by_ticker(doc._.asset_name)

        if doc._.asset_name in assets_added[current_vertical_line_position - 1]:
            entry_price_entry, exit_price_entry, trade_type_entry, trade_size_entry, profit_loss_label, trade_actions_add, entry_date_entry, exit_date_entry, index = add_trade(assets_added[current_vertical_line_position - 1].index(asset_name), entry_price=doc._.trade_entry, entry_date=doc._.trade_date, trade_size=doc._.trade_size, trade_type=doc._.trade_type)
            confirm_trade_entry(entry_price_entry, exit_price_entry, trade_type_entry, trade_size_entry, profit_loss_label, trade_actions_add, entry_date_entry, exit_date_entry, index)
            add_entry(yes_journal_frames_database_ids[current_vertical_line_position - 1], assets_added[current_vertical_line_position - 1][index], entry_price_entry.get(), exit_price_entry.get(), entry_date_entry.get(), exit_date_entry.get(), trade_size_entry.get(), trade_type_entry.get(), profit_loss_label)
        else:
            print("Sorry, you are adding a trade to an asset that does not exists in this journal.")
    else:
        print("Sorry, I can't understand your command.")