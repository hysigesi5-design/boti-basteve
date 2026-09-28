import time
import requests
from datetime import datetime, timezone, timedelta

TELEGRAM_TOKEN = "8836301007:AAF6gqPbAb1BImjUpafalu7IlGyQgreJRfA"
CHAT_ID = "6432339063"

def dergo_sinjalizimin(mesazhi):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mesazhi,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Gabim në Telegram: {e}")

def kontrollo_ndeshjet_72_oret():
    koha_tani = datetime.now(timezone.utc).replace(tzinfo=None)
    kufiri_72_ore = koha_tani + timedelta(hours=72)
    
    ndeshjet_e_dites = [
        {"ndeshje": "Milan - Inter", "pinnacle": 1.70, "bet365": 1.95, "koha": (koha_tani + timedelta(hours=10)).strftime("%Y-%m-%dT%H:%M:%S")},
        {"ndeshje": "Juventus - Torino", "pinnacle": 1.50, "bet365": 1.55, "koha": (koha_tani + timedelta(hours=50)).strftime("%Y-%m-%dT%H:%M:%S")}
    ]
    
    print(f"[{datetime.now()}] Po kontrollohet programi për ndeshjet brenda 72 orëve...")

    for match in ndeshjet_e_dites:
        koha_str = match["koha"].split(".")[0].replace("Z", "")
        koha_ndeshjes = datetime.strptime(koha_str, "%Y-%m-%dT%H:%M:%S")
        
        if koha_tani <= koha_ndeshjes <= kufiri_72_ore:
            emri = match["ndeshje"]
            pin = match["pinnacle"]
            b365 = match["bet365"]
            diferenca = b365 - pin
            
            if diferenca >= 0.15:
                mesazhi = (
                    f"🚨 *ALARM: DROPPING ODDS (72H)* 🚨\n\n"
                    f"⚽ Ndeshja: *{emri}*\n"
                    f"📉 Pinnacle (Ulur): *{pin}*\n"
                    f"📈 Bet365 (Lart): *{b365}*\n"
                    f"💡 Diferenca: *+{diferenca:.2f}*"
                )
                dergo_sinjalizimin(mesazhi)

if __name__ == "__main__":
    print("Boti u nis në Cloud dhe po punon 24/7...")
    while True:
        kontrollo_ndeshjet_72_oret()
        time.sleep(1800)  # Kontrollon çdo 30 minuta
