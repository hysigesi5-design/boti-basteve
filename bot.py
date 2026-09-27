
import os
import time
import requests
import logging
from telegram import Bot

# Konfigurimi i logimit
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Konfigurimet e Telegramit (merren nga Environment Variables te Render ose vendosen ketu)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "VENDOS_TOKEN_E_BOT_FATHER_KETU")
CHAT_ID = os.getenv("CHAT_ID", "VENDOS_CHAT_ID_KETU")

bot = Bot(token=TELEGRAM_TOKEN)

def get_odds_data():
    """
    Funksioni ku lidhesh me burimin e kuotave (Pinnacle dhe Bet365).
    Këtu mund të vendosësh logjikën për të marrë të dhënat në kohë reale.
    """
    # Shembull simulimi i marrjes së kuotave
    pinnacle_odd = 1.95
    bet365_odd = 1.90
    
    return pinnacle_odd, bet365_odd

def check_and_alert():
    pinnacle_old = None
    bet365_old = None
    
    logging.info("Monitorimi i kuotave u nis...")
    
    while True:
        try:
            pinnacle_current, bet365_current = get_odds_data()
            
            # Krahasojme nese ka ndryshim te kuotave
            if pinnacle_current != pinnacle_old or bet365_current != bet365_old:
                message = (
                    f"🚨 **Lëvizje Kuotash e Identifikuar!**\n\n"
                    f"🔴 **Pinnacle:** {pinnacle_current}\n"
                    f"🔵 **Bet365:** {bet365_current}\n"
                    f"⚡ Pinnacle ka lëvizur më shpejt!"
                )
                
                # Dërgo mesazhin në Telegram
                bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")
                logging.info("Njoftimi u dërgua në Telegram!")
                
                pinnacle_old = pinnacle_current
                bet365_old = bet365_current
                
        except Exception as e:
            logging.error(f"Gabim gjatë kontrollit të kuotave: {e}")
            
        # Kontrollo çdo 10 sekonda
        time.sleep(10)

if __name__ == "__main__":
    check_and_alert()
