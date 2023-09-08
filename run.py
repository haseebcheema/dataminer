from daadbot.daad import Daad
import time

with Daad() as bot:
    bot.land_first_page()
    bot.accept_cookies()
    bot.change_language()
    bot.go_to_international_programs()

    time.sleep(10)

    bot.choose_programme('Computer Science')

    time.sleep(5)

    bot.apply_filters()
    bot.filter_amount_on_page()

    time.sleep(5)

    num_of_pages = bot.total_pages()
    for page in range(num_of_pages):
        time.sleep(20)
        print('SCRAPING PAGE ' + str(page+1))
        bot.get_daad_results()
        bot.go_to_next_page()

    print("Data is scraped successfully!")
