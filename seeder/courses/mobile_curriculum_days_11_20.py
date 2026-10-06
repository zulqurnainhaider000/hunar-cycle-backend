"""
Mobile App Development 40-Day Curriculum - Module 2 (Part 2), Module 3 & Module 4 (Days 11 to 20)
Module 2: Navigation Project (Day 11)
Module 3: State Management (Days 12-15)
Module 4: APIs & Networking (Days 16-20)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_11_TO_20 = [
    # -------------------------------------------------------------
    # DAY 11 (Project)
    # -------------------------------------------------------------
    DayBlueprint(
        order=11,
        title="Day 11: Multi-Screen E-Commerce UI Project",
        concept="Architecting a complete multi-navigator app combining Bottom Tabs, Native Stacks, and Route Parameters",
        analogy="Think of this project like building a modern shopping mall. The ground floor has the main directory signs (Bottom Tabs: Shop, Cart, Profile). When you enter the Electronics store, you walk down a dedicated aisle of laptops and phones (Stack Navigator). When you pick up a specific laptop box to read the specifications, you are examining the product detail card (`route.params`)!",
        theory_sections=[
            {
                "heading": "Multi-Navigator Architectural Pattern",
                "body": "Real-world mobile apps do not rely on a single navigator. They nest navigators: an outer Bottom Tab Navigator holds core tabs ('Shop', 'Cart', 'Profile'). The 'Shop' tab contains a child Native Stack Navigator that pushes from the Product Grid to Product Details and Reviews, maintaining seamless back-navigation."
            },
            {
                "heading": "Parameter Passing in E-Commerce Flows",
                "body": "When a shopper taps an item on the grid, the card invokes `navigation.navigate('ProductDetail', { product: item })`. The detail screen displays full photos, descriptions, and price, with an 'Add to Cart' button."
            }
        ],
        code_snippets=[
            {
                "title": "Nested Navigation Architecture (Navigation.tsx)",
                "code": "import React from 'react';\nimport { NavigationContainer } from '@react-navigation/native';\nimport { createBottomTabNavigator } from '@react-navigation/bottom-tabs';\nimport { createNativeStackNavigator } from '@react-navigation/native-stack';\n\nconst Tab = createBottomTabNavigator();\nconst ShopStack = createNativeStackNavigator();\n\nconst ShopNavigator = () => (\n  <ShopStack.Navigator screenOptions={{ headerStyle: { backgroundColor: '#0F172A' }, headerTintColor: '#10B981' }}>\n    <ShopStack.Screen name=\"Catalog\" component={CatalogScreen} options={{ title: 'Explore Gear' }} />\n    <ShopStack.Screen name=\"ProductDetail\" component={ProductDetailScreen} options={({ route }) => ({ title: route.params.product.name })} />\n  </ShopStack.Navigator>\n);\n\nexport const RootAppNavigator = () => (\n  <NavigationContainer>\n    <Tab.Navigator screenOptions={{ headerShown: false, tabBarStyle: { backgroundColor: '#0F172A' } }}>\n      <Tab.Screen name=\"ShopTab\" component={ShopNavigator} options={{ title: 'Shop' }} />\n      <Tab.Screen name=\"CartTab\" component={CartScreen} options={{ title: 'Cart' }} />\n      <Tab.Screen name=\"ProfileTab\" component={ProfileScreen} options={{ title: 'Profile' }} />\n    </Tab.Navigator>\n  </NavigationContainer>\n);"
            },
            {
                "title": "Catalog Grid Screen with Navigation Cards",
                "code": "const CatalogScreen = ({ navigation }) => (\n  <FlatList\n    data={PRODUCTS}\n    keyExtractor={item => item.id}\n    numColumns={2}\n    renderItem={({ item }) => (\n      <TouchableOpacity\n        style={styles.card}\n        onPress={() => navigation.navigate('ProductDetail', { product: item })}\n      >\n        <Image source={{ uri: item.image }} style={styles.thumbnail} />\n        <Text style={styles.title}>{item.name}</Text>\n        <Text style={styles.price}>${item.price.toFixed(2)}</Text>\n      </TouchableOpacity>\n    )}\n  />\n);"
            },
            {
                "title": "Product Detail Screen Consuming Route Params",
                "code": "const ProductDetailScreen = ({ route, navigation }) => {\n  const { product } = route.params;\n  return (\n    <View style={styles.container}>\n      <Image source={{ uri: product.image }} style={styles.heroImage} />\n      <Text style={styles.detailTitle}>{product.name}</Text>\n      <Text style={styles.detailPrice}>${product.price.toFixed(2)}</Text>\n      <Text style={styles.detailDesc}>{product.description}</Text>\n      <TouchableOpacity style={styles.buyBtn} onPress={() => alert('Added to cart!')}>\n        <Text style={styles.buyBtnText}>Add to Cart</Text>\n      </TouchableOpacity>\n    </View>\n  );\n};"
            },
            {
                "title": "Styling the E-Commerce Grid",
                "code": "const styles = StyleSheet.create({\n  card: { flex: 0.5, margin: 8, backgroundColor: '#1E293B', borderRadius: 16, padding: 12 },\n  thumbnail: { width: '100%', height: 140, borderRadius: 12, marginBottom: 8 },\n  title: { color: '#F8FAFC', fontWeight: '700', fontSize: 14 },\n  price: { color: '#10B981', fontWeight: '800', marginTop: 4 },\n  buyBtn: { backgroundColor: '#10B981', padding: 16, borderRadius: 12, alignItems: 'center', marginTop: 24 },\n  buyBtnText: { color: '#FFF', fontWeight: 'bold', fontSize: 16 }\n});"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Cart Item Subtotal Calculator",
            description="Write a function `calculate_cart_subtotal(cart_items)` that takes a list of dicts `[{'price': float, 'quantity': int}]` and returns the rounded subtotal.",
            starter_code="def calculate_cart_subtotal(cart_items):\n    # TODO: Calculate subtotal\n    pass\n",
            solution_code="def calculate_cart_subtotal(cart_items):\n    return round(sum(item['price'] * item['quantity'] for item in cart_items), 2)\n\nitems = [{'price': 29.99, 'quantity': 2}, {'price': 15.00, 'quantity': 1}]\nprint('Subtotal:', calculate_cart_subtotal(items))",
            expected_output="Subtotal: 74.98"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What pattern is used to give each Bottom Tab its own independent history of screen transitions?",
                options=[
                    "Nesting a Stack Navigator inside each Tab Screen component.",
                    "Creating three separate NavigationContainers.",
                    "Using HTML iframes.",
                    "Using window.location."
                ],
                correct_answer="Nesting a Stack Navigator inside each Tab Screen component.",
                explanation="Mounting a StackNavigator inside a Tab.Screen gives that tab its own independent navigation stack."
            ),
            QuizQuestionBlueprint(
                question="How do you dynamically set the header title of a stack screen from route parameters?",
                options=[
                    "options={({ route }) => ({ title: route.params.product.name })}",
                    "options={{ title: params.title }}",
                    "options={{ dynamicTitle: true }}",
                    "header.setTitle()"
                ],
                correct_answer="options={({ route }) => ({ title: route.params.product.name })}",
                explanation="`options` can be a function receiving `({ route, navigation })` to derive title from params."
            ),
            QuizQuestionBlueprint(
                question="What happens when a user on 'ProductDetail' taps the 'Cart' tab at the bottom?",
                options=[
                    "The app switches to the Cart tab immediately, preserving the Shop tab's position in the background.",
                    "The Shop tab is deleted.",
                    "The app reloads from scratch.",
                    "The app crashes."
                ],
                correct_answer="The app switches to the Cart tab immediately, preserving the Shop tab's position in the background.",
                explanation="Tab navigation preserves state in each tab so users can switch back without losing their place."
            ),
            QuizQuestionBlueprint(
                question="Why should you avoid passing huge, deeply nested objects inside `route.params`?",
                options=[
                    "Params are serialized into navigation state; passing huge objects harms memory and deep-linking serialization.",
                    "React Navigation can only pass strings.",
                    "Because numbers cannot be passed in params.",
                    "It causes visual screen tearing."
                ],
                correct_answer="Params are serialized into navigation state; passing huge objects harms memory and deep-linking serialization.",
                explanation="Best practice is to pass small IDs (e.g. `productId: 42`) and fetch or select the full item from state."
            ),
            QuizQuestionBlueprint(
                question="What prop on `<FlatList>` splits items into a multi-column grid layout?",
                options=["numColumns={2}", "columns={2}", "grid={2}", "split={2}"],
                correct_answer="numColumns={2}",
                explanation="`numColumns={2}` lays out children into a two-column grid."
            )
        ],
        is_project_day=True,
        project_name="Multi-Screen E-Commerce UI"
    ),

    # -------------------------------------------------------------
    # DAY 12
    # -------------------------------------------------------------
    DayBlueprint(
        order=12,
        title="Day 12: Local Component State Management",
        concept="Managing reactive component state using the useState hook, forms, and controlled inputs",
        analogy="Think of local component state like your short-term working memory while solving a puzzle. If you are calculating 15 + 27, you hold the partial sum 42 in your head (`useState`). Nobody else in the room needs to know about that temporary calculation; once you write down the answer, that memory has done its job!",
        theory_sections=[
            {
                "heading": "The Component State Lifecycle",
                "body": "State represents data that changes over time and directly affects what renders on screen. When a component's state changes via its setter function (`setCount(newCount)`), React automatically schedules a re-render of that component to update the mobile UI."
            },
            {
                "heading": "Controlled Inputs & Functional State Updates",
                "body": "In mobile apps, form inputs are 'controlled' when their displayed text is driven by React state (`value={text}`) and updated via `onChangeText={setText}`. When the new state depends on previous state (like toggling a boolean or incrementing a counter), always use the functional updater form: `setIsActive(prev => !prev)`."
            }
        ],
        code_snippets=[
            {
                "title": "Declaring Local State with useState",
                "code": "import React, { useState } from 'react';\nimport { View, Text, TouchableOpacity, StyleSheet } from 'react-native';\n\nconst Counter = () => {\n  const [count, setCount] = useState(0);\n  \n  return (\n    <View style={styles.container}>\n      <Text style={styles.text}>Current Count: {count}</Text>\n      <TouchableOpacity \n        style={styles.btn} \n        onPress={() => setCount(prev => prev + 1)}\n      >\n        <Text style={styles.btnText}>Add One</Text>\n      </TouchableOpacity>\n    </View>\n  );\n};"
            },
            {
                "title": "Managing Multi-Field Form State with an Object",
                "code": "const LoginForm = () => {\n  const [form, setForm] = useState({ email: '', password: '' });\n\n  const updateField = (key: string, value: string) => {\n    setForm(prev => ({ ...prev, [key]: value }));\n  };\n\n  return (\n    <View>\n      <TextInput\n        placeholder=\"Email\"\n        value={form.email}\n        onChangeText={val => updateField('email', val)}\n      />\n      <TextInput\n        placeholder=\"Password\"\n        secureTextEntry\n        value={form.password}\n        onChangeText={val => updateField('password', val)}\n      />\n    </View>\n  );\n};"
            },
            {
                "title": "Boolean State Toggle for UI Controls",
                "code": "const PasswordToggle = () => {\n  const [showPassword, setShowPassword] = useState(false);\n  return (\n    <View>\n      <TextInput secureTextEntry={!showPassword} />\n      <TouchableOpacity onPress={() => setShowPassword(p => !p)}>\n        <Text>{showPassword ? 'Hide' : 'Show'}</Text>\n      </TouchableOpacity>\n    </View>\n  );\n};"
            },
            {
                "title": "Resetting Local State on Submit",
                "code": "const handleCommentSubmit = () => {\n  if (!commentText.trim()) return;\n  submitComment(commentText);\n  setCommentText(''); // Clear input field\n};"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Form State Merger Function",
            description="Write a Python simulation of an immutable form state update function `update_form(current_state, field, value)` that returns a new dictionary with the updated field without mutating the original.",
            starter_code="def update_form(current_state, field, value):\n    # TODO: Return new updated dict\n    pass\n",
            solution_code="def update_form(current_state, field, value):\n    new_state = dict(current_state)\n    new_state[field] = value\n    return new_state\n\ns = {'username': 'ali', 'role': 'guest'}\ns2 = update_form(s, 'role', 'admin')\nprint('Updated:', s2)\nprint('Original untouched:', s['role'])",
            expected_output="Updated: {'username': 'ali', 'role': 'admin'}\nOriginal untouched: guest"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why should you use functional state updates (e.g. `setCount(prev => prev + 1)`) when updating state based on previous values?",
                options=[
                    "It guarantees access to the freshest state value, preventing race conditions during rapid asynchronous state batches.",
                    "It runs faster in C++.",
                    "Because React forbids passing numbers to setState.",
                    "It automatically saves to local storage."
                ],
                correct_answer="It guarantees access to the freshest state value, preventing race conditions during rapid asynchronous state batches.",
                explanation="Functional updaters receive the guaranteed latest state snapshot from React's render queue."
            ),
            QuizQuestionBlueprint(
                question="What happens when a component's local state is modified via its setter function?",
                options=[
                    "React schedules a re-render of that component and its children to reflect the updated state in the UI.",
                    "The entire smartphone restarts.",
                    "All network requests are cancelled.",
                    "The app bundle is recompiled."
                ],
                correct_answer="React schedules a re-render of that component and its children to reflect the updated state in the UI.",
                explanation="State changes trigger React's reconciliation engine to calculate UI diffs and re-render."
            ),
            QuizQuestionBlueprint(
                question="What is a 'controlled component' in mobile input forms?",
                options=[
                    "An input component whose displayed value is bound to and controlled by React state.",
                    "A component that requires administrator permissions.",
                    "A button that cannot be tapped.",
                    "An encrypted view."
                ],
                correct_answer="An input component whose displayed value is bound to and controlled by React state.",
                explanation="Controlled inputs use `value={state}` and `onChangeText={setState}` as a single source of truth."
            ),
            QuizQuestionBlueprint(
                question="Can you directly mutate a state variable (e.g. `form.email = 'new@mail.com'`) in React?",
                options=[
                    "No, mutating state directly does not trigger a re-render and causes subtle synchronization bugs.",
                    "Yes, mutation is the recommended React pattern.",
                    "Only on Android.",
                    "Only inside useEffect."
                ],
                correct_answer="No, mutating state directly does not trigger a re-render and causes subtle synchronization bugs.",
                explanation="State must always be treated as immutable and updated only through its setter function."
            ),
            QuizQuestionBlueprint(
                question="Where should state live if two sibling components both need access to the same data?",
                options=[
                    "Lifting state up to their closest common parent component.",
                    "Storing it in a global JavaScript window variable.",
                    "Saving it to an external server on every keystroke.",
                    "Duplicate the state in both components."
                ],
                correct_answer="Lifting state up to their closest common parent component.",
                explanation="'Lifting state up' to a common ancestor allows sharing state downward via props."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 13
    # -------------------------------------------------------------
    DayBlueprint(
        order=13,
        title="Day 13: Global State Concepts & The Prop-Drilling Problem",
        concept="Understanding shared application state, single sources of truth, and prop-drilling bottlenecks",
        analogy="Think of prop drilling like a game of telephone across a 10-story skyscraper. The CEO on the 10th floor wants to tell the security guard in the basement that VIP visitor #42 has arrived. Instead of an elevator announcement speaker (Global State), the message has to be whispered down floor-by-floor through 9 managers who don't care about the message just to reach the basement!",
        theory_sections=[
            {
                "heading": "The Prop-Drilling Bottleneck",
                "body": "As apps scale, components deep inside the hierarchy need access to common data (such as the authenticated User object, shopping cart count, or active theme). Passing props down through 5 or 6 intermediary components that don't need the data themselves is called 'prop drilling'. It leads to brittle, hard-to-maintain code."
            },
            {
                "heading": "The Single Source of Truth Principle",
                "body": "Global state management solves this by holding shared app data in a centralized store outside the UI tree. Any component at any level of the hierarchy can subscribe directly to the data and re-render only when relevant parts update."
            }
        ],
        code_snippets=[
            {
                "title": "Illustrating the Prop Drilling Anti-Pattern",
                "code": "// ❌ Prop Drilling: Intermediate containers pass props they don't care about\nconst Screen = ({ user, theme }) => <Header user={user} theme={theme} />;\nconst Header = ({ user, theme }) => <NavProfile user={user} theme={theme} />;\nconst NavProfile = ({ user, theme }) => (\n  <View style={{ backgroundColor: theme.card }}>\n    <Text>{user.name}</Text>\n  </View>\n);"
            },
            {
                "title": "The Global Store Concept (Mental Model)",
                "code": "// ✅ Global State: NavProfile reads directly from the store\n// [Global User Store] ───> Directly consumed by <NavProfile />\n// Intermediate components (<Screen />, <Header />) remain clean and decoupled!"
            },
            {
                "title": "Categorizing Mobile App State",
                "code": "// 1. Local State: Dropdown open/closed, form input text, modal visibility\n// 2. Global UI State: Dark/Light theme, active bottom tab, notification badges\n// 3. Global Business State: Auth user, auth token, shopping cart, cached feed items"
            },
            {
                "title": "Predictable State Transformations",
                "code": "# State should update predictably through pure functions:\ndef state_reducer(current_state, action):\n    if action['type'] == 'SET_USER':\n        return {**current_state, 'user': action['payload']}\n    elif action['type'] == 'LOGOUT':\n        return {**current_state, 'user': None}\n    return current_state"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="State Reducer Action Dispatcher",
            description="Write a Python reducer function `auth_reducer(state, action)` that sets `{'user': action['user'], 'isAuth': True}` on action 'LOGIN' and `{'user': None, 'isAuth': False}` on action 'LOGOUT'.",
            starter_code="def auth_reducer(state, action):\n    # TODO: Implement reducer\n    pass\n",
            solution_code="def auth_reducer(state, action):\n    if action.get('type') == 'LOGIN':\n        return {'user': action['user'], 'isAuth': True}\n    elif action.get('type') == 'LOGOUT':\n        return {'user': None, 'isAuth': False}\n    return state\n\ninit = {'user': None, 'isAuth': False}\nlogged = auth_reducer(init, {'type': 'LOGIN', 'user': 'Zubair'})\nprint('Logged In:', logged)",
            expected_output="Logged In: {'user': 'Zubair', 'isAuth': True}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is 'prop drilling' in mobile application development?",
                options=[
                    "Passing props down through multiple layers of intermediate components that do not need the data themselves just to reach a deep child component.",
                    "Creating a database index.",
                    "Drilling holes in hardware phones.",
                    "A compiler optimization in Metro."
                ],
                correct_answer="Passing props down through multiple layers of intermediate components that do not need the data themselves just to reach a deep child component.",
                explanation="Prop drilling creates tight coupling and tedious maintenance across intermediate components."
            ),
            QuizQuestionBlueprint(
                question="What is the 'Single Source of Truth' principle in state architecture?",
                options=[
                    "Storing shared state in a single centralized location so all components stay synchronized without data divergence.",
                    "Only allowing one database query per minute.",
                    "Having only one screen in the app.",
                    "Never using third-party libraries."
                ],
                correct_answer="Storing shared state in a single centralized location so all components stay synchronized without data divergence.",
                explanation="A single source of truth guarantees that all views reflect identical, synchronized state."
            ),
            QuizQuestionBlueprint(
                question="Which of the following is best suited for local state rather than global state?",
                options=[
                    "Whether a password visibility toggle is active (eye icon).",
                    "The authenticated user profile and JWT token.",
                    "The items currently in the shopping cart.",
                    "The app-wide light/dark theme preference."
                ],
                correct_answer="Whether a password visibility toggle is active (eye icon).",
                explanation="Ephemeral UI toggles that affect only a single input field should remain local to that component."
            ),
            QuizQuestionBlueprint(
                question="Why is mutating global state directly outside of approved updater functions considered an anti-pattern?",
                options=[
                    "It causes state desynchronization because React cannot detect unmanaged mutations to trigger re-renders.",
                    "It uses too much internet bandwidth.",
                    "It automatically logs out the user.",
                    "It breaks the phone's touch screen."
                ],
                correct_answer="It causes state desynchronization because React cannot detect unmanaged mutations to trigger re-renders.",
                explanation="Direct mutations bypass change detection, leaving views out of date."
            ),
            QuizQuestionBlueprint(
                question="What architectural pattern models state changes as dispatched action objects processed by pure reducer functions?",
                options=["Flux / Redux pattern", "Observer pattern", "Singleton pattern", "Decorator pattern"],
                correct_answer="Flux / Redux pattern",
                explanation="The Flux/Redux architecture dispatches action objects to pure reducers for predictable updates."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 14
    # -------------------------------------------------------------
    DayBlueprint(
        order=14,
        title="Day 14: React Context API & State Management Tools",
        concept="Implementing global state providers using createContext, useContext, and modern state tools",
        analogy="Think of React Context like a radio broadcasting tower in a city. Instead of the tower driving cables to every individual house in town, it broadcasts the signal freely into the air (`<Provider>`). Any home with a radio receiver (`useContext()`) can tune into the broadcast station anytime and hear the music!",
        theory_sections=[
            {
                "heading": "The Built-In React Context Solution",
                "body": "For many mobile applications, installing massive external state libraries is unnecessary. React includes the Context API natively. You create a context via `createContext()`, wrap your application root inside a `<Context.Provider value={{ state, actions }}>`, and consume it anywhere via `useContext(Context)`."
            },
            {
                "heading": "When to Use Zustand or Redux Toolkit",
                "body": "When state updates occur at high frequencies (e.g. 60fps animations, large collections), Context can cause excessive re-renders because every subscriber re-evaluates when any part of the context value changes. Specialized tools like **Zustand** or **Redux Toolkit** provide fine-grained selector subscriptions (`useStore(state => state.cartCount)`)."
            }
        ],
        code_snippets=[
            {
                "title": "Creating an Authentication Context (AuthContext.tsx)",
                "code": "import React, { createContext, useState, useContext } from 'react';\n\ninterface AuthContextType {\n  user: string | null;\n  login: (name: string) => void;\n  logout: () => void;\n}\n\nconst AuthContext = createContext<AuthContextType>({} as AuthContextType);\n\nexport const AuthProvider = ({ children }: { children: React.ReactNode }) => {\n  const [user, setUser] = useState<string | null>(null);\n\n  const login = (name: string) => setUser(name);\n  const logout = () => setUser(null);\n\n  return (\n    <AuthContext.Provider value={{ user, login, logout }}>\n      {children}\n    </AuthContext.Provider>\n  );\n};\n\n// Custom hook for ergonomic consumption\nexport const useAuth = () => useContext(AuthContext);"
            },
            {
                "title": "Wrapping the App Root with Provider",
                "code": "export default function App() {\n  return (\n    <AuthProvider>\n      <RootNavigator />\n    </AuthProvider>\n  );\n}"
            },
            {
                "title": "Consuming Global Context in a Deep Child Component",
                "code": "const UserBadge = () => {\n  // Directly consumes user without prop drilling!\n  const { user, logout } = useAuth();\n\n  if (!user) return <Text>Guest User</Text>;\n\n  return (\n    <View>\n      <Text>Logged in as: {user}</Text>\n      <TouchableOpacity onPress={logout}><Text>Log Out</Text></TouchableOpacity>\n    </View>\n  );\n};"
            },
            {
                "title": "Modern Zustand Lightweight Store (Alternative)",
                "code": "import { create } from 'zustand';\n\nexport const useCartStore = create((set) => ({\n  items: [],\n  addItem: (item) => set((state) => ({ items: [...state.items, item] })),\n  clearCart: () => set({ items: [] })\n}));"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Context Value Selector Simulation",
            description="Write a function `select_state(store_dict, selector_fn)` that applies a selector function to extract a targeted slice of state without exposing the entire dictionary.",
            starter_code="def select_state(store_dict, selector_fn):\n    # TODO: Apply selector\n    pass\n",
            solution_code="def select_state(store_dict, selector_fn):\n    return selector_fn(store_dict)\n\nstore = {'user': {'name': 'Ali', 'token': 'xyz'}, 'cart': [1, 2, 3]}\nuser_name = select_state(store, lambda s: s['user']['name'])\nprint('Selected Slice:', user_name)",
            expected_output="Selected Slice: Ali"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What hook is used to consume data provided by a `<Context.Provider>` in a functional component?",
                options=["useContext(Context)", "useProvider(Context)", "useStore(Context)", "useGlobal(Context)"],
                correct_answer="useContext(Context)",
                explanation="`useContext(MyContext)` subscribes the component to the nearest Provider ancestor."
            ),
            QuizQuestionBlueprint(
                question="What is the potential performance caveat of using standard React Context for frequently changing data?",
                options=[
                    "All components consuming the context will re-render whenever any value in the provider changes, even if they only use an unchanged property.",
                    "It causes memory leaks in the camera.",
                    "It only works on iOS.",
                    "It cannot hold arrays."
                ],
                correct_answer="All components consuming the context will re-render whenever any value in the provider changes, even if they only use an unchanged property.",
                explanation="Context lacks fine-grained selector subscriptions out of the box, leading to broad re-renders."
            ),
            QuizQuestionBlueprint(
                question="Why is it best practice to create a custom hook like `useAuth()` around `useContext(AuthContext)`?",
                options=[
                    "It encapsulates error checking (e.g. verifying the component is inside the Provider) and cleans up component imports.",
                    "It encrypts the user object.",
                    "React requires all hooks to start with 'useAuth'.",
                    "It prevents re-renders entirely."
                ],
                correct_answer="It encapsulates error checking (e.g. verifying the component is inside the Provider) and cleans up component imports.",
                explanation="Custom wrapper hooks provide cleaner syntax and runtime provider presence validation."
            ),
            QuizQuestionBlueprint(
                question="What does the `createContext()` function accept as its argument?",
                options=[
                    "A default fallback value used if a component consumes context without a matching Provider ancestor.",
                    "The database connection URL.",
                    "An array of screen names.",
                    "The app version number."
                ],
                correct_answer="A default fallback value used if a component consumes context without a matching Provider ancestor.",
                explanation="The argument to `createContext(defaultValue)` acts as the fallback."
            ),
            QuizQuestionBlueprint(
                question="What lightweight state management library uses the `create((set) => ({ ... }))` hook pattern without requiring a root Provider?",
                options=["Zustand", "Redux", "MobX", "Recoil"],
                correct_answer="Zustand",
                explanation="Zustand provides boilerplate-free store creation with direct hook-based selector consumption."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 15 (Project)
    # -------------------------------------------------------------
    DayBlueprint(
        order=15,
        title="Day 15: Interactive Shopping Cart State Management Project",
        concept="Engineering a complete global cart system with add, remove, quantity adjustments, and badge synchronization",
        analogy="Think of this project like the digital shopping cart at a supermarket checkout line. As you walk through different aisles (Product screens), you drop items into your cart (`addToCart`). The cart counter badge on your screen's top corner automatically increments (`badge: 3`), and the checkout drawer dynamically calculates subtotal, taxes, and shipping in real-time!",
        theory_sections=[
            {
                "heading": "Shopping Cart State Architecture",
                "body": "In this Module 3 milestone project, you build an integrated `CartContext` supporting all core shopping cart mutations: adding items (incrementing quantity if already present), removing items, adjusting quantities, and calculating dynamic totals (item count, subtotal, tax, and final checkout price)."
            },
            {
                "heading": "Synchronizing Badge Counts Across Navigators",
                "body": "Because the cart count lives in global state, the bottom tab bar's `tabBarBadge` automatically stays synchronized with the user's cart without manual refresh or inter-screen callbacks."
            }
        ],
        code_snippets=[
            {
                "title": "Complete Shopping Cart Context (CartContext.tsx)",
                "code": "import React, { createContext, useContext, useState } from 'react';\n\nexport interface CartItem {\n  id: string;\n  name: string;\n  price: number;\n  quantity: number;\n}\n\ninterface CartContextType {\n  items: CartItem[];\n  addToCart: (product: { id: string; name: string; price: number }) => void;\n  removeFromCart: (id: string) => void;\n  updateQuantity: (id: string, delta: number) => void;\n  totalCount: number;\n  totalPrice: number;\n}\n\nconst CartContext = createContext<CartContextType>({} as CartContextType);\n\nexport const CartProvider = ({ children }: { children: React.ReactNode }) => {\n  const [items, setItems] = useState<CartItem[]>([]);\n\n  const addToCart = (product: { id: string; name: string; price: number }) => {\n    setItems(prev => {\n      const existing = prev.find(i => i.id === product.id);\n      if (existing) {\n        return prev.map(i => i.id === product.id ? { ...i, quantity: i.quantity + 1 } : i);\n      }\n      return [...prev, { ...product, quantity: 1 }];\n    });\n  };\n\n  const updateQuantity = (id: string, delta: number) => {\n    setItems(prev => prev.map(i => {\n      if (i.id === id) {\n        const newQ = i.quantity + delta;\n        return newQ > 0 ? { ...i, quantity: newQ } : null;\n      }\n      return i;\n    }).filter(Boolean) as CartItem[]);\n  };\n\n  const removeFromCart = (id: string) => {\n    setItems(prev => prev.filter(i => i.id !== id));\n  };\n\n  const totalCount = items.reduce((sum, item) => sum + item.quantity, 0);\n  const totalPrice = items.reduce((sum, item) => sum + item.price * item.quantity, 0);\n\n  return (\n    <CartContext.Provider value={{ items, addToCart, removeFromCart, updateQuantity, totalCount, totalPrice }}>\n      {children}\n    </CartContext.Provider>\n  );\n};\n\nexport const useCart = () => useContext(CartContext);"
            },
            {
                "title": "Binding Cart Count to Bottom Tab Badge",
                "code": "const MainTabs = () => {\n  const { totalCount } = useCart();\n  return (\n    <Tab.Navigator>\n      <Tab.Screen name=\"Shop\" component={CatalogScreen} />\n      <Tab.Screen \n        name=\"Cart\" \n        component={CartScreen} \n        options={{\n          tabBarBadge: totalCount > 0 ? totalCount : undefined\n        }}\n      />\n    </Tab.Navigator>\n  );\n};"
            },
            {
                "title": "Interactive Cart Screen UI (CartScreen.tsx)",
                "code": "const CartScreen = () => {\n  const { items, updateQuantity, removeFromCart, totalPrice } = useCart();\n  \n  return (\n    <SafeAreaView style={styles.container}>\n      <FlatList\n        data={items}\n        keyExtractor={item => item.id}\n        renderItem={({ item }) => (\n          <View style={styles.cartRow}>\n            <Text style={styles.itemName}>{item.name}</Text>\n            <View style={styles.qtyControls}>\n              <TouchableOpacity onPress={() => updateQuantity(item.id, -1)}><Text style={styles.btn}>-</Text></TouchableOpacity>\n              <Text style={styles.qtyText}>{item.quantity}</Text>\n              <TouchableOpacity onPress={() => updateQuantity(item.id, 1)}><Text style={styles.btn}>+</Text></TouchableOpacity>\n            </View>\n            <Text style={styles.price}>${(item.price * item.quantity).toFixed(2)}</Text>\n          </View>\n        )}\n      />\n      <View style={styles.footer}>\n        <Text style={styles.totalText}>Total: ${totalPrice.toFixed(2)}</Text>\n      </View>\n    </SafeAreaView>\n  );\n};"
            },
            {
                "title": "Styling the Cart Summary",
                "code": "const styles = StyleSheet.create({\n  container: { flex: 1, backgroundColor: '#0F172A', padding: 16 },\n  cartRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', paddingVertical: 12, borderBottomWidth: 1, borderBottomColor: '#334155' },\n  itemName: { color: '#F8FAFC', fontWeight: 'bold', flex: 1 },\n  qtyControls: { flexDirection: 'row', alignItems: 'center', gap: 12, marginHorizontal: 16 },\n  btn: { color: '#10B981', fontSize: 20, fontWeight: 'bold', paddingHorizontal: 8 },\n  qtyText: { color: '#F8FAFC', fontWeight: 'bold' },\n  price: { color: '#10B981', fontWeight: 'bold' },\n  footer: { padding: 20, backgroundColor: '#1E293B', borderRadius: 16, marginTop: 12 },\n  totalText: { color: '#F8FAFC', fontSize: 20, fontWeight: '800', textAlign: 'right' }\n});"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Cart Item Quantity Incrementor Logic",
            description="Write a function `add_or_increment(cart, item_id, name, price)` that increments quantity if item exists, or appends a new item dict with quantity 1 if absent.",
            starter_code="def add_or_increment(cart, item_id, name, price):\n    # TODO: Update cart list\n    pass\n",
            solution_code="def add_or_increment(cart, item_id, name, price):\n    updated = list(cart)\n    for item in updated:\n        if item['id'] == item_id:\n            item['quantity'] += 1\n            return updated\n    updated.append({'id': item_id, 'name': name, 'price': price, 'quantity': 1})\n    return updated\n\nc = [{'id': '1', 'name': 'Mouse', 'price': 25, 'quantity': 1}]\nc = add_or_increment(c, '1', 'Mouse', 25)\nprint('Quantity:', c[0]['quantity'])",
            expected_output="Quantity: 2"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="How does `addToCart` handle an item that is already present in the user's cart?",
                options=[
                    "It maps over the existing array and increments the `quantity` count of the matching item rather than creating duplicate rows.",
                    "It deletes the item.",
                    "It throws an unhandled duplicate exception.",
                    "It prompts the user to clear the cart."
                ],
                correct_answer="It maps over the existing array and increments the `quantity` count of the matching item rather than creating duplicate rows.",
                explanation="Incrementing quantity for existing IDs keeps the cart neat and consolidated."
            ),
            QuizQuestionBlueprint(
                question="What array method is ideal for calculating total cart price by accumulating `price * quantity`?",
                options=[".reduce()", ".map()", ".forEach()", ".filter()"],
                correct_answer=".reduce()",
                explanation="`items.reduce((sum, item) => sum + item.price * item.quantity, 0)` computes total sum."
            ),
            QuizQuestionBlueprint(
                question="How can you automatically remove an item from the cart if the user clicks decrement when quantity is 1?",
                options=[
                    "Check if `newQuantity <= 0` and filter the item out of the array.",
                    "Throw an error.",
                    "Allow negative quantities (-1).",
                    "Freeze the button."
                ],
                correct_answer="Check if `newQuantity <= 0` and filter the item out of the array.",
                explanation="Filtering out items when quantity drops below 1 provides intuitive UX."
            ),
            QuizQuestionBlueprint(
                question="Why is it helpful that `tabBarBadge` accepts `undefined` in React Navigation?",
                options=[
                    "Passing `undefined` hides the badge completely when the cart count is 0.",
                    "It displays a green question mark.",
                    "It resets the app memory.",
                    "It enables audio alerts."
                ],
                correct_answer="Passing `undefined` hides the badge completely when the cart count is 0.",
                explanation="`tabBarBadge: count > 0 ? count : undefined` hides the badge on empty state."
            ),
            QuizQuestionBlueprint(
                question="Why should cart mathematical totals (subtotal, totalCount) be computed as derived values rather than separate state variables?",
                options=[
                    "Derived values stay perfectly synchronized with the `items` array automatically, eliminating state desynchronization bugs.",
                    "Because React forbids having more than two states.",
                    "To reduce database cost.",
                    "Derived values run on the GPU."
                ],
                correct_answer="Derived values stay perfectly synchronized with the `items` array automatically, eliminating state desynchronization bugs.",
                explanation="Computing derived values during render prevents keeping redundant state variables in sync."
            )
        ],
        is_project_day=True,
        project_name="Interactive Shopping Cart State Management"
    ),

    # -------------------------------------------------------------
    # DAY 16
    # -------------------------------------------------------------
    DayBlueprint(
        order=16,
        title="Day 16: Mobile HTTP Networking (Fetch & Axios)",
        concept="Making asynchronous network requests to backend REST APIs using native fetch and Axios",
        analogy="Think of mobile HTTP networking like placing a takeout order over the phone from your apartment. You dial the restaurant's phone number (`API URL`), state what meal you want (`GET` or `POST`), wait while the kitchen prepares the food (`await response`), and unpack the delivered takeout box (`JSON data`)!",
        theory_sections=[
            {
                "heading": "Network Architecture in Mobile Apps",
                "body": "Mobile applications rarely store all their data locally. They connect over cellular data or Wi-Fi to remote cloud servers via HTTP/HTTPS. React Native provides the standard web `fetch()` API out of the box, as well as support for the popular `axios` library for automated response transforms and request cancellation."
            },
            {
                "heading": "Async/Await and the Mobile Lifecycle",
                "body": "Network requests are asynchronous operations that take unpredictable amounts of time (from 50ms on fast 5G to 5 seconds on weak signals). Modern mobile code uses `async/await` with `try...catch` blocks to handle network timeouts and server responses without blocking the 60fps UI thread."
            }
        ],
        code_snippets=[
            {
                "title": "Basic HTTP GET Request with fetch",
                "code": "const fetchLessons = async () => {\n  try {\n    const response = await fetch('http://192.168.18.62:5000/api/lessons');\n    if (!response.ok) {\n      throw new Error(`HTTP error! status: ${response.status}`);\n    }\n    const data = await response.json();\n    console.log('Fetched lessons:', data.length);\n    return data;\n  } catch (error) {\n    console.error('Network request failed:', error);\n    throw error;\n  }\n};"
            },
            {
                "title": "Making an HTTP POST Request with Headers and JSON Body",
                "code": "const submitFeedback = async (message: string) => {\n  const response = await fetch('http://192.168.18.62:5000/api/feedback', {\n    method: 'POST',\n    headers: {\n      'Content-Type': 'application/json',\n      'Accept': 'application/json'\n    },\n    body: JSON.stringify({ message, timestamp: Date.now() })\n  });\n  return await response.json();\n};"
            },
            {
                "title": "Using Axios for Automated Transforms and Timeouts",
                "code": "import axios from 'axios';\n\nconst apiClient = axios.create({\n  baseURL: 'http://192.168.18.62:5000/api',\n  timeout: 10000, // 10 second timeout\n  headers: { 'Content-Type': 'application/json' }\n});\n\n// Axios automatically parses JSON into response.data!\nconst getProfile = async () => {\n  const response = await apiClient.get('/users/me');\n  return response.data;\n};"
            },
            {
                "title": "Configuring Localhost IP for Physical Devices vs Emulators",
                "code": "// ⚠️ 'localhost' or '127.0.0.1' points to the PHONE itself, not your laptop!\n// For Android Emulator: use 'http://10.0.2.2:5000'\n// For Physical Phone over Wi-Fi: use your laptop's LAN IP (e.g. 'http://192.168.18.62:5000')"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Safe JSON API Fetcher Simulation",
            description="Write a Python simulation of an API fetch function `mock_api_get(url, is_online)` that returns `{'status': 200, 'data': ['Item 1', 'Item 2']}` if online, or raises ConnectionError('No internet') if offline.",
            starter_code="def mock_api_get(url, is_online):\n    # TODO: Implement mock fetcher\n    pass\n",
            solution_code="def mock_api_get(url, is_online):\n    if not is_online:\n        raise ConnectionError('No internet')\n    return {'status': 200, 'data': ['Item 1', 'Item 2']}\n\nprint(mock_api_get('http://api.test/data', True))",
            expected_output="{'status': 200, 'data': ['Item 1', 'Item 2']}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why does `http://localhost:5000` fail to connect when tested on a physical smartphone connected to your Wi-Fi?",
                options=[
                    "Because 'localhost' on the phone refers to the phone's internal loopback interface, not your development laptop running the server.",
                    "Phones cannot send HTTP requests.",
                    "React Native blocks localhost.",
                    "Port 5000 is reserved for phone calls."
                ],
                correct_answer="Because 'localhost' on the phone refers to the phone's internal loopback interface, not your development laptop running the server.",
                explanation="Mobile devices are separate computers; you must use your development machine's LAN IP."
            ),
            QuizQuestionBlueprint(
                question="What special IP address does the Android Studio Virtual Device emulator use to access the host machine's localhost?",
                options=["10.0.2.2", "192.168.0.1", "127.0.0.1", "0.0.0.0"],
                correct_answer="10.0.2.2",
                explanation="`10.0.2.2` is the special virtual network alias mapped by Android emulator to the host computer's 127.0.0.1."
            ),
            QuizQuestionBlueprint(
                question="What header must be included when transmitting JSON payloads via POST in `fetch`?",
                options=["'Content-Type': 'application/json'", "'Format': 'json'", "'Type': 'data'", "'Encoding': 'utf-8'"],
                correct_answer="'Content-Type': 'application/json'",
                explanation="`Content-Type: application/json` informs the backend how to deserialize the request body."
            ),
            QuizQuestionBlueprint(
                question="How does Axios differ from native `fetch` when parsing responses?",
                options=[
                    "Axios automatically deserializes JSON into `response.data`; `fetch` requires an explicit `await response.json()` call.",
                    "Axios only works in Node.js.",
                    "Fetch cannot send POST requests.",
                    "Axios is slower than fetch."
                ],
                correct_answer="Axios automatically deserializes JSON into `response.data`; `fetch` requires an explicit `await response.json()` call.",
                explanation="Axios simplifies networking by parsing JSON bodies and throwing on HTTP error status codes automatically."
            ),
            QuizQuestionBlueprint(
                question="Why should network calls always specify a `timeout` configuration on mobile?",
                options=[
                    "To prevent requests from hanging indefinitely on weak or dropping cellular signals (like entering an elevator or subway).",
                    "To save battery on the server.",
                    "Because mobile operating systems crash after 3 seconds of network activity.",
                    "Timeouts are required by HTTP specifications."
                ],
                correct_answer="To prevent requests from hanging indefinitely on weak or dropping cellular signals (like entering an elevator or subway).",
                explanation="Mobile connections are fragile; timeouts allow apps to fail gracefully and prompt retries."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 17
    # -------------------------------------------------------------
    DayBlueprint(
        order=17,
        title="Day 17: JSON Parsing, TypeScript Interfaces & Data Mapping",
        concept="Typing API responses with TypeScript interfaces and mapping remote arrays into mobile UI components",
        analogy="Think of TypeScript interfaces like a strict recipe card for assembling a dish. When a box of ingredients (raw API JSON) arrives at the kitchen, the interface specifies: 'There must be a title string, an integer ID, and an array of steps'. If an ingredient is missing or spoiled, your editor warns you before you ever turn on the stove!",
        theory_sections=[
            {
                "heading": "Type-Safe Mobile API Consumption",
                "body": "Consuming untyped JSON data (`any`) leads to runtime crashes when properties are missing or misspelled (e.g. `item.total_steps` vs `item.totalSteps`). Defining TypeScript interfaces for all API payloads catches typos at compile time and powers editor autocomplete."
            },
            {
                "heading": "Mapping Remote DTOs to UI Models",
                "body": "Backend database representations often contain extraneous fields or different naming conventions (snake_case vs camelCase). Creating mapping adapter functions transforms raw Data Transfer Objects (DTOs) into clean UI domain models ready for `<FlatList>` consumption."
            }
        ],
        code_snippets=[
            {
                "title": "Defining API Response TypeScript Interfaces",
                "code": "export interface LessonDTO {\n  id: string;\n  title: string;\n  category: string;\n  description: string;\n  color: string;\n  totalSteps: number;\n  totalFlashcards: number;\n  isFeatured: boolean;\n}\n\nexport interface ApiResponse<T> {\n  status: string;\n  data: T;\n  message?: string;\n}"
            },
            {
                "title": "Type-Safe Fetcher Function",
                "code": "const getLessons = async (): Promise<LessonDTO[]> => {\n  const res = await fetch('http://192.168.18.62:5000/api/lessons');\n  if (!res.ok) throw new Error('API fetch failed');\n  const data: LessonDTO[] = await res.json();\n  return data;\n};"
            },
            {
                "title": "Adapter Function Normalizing Raw Backend DTOs",
                "code": "export interface UIModuleCard {\n  id: string;\n  headline: string;\n  badgeText: string;\n  accentColor: string;\n}\n\nexport const mapLessonToCard = (dto: LessonDTO): UIModuleCard => ({\n  id: dto.id,\n  headline: dto.title,\n  badgeText: `⏱ ${dto.totalSteps} Days`,\n  accentColor: dto.color || '#3B82F6'\n});"
            },
            {
                "title": "Rendering Strongly Typed Data in FlatList",
                "code": "const ModuleFeed = ({ modules }: { modules: LessonDTO[] }) => (\n  <FlatList\n    data={modules}\n    keyExtractor={item => item.id}\n    renderItem={({ item }: { item: LessonDTO }) => (\n      <View style={{ borderLeftColor: item.color, borderLeftWidth: 4, padding: 12 }}>\n        <Text style={{ fontWeight: 'bold' }}>{item.title}</Text>\n        <Text>{item.description}</Text>\n      </View>\n    )}\n  />\n);"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="DTO Mapper Implementation",
            description="Write a Python function `map_user_dto(raw_dto)` that converts a dictionary with keys `'first_name'`, `'last_name'`, `'email_addr'` into a normalized dictionary `{'fullName': f'{first} {last}', 'email': email}`.",
            starter_code="def map_user_dto(raw_dto):\n    # TODO: Transform DTO\n    pass\n",
            solution_code="def map_user_dto(raw_dto):\n    first = raw_dto.get('first_name', '')\n    last = raw_dto.get('last_name', '')\n    return {\n        'fullName': f'{first} {last}'.strip(),\n        'email': raw_dto.get('email_addr', '')\n    }\n\nraw = {'first_name': 'Ali', 'last_name': 'Raza', 'email_addr': 'ali@test.com'}\nprint('Mapped:', map_user_dto(raw))",
            expected_output="Mapped: {'fullName': 'Ali Raza', 'email': 'ali@test.com'}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is defining TypeScript interfaces for API responses recommended in mobile apps?",
                options=[
                    "It catches property typos and missing data at compile time, preventing runtime 'cannot read property of undefined' crashes.",
                    "It automatically translates text to Urdu.",
                    "It eliminates the need for unit testing.",
                    "It compresses JSON data by 50%."
                ],
                correct_answer="It catches property typos and missing data at compile time, preventing runtime 'cannot read property of undefined' crashes.",
                explanation="Type-safe interfaces ensure your components only access properties guaranteed to exist."
            ),
            QuizQuestionBlueprint(
                question="What is an adapter/mapper function in mobile networking architecture?",
                options=[
                    "A function that transforms raw backend JSON into a clean, normalized data format tailored for the UI.",
                    "A Wi-Fi hardware driver.",
                    "A function that converts PNG images to JPEG.",
                    "A database migration script."
                ],
                correct_answer="A function that transforms raw backend JSON into a clean, normalized data format tailored for the UI.",
                explanation="Adapters decouple your mobile UI components from backend schema naming conventions."
            ),
            QuizQuestionBlueprint(
                question="What does the TypeScript generic syntax `Promise<LessonDTO[]>` declare as the return value of an async function?",
                options=[
                    "An asynchronous Promise that resolves to an array of LessonDTO objects.",
                    "A synchronous list of strings.",
                    "A database transaction.",
                    "An error object."
                ],
                correct_answer="An asynchronous Promise that resolves to an array of LessonDTO objects.",
                explanation="`Promise<T>` defines the type of value returned when an asynchronous function resolves."
            ),
            QuizQuestionBlueprint(
                question="How do you handle optional fields that might be null or omitted by an API in a TypeScript interface?",
                options=["Using a question mark: `bio?: string;`", "Using `nullable bio;`", "Using `optional(bio)`", "Writing `bio = null`"],
                correct_answer="Using a question mark: `bio?: string;`",
                explanation="The `?` modifier declares that a property may be present or undefined."
            ),
            QuizQuestionBlueprint(
                question="What operator safely accesses nested JSON properties without crashing if an intermediate key is null?",
                options=["Optional chaining (`?.`)", "Double bang (`!!`)", "Nullish coalescing (`??`)", "Bitwise AND (`&`)"],
                correct_answer="Optional chaining (`?.`)",
                explanation="`user?.profile?.avatar` short-circuits to `undefined` if `user` or `profile` is null."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 18
    # -------------------------------------------------------------
    DayBlueprint(
        order=18,
        title="Day 18: Loading Indicators, Skeletons & Error Handling",
        concept="Delivering polished user experiences using ActivityIndicator, skeleton loaders, and retry banners",
        analogy="Think of loading indicators like the visual progress bar while an espresso machine brews your coffee. If the machine remained completely silent and motionless for 20 seconds, you would think it was broken and press the cancel button! A spinning indicator (`ActivityIndicator`) reassures the customer that their drink is being freshly prepared!",
        theory_sections=[
            {
                "heading": "The Three Async UI States",
                "body": "Every screen that loads data over the network must explicitly manage three distinct visual states: (1) **Loading State**: Show an `<ActivityIndicator>` or skeleton placeholders while fetching. (2) **Success State**: Render the populated `<FlatList>`. (3) **Error State**: Display a friendly error message with a 'Try Again' retry button if the network fails."
            },
            {
                "heading": "ActivityIndicator vs Skeleton Loading Screens",
                "body": "While `<ActivityIndicator size=\"large\" color=\"#10B981\" />` is simple to implement, modern mobile apps increasingly use **Skeleton Loaders** (dim gray animated card outlines that mirror the final screen layout). Skeletons reduce perceived wait times and prevent layout shift."
            }
        ],
        code_snippets=[
            {
                "title": "Comprehensive 3-State Screen Controller",
                "code": "import React, { useState, useEffect } from 'react';\nimport { View, Text, ActivityIndicator, TouchableOpacity, FlatList, StyleSheet } from 'react-native';\n\nexport const DataFeedScreen = () => {\n  const [data, setData] = useState([]);\n  const [isLoading, setIsLoading] = useState(true);\n  const [errorMessage, setErrorMessage] = useState<string | null>(null);\n\n  const loadData = async () => {\n    setIsLoading(true);\n    setErrorMessage(null);\n    try {\n      const res = await fetch('http://192.168.18.62:5000/api/lessons');\n      if (!res.ok) throw new Error('Server returned an error');\n      const items = await res.json();\n      setData(items);\n    } catch (err: any) {\n      setErrorMessage(err.message || 'Unable to connect to server.');\n    } finally {\n      setIsLoading(false);\n    }\n  };\n\n  useEffect(() => {\n    loadData();\n  }, []);\n\n  // 1. Loading State\n  if (isLoading) {\n    return (\n      <View style={styles.center}>\n        <ActivityIndicator size=\"large\" color=\"#10B981\" />\n        <Text style={styles.loadingText}>Loading curriculum...</Text>\n      </View>\n    );\n  }\n\n  // 2. Error State with Retry Button\n  if (errorMessage) {\n    return (\n      <View style={styles.center}>\n        <Text style={styles.errorIcon}>⚠️</Text>\n        <Text style={styles.errorText}>{errorMessage}</Text>\n        <TouchableOpacity style={styles.retryBtn} onPress={loadData}>\n          <Text style={styles.retryBtnText}>Tap to Retry</Text>\n        </TouchableOpacity>\n      </View>\n    );\n  }\n\n  // 3. Success State\n  return (\n    <FlatList\n      data={data}\n      keyExtractor={item => item.id}\n      renderItem={({ item }) => <Text style={styles.card}>{item.title}</Text>}\n    />\n  );\n};"
            },
            {
                "title": "Building a Lightweight Skeleton Placeholder",
                "code": "const SkeletonCard = () => (\n  <View style={styles.skeletonContainer}>\n    <View style={styles.skeletonImage} />\n    <View style={styles.skeletonTitle} />\n    <View style={styles.skeletonSubtitle} />\n  </View>\n);\n\nconst styles = StyleSheet.create({\n  skeletonContainer: { padding: 16, backgroundColor: '#1E293B', borderRadius: 16, marginBottom: 12 },\n  skeletonImage: { height: 120, backgroundColor: '#334155', borderRadius: 12, marginBottom: 8 },\n  skeletonTitle: { height: 16, width: '70%', backgroundColor: '#334155', borderRadius: 4, marginBottom: 6 },\n  skeletonSubtitle: { height: 12, width: '40%', backgroundColor: '#334155', borderRadius: 4 }\n});"
            },
            {
                "title": "Inline Banner Error Alerts",
                "code": "const ErrorBanner = ({ message, onDismiss }) => (\n  <View style={{ backgroundColor: '#EF444420', borderColor: '#EF4444', borderWidth: 1, padding: 12, borderRadius: 12, flexDirection: 'row', justifyContent: 'space-between' }}>\n    <Text style={{ color: '#F87171' }}>{message}</Text>\n    <TouchableOpacity onPress={onDismiss}><Text style={{ color: '#F87171', fontWeight: 'bold' }}>✕</Text></TouchableOpacity>\n  </View>\n);"
            },
            {
                "title": "Pull to Refresh with Loading Spinner",
                "code": "<FlatList\n  data={data}\n  renderItem={renderItem}\n  refreshing={isLoading}\n  onRefresh={loadData}\n/>"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Async State Reducer Simulator",
            description="Write a Python reducer function `async_reducer(state, action)` that updates status to 'loading', 'success' (with data), or 'error' (with message) based on action type.",
            starter_code="def async_reducer(state, action):\n    # TODO: Implement async reducer\n    pass\n",
            solution_code="def async_reducer(state, action):\n    t = action.get('type')\n    if t == 'FETCH_INIT':\n        return {'status': 'loading', 'data': None, 'error': None}\n    elif t == 'FETCH_SUCCESS':\n        return {'status': 'success', 'data': action['payload'], 'error': None}\n    elif t == 'FETCH_ERROR':\n        return {'status': 'error', 'data': None, 'error': action['error']}\n    return state\n\ns = async_reducer({}, {'type': 'FETCH_SUCCESS', 'payload': [1, 2, 3]})\nprint('State:', s['status'], s['data'])",
            expected_output="State: success [1, 2, 3]"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What built-in React Native component renders a circular animated spinning loader?",
                options=["ActivityIndicator", "SpinnerView", "CircularProgress", "LoadingWheel"],
                correct_answer="ActivityIndicator",
                explanation="`<ActivityIndicator size=\"large\" color=\"...\" />` renders the platform-native spinning wheel."
            ),
            QuizQuestionBlueprint(
                question="What is the key advantage of Skeleton Loaders over a simple centered spinning wheel?",
                options=[
                    "They provide immediate visual context of where content will appear, reducing perceived wait time and avoiding layout shift.",
                    "They reduce backend CPU usage.",
                    "They allow offline data generation.",
                    "They do not require CSS."
                ],
                correct_answer="They provide immediate visual context of where content will appear, reducing perceived wait time and avoiding layout shift.",
                explanation="Skeleton screens create visual anticipation matching the target layout."
            ),
            QuizQuestionBlueprint(
                question="Why is it critical to provide a 'Retry' action when an API request fails on mobile?",
                options=[
                    "Mobile network connections frequently drop temporarily; allowing users to tap retry avoids forcing them to restart the app.",
                    "App stores require a retry button or they reject the binary.",
                    "Retry buttons automatically fix server bugs.",
                    "It charges the phone's battery."
                ],
                correct_answer="Mobile network connections frequently drop temporarily; allowing users to tap retry avoids forcing them to restart the app.",
                explanation="Giving users an instant retry option recovers gracefully from transient cellular drops."
            ),
            QuizQuestionBlueprint(
                question="What JavaScript block ensures that `setIsLoading(false)` always runs whether the network call succeeds or fails?",
                options=["finally { setIsLoading(false); }", "catch { ... }", "then { ... }", "always { ... }"],
                correct_answer="finally { setIsLoading(false); }",
                explanation="The `finally` block executes unconditionally after `try` or `catch` completes."
            ),
            QuizQuestionBlueprint(
                question="What props on `<FlatList>` enable native pull-down-to-refresh functionality?",
                options=["refreshing and onRefresh", "isPulling and onPull", "pullToRefresh and onReload", "refreshControl and onUpdate"],
                correct_answer="refreshing and onRefresh",
                explanation="`refreshing={isLoading}` and `onRefresh={handleRefresh}` wire up native pull-to-refresh."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 19
    # -------------------------------------------------------------
    DayBlueprint(
        order=19,
        title="Day 19: Network Interceptors & Bearer Token Authentication",
        concept="Automating Authorization header injection and handling 401 token expiration using Axios interceptors",
        analogy="Think of a network interceptor like a personal secretary who stamps and reviews all outgoing mail before it leaves your office. You just write your letter ('GET /profile'). The secretary automatically attaches your official digital seal (`Authorization: Bearer <token>`). If the mail returns stamped 'Signature Expired' (HTTP 401), the secretary immediately redirects you to the renewal desk!",
        theory_sections=[
            {
                "heading": "The Need for Network Interceptors",
                "body": "Manually attaching `headers: { 'Authorization': `Bearer ${token}` }` to 50 separate API calls is redundant and error-prone. Interceptors act as middleware for your HTTP client, intercepting every outgoing request to inject auth tokens and intercepting every incoming response to catch errors globally."
            },
            {
                "heading": "Handling Global 401 Unauthorized Expirations",
                "body": "When a user's JWT access token expires, the server responds with HTTP 401. A response interceptor detects this status, emits a logout event, clears cached tokens from storage, and redirects the user back to the Login screen automatically."
            }
        ],
        code_snippets=[
            {
                "title": "Creating an Authenticated Axios Instance with Interceptors",
                "code": "import axios from 'axios';\nimport AsyncStorage from '@react-native-async-storage/async-storage';\nimport { DeviceEventEmitter } from 'react-native';\n\nexport const api = axios.create({\n  baseURL: 'http://192.168.18.62:5000/api',\n  timeout: 10000,\n});\n\n// 1. Request Interceptor: Injects Bearer Token\napi.interceptors.request.use(\n  async (config) => {\n    const token = await AsyncStorage.getItem('user_token');\n    if (token) {\n      config.headers.Authorization = `Bearer ${token}`;\n    }\n    return config;\n  },\n  (error) => Promise.reject(error)\n);"
            },
            {
                "title": "Response Interceptor: Catching 401 and Triggering Global Logout",
                "code": "// 2. Response Interceptor: Catches 401 Unauthorized\napi.interceptors.response.use(\n  (response) => response,\n  async (error) => {\n    if (error.response && error.response.status === 401) {\n      console.warn('Session expired. Logging out...');\n      await AsyncStorage.removeItem('user_token');\n      // Notify global AuthProvider to reset state\n      DeviceEventEmitter.emit('on-token-expired');\n    }\n    return Promise.reject(error);\n  }\n);"
            },
            {
                "title": "Global Event Listener in AuthContext",
                "code": "useEffect(() => {\n  const subscription = DeviceEventEmitter.addListener('on-token-expired', () => {\n    setUser(null);\n    setToken(null);\n  });\n  return () => subscription.remove();\n}, []);"
            },
            {
                "title": "Simplified Clean API Calls in Components",
                "code": "// Components make simple clean calls without managing headers!\nconst fetchMyStats = async () => {\n  const { data } = await api.get('/users/me');\n  return data;\n};"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Authorization Header Builder",
            description="Write a Python helper `build_auth_header(token)` that returns `{'Authorization': f'Bearer {token}'}` if token is present, or an empty dictionary if token is None.",
            starter_code="def build_auth_header(token):\n    # TODO: Build header\n    pass\n",
            solution_code="def build_auth_header(token):\n    if token:\n        return {'Authorization': f'Bearer {token}'}\n    return {}\n\nprint('With token:', build_auth_header('jwt_xyz_123'))\nprint('Without token:', build_auth_header(None))",
            expected_output="With token: {'Authorization': 'Bearer jwt_xyz_123'}\nWithout token: {}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the purpose of an Axios Request Interceptor in mobile applications?",
                options=[
                    "To intercept and modify outgoing HTTP requests before they leave the device (e.g. automatically injecting the Bearer auth token).",
                    "To speed up the phone's CPU.",
                    "To block all outgoing network calls.",
                    "To convert JavaScript to Swift."
                ],
                correct_answer="To intercept and modify outgoing HTTP requests before they leave the device (e.g. automatically injecting the Bearer auth token).",
                explanation="Request interceptors execute middleware logic prior to dispatching network calls."
            ),
            QuizQuestionBlueprint(
                question="What HTTP status code triggers a response interceptor to handle session expiration?",
                options=["401 Unauthorized", "404 Not Found", "200 OK", "500 Internal Error"],
                correct_answer="401 Unauthorized",
                explanation="HTTP 401 signifies that credentials are missing, invalid, or expired."
            ),
            QuizQuestionBlueprint(
                question="What React Native utility allows non-React files (like an API interceptor) to notify the UI of an expired token?",
                options=["DeviceEventEmitter", "AsyncStorage", "StyleSheet", "Platform"],
                correct_answer="DeviceEventEmitter",
                explanation="`DeviceEventEmitter.emit()` broadcasts cross-module events across the app."
            ),
            QuizQuestionBlueprint(
                question="What format does standard Bearer token authentication expect in the HTTP Authorization header?",
                options=["Authorization: Bearer <token>", "Authorization: Token <token>", "Bearer: <token>", "Auth: <token>"],
                correct_answer="Authorization: Bearer <token>",
                explanation="The standard HTTP authorization header format is `Authorization: Bearer <jwt_token>`."
            ),
            QuizQuestionBlueprint(
                question="Why is centralizing token injection in an interceptor superior to manual per-request headers?",
                options=[
                    "It ensures 100% consistency across all API calls and allows updating auth logic in a single file.",
                    "It bypasses CORS restrictions.",
                    "It allows unauthenticated database writes.",
                    "It encrypts the phone's battery."
                ],
                correct_answer="It ensures 100% consistency across all API calls and allows updating auth logic in a single file.",
                explanation="Centralizing logic in an interceptor adheres to DRY and eliminates manual header bugs."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 20 (Project)
    # -------------------------------------------------------------
    DayBlueprint(
        order=20,
        title="Day 20: Live Weather Mobile App Project",
        concept="Building a complete live Weather application fetching real-time OpenWeather REST API with search and dynamic weather cards",
        analogy="Think of building this weather app like creating a live radar display in an airplane cockpit. When the pilot types in the target airport code ('London' or 'Islamabad'), the navigation computer queries satellite meteorological stations via REST API, parses temperature, humidity, and wind, and renders clear visual sun or thunderstorm icons immediately!",
        theory_sections=[
            {
                "heading": "Module 4 Capstone Architecture",
                "body": "In this project, you unify all networking concepts from Module 4: accepting user city queries via `<TextInput>`, managing asynchronous fetching states (`isLoading`, `error`, `data`), parsing real-world JSON weather payloads, handling temperature conversions (Kelvin to Celsius), and rendering dynamic condition cards."
            },
            {
                "heading": "Handling Network Edge Cases on Mobile",
                "body": "Real-world mobile apps must handle empty searches, invalid city names (HTTP 404), network timeouts, and device keyboard dismissal (`Keyboard.dismiss()`) when the user taps 'Search'."
            }
        ],
        code_snippets=[
            {
                "title": "Weather Data TypeScript Interface",
                "code": "export interface WeatherData {\n  city: string;\n  tempC: number;\n  condition: string;\n  icon: string;\n  humidity: number;\n  windSpeed: number;\n}"
            },
            {
                "title": "Live API Fetcher Service (weatherService.ts)",
                "code": "const API_KEY = 'YOUR_OPENWEATHER_API_KEY';\n\nexport const fetchWeatherByCity = async (city: string): Promise<WeatherData> => {\n  const url = `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&units=metric&appid=${API_KEY}`;\n  const res = await fetch(url);\n  if (!res.ok) {\n    if (res.status === 404) throw new Error('City not found. Please check spelling.');\n    throw new Error('Unable to retrieve weather data.');\n  }\n  const json = await res.json();\n  return {\n    city: json.name,\n    tempC: Math.round(json.main.temp),\n    condition: json.weather[0].main,\n    icon: json.weather[0].icon,\n    humidity: json.main.humidity,\n    windSpeed: Math.round(json.wind.speed * 3.6)\n  };\n};"
            },
            {
                "title": "Complete Weather Screen Component (WeatherScreen.tsx)",
                "code": "import React, { useState } from 'react';\nimport { View, Text, TextInput, TouchableOpacity, ActivityIndicator, Keyboard, StyleSheet } from 'react-native';\nimport { SafeAreaView } from 'react-native-safe-area-context';\nimport { fetchWeatherByCity, WeatherData } from './weatherService';\n\nexport const WeatherScreen = () => {\n  const [query, setQuery] = useState('');\n  const [weather, setWeather] = useState<WeatherData | null>(null);\n  const [loading, setLoading] = useState(false);\n  const [error, setError] = useState<string | null>(null);\n\n  const handleSearch = async () => {\n    if (!query.trim()) return;\n    Keyboard.dismiss();\n    setLoading(true);\n    setError(null);\n    try {\n      const result = await fetchWeatherByCity(query);\n      setWeather(result);\n    } catch (err: any) {\n      setError(err.message);\n      setWeather(null);\n    } finally {\n      setLoading(false);\n    }\n  };\n\n  return (\n    <SafeAreaView style={styles.container}>\n      <Text style={styles.appTitle}>🌤 Live Weather Radar</Text>\n      <View style={styles.searchRow}>\n        <TextInput\n          style={styles.input}\n          placeholder=\"Enter city (e.g. Islamabad, London)\"\n          placeholderTextColor=\"#94A3B8\"\n          value={query}\n          onChangeText={setQuery}\n        />\n        <TouchableOpacity style={styles.searchBtn} onPress={handleSearch}>\n          <Text style={styles.searchBtnText}>Search</Text>\n        </TouchableOpacity>\n      </View>\n\n      {loading && <ActivityIndicator size=\"large\" color=\"#38BDF8\" style={{ marginTop: 40 }} />}\n      {error && <Text style={styles.errorText}>{error}</Text>}\n\n      {weather && (\n        <View style={styles.card}>\n          <Text style={styles.city}>{weather.city}</Text>\n          <Text style={styles.temp}>{weather.tempC}°C</Text>\n          <Text style={styles.condition}>{weather.condition}</Text>\n          <View style={styles.metaRow}>\n            <Text style={styles.metaText}>💧 Humidity: {weather.humidity}%</Text>\n            <Text style={styles.metaText}>💨 Wind: {weather.windSpeed} km/h</Text>\n          </View>\n        </View>\n      )}\n    </SafeAreaView>\n  );\n};"
            },
            {
                "title": "Weather Screen Stylesheet",
                "code": "const styles = StyleSheet.create({\n  container: { flex: 1, backgroundColor: '#0B1120', padding: 20 },\n  appTitle: { fontSize: 24, fontWeight: '800', color: '#F8FAFC', marginBottom: 20, textAlign: 'center' },\n  searchRow: { flexDirection: 'row', gap: 10, marginBottom: 24 },\n  input: { flex: 1, backgroundColor: '#1E293B', borderRadius: 12, paddingHorizontal: 16, color: '#FFF' },\n  searchBtn: { backgroundColor: '#0284C7', paddingHorizontal: 20, justifyContent: 'center', borderRadius: 12 },\n  searchBtnText: { color: '#FFF', fontWeight: 'bold' },\n  card: { backgroundColor: '#1E293B', borderRadius: 24, padding: 30, alignItems: 'center', borderWidth: 1, borderColor: '#38BDF840' },\n  city: { fontSize: 28, fontWeight: 'bold', color: '#F8FAFC' },\n  temp: { fontSize: 64, fontWeight: '900', color: '#38BDF8', marginVertical: 10 },\n  condition: { fontSize: 20, color: '#94A3B8', marginBottom: 20 },\n  metaRow: { flexDirection: 'row', gap: 20 },\n  metaText: { color: '#CBD5E1', fontSize: 14 },\n  errorText: { color: '#F87171', textAlign: 'center', marginTop: 20 }\n});"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Temperature Scale Converter",
            description="Write a function `convert_temp(temp, from_scale, to_scale)` that converts between Celsius ('C') and Fahrenheit ('F') with rounding to 1 decimal place.",
            starter_code="def convert_temp(temp, from_scale, to_scale):\n    # TODO: Implement conversion\n    pass\n",
            solution_code="def convert_temp(temp, from_scale, to_scale):\n    if from_scale == to_scale:\n        return round(float(temp), 1)\n    if from_scale == 'C' and to_scale == 'F':\n        return round((temp * 9/5) + 32, 1)\n    if from_scale == 'F' and to_scale == 'C':\n        return round((temp - 32) * 5/9, 1)\n    return round(float(temp), 1)\n\nprint('25C to F:', convert_temp(25, 'C', 'F'))\nprint('77F to C:', convert_temp(77, 'F', 'C'))",
            expected_output="25C to F: 77.0\n77F to C: 25.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What method dismisses the virtual keyboard programmatically when a search action triggers on mobile?",
                options=["Keyboard.dismiss()", "Keyboard.close()", "Keyboard.hide()", "TextInput.blurAll()"],
                correct_answer="Keyboard.dismiss()",
                explanation="`Keyboard.dismiss()` closes the active software keyboard."
            ),
            QuizQuestionBlueprint(
                question="Why is `encodeURIComponent(city)` used when inserting city names into query URLs?",
                options=[
                    "It properly escapes spaces and special characters (e.g. 'San Francisco' becomes 'San%20Francisco'), preventing broken URLs.",
                    "It translates city names into French.",
                    "It encrypts the city name.",
                    "It is required by TypeScript."
                ],
                correct_answer="It properly escapes spaces and special characters (e.g. 'San Francisco' becomes 'San%20Francisco'), preventing broken URLs.",
                explanation="`encodeURIComponent` safely encodes spaces, commas, and unicode characters for URLs."
            ),
            QuizQuestionBlueprint(
                question="What HTTP status code from a weather API signifies that the searched city could not be located in their database?",
                options=["404 Not Found", "401 Unauthorized", "500 Server Error", "200 OK"],
                correct_answer="404 Not Found",
                explanation="HTTP 404 indicates the requested city resource does not exist in the API database."
            ),
            QuizQuestionBlueprint(
                question="Where should third-party API private keys be stored in production mobile apps rather than hardcoded into source code?",
                options=[
                    "In environment variables (e.g. `.env` via `react-native-dotenv` or EAS Secrets), or proxied through your own backend server.",
                    "In comments in App.tsx.",
                    "In the public README file.",
                    "In the device contact list."
                ],
                correct_answer="In environment variables (e.g. `.env` via `react-native-dotenv` or EAS Secrets), or proxied through your own backend server.",
                explanation="Proxying keys through your backend or injecting via secure build secrets prevents key theft."
            ),
            QuizQuestionBlueprint(
                question="What is the unit conversion formula to convert temperature from Celsius (°C) to Fahrenheit (°F)?",
                options=["(C * 9/5) + 32", "(C * 5/9) - 32", "C + 273.15", "C * 2"],
                correct_answer="(C * 9/5) + 32",
                explanation="Fahrenheit = (Celsius * 9/5) + 32."
            )
        ],
        is_project_day=True,
        project_name="Live Weather Mobile App"
    ),
]
