from booking.booking import Booking
import time
# inst=Booking()
# inst.land_first_page()

with Booking() as bot:
    bot.land_first_page()
    bot.click_cross()
    inp="USD"
    bot.change_currency(inp)
    bot.dest('Munnar')
    bot.date('23-05-17', '23-05-20')
    bot.search()
    bot.apply_filterations()
    time.sleep(3)
    bot.report_results()
    print("Exiting...")