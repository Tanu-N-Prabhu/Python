from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from plyer import filechooser
import re
import pyrebase

kv = '''
<MainScreen>:
    name: 'mainscreen'
    MDLabel:
        id: username_info
        text: 'Hello Main'
        font_style: 'H1'
        halign: 'center'

    MDFloatLayout:
        id: floate
        Video:
            id: vid

        MDToolbar:
            title: 'Bottom navigation'
            md_bg_color: .2, .2, .2, 1
            specific_text_color: 1, 1, 1, 1

        MDBottomNavigation:
            panel_color: 1, 1, 1, 1
            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Home'
                icon: 'home-outline'
                MDRaisedButton:
                    id: upload
                    text: 'Upload'
                    pos_hint: {'center_x': .5, 'center_y': .4}
                    on_release:
                        app.file_chooser()
'''

class VideoUploadApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(kv)
        self.url = "link.json"  # Replace with your Firebase config
        return self.strng

    def file_chooser(self):
        try:
            # Support both Android and desktop platforms
            if platform == 'android':
                from android.permissions import request_permissions, Permission
                request_permissions([Permission.READ_EXTERNAL_STORAGE])
            
            filechooser.open_file(
                on_selection=self.selected,
                filters=['*.mp4', '*.avi', '*.mkv']  # Filter for video files
            )
        except Exception as e:
            print(f"Error opening file chooser: {e}")

    def selected(self, selection):
        try:
            # Handle case when user cancels file selection
            if not selection:
                print("File selection cancelled")
                return

            config = {
                # Add your Firebase config here
                'apiKey': 'your-api-key',
                'authDomain': 'your-auth-domain',
                'projectId': 'your-project-id',
                'storageBucket': 'your-storage-bucket',
                'messagingSenderId': 'your-messaging-sender-id',
                'appId': 'your-app-id'
            }

            firebase = pyrebase.initialize_app(config)
            storage = firebase.storage()

            file_path = selection[0]
            file_name = re.findall(r'[^/\\]+$', file_path)[0]  # Extract filename safely
            
            # Get login email from the login screen
            try:
                login_email = self.strng.get_screen('loginscreen').ids.login_email.text
            except:
                login_email = "default_user"  # Fallback if login screen not available

            # Upload file to Firebase
            storage.child(f"{login_email}/{file_name}").put(file_path)
            
            # Update UI
            self.root.ids.vid.source = file_path
            self.root.ids.upload.disabled = True

            # Optional: Switch to upload screen if it exists
            if 'uploadscreen' in self.strng.screen_manager.screen_names:
                self.strng.get_screen('mainscreen').manager.current = 'uploadscreen'
                self.strng.get_screen('mainscreen').manager.transition.direction = 'left'

        except Exception as e:
            print(f"Error during file upload: {e}")
            self.root.ids.upload.disabled = False

if __name__ == '__main__':
    VideoUploadApp().run()