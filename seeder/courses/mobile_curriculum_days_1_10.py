"""
Mobile App Development 40-Day Curriculum - Module 1 & Module 2 (Days 1 to 10)
Module 1: App Basics & UI (Days 1-7)
Module 2: Navigation & Routing (Days 8-10, with Day 11 in next chunk)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_1_TO_10 = [
    # -------------------------------------------------------------
    # DAY 1
    # -------------------------------------------------------------
    DayBlueprint(
        order=1,
        title="Day 1: Mobile IDE & Environment Setup",
        concept="Configuring Node.js, Android Studio, VS Code, and Virtual Device Emulators",
        analogy="Think of setting up a mobile development environment like assembling a professional artist's studio. You need your easel and brushes (VS Code), your specialized canvas and paints (Node.js & React Native / Flutter SDK), and a test mannequin (the Android/iOS phone emulator) so you can preview your artwork without needing a live gallery visitor every time you make a stroke!",
        theory_sections=[
            {
                "heading": "The Mobile Development Toolchain",
                "body": "Building cross-platform mobile apps requires three foundational tools: (1) A code editor (Visual Studio Code), (2) The runtime environment (Node.js LTS for React Native or Flutter SDK), and (3) Platform simulators (Android Studio AVD for Android and Xcode Simulator for iOS). These tools compile and hot-reload your code directly onto virtual or physical devices."
            },
            {
                "heading": "Expo vs React Native CLI",
                "body": "React Native provides two primary workflows: **Expo**, a managed ecosystem that handles native build tools, dependencies, and testing on real phones via QR code without installing Android Studio immediately; and **Bare React Native CLI**, which provides direct access to native Java/Kotlin and Objective-C/Swift source code."
            }
        ],
        code_snippets=[
            {
                "title": "Verifying Node.js and npm Installation",
                "code": "# In your terminal, verify Node LTS (v18+ or v20+ recommended):\nnode --version\nnpm --version"
            },
            {
                "title": "Creating a Modern Mobile App with Expo CLI",
                "code": "# Initialize a new mobile app project:\nnpx create-expo-app@latest MyMobileApp --template blank-typescript\n\n# Navigate into directory:\ncd MyMobileApp"
            },
            {
                "title": "Starting the Mobile Metro Bundler",
                "code": "# Launch the Metro bundler local server:\nnpx expo start\n\n# Press 'a' to open Android Emulator\n# Press 'i' to open iOS Simulator (macOS only)\n# Scan QR code with the Expo Go app on your physical smartphone!"
            },
            {
                "title": "Configuring Android Virtual Device (AVD) in Android Studio",
                "code": "# Tools -> Device Manager -> Create Device\n# Select 'Pixel 7' -> Download System Image (e.g. Android 14 API 34)\n# Ensure ANDROID_HOME is set in system environment variables"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="App Entrypoint Environment Inspector",
            description="Write a minimal React Native App component that imports Text and View from 'react-native', centers content on screen, and renders 'Mobile Environment: Online'.",
            starter_code="import React from 'react';\nimport { View, Text, StyleSheet } from 'react-native';\n\n// TODO: Implement App component\n",
            solution_code="import React from 'react';\nimport { View, Text, StyleSheet } from 'react-native';\n\nexport default function App() {\n  return (\n    <View style={styles.container}>\n      <Text style={styles.text}>Mobile Environment: Online</Text>\n    </View>\n  );\n}\n\nconst styles = StyleSheet.create({\n  container: { flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: '#0F172A' },\n  text: { color: '#10B981', fontSize: 18, fontWeight: 'bold' },\n});",
            expected_output="Mobile Environment: Online"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the JavaScript bundler used by React Native to compile and serve code to devices?",
                options=["Metro", "Webpack", "Vite", "Rollup"],
                correct_answer="Metro",
                explanation="Metro is the dedicated, high-speed JavaScript bundler optimized for React Native mobile apps."
            ),
            QuizQuestionBlueprint(
                question="What is the primary benefit of the Expo framework for mobile developers?",
                options=[
                    "It streamlines setup and enables instant live preview on real phones via QR code without native builds.",
                    "It replaces JavaScript with C++.",
                    "It automatically creates database schemas.",
                    "It allows apps to bypass Apple App Store review rules."
                ],
                correct_answer="It streamlines setup and enables instant live preview on real phones via QR code without native builds.",
                explanation="Expo abstracts away native Android/iOS complexity, enabling rapid development and device testing."
            ),
            QuizQuestionBlueprint(
                question="Which tool inside Android Studio allows you to configure and run virtual smartphone emulators?",
                options=["Android Virtual Device (AVD) Manager", "Gradle Profiler", "ADB Terminal", "Logcat Viewer"],
                correct_answer="Android Virtual Device (AVD) Manager",
                explanation="The AVD Manager creates virtual hardware profiles running Android system images on your computer."
            ),
            QuizQuestionBlueprint(
                question="What environment variable must point to your Android SDK installation directory?",
                options=["ANDROID_HOME", "SDK_PATH", "JAVA_HOME", "ANDROID_DIR"],
                correct_answer="ANDROID_HOME",
                explanation="`ANDROID_HOME` tells tools like React Native CLI and Gradle where the Android SDK lives."
            ),
            QuizQuestionBlueprint(
                question="What key combination or gesture in the mobile emulator reloads the application during development?",
                options=["Pressing 'R' twice (or Cmd/Ctrl + M for developer menu)", "Closing the terminal", "Restarting the computer", "Reinstalling Node.js"],
                correct_answer="Pressing 'R' twice (or Cmd/Ctrl + M for developer menu)",
                explanation="Pressing 'R' twice triggers a fast reload; Cmd/Ctrl + M opens the in-app developer debug menu."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 2
    # -------------------------------------------------------------
    DayBlueprint(
        order=2,
        title="Day 2: Core Mobile Widgets & Components",
        concept="Building mobile interfaces using View, Text, TouchableOpacity, and TextInput",
        analogy="Think of mobile components like building with specialized LEGO blocks. Instead of standard HTML tags like `<div>` and `<p>` (which phones do not understand), mobile frameworks provide native building blocks: `<View>` is the foundation brick (container), `<Text>` is the label brick, `<TouchableOpacity>` is the clickable button brick, and `<TextInput>` is the keyboard slot!",
        theory_sections=[
            {
                "heading": "Native Primitives vs HTML Elements",
                "body": "Mobile devices do not have an HTML Document Object Model (DOM). Instead, React Native maps your JSX components directly to platform-native UI widgets: `<View>` compiles to `android.view.ViewGroup` on Android and `UIView` on iOS. `<Text>` compiles to `TextView` and `UILabel`."
            },
            {
                "heading": "Interactive Buttons and Text Inputs",
                "body": "To handle touch interactions, use `<TouchableOpacity>` or `<Pressable>`, which automatically provide visual opacity feedback when tapped. `<TextInput>` connects directly to the device's native virtual keyboard, handling placeholder text, password masking (`secureTextEntry`), and keyboard types."
            }
        ],
        code_snippets=[
            {
                "title": "Importing Core Native Primitives",
                "code": "import React, { useState } from 'react';\nimport { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';"
            },
            {
                "title": "The Native View and Text Primitives",
                "code": "const Greeting = () => (\n  <View style={styles.card}>\n    <Text style={styles.heading}>Hello, Mobile Engineer!</Text>\n    <Text style={styles.subheading}>Welcome to Day 2.</Text>\n  </View>\n);"
            },
            {
                "title": "Building a Controlled TextInput",
                "code": "const SearchField = () => {\n  const [query, setQuery] = useState('');\n  return (\n    <TextInput\n      style={styles.input}\n      placeholder=\"Search skills...\"\n      placeholderTextColor=\"#94A3B8\"\n      value={query}\n      onChangeText={text => setQuery(text)}\n      autoCapitalize=\"none\"\n    />\n  );\n};"
            },
            {
                "title": "Creating an Interactive TouchableOpacity Button",
                "code": "const SubmitButton = ({ onPress }) => (\n  <TouchableOpacity \n    style={styles.button} \n    onPress={onPress} \n    activeOpacity={0.7}\n  >\n    <Text style={styles.buttonText}>Submit Form</Text>\n  </TouchableOpacity>\n);"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Interactive Counter Component",
            description="Write a React Native component with a Text element displaying a count number, and a TouchableOpacity button labeled 'Increment' that updates the count on tap.",
            starter_code="import React, { useState } from 'react';\nimport { View, Text, TouchableOpacity } from 'react-native';\n\n// TODO: Implement Counter\n",
            solution_code="import React, { useState } from 'react';\nimport { View, Text, TouchableOpacity, StyleSheet } from 'react-native';\n\nexport default function Counter() {\n  const [count, setCount] = useState(0);\n  return (\n    <View style={styles.container}>\n      <Text style={styles.countText}>Count: {count}</Text>\n      <TouchableOpacity style={styles.btn} onPress={() => setCount(c => c + 1)}>\n        <Text style={styles.btnText}>Increment</Text>\n      </TouchableOpacity>\n    </View>\n  );\n}\n\nconst styles = StyleSheet.create({\n  container: { padding: 20, alignItems: 'center' },\n  countText: { fontSize: 24, color: '#F8FAFC', marginBottom: 12 },\n  btn: { backgroundColor: '#3B82F6', paddingVertical: 12, paddingHorizontal: 24, borderRadius: 12 },\n  btnText: { color: '#FFF', fontWeight: 'bold' }\n});",
            expected_output="Count: 1"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why can you not use standard HTML tags like `<div>` and `<p>` in React Native?",
                options=[
                    "Mobile devices have no browser DOM; React Native maps native primitives like `<View>` and `<Text>` directly to iOS and Android UI widgets.",
                    "HTML is copyrighted by Google.",
                    "React Native only supports SVG.",
                    "Phones cannot display text."
                ],
                correct_answer="Mobile devices have no browser DOM; React Native maps native primitives like `<View>` and `<Text>` directly to iOS and Android UI widgets.",
                explanation="React Native compiles native primitives (`<View>`, `<Text>`) directly into native Android and iOS views."
            ),
            QuizQuestionBlueprint(
                question="What property on `<TextInput>` masks input characters for secure password entry?",
                options=["secureTextEntry={true}", "isPassword={true}", "mask={true}", "type=\"password\""],
                correct_answer="secureTextEntry={true}",
                explanation="`secureTextEntry={true}` hides typed characters for passwords and sensitive inputs."
            ),
            QuizQuestionBlueprint(
                question="What event prop on `<TextInput>` is called when the user types text (receiving the string directly)?",
                options=["onChangeText", "onChange", "onInput", "onValueChange"],
                correct_answer="onChangeText",
                explanation="`onChangeText={(text) => ...}` passes the updated string directly without synthetic event wrappers."
            ),
            QuizQuestionBlueprint(
                question="What component provides smooth opacity feedback when touched by a user on mobile?",
                options=["TouchableOpacity", "TouchableHighlight", "Pressable", "All of the above"],
                correct_answer="All of the above",
                explanation="React Native provides `TouchableOpacity`, `TouchableHighlight`, and `Pressable` for tactile touch responses."
            ),
            QuizQuestionBlueprint(
                question="What happens if you render raw text strings directly inside a `<View>` without wrapping them in `<Text>`?",
                options=[
                    "React Native crashes with an invariant violation error: 'Text strings must be rendered within a <Text> component'.",
                    "It displays normally.",
                    "It converts to a button automatically.",
                    "It renders in the terminal only."
                ],
                correct_answer="React Native crashes with an invariant violation error: 'Text strings must be rendered within a <Text> component'.",
                explanation="In React Native, all visible text must strictly reside inside `<Text>` tags."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 3
    # -------------------------------------------------------------
    DayBlueprint(
        order=3,
        title="Day 3: Mobile Layouts with Flexbox",
        concept="Mastering flexDirection, justifyContent, alignItems, and flex ratios on mobile displays",
        analogy="Think of Mobile Flexbox like packing luggage for a flight. The suitcase (`<View>`) has an orientation: by default, items are stacked vertically from top to bottom (Column). You can tell the clothes: 'Distribute evenly across the space' (`justifyContent: 'space-between'`) or 'Center perfectly in the middle' (`alignItems: 'center'`)!",
        theory_sections=[
            {
                "heading": "Mobile Flexbox vs Web Flexbox: Key Differences",
                "body": "React Native implements the CSS Flexbox specification, but with one critical default difference: on the web, `flexDirection` defaults to `row` (horizontal). In React Native, `flexDirection` defaults to `column` (vertical), matching how smartphone screens naturally flow from top to bottom."
            },
            {
                "heading": "Primary Axis vs Cross Axis",
                "body": "`justifyContent` controls alignment along the primary axis (vertical in column, horizontal in row). Options include `flex-start`, `center`, `flex-end`, `space-between`, and `space-around`. `alignItems` controls alignment along the opposing cross axis."
            }
        ],
        code_snippets=[
            {
                "title": "Default Column Layout with Centering",
                "code": "const CenterBox = () => (\n  <View style={styles.centerContainer}>\n    <Text style={styles.text}>Perfect Center</Text>\n  </View>\n);\n\nconst styles = StyleSheet.create({\n  centerContainer: {\n    flex: 1, // Takes 100% of available screen height\n    justifyContent: 'center', // Primary axis (Vertical)\n    alignItems: 'center',     // Cross axis (Horizontal)\n    backgroundColor: '#0F172A'\n  }\n});"
            },
            {
                "title": "Row Layout with Space-Between (Header Navbar)",
                "code": "const Header = () => (\n  <View style={styles.headerRow}>\n    <Text style={styles.logo}>HunarCycle</Text>\n    <View style={styles.badge}><Text style={styles.badgeText}>🔥 5</Text></View>\n  </View>\n);\n\nconst styles = StyleSheet.create({\n  headerRow: {\n    flexDirection: 'row',\n    justifyContent: 'space-between',\n    alignItems: 'center',\n    paddingHorizontal: 20,\n    paddingVertical: 16,\n    backgroundColor: '#1E293B'\n  }\n});"
            },
            {
                "title": "Proportional Flex Ratios",
                "code": "const TwoColumnLayout = () => (\n  <View style={{ flex: 1, flexDirection: 'row' }}>\n    {/* Left pane takes 1/3 of width (flex: 1) */}\n    <View style={{ flex: 1, backgroundColor: '#334155' }} />\n    {/* Right pane takes 2/3 of width (flex: 2) */}\n    <View style={{ flex: 2, backgroundColor: '#1E293B' }} />\n  </View>\n);"
            },
            {
                "title": "Flex Wrapping for Chip Tags",
                "code": "const TagList = () => (\n  <View style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 8 }}>\n    <Text style={styles.chip}>React Native</Text>\n    <Text style={styles.chip}>TypeScript</Text>\n    <Text style={styles.chip}>Mobile UI</Text>\n    <Text style={styles.chip}>Flexbox</Text>\n  </View>\n);"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Top-Bar Navigation Layout",
            description="Write a StyleSheet with a `navBar` style that lays out children horizontally in a row, spaces items with 'space-between', centers them vertically with 'center', and has a height of 60.",
            starter_code="import { StyleSheet } from 'react-native';\n\n// TODO: Implement navBar style\n",
            solution_code="import { StyleSheet } from 'react-native';\n\nexport const styles = StyleSheet.create({\n  navBar: {\n    flexDirection: 'row',\n    justifyContent: 'space-between',\n    alignItems: 'center',\n    height: 60,\n    paddingHorizontal: 16,\n    backgroundColor: '#1E293B'\n  }\n});",
            expected_output="navBar style defined with flexDirection row and space-between"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the default `flexDirection` in React Native?",
                options=["column", "row", "row-reverse", "column-reverse"],
                correct_answer="column",
                explanation="In React Native, `flexDirection` defaults to `column` to suit vertical smartphone screens."
            ),
            QuizQuestionBlueprint(
                question="Which Flexbox property aligns items along the cross axis?",
                options=["alignItems", "justifyContent", "alignSelf", "flexWrap"],
                correct_answer="alignItems",
                explanation="`alignItems` controls alignment across the secondary (cross) axis."
            ),
            QuizQuestionBlueprint(
                question="What does setting `flex: 1` on a root container `<View>` accomplish?",
                options=[
                    "It instructs the view to expand and occupy 100% of the available display screen area.",
                    "It fixes the height to 100 pixels.",
                    "It rotates the screen by 90 degrees.",
                    "It creates a 1px border."
                ],
                correct_answer="It instructs the view to expand and occupy 100% of the available display screen area.",
                explanation="`flex: 1` expands the component to fill all unoccupied space of its parent container."
            ),
            QuizQuestionBlueprint(
                question="If two sibling Views have `flex: 1` and `flex: 3`, how much screen space does the second View occupy?",
                options=[
                    "75% of the available space (3 parts out of 4 total parts).",
                    "300 pixels.",
                    "33% of the space.",
                    "50% of the space."
                ],
                correct_answer="75% of the available space (3 parts out of 4 total parts).",
                explanation="Flex ratios divide space proportionally: 1 + 3 = 4 total units, so 3 units = 75%."
            ),
            QuizQuestionBlueprint(
                question="Which property distributes children with equal spacing between them along the primary axis?",
                options=["justifyContent: 'space-between'", "justifyContent: 'center'", "alignItems: 'stretch'", "flexWrap: 'wrap'"],
                correct_answer="justifyContent: 'space-between'",
                explanation="`space-between` places the first item at the start, the last item at the end, and distributes extra space evenly."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 4
    # -------------------------------------------------------------
    DayBlueprint(
        order=4,
        title="Day 4: High-Performance Lists with FlatList & ScrollView",
        concept="Rendering scalable datasets efficiently with FlatList virtualization, keyExtractor, and renderItem",
        analogy="Think of `<ScrollView>` like a physical paper scroll 5 miles long: even if you can only see 6 inches of paper through your magnifying glass, the entire 5 miles is unrolled on your carpet (wasting all your RAM!). `<FlatList>` is like a conveyor belt: it only creates the 5 cards you can currently see on screen, recycling them as you scroll!",
        theory_sections=[
            {
                "heading": "ScrollView vs FlatList",
                "body": "`<ScrollView>` renders all children simultaneously upon mount. It is suitable for small, bounded content (like an article or settings screen). If you pass 1,000 items to a `ScrollView`, the phone will stutter and run out of memory. `<FlatList>` uses list virtualization: it only mounts visible items, recycling off-screen views for maximum 60fps performance."
            },
            {
                "heading": "The Three Core FlatList Props",
                "body": "`<FlatList>` requires: (1) `data`: an array of items, (2) `renderItem`: a callback function returning the JSX card for each item (`({ item }) => <Card item={item} />`), and (3) `keyExtractor`: a function returning a unique string ID for each item (`item => item.id`), enabling React to optimize re-renders."
            }
        ],
        code_snippets=[
            {
                "title": "Basic FlatList Implementation",
                "code": "import React from 'react';\nimport { FlatList, View, Text, StyleSheet } from 'react-native';\n\nconst COURSES = [\n  { id: 'c1', title: 'React Native Fundamentals' },\n  { id: 'c2', title: 'Python Backend Systems' },\n  { id: 'c3', title: 'Mobile UI/UX Masterclass' }\n];\n\nconst CourseList = () => (\n  <FlatList\n    data={COURSES}\n    keyExtractor={item => item.id}\n    renderItem={({ item }) => (\n      <View style={styles.card}>\n        <Text style={styles.cardTitle}>{item.title}</Text>\n      </View>\n    )}\n  />\n);"
            },
            {
                "title": "Horizontal Scrolling FlatList",
                "code": "<FlatList\n  data={COURSES}\n  keyExtractor={item => item.id}\n  renderItem={({ item }) => <HorizontalCard title={item.title} />}\n  horizontal={true}\n  showsHorizontalScrollIndicator={false}\n  snapToInterval={280} // Snaps smoothly like a carousel\n  decelerationRate=\"fast\"\n/>"
            },
            {
                "title": "Adding Header, Footer & Empty State to FlatList",
                "code": "<FlatList\n  data={filteredData}\n  keyExtractor={item => item.id}\n  renderItem={renderItem}\n  ListHeaderComponent={<Text style={styles.header}>Available Modules</Text>}\n  ListEmptyComponent={<Text style={styles.empty}>No courses found.</Text>}\n  ListFooterComponent={<View style={{ height: 40 }} />}\n/>"
            },
            {
                "title": "Pull-to-Refresh & Infinite Scrolling Endpoints",
                "code": "<FlatList\n  data={items}\n  keyExtractor={item => item.id}\n  renderItem={renderItem}\n  refreshing={isRefreshing}\n  onRefresh={handleRefresh} // Triggered on pull-down\n  onEndReached={fetchNextPage} // Triggered when scrolling near bottom\n  onEndReachedThreshold={0.5}\n/>"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="FlatList Data Render Configuration",
            description="Write a FlatList JSX declaration passing `data={students}`, extracting key with `item => item.id.toString()`, and rendering `<Text>{item.name}</Text>`.",
            starter_code="import React from 'react';\nimport { FlatList, Text } from 'react-native';\n\nconst students = [{ id: 1, name: 'Zubair' }, { id: 2, name: 'Amina' }];\n// TODO: Implement FlatList\n",
            solution_code="import React from 'react';\nimport { FlatList, Text } from 'react-native';\n\nconst students = [{ id: 1, name: 'Zubair' }, { id: 2, name: 'Amina' }];\n\nexport const StudentList = () => (\n  <FlatList\n    data={students}\n    keyExtractor={item => item.id.toString()}\n    renderItem={({ item }) => <Text>{item.name}</Text>}\n  />\n);",
            expected_output="FlatList configured with data, keyExtractor, and renderItem"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is `<FlatList>` preferred over `<ScrollView>` for long or infinite lists of data?",
                options=[
                    "`FlatList` uses virtualization to only render items currently visible on screen, conserving RAM and battery.",
                    "`FlatList` automatically downloads fonts.",
                    "`ScrollView` does not support touch interactions.",
                    "`FlatList` compiles to WebAssembly."
                ],
                correct_answer="`FlatList` uses virtualization to only render items currently visible on screen, conserving RAM and battery.",
                explanation="Virtualization dynamically unmounts off-screen items, preventing memory crashes."
            ),
            QuizQuestionBlueprint(
                question="What prop on `<FlatList>` extracts a unique key for each item in the data array?",
                options=["keyExtractor", "idExtractor", "itemKey", "primaryKey"],
                correct_answer="keyExtractor",
                explanation="`keyExtractor={(item, index) => item.id}` assigns a unique React key to each item."
            ),
            QuizQuestionBlueprint(
                question="What prop renders custom JSX when the `data` array passed to `<FlatList>` is completely empty?",
                options=["ListEmptyComponent", "emptyView", "fallbackComponent", "renderEmpty"],
                correct_answer="ListEmptyComponent",
                explanation="`ListEmptyComponent={<EmptyView />}` displays automatically whenever `data` has length 0."
            ),
            QuizQuestionBlueprint(
                question="How do you transform a vertical FlatList into a horizontal carousel?",
                options=["horizontal={true}", "direction=\"horizontal\"", "flexDirection=\"row\"", "orientation=\"landscape\""],
                correct_answer="horizontal={true}",
                explanation="`horizontal={true}` configures the layout and scrolling direction horizontally."
            ),
            QuizQuestionBlueprint(
                question="What prop triggers a callback when the user scrolls near the bottom of the list for infinite pagination?",
                options=["onEndReached", "onBottom", "onLoadMore", "onScrollLimit"],
                correct_answer="onEndReached",
                explanation="`onEndReached` executes when the scroll offset is within `onEndReachedThreshold` of the list bottom."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 5
    # -------------------------------------------------------------
    DayBlueprint(
        order=5,
        title="Day 5: Mobile Styling, Design Tokens & Dark Mode",
        concept="Creating scalable design systems with StyleSheet.create, color tokens, and useColorScheme",
        analogy="Think of an app's styling system like a theatre costume department. Instead of sewing each actor's shirt individually from scratch on stage, the wardrobe director creates a unified palette of fabrics and design rules (Design Tokens). When the scene shifts from day to night (Dark Mode), the crew switches the lighting preset, and the entire set adapts instantly!",
        theory_sections=[
            {
                "heading": "StyleSheet.create and Performance",
                "body": "While inline style objects work (`style={{ color: 'red' }}`), they allocate new JavaScript objects on every render pass, triggering garbage collection churn. `StyleSheet.create` sends style IDs to the native bridge once, caching styles and validating syntax at compile time."
            },
            {
                "heading": "System Dark Mode Detection with useColorScheme",
                "body": "Modern mobile operating systems allow users to toggle Light and Dark appearances globally. React Native provides the `useColorScheme()` hook, which returns `'light'` or `'dark'`, updating reactively when the user changes system settings."
            }
        ],
        code_snippets=[
            {
                "title": "Centralized Design Tokens (tokens.ts)",
                "code": "export const Colors = {\n  dark: {\n    background: '#0F172A', // Slate 900\n    card: '#1E293B',       // Slate 800\n    text: '#F8FAFC',       // Slate 50\n    textMuted: '#94A3B8',  // Slate 400\n    primary: '#10B981',    // Emerald 500\n    border: '#334155'\n  },\n  light: {\n    background: '#F8FAFC',\n    card: '#FFFFFF',\n    text: '#0F172A',\n    textMuted: '#64748B',\n    primary: '#059669',\n    border: '#E2E8F0'\n  }\n};"
            },
            {
                "title": "Reactive Dark Mode with useColorScheme",
                "code": "import React from 'react';\nimport { View, Text, useColorScheme, StyleSheet } from 'react-native';\nimport { Colors } from './tokens';\n\nconst ThemedScreen = () => {\n  const scheme = useColorScheme(); // 'light' or 'dark'\n  const theme = Colors[scheme === 'dark' ? 'dark' : 'light'];\n\n  return (\n    <View style={[styles.container, { backgroundColor: theme.background }]}>\n      <Text style={[styles.title, { color: theme.text }]}>Welcome to Hunar Cycle</Text>\n      <Text style={{ color: theme.textMuted }}>Theme: {scheme}</Text>\n    </View>\n  );\n};"
            },
            {
                "title": "Reusable Component Style Composition",
                "code": "const styles = StyleSheet.create({\n  container: { flex: 1, padding: 20, justifyContent: 'center' },\n  title: { fontSize: 22, fontWeight: '800', marginBottom: 8 }\n});"
            },
            {
                "title": "Platform-Specific Elevation and Shadows",
                "code": "import { Platform, StyleSheet } from 'react-native';\n\nconst cardShadow = StyleSheet.create({\n  shadow: {\n    ...Platform.select({\n      ios: {\n        shadowColor: '#000',\n        shadowOffset: { width: 0, height: 4 },\n        shadowOpacity: 0.2,\n        shadowRadius: 8,\n      },\n      android: {\n        elevation: 6,\n      },\n    }),\n  }\n});"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Dynamic Theme Style Selector",
            description="Write a function `getThemeColors(isDark)` that returns `{ bg: '#0F172A', text: '#F8FAFC' }` if isDark is true, and `{ bg: '#FFFFFF', text: '#0F172A' }` if false.",
            starter_code="def getThemeColors(isDark):\n    # TODO: Return color dictionary\n    pass\n",
            solution_code="def getThemeColors(isDark):\n    if isDark:\n        return {'bg': '#0F172A', 'text': '#F8FAFC'}\n    return {'bg': '#FFFFFF', 'text': '#0F172A'}\n\nprint('Dark Theme:', getThemeColors(True))",
            expected_output="Dark Theme: {'bg': '#0F172A', 'text': '#F8FAFC'}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is `StyleSheet.create` preferred over inline style objects in React Native?",
                options=[
                    "It improves performance by caching style IDs across the native bridge and validates property names at compile time.",
                    "It compiles styles to SASS.",
                    "It automatically animates components.",
                    "It enables Tailwind CSS."
                ],
                correct_answer="It improves performance by caching style IDs across the native bridge and validates property names at compile time.",
                explanation="`StyleSheet.create` avoids re-allocating new object literals on every re-render."
            ),
            QuizQuestionBlueprint(
                question="What React Native hook detects whether the user's mobile OS is in Light or Dark mode?",
                options=["useColorScheme()", "useTheme()", "useDarkMode()", "useSystemAppearance()"],
                correct_answer="useColorScheme()",
                explanation="`useColorScheme()` returns `'light'`, `'dark'`, or `null` reactively."
            ),
            QuizQuestionBlueprint(
                question="How do Android and iOS differ in how card drop shadows are configured in React Native?",
                options=[
                    "iOS uses `shadowColor`, `shadowOffset`, `shadowOpacity`; Android uses the `elevation` integer property.",
                    "iOS uses CSS `box-shadow`; Android does not support shadows.",
                    "Android requires SVG filters.",
                    "Shadows are identical on both platforms."
                ],
                correct_answer="iOS uses `shadowColor`, `shadowOffset`, `shadowOpacity`; Android uses the `elevation` integer property.",
                explanation="Android renders Material elevation shadows, whereas iOS uses CoreGraphics shadow properties."
            ),
            QuizQuestionBlueprint(
                question="What helper in React Native allows selecting different styles or values based on operating system?",
                options=["Platform.select({ ios: ..., android: ... })", "OS.choose()", "Device.isAndroid()", "System.platform()"],
                correct_answer="Platform.select({ ios: ..., android: ... })",
                explanation="`Platform.select()` returns the matching property value for the active operating system."
            ),
            QuizQuestionBlueprint(
                question="Can you combine multiple style objects onto a single component in React Native?",
                options=[
                    "Yes, by passing an array of styles: `style={[styles.base, styles.active]}`.",
                    "No, only a single style object is allowed.",
                    "Only using template strings.",
                    "Only on iOS."
                ],
                correct_answer="Yes, by passing an array of styles: `style={[styles.base, styles.active]}`.",
                explanation="React Native accepts arrays of styles, merging properties from left to right."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 6
    # -------------------------------------------------------------
    DayBlueprint(
        order=6,
        title="Day 6: Responsive Layouts (Mobile vs Tablet & Orientation)",
        concept="Adapting UI layouts dynamically across compact phones, foldables, tablets, and orientation shifts",
        analogy="Think of responsive mobile design like an accordion. When played in a small room (compact phone screen), it folds together tightly with a single column. When played in a grand auditorium (iPad or tablet display), it expands outward, revealing multiple side-by-side columns and larger panels without losing musical harmony!",
        theory_sections=[
            {
                "heading": "Handling Device Diversity",
                "body": "The mobile ecosystem spans compact smartphones (360dp width), large pro phones (430dp), foldables, and tablets (768dp+ to 1024dp). Hardcoding fixed widths like `width: 380` will break or clip on smaller devices. Responsive mobile design uses proportional percentages, Flexbox wrapping, and dynamic window hooks."
            },
            {
                "heading": "useWindowDimensions vs Dimensions API",
                "body": "The older `Dimensions.get('window')` returns static dimensions measured at startup, failing when a user rotates their phone into landscape. The modern `useWindowDimensions()` hook updates automatically on orientation changes, split-screen mode, or foldable unfolding."
            }
        ],
        code_snippets=[
            {
                "title": "Listening to Window Dimensions Reactively",
                "code": "import React from 'react';\nimport { View, Text, useWindowDimensions, StyleSheet } from 'react-native';\n\nconst ResponsiveScreen = () => {\n  const { width, height } = useWindowDimensions();\n  const isTablet = width >= 768;\n  const isLandscape = width > height;\n\n  return (\n    <View style={styles.container}>\n      <Text style={styles.text}>\n        Device Width: {Math.round(width)}px ({isTablet ? 'Tablet' : 'Phone'})\n      </Text>\n      <Text style={styles.text}>\n        Orientation: {isLandscape ? 'Landscape' : 'Portrait'}\n      </Text>\n    </View>\n  );\n};"
            },
            {
                "title": "Adaptive Multi-Column Grid",
                "code": "const AdaptiveGrid = () => {\n  const { width } = useWindowDimensions();\n  // 1 column on phones (< 600), 2 columns on small tablets, 3 on large screens\n  const numColumns = width > 900 ? 3 : width > 600 ? 2 : 1;\n\n  return (\n    <FlatList\n      key={numColumns} // Changing key forces clean FlatList grid re-render\n      data={data}\n      numColumns={numColumns}\n      renderItem={({ item }) => <Card item={item} />}\n    />\n  );\n};"
            },
            {
                "title": "SafeAreaView and Device Notches",
                "code": "import { SafeAreaView } from 'react-native-safe-area-context';\n\n// Protects content from overlapping iPhone Dynamic Island, notches, and home indicator\nconst SafeScreen = ({ children }) => (\n  <SafeAreaView style={{ flex: 1, backgroundColor: '#0F172A' }}>\n    {children}\n  </SafeAreaView>\n);"
            },
            {
                "title": "Percentage-Based Dimensions and Max Widths",
                "code": "const Card = () => (\n  <View style={{\n    width: '90%',        // Fluid on small phones\n    maxWidth: 600,       // Restricts width on iPad / desktop web\n    alignSelf: 'center'\n  }} />\n);"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Device Form-Factor Classifier",
            description="Write a Python helper `classify_device(width)` that returns 'phone' if width < 600, 'tablet' if 600 <= width < 1024, and 'desktop' if width >= 1024.",
            starter_code="def classify_device(width):\n    # TODO: Implement classifier\n    pass\n",
            solution_code="def classify_device(width):\n    if width < 600:\n        return 'phone'\n    elif width < 1024:\n        return 'tablet'\n    return 'desktop'\n\nprint('820px width:', classify_device(820))",
            expected_output="820px width: tablet"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is `useWindowDimensions()` superior to `Dimensions.get('window')`?",
                options=[
                    "`useWindowDimensions()` automatically triggers a component re-render when the user rotates the device or splits screen.",
                    "`Dimensions.get` is deprecated on iOS.",
                    "`useWindowDimensions` returns measurements in inches instead of pixels.",
                    "It works without React."
                ],
                correct_answer="`useWindowDimensions()` automatically triggers a component re-render when the user rotates the device or splits screen.",
                explanation="`useWindowDimensions` is a reactive hook that listens to live dimension changes."
            ),
            QuizQuestionBlueprint(
                question="What component prevents mobile content from rendering underneath camera notches and the iOS Dynamic Island?",
                options=["SafeAreaView (from react-native-safe-area-context)", "NotchGuard", "ScreenShield", "PaddingView"],
                correct_answer="SafeAreaView (from react-native-safe-area-context)",
                explanation="`SafeAreaView` automatically applies device-specific insets for notches and home bars."
            ),
            QuizQuestionBlueprint(
                question="Why must you change the `key` prop on `<FlatList>` when dynamically switching `numColumns`?",
                options=[
                    "React Native requires re-mounting the layout when changing the column layout count dynamically.",
                    "To change the background color.",
                    "It resets the device memory.",
                    "To prevent network requests."
                ],
                correct_answer="React Native requires re-mounting the layout when changing the column layout count dynamically.",
                explanation="Changing `key={numColumns}` forces FlatList to cleanly reconstruct its grid layout."
            ),
            QuizQuestionBlueprint(
                question="What is the standard breakpoint width in dp commonly used to differentiate tablets from phones?",
                options=["600dp to 768dp", "200dp", "1440dp", "50dp"],
                correct_answer="600dp to 768dp",
                explanation="600dp (Android tablet standard) and 768dp (iPad standard) define tablet breakpoints."
            ),
            QuizQuestionBlueprint(
                question="How do you ensure a form input looks good on both a compact phone and a wide iPad?",
                options=[
                    "Set `width: '90%'` with a reasonable `maxWidth: 500` centered with `alignSelf: 'center'`.",
                    "Hardcode width: 380px.",
                    "Disable tablet installations.",
                    "Force landscape orientation only."
                ],
                correct_answer="Set `width: '90%'` with a reasonable `maxWidth: 500` centered with `alignSelf: 'center'`.",
                explanation="Combining fluid percentage widths with `maxWidth` creates adaptable interfaces."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 7 (Project)
    # -------------------------------------------------------------
    DayBlueprint(
        order=7,
        title="Day 7: Complete Mobile Profile Screen UI Project",
        concept="Synthesizing components, Flexbox layouts, theming, avatars, and responsive badges into a mobile profile UI",
        analogy="Think of building this profile screen like creating an athlete's official digital trading card. The card features a clear photo avatar at the top, bold achievement stats (XP, Rank, Streak) in the center badges, biography details, and an interactive 'Edit Profile' button at the bottom!",
        theory_sections=[
            {
                "heading": "Capstone Architecture for Profile UI",
                "body": "In this Module 1 milestone project, you combine all foundational mobile UI principles: structuring content cleanly with `<SafeAreaView>` and `<ScrollView>`, creating circular avatar images using `borderRadius`, displaying multi-column stat counters using horizontal Flexbox rows, and providing tactile buttons."
            },
            {
                "heading": "Creating Perfect Circular Avatars in Mobile",
                "body": "To render a circular image or avatar container in React Native, assign equal `width` and `height` (e.g. 100x100), and set `borderRadius` to exactly half the dimension (`borderRadius: 50`). This works across both iOS and Android natively."
            }
        ],
        code_snippets=[
            {
                "title": "Complete Profile Screen Component (ProfileScreen.tsx)",
                "code": "import React from 'react';\nimport {\n  View,\n  Text,\n  StyleSheet,\n  TouchableOpacity,\n  ScrollView,\n  Image,\n  useColorScheme\n} from 'react-native';\nimport { SafeAreaView } from 'react-native-safe-area-context';\n\nexport const ProfileScreen = () => {\n  const isDark = useColorScheme() === 'dark';\n  \n  return (\n    <SafeAreaView style={[styles.safeArea, isDark && styles.darkBackground]}>\n      <ScrollView contentContainerStyle={styles.scrollContent}>\n        {/* 1. Avatar and Identity */}\n        <View style={styles.headerSection}>\n          <View style={styles.avatarContainer}>\n            <Text style={styles.avatarEmoji}>👨‍💻</Text>\n          </View>\n          <Text style={[styles.userName, isDark && styles.darkText]}>Zubair Ahmed</Text>\n          <Text style={styles.userHandle}>@zubair_dev • Full-Stack Engineer</Text>\n        </View>\n\n        {/* 2. Gamified Stat Badges */}\n        <View style={styles.statsRow}>\n          <View style={styles.statBox}>\n            <Text style={styles.statNumber}>1,450</Text>\n            <Text style={styles.statLabel}>XP Earned</Text>\n          </View>\n          <View style={styles.statBox}>\n            <Text style={styles.statNumber}>🔥 12</Text>\n            <Text style={styles.statLabel}>Day Streak</Text>\n          </View>\n          <View style={styles.statBox}>\n            <Text style={styles.statNumber}>#4</Text>\n            <Text style={styles.statLabel}>League Rank</Text>\n          </View>\n        </View>\n\n        {/* 3. Action Buttons */}\n        <View style={styles.actionSection}>\n          <TouchableOpacity style={styles.primaryBtn}>\n            <Text style={styles.primaryBtnText}>Edit Profile</Text>\n          </TouchableOpacity>\n          <TouchableOpacity style={styles.secondaryBtn}>\n            <Text style={styles.secondaryBtnText}>Share Portfolio</Text>\n          </TouchableOpacity>\n        </View>\n      </ScrollView>\n    </SafeAreaView>\n  );\n};"
            },
            {
                "title": "Profile Screen Stylesheet (styles.ts)",
                "code": "const styles = StyleSheet.create({\n  safeArea: { flex: 1, backgroundColor: '#F8FAFC' },\n  darkBackground: { backgroundColor: '#0F172A' },\n  darkText: { color: '#F8FAFC' },\n  scrollContent: { padding: 24, alignItems: 'center' },\n  headerSection: { alignItems: 'center', marginBottom: 24 },\n  avatarContainer: {\n    width: 96,\n    height: 96,\n    borderRadius: 48, // Half of width/height creates a circle\n    backgroundColor: '#3B82F620',\n    borderWidth: 3,\n    borderColor: '#3B82F6',\n    justifyContent: 'center',\n    alignItems: 'center',\n    marginBottom: 16\n  },\n  avatarEmoji: { fontSize: 44 },\n  userName: { fontSize: 24, fontWeight: '800', color: '#0F172A', marginBottom: 4 },\n  userHandle: { fontSize: 14, color: '#64748B' },\n  statsRow: {\n    flexDirection: 'row',\n    justifyContent: 'space-between',\n    width: '100%',\n    backgroundColor: '#1E293B',\n    borderRadius: 16,\n    padding: 16,\n    marginBottom: 24\n  },\n  statBox: { alignItems: 'center', flex: 1 },\n  statNumber: { fontSize: 18, fontWeight: '800', color: '#10B981', marginBottom: 2 },\n  statLabel: { fontSize: 12, color: '#94A3B8' },\n  actionSection: { width: '100%', gap: 12 },\n  primaryBtn: { backgroundColor: '#10B981', paddingVertical: 14, borderRadius: 12, alignItems: 'center' },\n  primaryBtnText: { color: '#FFFFFF', fontWeight: '700', fontSize: 16 },\n  secondaryBtn: { backgroundColor: '#334155', paddingVertical: 14, borderRadius: 12, alignItems: 'center' },\n  secondaryBtnText: { color: '#CBD5E1', fontWeight: '600', fontSize: 16 }\n});"
            },
            {
                "title": "Displaying Real Images with fallback",
                "code": "<Image\n  source={{ uri: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb' }}\n  style={{ width: 96, height: 96, borderRadius: 48 }}\n  resizeMode=\"cover\"\n/>"
            },
            {
                "title": "Adding Settings Menu List",
                "code": "const SettingsRow = ({ icon, title }) => (\n  <TouchableOpacity style={styles.settingsRow}>\n    <Text style={styles.settingsIcon}>{icon}</Text>\n    <Text style={styles.settingsTitle}>{title}</Text>\n    <Text style={styles.chevron}>&rarr;</Text>\n  </TouchableOpacity>\n);"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Circular Avatar Dimension Calculator",
            description="Write a function `get_avatar_style(diameter)` that returns a dictionary with width, height, and borderRadius set to exactly diameter // 2.",
            starter_code="def get_avatar_style(diameter):\n    # TODO: Calculate styles\n    pass\n",
            solution_code="def get_avatar_style(diameter):\n    return {'width': diameter, 'height': diameter, 'borderRadius': diameter // 2}\n\nprint('Avatar Style 100px:', get_avatar_style(100))",
            expected_output="Avatar Style 100px: {'width': 100, 'height': 100, 'borderRadius': 50}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="How do you create a perfect circular avatar image in React Native?",
                options=[
                    "Set equal width and height, and set `borderRadius` to half the width/height dimension.",
                    "Set `shape=\"circle\"` on `<Image>`.",
                    "Use CSS clip-path.",
                    "Mobile images are circular by default."
                ],
                correct_answer="Set equal width and height, and set `borderRadius` to half the width/height dimension.",
                explanation="Setting `borderRadius: size / 2` creates a perfectly circular border radius."
            ),
            QuizQuestionBlueprint(
                question="What prop on React Native's `<Image>` controls scaling behavior (e.g. maintaining aspect ratio)?",
                options=["resizeMode", "scaleType", "objectFit", "fitMode"],
                correct_answer="resizeMode",
                explanation="`resizeMode` accepts `'cover'`, `'contain'`, `'stretch'`, `'repeat'`, and `'center'`."
            ),
            QuizQuestionBlueprint(
                question="Why is `contentContainerStyle` used on `<ScrollView>` instead of standard `style`?",
                options=[
                    "`contentContainerStyle` applies styling directly to the inner scrollable content container, whereas `style` applies to the outer viewport wrapper.",
                    "Because `style` is disabled on ScrollView.",
                    "To enable horizontal scrolling.",
                    "To compress child images."
                ],
                correct_answer="`contentContainerStyle` applies styling directly to the inner scrollable content container, whereas `style` applies to the outer viewport wrapper.",
                explanation="ScrollView requires `contentContainerStyle` to format padding and alignment of scrollable children."
            ),
            QuizQuestionBlueprint(
                question="What is the benefit of wrapping the entire screen inside `<SafeAreaView>`?",
                options=[
                    "It automatically applies padding to avoid rendering behind the status bar, notch, and home swipe bar.",
                    "It prevents users from taking screenshots.",
                    "It checks for malware.",
                    "It speeds up app launch."
                ],
                correct_answer="It automatically applies padding to avoid rendering behind the status bar, notch, and home swipe bar.",
                explanation="SafeAreaView protects content from screen obstructions across modern devices."
            ),
            QuizQuestionBlueprint(
                question="How do you arrange three stat badges horizontally with equal spacing across the screen width?",
                options=[
                    "Wrap in a `<View>` with `flexDirection: 'row'`, `justifyContent: 'space-between'`, and give each badge `flex: 1`.",
                    "Use float: left on each badge.",
                    "Hardcode margin: 20px.",
                    "Use a Table component."
                ],
                correct_answer="Wrap in a `<View>` with `flexDirection: 'row'`, `justifyContent: 'space-between'`, and give each badge `flex: 1`.",
                explanation="`flexDirection: 'row'` with `flex: 1` evenly distributes column badges across the row."
            )
        ],
        is_project_day=True,
        project_name="Complete Mobile Profile Screen UI"
    ),

    # -------------------------------------------------------------
    # DAY 8
    # -------------------------------------------------------------
    DayBlueprint(
        order=8,
        title="Day 8: Stack Navigation (Push & Pop Mechanics)",
        concept="Managing hierarchical screen transitions with React Navigation Native Stack",
        analogy="Think of Stack Navigation like a deck of playing cards on a table. When you tap on a blog post or product, you place a new card on top of the deck (`navigation.push('Detail')`). When you tap the Back arrow, you discard the top card from the deck (`navigation.goBack()`), revealing the card underneath exactly where you left off!",
        theory_sections=[
            {
                "heading": "Hierarchical Screen Stacks",
                "body": "Mobile applications structure workflows hierarchically: Home &rarr; Category &rarr; Product Details &rarr; Checkout. React Navigation's Native Stack Navigator (`createNativeStackNavigator`) utilizes native platform navigation primitives (`UINavigationController` on iOS and `Fragment` transitions on Android), delivering 60fps animations."
            },
            {
                "heading": "Push, Navigate, and goBack",
                "body": "`navigation.navigate('ScreenName')` navigates to an existing screen in the stack. `navigation.push('ScreenName')` pushes a fresh instance of the screen on top (useful for infinite recursive navigation, like 'Similar Products'). `navigation.goBack()` pops the top screen."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring Navigation Container & Native Stack",
                "code": "import React from 'react';\nimport { NavigationContainer } from '@react-navigation/native';\nimport { createNativeStackNavigator } from '@react-navigation/native-stack';\n\nconst Stack = createNativeStackNavigator();\n\nexport const AppNavigator = () => (\n  <NavigationContainer>\n    <Stack.Navigator initialRouteName=\"Home\">\n      <Stack.Screen name=\"Home\" component={HomeScreen} options={{ title: 'Feed' }} />\n      <Stack.Screen name=\"Detail\" component={DetailScreen} options={{ title: 'Details' }} />\n    </Stack.Navigator>\n  </NavigationContainer>\n);"
            },
            {
                "title": "Navigating to a New Screen",
                "code": "const HomeScreen = ({ navigation }) => (\n  <TouchableOpacity \n    onPress={() => navigation.navigate('Detail')}\n  >\n    <Text>View Details &rarr;</Text>\n  </TouchableOpacity>\n);"
            },
            {
                "title": "Popping Screens with goBack() & popToTop()",
                "code": "const DetailScreen = ({ navigation }) => (\n  <View>\n    {/* Pop one screen back */}\n    <TouchableOpacity onPress={() => navigation.goBack()}>\n      <Text>Go Back</Text>\n    </TouchableOpacity>\n    \n    {/* Jump directly to root screen */}\n    <TouchableOpacity onPress={() => navigation.popToTop()}>\n      <Text>Return to Home Root</Text>\n    </TouchableOpacity>\n  </View>\n);"
            },
            {
                "title": "Customizing Native Header Colors & Styling",
                "code": "<Stack.Navigator\n  screenOptions={{\n    headerStyle: { backgroundColor: '#0F172A' },\n    headerTintColor: '#10B981',\n    headerTitleStyle: { fontWeight: 'bold' },\n    headerShadowVisible: false\n  }}\n>"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Navigation Action Resolver",
            description="Write a Python simulation function `simulate_stack_nav(stack, action, screen=None)` that pushes `screen` if action is 'push', pops the top if 'pop', and returns the updated stack list.",
            starter_code="def simulate_stack_nav(stack, action, screen=None):\n    # TODO: Implement stack simulator\n    pass\n",
            solution_code="def simulate_stack_nav(stack, action, screen=None):\n    st = list(stack)\n    if action == 'push' and screen:\n        st.append(screen)\n    elif action == 'pop' and len(st) > 1:\n        st.pop()\n    return st\n\ns = ['Home']\ns = simulate_stack_nav(s, 'push', 'Profile')\nprint('Current Stack:', s)",
            expected_output="Current Stack: ['Home', 'Profile']"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary visual behavior of a Stack Navigator on mobile?",
                options=[
                    "It animates new screens sliding in on top of previous screens, and slides them off when going back.",
                    "It displays tabs at the bottom of the screen.",
                    "It opens a hamburger side menu.",
                    "It rotates the screen 180 degrees."
                ],
                correct_answer="It animates new screens sliding in on top of previous screens, and slides them off when going back.",
                explanation="Stack navigators model screens as a stack of cards pushed on top of one another."
            ),
            QuizQuestionBlueprint(
                question="What method pops all screens off the stack and returns the user to the initial root screen?",
                options=["navigation.popToTop()", "navigation.resetRoot()", "navigation.home()", "navigation.clearAll()"],
                correct_answer="navigation.popToTop()",
                explanation="`navigation.popToTop()` dismisses all screens down to the very first route."
            ),
            QuizQuestionBlueprint(
                question="Why is `createNativeStackNavigator` preferred over the older JS-based `createStackNavigator`?",
                options=[
                    "It uses native platform navigation primitives (UINavigationController / Fragments) for native 60fps gesture performance.",
                    "It does not require React.",
                    "It runs inside the browser.",
                    "It is written in PHP."
                ],
                correct_answer="It uses native platform navigation primitives (UINavigationController / Fragments) for native 60fps gesture performance.",
                explanation="Native stack leverages native OS view controllers rather than re-creating gestures in JS."
            ),
            QuizQuestionBlueprint(
                question="What component must wrap your entire navigation tree at the root of a React Native app?",
                options=["<NavigationContainer>", "<AppStack>", "<RootNavigation>", "<Router>"],
                correct_answer="<NavigationContainer>",
                explanation="`<NavigationContainer>` manages the navigation state and links the top-level navigator."
            ),
            QuizQuestionBlueprint(
                question="How do you hide the top navigation header bar for a specific screen?",
                options=["options={{ headerShown: false }}", "options={{ noHeader: true }}", "options={{ hide: true }}", "header=\"none\""],
                correct_answer="options={{ headerShown: false }}",
                explanation="`headerShown: false` hides the platform header bar."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 9
    # -------------------------------------------------------------
    DayBlueprint(
        order=9,
        title="Day 9: Bottom Tab Navigation",
        concept="Implementing thumb-friendly primary app navigation with React Navigation Bottom Tabs",
        analogy="Think of Bottom Tab Navigation like the remote control buttons at the base of your smartphone screen. Instead of making you dig through deep menus, the 4 or 5 primary sections of your app (Learn, Dojos, Gigs, Hub, Profile) are permanently accessible right under your thumb with a single tap!",
        theory_sections=[
            {
                "heading": "The Ergonomics of Bottom Tabs",
                "body": "Modern mobile UX places core app destinations at the bottom of the screen, where the user's thumb can reach them easily with one hand. React Navigation's `@react-navigation/bottom-tabs` maintains persistent top-level tabs while keeping child stack navigation intact."
            },
            {
                "heading": "Configuring Tab Icons and Active Tint Colors",
                "body": "Using `screenOptions`, you define dynamic `tabBarIcon` rendering based on the `focused` boolean state, customize active colors (`tabBarActiveTintColor: '#10B981'`), inactive colors (`#64748B`), and add notification badges (`tabBarBadge: 3`)."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring BottomTabNavigator",
                "code": "import React from 'react';\nimport { createBottomTabNavigator } from '@react-navigation/bottom-tabs';\nimport { Ionicons } from '@expo/vector-icons';\n\nconst Tab = createBottomTabNavigator();\n\nexport const MainTabs = () => (\n  <Tab.Navigator\n    screenOptions={({ route }) => ({\n      headerShown: false,\n      tabBarActiveTintColor: '#10B981',\n      tabBarInactiveTintColor: '#64748B',\n      tabBarStyle: { backgroundColor: '#0F172A', borderTopColor: '#334155' },\n      tabBarIcon: ({ focused, color, size }) => {\n        let iconName = 'book';\n        if (route.name === 'Learn') iconName = focused ? 'book' : 'book-outline';\n        else if (route.name === 'Profile') iconName = focused ? 'person' : 'person-outline';\n        return <Ionicons name={iconName} size={size} color={color} />;\n      }\n    })}\n  >\n    <Tab.Screen name=\"Learn\" component={LearnScreen} />\n    <Tab.Screen name=\"Profile\" component={ProfileScreen} />\n  </Tab.Navigator>\n);"
            },
            {
                "title": "Adding Notification Badges to Tabs",
                "code": "<Tab.Screen \n  name=\"Notifications\" \n  component={NotificationsScreen}\n  options={{\n    tabBarBadge: 4, // Displays a red badge with count\n    tabBarBadgeStyle: { backgroundColor: '#EF4444' }\n  }}\n/>"
            },
            {
                "title": "Nesting Stacks Inside Tabs",
                "code": "// Each tab can be an entire StackNavigator!\nconst LearnTab = () => (\n  <Stack.Navigator>\n    <Stack.Screen name=\"Feed\" component={LearnFeedScreen} />\n    <Stack.Screen name=\"Detail\" component={LessonDetailScreen} />\n  </Stack.Navigator>\n);\n\n// Mount LearnTab as component of Tab.Screen\n<Tab.Screen name=\"Learn\" component={LearnTab} />"
            },
            {
                "title": "Hiding Tabs on Nested Screens",
                "code": "// In child stack screen options:\noptions={({ route }) => ({\n  tabBarStyle: ((route) => {\n    // Hide tab bar on checkout or camera\n    return { display: 'none' };\n  })(route)\n})}"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Tab Icon Resolver Function",
            description="Write a function `resolveTabIcon(routeName, isFocused)` that returns 'home-active' for 'Home' when focused, 'home-outline' when not, and 'settings' for other routes.",
            starter_code="def resolveTabIcon(routeName, isFocused):\n    # TODO: Implement icon resolver\n    pass\n",
            solution_code="def resolveTabIcon(routeName, isFocused):\n    if routeName == 'Home':\n        return 'home-active' if isFocused else 'home-outline'\n    return 'settings'\n\nprint('Home Focused:', resolveTabIcon('Home', True))",
            expected_output="Home Focused: home-active"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is bottom tab navigation preferred over top tabs for mobile applications?",
                options=[
                    "It sits directly within the natural ergonomic thumb zone of smartphone users holding devices one-handed.",
                    "Top tabs are banned on iOS.",
                    "Bottom tabs load 50% faster.",
                    "Bottom tabs consume zero battery."
                ],
                correct_answer="It sits directly within the natural ergonomic thumb zone of smartphone users holding devices one-handed.",
                explanation="Ergonomic thumb zones favor placing primary navigation targets along the bottom edge."
            ),
            QuizQuestionBlueprint(
                question="How do you display an unread notification count badge on a bottom tab?",
                options=["options={{ tabBarBadge: 3 }}", "options={{ badgeCount: 3 }}", "options={{ notification: 3 }}", "options={{ alert: 3 }}"],
                correct_answer="options={{ tabBarBadge: 3 }}",
                explanation="`tabBarBadge` automatically renders a styled numeric badge over the tab icon."
            ),
            QuizQuestionBlueprint(
                question="Can an individual Tab inside a `Tab.Navigator` contain its own nested `StackNavigator`?",
                options=[
                    "Yes, nesting a Stack Navigator inside a Tab Screen is the standard architectural pattern for mobile apps.",
                    "No, React Navigation forbids nested navigators.",
                    "Only on Android.",
                    "Only in React Native CLI."
                ],
                correct_answer="Yes, nesting a Stack Navigator inside a Tab Screen is the standard architectural pattern for mobile apps.",
                explanation="Nesting allows independent drill-down screen stacks within each main bottom tab."
            ),
            QuizQuestionBlueprint(
                question="What property controls the highlight color of the currently selected active tab?",
                options=["tabBarActiveTintColor", "activeColor", "tintColor", "selectedColor"],
                correct_answer="tabBarActiveTintColor",
                explanation="`tabBarActiveTintColor` sets the color for active icons and text labels."
            ),
            QuizQuestionBlueprint(
                question="What function is used inside `screenOptions` to dynamically render custom icon vectors per tab?",
                options=["tabBarIcon: ({ focused, color, size }) => ...", "renderIcon: () => ...", "iconBuilder: () => ...", "getTabIcon: () => ..."],
                correct_answer="tabBarIcon: ({ focused, color, size }) => ...",
                explanation="`tabBarIcon` receives the focus state, active color, and size to return the correct vector icon."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 10
    # -------------------------------------------------------------
    DayBlueprint(
        order=10,
        title="Day 10: Drawer Navigation & Passing Screen Parameters",
        concept="Creating slide-out side menus with Drawer Navigator and passing typed parameters between routes",
        analogy="Think of passing route parameters like handing a boarding pass to a flight attendant at the gate. When you tap on a flight in the schedule (`navigation.navigate('GateScreen', { flightId: 'PK-302' })`), you hand over the boarding pass containing the flight number. The gate screen inspects the pass (`route.params.flightId`) and opens the correct airplane door!",
        theory_sections=[
            {
                "heading": "Slide-Out Drawer Menus",
                "body": "Drawer navigation (`@react-navigation/drawer`) provides a slide-out drawer panel from the left or right edge of the screen, typically revealed by a hamburger menu icon or an edge-swipe gesture. It is ideal for secondary destinations: Settings, Support, Terms of Service, and Logout."
            },
            {
                "heading": "Passing and Reading Route Parameters",
                "body": "To pass parameters to a screen, provide a second object argument to `navigate`: `navigation.navigate('Detail', { itemId: 42, title: 'Python Book' })`. Inside the destination screen, read the parameters via `route.params`. In TypeScript, define a typed `ParamList` to ensure compile-time parameter safety."
            }
        ],
        code_snippets=[
            {
                "title": "Passing Parameters from Source Screen",
                "code": "const CourseCard = ({ course, navigation }) => (\n  <TouchableOpacity \n    onPress={() => {\n      // Pass params object to the destination screen\n      navigation.navigate('LessonDetail', {\n        lessonId: course.id,\n        lessonTitle: course.title\n      });\n    }}\n  >\n    <Text>{course.title}</Text>\n  </TouchableOpacity>\n);"
            },
            {
                "title": "Reading Route Parameters in Destination Screen",
                "code": "const LessonDetailScreen = ({ route, navigation }) => {\n  // Destructure passed parameters from route.params\n  const { lessonId, lessonTitle } = route.params;\n\n  return (\n    <View style={styles.container}>\n      <Text style={styles.title}>{lessonTitle}</Text>\n      <Text style={styles.sub}>ID: {lessonId}</Text>\n    </View>\n  );\n};"
            },
            {
                "title": "Configuring Drawer Navigation",
                "code": "import { createDrawerNavigator } from '@react-navigation/drawer';\n\nconst Drawer = createDrawerNavigator();\n\nexport const DrawerNav = () => (\n  <Drawer.Navigator screenOptions={{ drawerActiveTintColor: '#10B981' }}>\n    <Drawer.Screen name=\"Home\" component={MainTabs} />\n    <Drawer.Screen name=\"Settings\" component={SettingsScreen} />\n    <Drawer.Screen name=\"Help\" component={HelpDeskScreen} />\n  </Drawer.Navigator>\n);"
            },
            {
                "title": "TypeScript Navigation Types (types.ts)",
                "code": "export type RootStackParamList = {\n  Home: undefined;\n  LessonDetail: { lessonId: string; lessonTitle: string };\n  Checkout: { cartTotal: number };\n};"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Safe Route Parameter Extractor",
            description="Write a function `get_param(params_dict, key, default_val=None)` that safely extracts a key from a dictionary, returning default_val if params is None or key is missing.",
            starter_code="def get_param(params_dict, key, default_val=None):\n    # TODO: Implement safe extractor\n    pass\n",
            solution_code="def get_param(params_dict, key, default_val=None):\n    if not params_dict or not isinstance(params_dict, dict):\n        return default_val\n    return params_dict.get(key, default_val)\n\nprint('Param:', get_param({'userId': 101}, 'userId'))\nprint('Missing:', get_param(None, 'userId', 0))",
            expected_output="Param: 101\nMissing: 0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="How do you pass parameters to another screen when calling `navigation.navigate()`?",
                options=[
                    "Pass a second argument object: `navigation.navigate('Detail', { id: 42 })`.",
                    "Append to the URL string: `navigation.navigate('Detail?id=42')`.",
                    "Save it to a text file.",
                    "Pass it as an HTTP header."
                ],
                correct_answer="Pass a second argument object: `navigation.navigate('Detail', { id: 42 })`.",
                explanation="The second argument to `navigation.navigate` is the `params` dictionary."
            ),
            QuizQuestionBlueprint(
                question="Where are received parameters accessed on the destination screen component?",
                options=["route.params", "navigation.params", "props.query", "this.params"],
                correct_answer="route.params",
                explanation="React Navigation injects `route.params` containing all passed arguments."
            ),
            QuizQuestionBlueprint(
                question="What gesture commonly opens a Drawer Navigator menu on mobile devices?",
                options=["Swiping inward from the left or right edge of the screen.", "Double-tapping the screen.", "Shaking the phone.", "Pinching with two fingers."],
                correct_answer="Swiping inward from the left or right edge of the screen.",
                explanation="Edge-swiping or tapping the hamburger icon reveals the drawer panel."
            ),
            QuizQuestionBlueprint(
                question="What method programmatically opens the side drawer menu from a button press?",
                options=["navigation.openDrawer()", "navigation.showMenu()", "navigation.slideDrawer()", "navigation.drawer()"],
                correct_answer="navigation.openDrawer()",
                explanation="`navigation.openDrawer()` and `navigation.toggleDrawer()` control drawer visibility."
            ),
            QuizQuestionBlueprint(
                question="Why is defining a `RootStackParamList` type in TypeScript recommended for mobile navigation?",
                options=[
                    "It provides autocomplete and compile-time type-safety, catching missing or misspelled route parameter errors before runtime.",
                    "It compresses image files.",
                    "It encrypts navigation routes.",
                    "It reduces app bundle size by 50%."
                ],
                correct_answer="It provides autocomplete and compile-time type-safety, catching missing or misspelled route parameter errors before runtime.",
                explanation="TypeScript parameter lists ensure you pass the exact types each screen expects."
            )
        ]
    ),
]
