import json
import websocket
from datetime import datetime

# WebSocket URL and SOL/USD feed ID
WS_URL = "wss://hermes.pyth.network/ws"
SOL_FEED_ID = "0xef0d8b6fda2ceba41da15d4095d1da392a0d2f8ed0c6c7bc0f4cfac8c280b56d"

# ANSI color codes for max visual flair
GREEN = '\033[92m'  # Bright green for price increases
RED = '\033[91m'    # Bright red for price decreases
CYAN = '\033[96m'   # Cyan for neutral/info
RESET = '\033[0m'

# Track the last price for comparison
last_price = None

def on_message(ws, message):
    global last_price
    try:
        data = json.loads(message)
        if data.get("type") == "price_update" and "price_feed" in data:
            price_feed = data["price_feed"]
            price_data = price_feed["price"]
            
            # Extract price, exponent, timestamp, and confidence
            price = int(price_data["price"])
            expo = int(price_data["expo"])
            publish_time = price_data["publish_time"]
            conf = int(price_data["conf"])
            
            # Convert to real values
            real_price = price * (10 ** expo)
            real_conf = conf * (10 ** expo)
            
            # Convert publish_time to readable format
            readable_time = datetime.utcfromtimestamp(publish_time).strftime('%H:%M:%S')
            
            # Visual trend indicator
            if last_price is not None:
                price_change = real_price - last_price
                direction = '▲' if price_change > 0 else '▼'
                color = GREEN if price_change > 0 else RED
                # Scale bars based on change magnitude (cap at 10)
                bar_count = min(int(abs(price_change) * 100), 10)
                trend_bars = '|' * bar_count if bar_count > 0 else ''
                trend = f"{color}{direction}{trend_bars}{RESET}"
                change_str = f"{color}{price_change:+.4f}{RESET}"
            else:
                trend = f"{CYAN}START{RESET}"
                change_str = f"{CYAN}N/A{RESET}"
            
            # Print only if price changes by 0.001 or more (or first update)
            if last_price is None or abs(real_price - last_price) >= 0.001:
                print(f"{CYAN}SOL/USD{RESET} | ${real_price:>9.4f} ± {real_conf:<6.4f} | {readable_time} UTC | {trend} | Change: {change_str}")
                last_price = real_price
    except Exception as e:
        print(f"{RED}❌ Error:{RESET} {e}")

def on_error(ws, error):
    print(f"{RED}❌ WebSocket Error:{RESET} {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"{RED}Connection closed:{RESET} {close_status_code} - {close_msg}")

def on_open(ws):
    subscribe_msg = {
        "type": "subscribe",
        "ids": [SOL_FEED_ID]
    }
    ws.send(json.dumps(subscribe_msg))
    print(f"{CYAN}🔄 Subscribed to SOL/USD feed{RESET}")

ws = websocket.WebSocketApp(
    WS_URL,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)

ws.run_forever()