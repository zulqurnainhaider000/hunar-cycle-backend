"""
Cross-Platform Mobile UI & Native Device APIs Curriculum
Course 2 for Mobile Dev category (15 Days).
"""

from seeder.curriculum_builder import make_day, make_course

MOBILE_EXTRA_DAYS = []

mob_titles = {
    1: ("React Native New Architecture: Fabric & TurboModules", "The New Architecture eliminates the asynchronous JSON bridge with synchronous C++ JSI bindings.", "Replacing a slow postal messenger with an instant fiber-optic phone line directly connecting Javascript to native iOS and Android."),
    2: ("Flexbox Layout Engine on Mobile Viewports", "Master responsive mobile layouts with flexDirection, justifyContent, alignItems, and flexWrap.", "Organizing books in a modular bookshelf; books stack vertically or line up horizontally based on the shelf direction."),
    3: ("Touch Handling: Pressable, Haptics & Gesture Responder", "Design responsive tactile interactions with Pressable states and physical haptic engine pulses.", "A physical piano key; pressing down gives resistance, reaches a key bed, and springs back with immediate tactile feedback."),
    4: ("High-Performance Lists: FlatList & VirtualizedList", "Render thousands of items smoothly by unmounting off-screen list elements from memory.", "A theater spotlight showing only the 3 actors currently on stage, keeping the other 100 backstage until their cue."),
    5: ("Stack & Bottom Tab Navigation Architecture", "Construct native mobile navigation hierarchies with deep linking and smooth screen transitions.", "A deck of cards in a casino; stacking new cards on top (push) and flipping them off (pop) with silky finger gestures."),
    6: ("Camera & Photo Library Hardware Integration", "Request runtime permissions and capture high-resolution imagery using native device cameras.", "A security guard asking for an ID badge before unlocking the door to the photography studio."),
    7: ("Geolocation, GPS Tracking & Background Location", "Track real-time device coordinates with foreground and battery-efficient background listeners.", "A maritime ship using satellite GPS signals to plot navigation coordinates across the open ocean."),
    8: ("Local Persistence: AsyncStorage & SQLite Relational Storage", "Persist user authentication tokens, cache feeds, and store structured offline data.", "A personal diary in your backpack; you can read and write notes on an airplane with zero Wi-Fi connection."),
    9: ("Device Sensors: Accelerometer, Gyroscope & Step Counting", "Read hardware sensor feeds to detect device motion, screen tilt, and physical orientation.", "An airplane's attitude gyroscope indicating whether the aircraft is banking left, diving, or flying level."),
    10: ("Push Notifications: Expo Notifications, APNs & FCM", "Schedule local time-sensitive reminders and route remote cloud push notifications.", "A courier delivering an urgent telegram directly to the front doorstep with an attention-grabbing bell ring."),
    11: ("Audio Playback & Background Media Services", "Manage audio focus, stream background sound, and interface with system lock screen media controls.", "A car stereo system; music pauses automatically when the GPS announces a turn and resumes afterward."),
    12: ("Biometric Authentication: FaceID & Fingerprint Security", "Authenticate users securely using device hardware biometrics via LocalAuthentication.", "A high-security biometric vault door that unlocks instantly with a retinal scan or fingerprint touch."),
    13: ("Offline-First Architecture & Network Listeners", "Queue API mutations in local SQLite when offline and sync automatically upon reconnection.", "A postal mailbox where letters wait safely until the mail carrier arrives to pick them up for delivery."),
    14: ("Native Profiling: Hermes Memory Dumps & JS Thread FPS", "Profile JavaScript thread frame rates (60 FPS) and eliminate memory leaks using Chrome DevTools.", "A racecar telemetry computer monitoring engine RPM, oil pressure, and tire temperature in real-time."),
    15: ("Capstone: Cross-Platform Native Mobile Production App", "Synthesize navigation, hardware APIs, local caching, and biometrics into an app-store ready build.", "You have mastered native cross-platform mobile engineering for production enterprise applications.")
}

