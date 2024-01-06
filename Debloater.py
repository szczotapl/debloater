import wx
import subprocess

# Made by riviox

class AppDebloaterFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(AppDebloaterFrame, self).__init__(*args, **kw)

        self.panel = wx.Panel(self)

        self.action_label = wx.StaticText(self.panel, label="Select action:")
        self.action_radio_remove = wx.RadioButton(self.panel, label="Remove", style=wx.RB_GROUP)
        self.action_radio_install = wx.RadioButton(self.panel, label="Install")

        self.toggle_button = wx.Button(self.panel, label="Toggle Selected Apps", style=wx.BU_EXACTFIT)
        self.toggle_button.Bind(wx.EVT_BUTTON, self.on_toggle_button)

        self.apps_list = wx.CheckListBox(self.panel, choices=sorted(set(all_apps)))

        self.create_layout()

    def create_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(self.action_label, 0, wx.ALL, 5)
        sizer.Add(self.action_radio_remove, 0, wx.ALL, 5)
        sizer.Add(self.action_radio_install, 0, wx.ALL, 5)
        sizer.Add(self.toggle_button, 0, wx.ALL, 5)
        sizer.Add(self.apps_list, 1, wx.EXPAND | wx.ALL, 5)

        self.panel.SetSizer(sizer)
        self.Layout()

    def run_powershell_command(self, command):
        try:
            result = subprocess.run(["powershell", command], capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return e.stderr.strip()

    def toggle_apps(self, apps, action):
        for app in apps:
            command = None
            if action == "Remove":
                command = f"Get-AppxPackage -allusers {app} | Remove-AppxPackage"
            elif action == "Install":
                command = f"Get-AppxPackage -allusers {app} | Add-AppxPackage"

            if command:
                result = self.run_powershell_command(command)
                print(result)

        wx.MessageBox(f"{', '.join(apps)} apps have been {action}ed.", "App Debloater", wx.OK | wx.ICON_INFORMATION)

    def on_toggle_button(self, event):
        action = "Remove" if self.action_radio_remove.GetValue() else "Install"
        self.toggle_apps(self.apps_list.GetCheckedStrings(), action)


all_apps = sorted(set([
    "Microsoft.Windows.Photos",      # Photos
    "Microsoft.Windows.Calculator",  # Calculator
    "Microsoft.MicrosoftStickyNotes",# Sticky Notes
    "Microsoft.Windows.Camera",       # Camera
    "Microsoft.WindowsStore",         # Microsoft Store
    "Microsoft.WindowsFeedbackHub",   # Feedback Hub
    "Microsoft.MicrosoftSolitaireCollection",  # Solitaire Collection
    "Microsoft.WindowsAlarms",        # Alarms & Clock
    "Microsoft.YourPhone",            # Your Phone
    "Microsoft.WindowsSoundRecorder", # Voice Recorder
    "Microsoft.WindowsCalculator",    # Calculator
    "Microsoft.MicrosoftEdge",        # Microsoft Edge
    "Microsoft.WindowsMaps",          # Maps
    "Microsoft.Microsoft3DViewer",    # 3D Viewer
    "Microsoft.Windows.Photos",       # Photos
    "Microsoft.MicrosoftEdge",        # Microsoft Edge
    "Microsoft.XboxIdentityProvider", # Xbox Identity Provider
    "Microsoft.XboxGameOverlay",      # Xbox Game Overlay
    "Microsoft.SkypeApp",             # Skype
    "Microsoft.MicrosoftOneNote",     # OneNote
    "Microsoft.MicrosoftTo-Do",       # Microsoft To-Do
    "Microsoft.MicrosoftEdgeDevToolsClient",  # Microsoft Edge DevTools Client
    "Microsoft.Windows.ContentDeliveryManager",  # Content Delivery Manager
    "Microsoft.Windows.PrintDialog",  # Print Dialog
    "Microsoft.WindowsCalculator",    # Calculator
    "Microsoft.Windows.Photos",       # Photos
    "Microsoft.WindowsMaps",          # Maps
    "Microsoft.WindowsCamera",        # Camera
    "Microsoft.Windows.People",       # People
    "Microsoft.Windows.Cortana",      # Cortana
    "Microsoft.MicrosoftWhiteboard", # Microsoft Whiteboard
    "Microsoft.MicrosoftEdge.Stable", # Microsoft Edge Stable
    "Microsoft.Windows.HolographicFirstRun",  # Holographic First Run
]))

if __name__ == '__main__':
    app = wx.App(False)
    frame = AppDebloaterFrame(None, title='App Debloater', size=(400, 800))
    frame.Show()
    app.MainLoop()
