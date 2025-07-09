##to send mssg thru whatsapp to anybody
import pywhatkit
import time

try:
    print("Opening WhatsApp Web...")
    pywhatkit.sendwhatmsg_instantly("+919072773868", "Hello from Python! ✅", wait_time=20, tab_close=True)
    print("Waiting for message to send...")
    time.sleep(20)  
    print("✅ Message sent successfully!")
except Exception as e:
    print("❌ Error:", e)
    