for day_num in range(1, 16):
    t_info = mob_titles.get(day_num, (f"Day {day_num}: Mobile Architecture", "Build mobile native apps.", "Cross-platform mobile."))
    MOBILE_EXTRA_DAYS.append(make_day(
        order=day_num,
        title=f"Day {day_num}: {t_info[0]}",
        concept=t_info[1],
        analogy=t_info[2],
        sections=[
            (f"Mobile Architecture of {t_info[0]}", f"Mastering {t_info[0]} empowers mobile developers to build fluid, 60-FPS native applications that leverage device hardware with high battery efficiency."),
            ("Native API Integration & Production Patterns", "Handle Android and iOS permission lifecycles, configure background service threads, and prevent UI thread frame drops.")
        ],
        snippets=[
            (f"{t_info[0]} Component Snippet (TypeScript/React Native)", f"""import React from 'react';
import {{ View, Text, StyleSheet }} from 'react-native';

export const Day{day_num}Component = () => {{
  return (
    <View style={{styles.container}}>
      <Text style={{styles.title}}>{t_info[0]}</Text>
    </View>
  );
}};

const styles = StyleSheet.create({{
  container: {{ flex: 1, padding: 16, backgroundColor: '#0F172A' }},
  title: {{ color: '#F8FAFC', fontSize: 18, fontWeight: 'bold' }},
}});""", "typescript"),
            ("Device Permission State Checker (Python)", """def check_mobile_permission(granted: bool, can_ask_again: bool) -> str:
    if granted: return 'PERMISSION_GRANTED'
    if can_ask_again: return 'CAN_REQUEST_PERMISSION'
    return 'BLOCKED_OPEN_SETTINGS'

print("Permission check:", check_mobile_permission(True, False))""", "python")
        ],
        challenge=(f"Mobile Challenge Day {day_num}", "Write a function `calculate_aspect_ratio(width, height)` that returns `width / height` rounded to 2 decimal places.",
                   "def calculate_aspect_ratio(width: float, height: float) -> float:\n    pass",
                   "def calculate_aspect_ratio(width: float, height: float) -> float:\n    if height <= 0: return 0.0\n    return round(width / height, 2)", "1.78"),
        quizzes=[
            (f"What is the foundational role of {t_info[0]} in mobile app engineering?", [f"To leverage {t_info[0]} to deliver fluid, native 60 FPS mobile user experiences", "To cause app crashes on startup", "To disable touchscreen taps", "To drain device battery in 5 minutes"], f"To leverage {t_info[0]} to deliver fluid, native 60 FPS mobile user experiences", f"Day {day_num} covers {t_info[0]}."),
            ("How does React Native's New Architecture (JSI) improve performance over the old Bridge?", ["Enables direct, synchronous C++ memory access between JavaScript and Native without JSON serialization", "Replaces mobile phones with desktop towers", "Removes all styling from screens", "Disables all native device features"], "Enables direct, synchronous C++ memory access between JavaScript and Native without JSON serialization", "JSI allows JavaScript to invoke native methods synchronously with zero serialization overhead."),
            ("Why is FlatList vastly superior to ScrollView for rendering long lists of 1,000+ items?", ["FlatList virtualizes off-screen items, unmounting them to maintain constant memory usage", "FlatList deletes all images automatically", "FlatList only works on iPads", "ScrollView is not supported on Android"], "FlatList virtualizes off-screen items, unmounting them to maintain constant memory usage", "ScrollView renders all child elements immediately, causing high memory usage and dropped frames."),
            ("What must you always check before invoking device hardware (Camera, Location, Audio)?", ["Verify that runtime operating system permissions have been requested and granted by the user", "Restart the entire smartphone", "Turn off Wi-Fi", "Download a new operating system"], "Verify that runtime operating system permissions have been requested and granted by the user", "Invoking hardware without granted permissions throws fatal native security exceptions."),
            ("What does Biometric Authentication (FaceID / TouchID) protect in mobile security?", ["Verifies the physical user's presence before granting access to sensitive data or private keys", "Changes the phone wallpaper", "Tests the camera lens quality", "Calculates daily screen time"], "Verifies the physical user's presence before granting access to sensitive data or private keys", "Local biometrics provide hardware-level authentication without sending private keys across the network.")
        ]
    ))

CROSS_PLATFORM_MOBILE_BLUEPRINT = make_course(
    title="Cross-Platform Mobile UI & Native Device APIs",
    category="Mobile Dev",
    description=(
        "The complete 15-Day guide to professional React Native and cross-platform mobile engineering. "
        "Master the New Architecture (Fabric/TurboModules), Flexbox layouts, FlatList virtualization, "
        "hardware camera/audio/GPS integration, biometric FaceID security, offline SQLite persistence, and 60 FPS performance profiling."
    ),
    color="#4F46E5",
    days=MOBILE_EXTRA_DAYS
)
