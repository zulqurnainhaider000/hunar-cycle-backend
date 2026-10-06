"""
Mobile App Development 40-Day Curriculum - Module 5, Module 6 & Module 7 (Part 1) (Days 21 to 30)
Module 5: Local Storage & Databases (Days 21-24)
Module 6: Device Features & Hardware (Days 25-28)
Module 7: Cloud Services & BaaS (Days 29-30)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_21_TO_30 = [
    # -------------------------------------------------------------
    # DAY 21
    # -------------------------------------------------------------
    DayBlueprint(
        order=21,
        title="Day 21: Persistent Key-Value Storage with AsyncStorage",
        concept="Persisting user settings, JWT tokens, and cached strings on device flash storage using AsyncStorage",
        analogy="Think of AsyncStorage like a small, private safe inside a hotel guest's room. Even if the hotel power goes out or you turn off the room lights and leave for dinner (closing the app or restarting your phone), the items you locked inside the safe (`AsyncStorage.setItem`) remain safe and waiting for you when you return!",
        theory_sections=[
            {
                "heading": "Why In-Memory State Disappears",
                "body": "React state (`useState`, Redux) lives purely in dynamic RAM. When a user swipes an app closed or the mobile operating system kills background processes to save battery, all in-memory data is purged. Persistent key-value storage allows apps to save critical strings (such as login tokens and dark mode preferences) across app restarts."
            },
            {
                "heading": "The AsyncStorage API",
                "body": "`@react-native-async-storage/async-storage` provides an asynchronous, unencrypted key-value store. It stores data natively in SQLite or SharedPreferences on Android and small files/UserDefaults on iOS. All values must be strings; complex JavaScript objects must be serialized using `JSON.stringify()` on write and `JSON.parse()` on read."
            }
        ],
        code_snippets=[
            {
                "title": "Saving and Reading a Primitive String",
                "code": "import AsyncStorage from '@react-native-async-storage/async-storage';\n\n// 1. Save data to device storage\nconst storeUserToken = async (token: string) => {\n  try {\n    await AsyncStorage.setItem('auth_token', token);\n    console.log('Token securely saved to disk!');\n  } catch (e) {\n    console.error('Failed to save token:', e);\n  }\n};\n\n// 2. Read data from device storage\nconst getUserToken = async (): Promise<string | null> => {\n  try {\n    return await AsyncStorage.getItem('auth_token');\n  } catch (e) {\n    return null;\n  }\n};"
            },
            {
                "title": "Storing and Parsing Complex Objects with JSON",
                "code": "const saveUserProfile = async (profile: object) => {\n  const jsonValue = JSON.stringify(profile);\n  await AsyncStorage.setItem('user_profile', jsonValue);\n};\n\nconst loadUserProfile = async () => {\n  const jsonValue = await AsyncStorage.getItem('user_profile');\n  return jsonValue != null ? JSON.parse(jsonValue) : null;\n};"
            },
            {
                "title": "Removing Keys & Complete Storage Purge",
                "code": "// Remove specific item on user logout\nconst handleLogout = async () => {\n  await AsyncStorage.removeItem('auth_token');\n  await AsyncStorage.removeItem('user_profile');\n};\n\n// Clear entire app storage sandbox\nconst clearAllStorage = async () => {\n  await AsyncStorage.clear();\n};"
            },
            {
                "title": "Multi-Get Batch Operations",
                "code": "const loadStartupData = async () => {\n  // Fetches multiple keys simultaneously in a single native operation\n  const values = await AsyncStorage.multiGet(['auth_token', 'theme', 'language']);\n  // Returns array of pairs: [['auth_token', 'xyz'], ['theme', 'dark'], ...]\n  return Object.fromEntries(values);\n};"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="AsyncStorage Serialization Helper",
            description="Write a Python simulation function `serialize_for_storage(data_dict)` that returns a JSON string, and `deserialize_from_storage(raw_str)` that returns the dictionary or None if raw_str is None.",
            starter_code="import json\n\n# TODO: Implement serialization helpers\n",
            solution_code="import json\n\ndef serialize_for_storage(data_dict):\n    return json.dumps(data_dict)\n\ndef deserialize_from_storage(raw_str):\n    if raw_str is None:\n        return None\n    return json.loads(raw_str)\n\ns = serialize_for_storage({'token': '123'})\nprint('Deserialized:', deserialize_from_storage(s))",
            expected_output="Deserialized: {'token': '123'}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What data type must values be when passed into `AsyncStorage.setItem(key, value)`?",
                options=["String (objects must be serialized with `JSON.stringify()`)", "Any JavaScript object", "Raw binary bytes", "Integer only"],
                correct_answer="String (objects must be serialized with `JSON.stringify()`)",
                explanation="AsyncStorage only accepts string values; complex objects require JSON serialization."
            ),
            QuizQuestionBlueprint(
                question="Why is AsyncStorage described as 'asynchronous'?",
                options=[
                    "It reads and writes to physical flash storage on a background thread via Promises, preventing UI thread freezing.",
                    "It requires an internet connection.",
                    "It only updates once per day.",
                    "It uses WebSockets."
                ],
                correct_answer="It reads and writes to physical flash storage on a background thread via Promises, preventing UI thread freezing.",
                explanation="Disk I/O is slow; asynchronous promises ensure the 60fps UI never stutters during reads/writes."
            ),
            QuizQuestionBlueprint(
                question="Which method removes an individual key from AsyncStorage upon user logout?",
                options=["AsyncStorage.removeItem('key')", "AsyncStorage.delete('key')", "AsyncStorage.pop('key')", "AsyncStorage.remove('key')"],
                correct_answer="AsyncStorage.removeItem('key')",
                explanation="`AsyncStorage.removeItem('key')` deletes that specific key from device storage."
            ),
            QuizQuestionBlueprint(
                question="Should large multi-megabyte databases (like 50,000 offline products) be stored in AsyncStorage?",
                options=[
                    "No; AsyncStorage is meant for small key-value settings. Large structured data belongs in SQLite.",
                    "Yes, AsyncStorage has unlimited RAM.",
                    "Yes, because AsyncStorage supports SQL queries.",
                    "No, AsyncStorage can only store 10 characters."
                ],
                correct_answer="No; AsyncStorage is meant for small key-value settings. Large structured data belongs in SQLite.",
                explanation="AsyncStorage is an unindexed key-value store; structured records require relational SQLite."
            ),
            QuizQuestionBlueprint(
                question="What is the default return value of `AsyncStorage.getItem('missing_key')` if the key does not exist?",
                options=["null", "undefined", "'' (empty string)", "Throws a KeyNotFoundError"],
                correct_answer="null",
                explanation="If a key does not exist, `getItem()` resolves cleanly to `null`."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 22
    # -------------------------------------------------------------
    DayBlueprint(
        order=22,
        title="Day 22: Local Mobile Databases with SQLite",
        concept="Executing relational SQL queries and table creation locally on-device using expo-sqlite",
        analogy="Think of a local SQLite database like an offline notebook with structured ledger tables kept in your briefcase. Even if you are on an airplane with zero Wi-Fi or cellular connection, you can open your notebook, search through 10,000 customer entries in 2 milliseconds, add new ledger rows, and calculate totals instantly!",
        theory_sections=[
            {
                "heading": "Why Mobile Apps Need Local Relational Databases",
                "body": "When an application needs to store thousands of records (e.g. offline courses, chat logs, cached products) with relational foreign keys and indexed search queries, key-value storage is insufficient. SQLite is a lightweight, battle-tested C database engine embedded directly into both iOS and Android."
            },
            {
                "heading": "Using expo-sqlite for Local Queries",
                "body": "Using `expo-sqlite`, you open an on-device database file via `SQLite.openDatabaseSync('app.db')`. You execute schema initialization (`CREATE TABLE IF NOT EXISTS`), parameterized inserts (`INSERT INTO notes ...`), and queries with transactional atomicity."
            }
        ],
        code_snippets=[
            {
                "title": "Initializing Local SQLite Database (db.ts)",
                "code": "import * as SQLite from 'expo-sqlite';\n\n// Open or create local database on device storage\nconst db = SQLite.openDatabaseSync('hunar_offline.db');\n\nexport const initDatabase = () => {\n  db.execSync(`\n    PRAGMA journal_mode = WAL;\n    CREATE TABLE IF NOT EXISTS notes (\n      id INTEGER PRIMARY KEY AUTOINCREMENT,\n      title TEXT NOT NULL,\n      content TEXT NOT NULL,\n      category TEXT DEFAULT 'General',\n      created_at DATETIME DEFAULT CURRENT_TIMESTAMP\n    );\n  `);\n  console.log('Local SQLite database initialized!');\n};"
            },
            {
                "title": "Inserting Records with Parameterized Queries",
                "code": "export const addNote = (title: string, content: string, category: string) => {\n  // Parameterized query prevents SQL injection\n  const result = db.runSync(\n    'INSERT INTO notes (title, content, category) VALUES (?, ?, ?)',\n    [title, content, category]\n  );\n  return result.lastInsertRowId;\n};"
            },
            {
                "title": "Querying Records with getAllSync",
                "code": "export interface NoteRecord {\n  id: number;\n  title: string;\n  content: string;\n  category: string;\n  created_at: string;\n}\n\nexport const getAllNotes = (): NoteRecord[] => {\n  return db.getAllSync<NoteRecord>('SELECT * FROM notes ORDER BY id DESC');\n};"
            },
            {
                "title": "Search Query with SQL LIKE Clause",
                "code": "export const searchNotes = (query: string): NoteRecord[] => {\n  return db.getAllSync<NoteRecord>(\n    'SELECT * FROM notes WHERE title LIKE ? OR content LIKE ?',\n    [`%${query}%`, `%${query}%`]\n  );\n};"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Local SQL Insert Formatter",
            description="Write a Python helper `build_insert_query(table, fields)` that generates a parameterized SQL string in format 'INSERT INTO <table> (<f1>, <f2>) VALUES (?, ?)' given table name and field list.",
            starter_code="def build_insert_query(table, fields):\n    # TODO: Build parameterized query\n    pass\n",
            solution_code="def build_insert_query(table, fields):\n    cols = ', '.join(fields)\n    placeholders = ', '.join(['?'] * len(fields))\n    return f'INSERT INTO {table} ({cols}) VALUES ({placeholders})'\n\nprint(build_insert_query('notes', ['title', 'content']))",
            expected_output="INSERT INTO notes (title, content) VALUES (?, ?)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Where does a SQLite database file reside when running inside a mobile application?",
                options=[
                    "Locally on the device's internal flash storage within the app's sandboxed directory.",
                    "In the Google Cloud.",
                    "On the cellular carrier's tower.",
                    "In the user's browser cache."
                ],
                correct_answer="Locally on the device's internal flash storage within the app's sandboxed directory.",
                explanation="SQLite is an embedded database that runs completely inside the device's local filesystem."
            ),
            QuizQuestionBlueprint(
                question="Why should database queries always use parameterized placeholders (`?`) rather than string concatenation?",
                options=[
                    "To prevent SQL Injection vulnerabilities and safely escape quotes and special characters.",
                    "To make queries run on the GPU.",
                    "Because SQLite forbids quotes.",
                    "To reduce font size."
                ],
                correct_answer="To prevent SQL Injection vulnerabilities and safely escape quotes and special characters.",
                explanation="Parameterized statements treat values as data rather than executable SQL code, preventing attacks."
            ),
            QuizQuestionBlueprint(
                question="What SQL clause creates an auto-incrementing unique numeric identifier for rows in SQLite?",
                options=["id INTEGER PRIMARY KEY AUTOINCREMENT", "id SERIAL KEY", "id AUTO_INT", "id NUMERIC DEFAULT AUTO"],
                correct_answer="id INTEGER PRIMARY KEY AUTOINCREMENT",
                explanation="`INTEGER PRIMARY KEY AUTOINCREMENT` automatically increments row IDs in SQLite."
            ),
            QuizQuestionBlueprint(
                question="What SQL operator enables substring pattern matching (e.g. searching for '%python%')?",
                options=["LIKE", "MATCHES", "CONTAINS", "SEARCH"],
                correct_answer="LIKE",
                explanation="The `LIKE` operator matches text patterns using `%` wildcards."
            ),
            QuizQuestionBlueprint(
                question="Can a SQLite mobile database function when the smartphone has Airplane Mode turned on?",
                options=[
                    "Yes, SQLite operates completely offline with zero reliance on network connectivity.",
                    "No, SQLite requires continuous internet.",
                    "Only on Android, not iOS.",
                    "Only if plugged into a charger."
                ],
                correct_answer="Yes, SQLite operates completely offline with zero reliance on network connectivity.",
                explanation="SQLite is entirely on-device and requires no internet access."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 23
    # -------------------------------------------------------------
    DayBlueprint(
        order=23,
        title="Day 23: Offline-First Architecture & Network Sync",
        concept="Engineering resilient apps using NetInfo network detection, local caching, and optimistic UI updates",
        analogy="Think of offline-first architecture like a digital courier dispatch book. If you write down a message while driving through an underground mountain tunnel (no cell signal), the app writes it in your local notebook immediately (Optimistic Update) and places it in an outgoing outbox queue. The moment your car emerges from the tunnel into daylight, the courier automatically sends all queued messages to the cloud!",
        theory_sections=[
            {
                "heading": "The Offline-First Philosophy",
                "body": "In mobile development, network availability is a privilege, not a guarantee. An 'Offline-First' app treats the local device database as the primary source of truth for all reads and writes. Data is displayed immediately from local storage, and background sync engines synchronize changes with the cloud whenever connectivity is established."
            },
            {
                "heading": "Network State Detection & Optimistic Updates",
                "body": "Using `@react-native-community/netinfo`, apps listen to `isConnected` and `isInternetReachable` events. With **Optimistic UI Updates**, when a user taps 'Like' or 'Save Note', the UI updates instantly without waiting for a server round-trip; if the server call subsequently fails, the app rolls back or queues the action in an offline mutations table."
            }
        ],
        code_snippets=[
            {
                "title": "Monitoring Network Connectivity with NetInfo",
                "code": "import NetInfo from '@react-native-community/netinfo';\nimport { useEffect, useState } from 'react';\n\nexport const useNetworkStatus = () => {\n  const [isConnected, setIsConnected] = useState<boolean | null>(true);\n\n  useEffect(() => {\n    // Subscribe to network state updates\n    const unsubscribe = NetInfo.addEventListener(state => {\n      console.log('Connection type:', state.type);\n      console.log('Is connected?', state.isConnected);\n      setIsConnected(state.isConnected);\n    });\n    return () => unsubscribe();\n  }, []);\n\n  return isConnected;\n};"
            },
            {
                "title": "Persistent Offline Action Queue Pattern",
                "code": "// Queue pending mutations in SQLite when offline\nexport const queueOfflineAction = (actionType: string, payload: object) => {\n  db.runSync(\n    'INSERT INTO sync_queue (action_type, payload, status) VALUES (?, ?, ?)',\n    [actionType, JSON.stringify(payload), 'PENDING']\n  );\n};\n\n// Process queue when connection resumes\nexport const flushSyncQueue = async () => {\n  const pending = db.getAllSync('SELECT * FROM sync_queue WHERE status = \"PENDING\"');\n  for (const item of pending) {\n    try {\n      await sendToServer(item.action_type, JSON.parse(item.payload));\n      db.runSync('DELETE FROM sync_queue WHERE id = ?', [item.id]);\n    } catch (err) {\n      console.warn('Sync failed for item', item.id);\n    }\n  }\n};"
            },
            {
                "title": "Optimistic UI Update Implementation",
                "code": "const toggleLikeOptimistic = async (postId: string) => {\n  // 1. Update UI immediately\n  setLikes(prev => prev + 1);\n  \n  try {\n    // 2. Dispatch network call in background\n    await api.post(`/posts/${postId}/like`);\n  } catch (err) {\n    // 3. Rollback if network fails\n    setLikes(prev => prev - 1);\n    alert('Could not sync like. Please check connection.');\n  }\n};"
            },
            {
                "title": "Visual Offline Banner Component",
                "code": "const OfflineBanner = () => {\n  const isConnected = useNetworkStatus();\n  if (isConnected !== false) return null;\n  \n  return (\n    <View style={{ backgroundColor: '#EF4444', padding: 8, alignItems: 'center' }}>\n      <Text style={{ color: '#FFF', fontWeight: 'bold' }}>⚡ Offline Mode - Changes will sync when online</Text>\n    </View>\n  );\n};"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Offline Sync Queue Resolver",
            description="Write a Python function `process_sync_queue(queue, is_connected)` that empties and returns all items if is_connected is True, or returns the unchanged queue if False.",
            starter_code="def process_sync_queue(queue, is_connected):\n    # TODO: Process queue\n    pass\n",
            solution_code="def process_sync_queue(queue, is_connected):\n    if is_connected:\n        synced = list(queue)\n        queue.clear()\n        return {'synced': synced, 'remaining': []}\n    return {'synced': [], 'remaining': list(queue)}\n\nq = [{'action': 'ADD_NOTE', 'id': 1}]\nprint(process_sync_queue(q, True))",
            expected_output="{'synced': [{'action': 'ADD_NOTE', 'id': 1}], 'remaining': []}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is an 'Optimistic UI Update' in modern mobile applications?",
                options=[
                    "Updating the user interface immediately assuming the network call will succeed, and rolling back only if an error occurs.",
                    "Only showing positive reviews.",
                    "An AI algorithm that predicts what user will type.",
                    "Making the screen brighter."
                ],
                correct_answer="Updating the user interface immediately assuming the network call will succeed, and rolling back only if an error occurs.",
                explanation="Optimistic updates deliver instant zero-latency UI responsiveness."
            ),
            QuizQuestionBlueprint(
                question="What package is the community standard for inspecting mobile network connection status in React Native?",
                options=["@react-native-community/netinfo", "react-native-wifi", "react-native-network", "expo-internet"],
                correct_answer="@react-native-community/netinfo",
                explanation="`netinfo` provides real-time event listeners for network type and internet reachability."
            ),
            QuizQuestionBlueprint(
                question="In an offline-first architecture, what is treated as the primary source of truth for user data?",
                options=[
                    "The local on-device database (SQLite / local store).",
                    "The remote cloud server.",
                    "Browser cookies.",
                    "The device SIM card."
                ],
                correct_answer="The local on-device database (SQLite / local store).",
                explanation="Offline-first apps write and read locally first, synchronizing with the cloud in the background."
            ),
            QuizQuestionBlueprint(
                question="What is an 'offline sync queue'?",
                options=[
                    "A persistent table that stores user actions performed while offline so they can be dispatched when connectivity resumes.",
                    "A waiting line for app downloads.",
                    "A queue of failed push notifications.",
                    "An audio playlist."
                ],
                correct_answer="A persistent table that stores user actions performed while offline so they can be dispatched when connectivity resumes.",
                explanation="Sync queues buffer mutations until the device re-establishes a reliable connection."
            ),
            QuizQuestionBlueprint(
                question="What is a 'conflict resolution strategy' when syncing offline data with the server?",
                options=[
                    "A set of rules (like 'Last-Write-Wins' or version timestamps) determining how to merge conflicting edits made on two devices.",
                    "A method for deleting user accounts.",
                    "An antivirus scanner.",
                    "A legal agreement."
                ],
                correct_answer="A set of rules (like 'Last-Write-Wins' or version timestamps) determining how to merge conflicting edits made on two devices.",
                explanation="Conflict resolution reconciles edits made offline when synchronizing with cloud servers."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 24 (Project)
    # -------------------------------------------------------------
    DayBlueprint(
        order=24,
        title="Day 24: Offline Note-Taking Mobile App Project",
        concept="Developing a full-scale offline-first notes application with local SQLite database, category tags, and instant search",
        analogy="Think of this project like building a private leather-bound diary application for an undercover reporter. The reporter can type sensitive notes on an airplane or deep in the mountains with no signal. Every letter is saved to the local encrypted SQLite ledger, searchable in 1 millisecond, and organized by color tags!",
        theory_sections=[
            {
                "heading": "Module 5 Capstone Architecture",
                "body": "In this project, you construct a complete offline-first note-taking mobile application. You will implement: (1) SQLite database initialization on boot, (2) Creating notes with title, body, and category chips, (3) Real-time substring search using SQL `LIKE`, (4) Deleting notes, and (5) Displaying formatted creation timestamps."
            },
            {
                "heading": "Direct SQLite to FlatList Data Flow",
                "body": "Whenever a note is created or deleted, a database listener triggers a fresh `db.getAllSync()` query, immediately updating the component state and smoothly animating the `<FlatList>`."
            }
        ],
        code_snippets=[
            {
                "title": "Complete SQLite Note-Taking Application (NotesApp.tsx)",
                "code": "import React, { useState, useEffect } from 'react';\nimport {\n  View,\n  Text,\n  TextInput,\n  TouchableOpacity,\n  FlatList,\n  StyleSheet,\n  Alert\n} from 'react-native';\nimport { SafeAreaView } from 'react-native-safe-area-context';\nimport * as SQLite from 'expo-sqlite';\n\nconst db = SQLite.openDatabaseSync('notes_app.db');\n\ninterface Note {\n  id: number;\n  title: string;\n  content: string;\n  created_at: string;\n}\n\nexport const NotesScreen = () => {\n  const [notes, setNotes] = useState<Note[]>([]);\n  const [title, setTitle] = useState('');\n  const [content, setContent] = useState('');\n  const [search, setSearch] = useState('');\n\n  const refreshNotes = () => {\n    if (search.trim()) {\n      const filtered = db.getAllSync<Note>(\n        'SELECT * FROM notes WHERE title LIKE ? OR content LIKE ? ORDER BY id DESC',\n        [`%${search}%`, `%${search}%`]\n      );\n      setNotes(filtered);\n    } else {\n      const all = db.getAllSync<Note>('SELECT * FROM notes ORDER BY id DESC');\n      setNotes(all);\n    }\n  };\n\n  useEffect(() => {\n    db.execSync(`\n      CREATE TABLE IF NOT EXISTS notes (\n        id INTEGER PRIMARY KEY AUTOINCREMENT,\n        title TEXT NOT NULL,\n        content TEXT NOT NULL,\n        created_at DATETIME DEFAULT CURRENT_TIMESTAMP\n      );\n    `);\n    refreshNotes();\n  }, [search]);\n\n  const handleSave = () => {\n    if (!title.trim() || !content.trim()) {\n      Alert.alert('Validation Error', 'Title and content cannot be empty.');\n      return;\n    }\n    db.runSync('INSERT INTO notes (title, content) VALUES (?, ?)', [title, content]);\n    setTitle('');\n    setContent('');\n    refreshNotes();\n  };\n\n  const handleDelete = (id: number) => {\n    db.runSync('DELETE FROM notes WHERE id = ?', [id]);\n    refreshNotes();\n  };\n\n  return (\n    <SafeAreaView style={styles.container}>\n      <Text style={styles.header}>📝 Offline Notes Vault</Text>\n      <TextInput\n        style={styles.searchBar}\n        placeholder=\"Search notes...\"\n        placeholderTextColor=\"#94A3B8\"\n        value={search}\n        onChangeText={setSearch}\n      />\n      <View style={styles.editorBox}>\n        <TextInput\n          style={styles.inputTitle}\n          placeholder=\"Note Title\"\n          placeholderTextColor=\"#94A3B8\"\n          value={title}\n          onChangeText={setTitle}\n        />\n        <TextInput\n          style={styles.inputContent}\n          placeholder=\"Write your note here...\"\n          placeholderTextColor=\"#94A3B8\"\n          multiline\n          value={content}\n          onChangeText={setContent}\n        />\n        <TouchableOpacity style={styles.saveBtn} onPress={handleSave}>\n          <Text style={styles.saveBtnText}>Save to Vault</Text>\n        </TouchableOpacity>\n      </View>\n      <FlatList\n        data={notes}\n        keyExtractor={item => item.id.toString()}\n        renderItem={({ item }) => (\n          <View style={styles.noteCard}>\n            <View style={styles.noteHeader}>\n              <Text style={styles.noteTitle}>{item.title}</Text>\n              <TouchableOpacity onPress={() => handleDelete(item.id)}>\n                <Text style={styles.deleteText}>🗑</Text>\n              </TouchableOpacity>\n            </View>\n            <Text style={styles.noteBody}>{item.content}</Text>\n          </View>\n        )}\n      />\n    </SafeAreaView>\n  );\n};"
            },
            {
                "title": "Notes App Stylesheet (styles.ts)",
                "code": "const styles = StyleSheet.create({\n  container: { flex: 1, backgroundColor: '#0F172A', padding: 16 },\n  header: { fontSize: 24, fontWeight: '800', color: '#F8FAFC', marginBottom: 16 },\n  searchBar: { backgroundColor: '#1E293B', borderRadius: 12, padding: 12, color: '#FFF', marginBottom: 16 },\n  editorBox: { backgroundColor: '#1E293B', borderRadius: 16, padding: 16, marginBottom: 16, borderWidth: 1, borderColor: '#334155' },\n  inputTitle: { color: '#FFF', fontSize: 18, fontWeight: 'bold', marginBottom: 8, borderBottomWidth: 1, borderBottomColor: '#334155', paddingBottom: 6 },\n  inputContent: { color: '#CBD5E1', fontSize: 14, minHeight: 60, textAlignVertical: 'top' },\n  saveBtn: { backgroundColor: '#10B981', padding: 12, borderRadius: 10, alignItems: 'center', marginTop: 12 },\n  saveBtnText: { color: '#FFF', fontWeight: 'bold' },\n  noteCard: { backgroundColor: '#1E293B', borderRadius: 16, padding: 16, marginBottom: 12, borderWidth: 1, borderColor: '#334155' },\n  noteHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 },\n  noteTitle: { color: '#F8FAFC', fontSize: 16, fontWeight: 'bold' },\n  noteBody: { color: '#94A3B8', fontSize: 14, lineHeight: 20 },\n  deleteText: { fontSize: 16 }\n});"
            },
            {
                "title": "Database Repository Helper (notesDb.ts)",
                "code": "import * as SQLite from 'expo-sqlite';\n\nconst db = SQLite.openDatabaseSync('notes_app.db');\n\nexport const fetchAllNotes = () => {\n  return db.getAllSync('SELECT * FROM notes ORDER BY id DESC');\n};\n\nexport const insertNote = (title: string, content: string) => {\n  return db.runSync('INSERT INTO notes (title, content) VALUES (?, ?)', [title, content]);\n};"
            },
            {
                "title": "Note Card Component with Delete Confirmation (NoteCard.tsx)",
                "code": "import React from 'react';\nimport { View, Text, TouchableOpacity, Alert } from 'react-native';\n\nexport const NoteCard = ({ item, onDelete }: { item: any; onDelete: (id: number) => void }) => {\n  const confirmDelete = () => {\n    Alert.alert('Delete Note', 'Are you sure you want to delete this note?', [\n      { text: 'Cancel', style: 'cancel' },\n      { text: 'Delete', style: 'destructive', onPress: () => onDelete(item.id) }\n    ]);\n  };\n\n  return (\n    <View style={{ padding: 16, backgroundColor: '#1E293B', borderRadius: 12, marginBottom: 10 }}>\n      <Text style={{ color: '#FFF', fontWeight: 'bold', fontSize: 16 }}>{item.title}</Text>\n      <Text style={{ color: '#94A3B8', marginTop: 4 }}>{item.content}</Text>\n      <TouchableOpacity onPress={confirmDelete} style={{ marginTop: 8 }}>\n        <Text style={{ color: '#EF4444' }}>Delete</Text>\n      </TouchableOpacity>\n    </View>\n  );\n};"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Note Search Substring Filter",
            description="Write a function `filter_notes(notes, query)` that returns all notes where `query.lower()` is in `note['title'].lower()` or `note['content'].lower()`.",
            starter_code="def filter_notes(notes, query):\n    # TODO: Implement filter\n    pass\n",
            solution_code="def filter_notes(notes, query):\n    q = query.lower()\n    return [n for n in notes if q in n['title'].lower() or q in n['content'].lower()]\n\ndata = [\n    {'title': 'Shopping List', 'content': 'Apples, milk'},\n    {'title': 'Python Tips', 'content': 'Use list comprehensions'}\n]\nprint('Found:', len(filter_notes(data, 'python')))",
            expected_output="Found: 1"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is SQLite uniquely suited for an offline note-taking app compared to cloud databases?",
                options=[
                    "It reads and writes to local phone flash memory in microseconds without requiring cellular data or Wi-Fi.",
                    "It has unlimited cloud storage.",
                    "It renders HTML automatically.",
                    "It bypasses the operating system."
                ],
                correct_answer="It reads and writes to local phone flash memory in microseconds without requiring cellular data or Wi-Fi.",
                explanation="Local SQLite guarantees 100% offline functionality and zero-latency performance."
            ),
            QuizQuestionBlueprint(
                question="What property on `<TextInput>` allows writing multi-line text notes in React Native?",
                options=["multiline={true}", "rows={5}", "textarea={true}", "type=\"textarea\""],
                correct_answer="multiline={true}",
                explanation="`multiline={true}` enables multi-line text input with soft keyboard enter breaks."
            ),
            QuizQuestionBlueprint(
                question="What SQL statement removes a note with ID 5 from the database?",
                options=["DELETE FROM notes WHERE id = 5", "REMOVE FROM notes WHERE id = 5", "DROP ROW 5 FROM notes", "notes.delete(5)"],
                correct_answer="DELETE FROM notes WHERE id = 5",
                explanation="`DELETE FROM table WHERE condition` is standard SQL for row deletion."
            ),
            QuizQuestionBlueprint(
                question="Why is `textAlignVertical: 'top'` recommended for multi-line TextInput components on Android?",
                options=[
                    "Android centers placeholder text vertically by default inside multiline inputs; 'top' aligns it to the top edge.",
                    "To change font color.",
                    "To enable autocorrect.",
                    "It increases font size."
                ],
                correct_answer="Android centers placeholder text vertically by default inside multiline inputs; 'top' aligns it to the top edge.",
                explanation="`textAlignVertical: 'top'` pins text to the top-left on Android multi-line inputs."
            ),
            QuizQuestionBlueprint(
                question="How does the search bar trigger live filtering as the user types?",
                options=[
                    "By binding `search` to the `useEffect` dependency array so `refreshNotes()` re-executes on each keystroke.",
                    "By restarting the phone.",
                    "Using CSS animations.",
                    "By calling window.reload()."
                ],
                correct_answer="By binding `search` to the `useEffect` dependency array so `refreshNotes()` re-executes on each keystroke.",
                explanation="Re-running the query when `search` updates provides instantaneous live filtering."
            )
        ],
        is_project_day=True,
        project_name="Offline Note-Taking Mobile App"
    ),

    # -------------------------------------------------------------
    # DAY 25
    # -------------------------------------------------------------
    DayBlueprint(
        order=25,
        title="Day 25: Mobile Permissions (Camera, Location, Media)",
        concept="Requesting and managing user permissions at runtime on Android and iOS",
        analogy="Think of mobile app permissions like a security badge checkpoint at a secure facility. If an app wants to peek through your camera lens or see your exact GPS coordinates, the phone's operating system stops the app at the door, displays an official popup, and asks you directly: 'Do you grant this app permission to use your camera?'",
        theory_sections=[
            {
                "heading": "Runtime Permissions vs Manifest Declarations",
                "body": "Modern mobile operating systems enforce strict privacy guards. You cannot simply access hardware; you must: (1) Declare the permission in the platform manifest (`AndroidManifest.xml` and iOS `Info.plist`), and (2) Request permission from the user dynamically at runtime."
            },
            {
                "heading": "The Permission State Lifecycle",
                "body": "Permissions have three states: **Undetermined** (never asked), **Granted** (user approved), and **Denied** (user rejected). If denied, apps should explain why the permission is needed and gracefully offer manual 'Open Settings' fallback links."
            }
        ],
        code_snippets=[
            {
                "title": "Requesting Camera Permissions with Expo",
                "code": "import { Camera } from 'expo-camera';\nimport { useState, useEffect } from 'react';\nimport { View, Text, Button, Linking } from 'react-native';\n\nconst CameraGuard = () => {\n  const [permission, requestPermission] = Camera.useCameraPermissions();\n\n  if (!permission) {\n    return <Text>Loading permissions...</Text>;\n  }\n\n  if (!permission.granted) {\n    return (\n      <View style={{ padding: 20, alignItems: 'center' }}>\n        <Text>We need your permission to access the camera.</Text>\n        <Button title=\"Grant Camera Permission\" onPress={requestPermission} />\n        {permission.canAskAgain === false && (\n          <Button title=\"Open System Settings\" onPress={() => Linking.openSettings()} />\n        )}\n      </View>\n    );\n  }\n\n  return <Text>Camera access granted! Ready to scan.</Text>;\n};"
            },
            {
                "title": "Declaring iOS Info.plist Purpose Strings (app.json)",
                "code": "{\n  \"expo\": {\n    \"plugins\": [\n      [\n        \"expo-camera\",\n        {\n          \"cameraPermission\": \"Allow Hunar Cycle to access your camera to scan QR codes.\"\n        }\n      ]\n    ]\n  }\n}"
            },
            {
                "title": "Requesting Media Library Permissions",
                "code": "import * as ImagePicker from 'expo-image-picker';\n\nconst requestGalleryAccess = async () => {\n  const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();\n  return status === 'granted';\n};"
            },
            {
                "title": "Handling Permission Denied Gracefully",
                "code": "const verifyPermission = async () => {\n  const hasAccess = await requestGalleryAccess();\n  if (!hasAccess) {\n    alert('Permission required: Please enable photo gallery access in system settings.');\n    return false;\n  }\n  return true;\n};"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Permission Gate Checker",
            description="Write a function `check_permission_gate(status_string)` that returns True if status is 'granted', False if 'denied', and raises ValueError('Invalid status') otherwise.",
            starter_code="def check_permission_gate(status):\n    # TODO: Validate permission\n    pass\n",
            solution_code="def check_permission_gate(status):\n    if status == 'granted':\n        return True\n    elif status == 'denied':\n        return False\n    raise ValueError('Invalid status')\n\nprint('Granted:', check_permission_gate('granted'))\nprint('Denied:', check_permission_gate('denied'))",
            expected_output="Granted: True\nDenied: False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why will Apple immediately reject an iOS app submission that attempts to access the camera without an `NSCameraUsageDescription` string in `Info.plist`?",
                options=[
                    "Apple requires an explicit user-facing explanation in Info.plist describing why the application needs camera access.",
                    "Because iOS does not allow cameras.",
                    "Apple requires AndroidManifest.xml instead.",
                    "Only Swift apps can use the camera."
                ],
                correct_answer="Apple requires an explicit user-facing explanation in Info.plist describing why the application needs camera access.",
                explanation="Privacy usage descriptions explain why hardware access is needed before prompting users."
            ),
            QuizQuestionBlueprint(
                question="What method opens the native device system settings screen if a user permanently denied permissions?",
                options=["Linking.openSettings()", "Device.openSettings()", "System.permissions()", "Platform.settings()"],
                correct_answer="Linking.openSettings()",
                explanation="`Linking.openSettings()` takes users directly to their app's system settings toggle page."
            ),
            QuizQuestionBlueprint(
                question="When should an app request sensitive permissions like Location or Camera?",
                options=[
                    "Contextually, right when the user taps a feature that requires it (e.g. tapping 'Take Photo'), rather than upon initial app launch.",
                    "Immediately during splash screen loading.",
                    "Every 5 minutes automatically.",
                    "Only after uninstallation."
                ],
                correct_answer="Contextually, right when the user taps a feature that requires it (e.g. tapping 'Take Photo'), rather than upon initial app launch.",
                explanation="Contextual permission requests achieve much higher user approval rates."
            ),
            QuizQuestionBlueprint(
                question="What does `permission.canAskAgain === false` indicate on Android?",
                options=[
                    "The user selected 'Don't ask again'; subsequent programmatic prompts will be silently ignored by the OS.",
                    "The phone camera is broken.",
                    "The user granted root access.",
                    "The app is in offline mode."
                ],
                correct_answer="The user selected 'Don't ask again'; subsequent programmatic prompts will be silently ignored by the OS.",
                explanation="When 'Don't ask again' is toggled, apps must guide the user to manually enable it in Settings."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between foreground location permission and background location permission?",
                options=[
                    "Foreground location tracks only while the app is actively on screen; background location tracks even when the screen is locked or another app is open.",
                    "Foreground location is free; background costs money.",
                    "Background location only works on tablets.",
                    "There is no difference."
                ],
                correct_answer="Foreground location tracks only while the app is actively on screen; background location tracks even when the screen is locked or another app is open.",
                explanation="Background tracking has strict battery and privacy audits due to tracking while minimized."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 26
    # -------------------------------------------------------------
    DayBlueprint(
        order=26,
        title="Day 26: Camera & Photo Gallery Integration",
        concept="Capturing photos, selecting media from photo galleries, and image compression with expo-image-picker",
        analogy="Think of camera integration like equipping your mobile app with a personal photographer and photo album. With a single tap, the app can open the camera shutter to take a fresh photo (`launchCameraAsync`), or open the user's photo album (`launchImageLibraryAsync`) to pick an avatar image!",
        theory_sections=[
            {
                "heading": "Image Capture vs Gallery Selection",
                "body": "Mobile apps frequently require image uploads for avatars, verification IDs, or receipts. The `expo-image-picker` library provides unified cross-platform methods: `launchCameraAsync()` to open the device camera, and `launchImageLibraryAsync()` to let users browse their photo album."
            },
            {
                "heading": "Image Resizing and Quality Compression",
                "body": "Modern smartphone cameras take photos that are 12 to 48 Megapixels in size (5MB to 15MB each). Uploading full-resolution photos over cellular data burns battery and bandwidth. Always compress images using `quality: 0.7` and restrict maximum dimensions using `allowsEditing: true`."
            }
        ],
        code_snippets=[
            {
                "title": "Picking an Image from Photo Gallery",
                "code": "import * as ImagePicker from 'expo-image-picker';\nimport { useState } from 'react';\nimport { View, Image, TouchableOpacity, Text } from 'react-native';\n\nconst PhotoPicker = () => {\n  const [imageUri, setImageUri] = useState<string | null>(null);\n\n  const pickImage = async () => {\n    const result = await ImagePicker.launchImageLibraryAsync({\n      mediaTypes: ImagePicker.MediaTypeOptions.Images,\n      allowsEditing: true,\n      aspect: [1, 1], // Square crop for profile avatar\n      quality: 0.7,   // Compress to 70% quality\n    });\n\n    if (!result.canceled) {\n      setImageUri(result.assets[0].uri);\n    }\n  };\n\n  return (\n    <View>\n      {imageUri && <Image source={{ uri: imageUri }} style={{ width: 120, height: 120, borderRadius: 60 }} />}\n      <TouchableOpacity onPress={pickImage}><Text>Select Photo</Text></TouchableOpacity>\n    </View>\n  );\n};"
            },
            {
                "title": "Capturing a Photo with Device Camera",
                "code": "const takePhoto = async () => {\n  const { status } = await ImagePicker.requestCameraPermissionsAsync();\n  if (status !== 'granted') return;\n\n  const result = await ImagePicker.launchCameraAsync({\n    allowsEditing: true,\n    quality: 0.8,\n  });\n\n  if (!result.canceled) {\n    const photoUri = result.assets[0].uri;\n    console.log('Captured photo saved at:', photoUri);\n  }\n};"
            },
            {
                "title": "Preparing Image for Multipart Form Upload",
                "code": "const uploadPhoto = async (uri: string) => {\n  const formData = new FormData();\n  const filename = uri.split('/').pop() || 'photo.jpg';\n  \n  formData.append('avatar', {\n    uri,\n    name: filename,\n    type: 'image/jpeg'\n  } as any);\n\n  await fetch('http://192.168.18.62:5000/api/upload', {\n    method: 'POST',\n    body: formData\n  });\n};"
            },
            {
                "title": "Camera Action Sheet Dialog",
                "code": "import { ActionSheetIOS, Platform, Alert } from 'react-native';\n\nconst showImageOptions = (onCamera: () => void, onGallery: () => void) => {\n  Alert.alert(\n    'Upload Avatar',\n    'Choose image source',\n    [\n      { text: 'Take Photo', onPress: onCamera },\n      { text: 'Choose from Gallery', onPress: onGallery },\n      { text: 'Cancel', style: 'cancel' }\n    ]\n  );\n};"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Image URI Filename Extractor",
            description="Write a function `extract_filename(file_uri)` that extracts the last segment of a path (e.g. 'file:///var/mobile/photo_42.jpg' -> 'photo_42.jpg').",
            starter_code="def extract_filename(file_uri):\n    # TODO: Extract filename\n    pass\n",
            solution_code="def extract_filename(file_uri):\n    return file_uri.split('/')[-1]\n\nprint('Extracted:', extract_filename('file:///data/img_001.png'))",
            expected_output="Extracted: img_001.png"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What method in `expo-image-picker` opens the device camera shutter to snap a new photo?",
                options=["launchCameraAsync()", "openCamera()", "takeSnapshot()", "camera.capture()"],
                correct_answer="launchCameraAsync()",
                explanation="`ImagePicker.launchCameraAsync()` launches the platform camera application."
            ),
            QuizQuestionBlueprint(
                question="Why is setting `quality: 0.7` in ImagePicker settings recommended before uploading to backends?",
                options=[
                    "It drastically reduces image byte size while maintaining excellent visual sharpness, saving user cellular bandwidth.",
                    "It converts black-and-white photos to color.",
                    "It encrypts the image.",
                    "It adds a watermark."
                ],
                correct_answer="It drastically reduces image byte size while maintaining excellent visual sharpness, saving user cellular bandwidth.",
                explanation="Compression reduces multi-megabyte camera photos down to a few hundred kilobytes."
            ),
            QuizQuestionBlueprint(
                question="What property in ImagePicker options enables the built-in native crop and square alignment tool?",
                options=["allowsEditing: true", "crop: true", "square: true", "enableEdit: true"],
                correct_answer="allowsEditing: true",
                explanation="`allowsEditing: true` presents native cropping tools after photo selection."
            ),
            QuizQuestionBlueprint(
                question="How does React Native represent uploaded files inside `FormData`?",
                options=[
                    "An object containing `{ uri, name, type }`.",
                    "A raw binary ArrayBuffer.",
                    "A base64 string only.",
                    "A file path string."
                ],
                correct_answer="An object containing `{ uri, name, type }`.",
                explanation="React Native's FormData polyfill expects `{ uri, name, type }` for file uploads."
            ),
            QuizQuestionBlueprint(
                question="What property on the ImagePicker result indicates if the user exited without choosing a photo?",
                options=["result.canceled === true", "result.empty === true", "result.aborted === true", "result.failed === true"],
                correct_answer="result.canceled === true",
                explanation="`result.canceled` is a boolean flag indicating if the picker was dismissed."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 27
    # -------------------------------------------------------------
    DayBlueprint(
        order=27,
        title="Day 27: Geolocation & Interactive Maps",
        concept="Accessing GPS coordinates with expo-location and rendering interactive MapView markers",
        analogy="Think of GPS and maps like having a live compass and navigator on your dashboard. The compass hardware inside the phone measures your exact latitude and longitude (`expo-location`). The map renderer (`react-native-maps`) takes those coordinates and draws a visual street map with a pinpoint marker showing your exact location!",
        theory_sections=[
            {
                "heading": "Reading GPS Coordinates",
                "body": "Mobile devices combine satellite GPS, Wi-Fi triangulation, and cellular cell towers to calculate precise geographical coordinates (`latitude` and `longitude`). Using `expo-location`, you request location permissions and call `Location.getCurrentPositionAsync({})`."
            },
            {
                "heading": "Rendering Interactive Maps with react-native-maps",
                "body": "Using `react-native-maps`, you render a native Google Maps (Android) or Apple Maps (iOS) canvas with `<MapView>`. You center the viewport using `initialRegion` with delta zoom levels, and render interactive point-of-interest markers using `<Marker>`."
            }
        ],
        code_snippets=[
            {
                "title": "Fetching Device GPS Coordinates (useLocation.ts)",
                "code": "import * as Location from 'expo-location';\nimport { useState, useEffect } from 'react';\n\nexport const useCurrentLocation = () => {\n  const [coords, setCoords] = useState<{ lat: number; lng: number } | null>(null);\n\n  useEffect(() => {\n    (async () => {\n      const { status } = await Location.requestForegroundPermissionsAsync();\n      if (status !== 'granted') return;\n\n      const location = await Location.getCurrentPositionAsync({\n        accuracy: Location.Accuracy.High\n      });\n      setCoords({\n        lat: location.coords.latitude,\n        lng: location.coords.longitude\n      });\n    })();\n  }, []);\n\n  return coords;\n};"
            },
            {
                "title": "Rendering MapView with Markers",
                "code": "import MapView, { Marker } from 'react-native-maps';\nimport { View, StyleSheet } from 'react-native';\n\nconst CampusMap = ({ lat, lng }: { lat: number; lng: number }) => (\n  <View style={styles.container}>\n    <MapView\n      style={styles.map}\n      initialRegion={{\n        latitude: lat,\n        longitude: lng,\n        latitudeDelta: 0.01,  // Zoom level\n        longitudeDelta: 0.01,\n      }}\n    >\n      <Marker\n        coordinate={{ latitude: lat, longitude: lng }}\n        title=\"Hunar Cycle Tech Hub\"\n        description=\"Main Innovation Campus\"\n      />\n    </MapView>\n  </View>\n);\n\nconst styles = StyleSheet.create({\n  container: { flex: 1 },\n  map: { width: '100%', height: '100%' }\n});"
            },
            {
                "title": "Reverse Geocoding: Coordinates to Street Address",
                "code": "const getAddressFromCoords = async (lat: number, lng: number) => {\n  // Converts latitude/longitude into human-readable city and street address\n  const addresses = await Location.reverseGeocodeAsync({ latitude: lat, longitude: lng });\n  if (addresses.length > 0) {\n    const item = addresses[0];\n    return `${item.street}, ${item.city}, ${item.country}`;\n  }\n  return 'Unknown Location';\n};"
            },
            {
                "title": "Subscribing to Live Location Tracking",
                "code": "// Watches position changes as the user walks or drives\nconst subscription = await Location.watchPositionAsync(\n  { accuracy: Location.Accuracy.High, distanceInterval: 10 }, // Every 10 meters\n  (newLocation) => {\n    console.log('Updated location:', newLocation.coords);\n  }\n);"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Haversine Distance Calculator",
            description="Write a Python function `haversine_distance(lat1, lon1, lat2, lon2)` that calculates the straight-line distance in kilometers between two GPS coordinates.",
            starter_code="import math\n\ndef haversine_distance(lat1, lon1, lat2, lon2):\n    # TODO: Calculate distance in KM\n    pass\n",
            solution_code="import math\n\ndef haversine_distance(lat1, lon1, lat2, lon2):\n    R = 6371 # Earth radius in KM\n    dLat = math.radians(lat2 - lat1)\n    dLon = math.radians(lon2 - lon1)\n    a = math.sin(dLat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon/2)**2\n    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))\n    return round(R * c, 2)\n\nprint('Dist KM:', haversine_distance(33.738045, 73.084488, 33.684422, 73.047882))",
            expected_output="Dist KM: 6.95"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What method in `expo-location` fetches the current GPS position of the mobile device?",
                options=["getCurrentPositionAsync()", "getLocation()", "getGPS()", "readCoordinates()"],
                correct_answer="getCurrentPositionAsync()",
                explanation="`Location.getCurrentPositionAsync({})` requests high-accuracy coordinates from device hardware."
            ),
            QuizQuestionBlueprint(
                question="What is 'Reverse Geocoding'?",
                options=[
                    "Converting numeric GPS coordinates (latitude, longitude) into a human-readable street address and city.",
                    "Converting text to speech.",
                    "Rotating a map upside-down.",
                    "Driving backwards."
                ],
                correct_answer="Converting numeric GPS coordinates (latitude, longitude) into a human-readable street address and city.",
                explanation="Reverse geocoding resolves coordinates into addresses; forward geocoding converts addresses into coordinates."
            ),
            QuizQuestionBlueprint(
                question="What parameters control the initial zoom level of a `<MapView>` in react-native-maps?",
                options=["latitudeDelta and longitudeDelta", "zoomLevel", "magnification", "scaleRatio"],
                correct_answer="latitudeDelta and longitudeDelta",
                explanation="`latitudeDelta` and `longitudeDelta` define the coordinate span visible on screen (smaller values = closer zoom)."
            ),
            QuizQuestionBlueprint(
                question="What component places a pin on a `MapView` canvas?",
                options=["<Marker>", "<Pin>", "<LocationDot>", "<Point>"],
                correct_answer="<Marker>",
                explanation="`<Marker coordinate={{ latitude, longitude }} />` renders a point-of-interest pin."
            ),
            QuizQuestionBlueprint(
                question="Why should apps use `requestForegroundPermissionsAsync` instead of background location unless strictly necessary?",
                options=[
                    "Background tracking drains significant battery and undergoes strict Apple/Google privacy compliance scrutiny.",
                    "Foreground location is free.",
                    "Background location does not work on Android.",
                    "Phones overheat immediately."
                ],
                correct_answer="Background tracking drains significant battery and undergoes strict Apple/Google privacy compliance scrutiny.",
                explanation="Foreground location covers 95% of use cases without aggressive battery drain or store rejection risks."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 28
    # -------------------------------------------------------------
    DayBlueprint(
        order=28,
        title="Day 28: Device Sensors & Biometric Authentication",
        concept="Unlocking apps with FaceID / Fingerprint via expo-local-authentication and reading Accelerometer data",
        analogy="Think of biometric authentication like having a trusted palace guard who knows your face and fingerprint. Instead of making you remember a 20-character secret password every time you want to open your banking app, the guard looks at your face (`FaceID`) or checks your thumb (`Fingerprint`) and swings open the vault door in 200 milliseconds!",
        theory_sections=[
            {
                "heading": "Biometric Authentication with LocalAuthentication",
                "body": "Modern smartphones feature hardware-secured biometric chips (Secure Enclave on iOS and Trusted Execution Environment on Android). The `expo-local-authentication` library lets apps authenticate users via TouchID, FaceID, or Android BiometricPrompt without ever exposing raw biometric fingerprints to your JavaScript code."
            },
            {
                "heading": "Mobile Hardware Sensors",
                "body": "Smartphones contain physical sensors: the **Accelerometer** (measures acceleration and device tilt), the **Gyroscope** (measures rotation rate), and the **Magnetometer** (compass). Using `expo-sensors`, apps can build shake-to-report features, step counters, and motion-based controls."
            }
        ],
        code_snippets=[
            {
                "title": "Authenticating with Biometrics (BiometricAuth.ts)",
                "code": "import * as LocalAuthentication from 'expo-local-authentication';\n\nexport const authenticateWithBiometrics = async (): Promise<boolean> => {\n  // 1. Check if hardware supports biometrics\n  const hasHardware = await LocalAuthentication.hasHardwareAsync();\n  const isEnrolled = await LocalAuthentication.isEnrolledAsync();\n  \n  if (!hasHardware || !isEnrolled) {\n    console.warn('Biometric hardware not available or not enrolled');\n    return false;\n  }\n\n  // 2. Prompt user with native biometric dialog\n  const result = await LocalAuthentication.authenticateAsync({\n    promptMessage: 'Unlock Hunar Cycle with Biometrics',\n    fallbackLabel: 'Use Passcode',\n    cancelLabel: 'Cancel'\n  });\n\n  return result.success;\n};"
            },
            {
                "title": "Biometric Login Button Component",
                "code": "const BiometricLoginBtn = ({ onLoginSuccess }: { onLoginSuccess: () => void }) => (\n  <TouchableOpacity \n    style={styles.bioBtn} \n    onPress={async () => {\n      const success = await authenticateWithBiometrics();\n      if (success) onLoginSuccess();\n    }}\n  >\n    <Text style={styles.bioIcon}>👆</Text>\n    <Text style={styles.bioText}>Sign In with Face ID / Fingerprint</Text>\n  </TouchableOpacity>\n);"
            },
            {
                "title": "Listening to Accelerometer Motion Data",
                "code": "import { Accelerometer } from 'expo-sensors';\nimport { useEffect, useState } from 'react';\n\nexport const useShakeDetector = (onShake: () => void) => {\n  useEffect(() => {\n    Accelerometer.setUpdateInterval(100); // 100ms interval\n    const subscription = Accelerometer.addListener(({ x, y, z }) => {\n      const acceleration = Math.sqrt(x * x + y * y + z * z);\n      if (acceleration > 2.5) { // Threshold for vigorous shake\n        onShake();\n      }\n    });\n    return () => subscription.remove();\n  }, [onShake]);\n};"
            },
            {
                "title": "Checking Enrolled Biometric Types",
                "code": "const checkTypes = async () => {\n  const types = await LocalAuthentication.supportedAuthenticationTypesAsync();\n  // 1 = FINGERPRINT, 2 = FACIAL_RECOGNITION, 3 = IRIS\n  console.log('Supported biometric types:', types);\n};"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Shake Acceleration Calculator",
            description="Write a Python function `is_shake(x, y, z, threshold=2.5)` that calculates vector magnitude `math.sqrt(x**2 + y**2 + z**2)` and returns True if magnitude exceeds threshold.",
            starter_code="import math\n\ndef is_shake(x, y, z, threshold=2.5):\n    # TODO: Calculate magnitude\n    pass\n",
            solution_code="import math\n\ndef is_shake(x, y, z, threshold=2.5):\n    magnitude = math.sqrt(x**2 + y**2 + z**2)\n    return magnitude > threshold\n\nprint('Vigorous Shake:', is_shake(1.8, 2.0, 1.5))",
            expected_output="Vigorous Shake: True"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Does `expo-local-authentication` expose the user's raw fingerprint or face image to your JavaScript code?",
                options=[
                    "No; the biometric check is handled entirely by the phone's hardware Secure Enclave, returning only a verified boolean result.",
                    "Yes, it returns a JPEG file of the face.",
                    "Yes, as a base64 fingerprint.",
                    "Only on Android."
                ],
                correct_answer="No; the biometric check is handled entirely by the phone's hardware Secure Enclave, returning only a verified boolean result.",
                explanation="Operating systems never expose raw biometric data to third-party code for security reasons."
            ),
            QuizQuestionBlueprint(
                question="What method verifies if the user has actually enrolled at least one fingerprint or face on their device?",
                options=["LocalAuthentication.isEnrolledAsync()", "LocalAuthentication.hasFingerprint()", "LocalAuthentication.userEnrolled()", "LocalAuthentication.isReady()"],
                correct_answer="LocalAuthentication.isEnrolledAsync()",
                explanation="`isEnrolledAsync()` confirms that biometric credentials are configured on the device."
            ),
            QuizQuestionBlueprint(
                question="What method launches the native FaceID / Fingerprint dialog prompt?",
                options=["LocalAuthentication.authenticateAsync(options)", "LocalAuthentication.scan()", "LocalAuthentication.prompt()", "LocalAuthentication.unlock()"],
                correct_answer="LocalAuthentication.authenticateAsync(options)",
                explanation="`authenticateAsync()` displays the platform biometric prompt."
            ),
            QuizQuestionBlueprint(
                question="What mobile sensor measures device acceleration and physical orientation in 3-dimensional space (X, Y, Z)?",
                options=["Accelerometer", "Barometer", "Thermometer", "Proximity Sensor"],
                correct_answer="Accelerometer",
                explanation="The accelerometer detects movement, tilt, and shake gestures along 3 axes."
            ),
            QuizQuestionBlueprint(
                question="What sensor measures the rate of rotation around the device's physical axes?",
                options=["Gyroscope", "Pedometer", "Microphone", "Photometer"],
                correct_answer="Gyroscope",
                explanation="The gyroscope measures angular velocity and device orientation changes."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 29
    # -------------------------------------------------------------
    DayBlueprint(
        order=29,
        title="Day 29: Backend-as-a-Service with Firebase Authentication",
        concept="Integrating cloud authentication: Email/Password, Google Sign-In, and Phone OTP verification",
        analogy="Think of Backend-as-a-Service (BaaS) like hiring a 5-star hotel concierge service instead of building your own hotel from scratch. Instead of spending 3 months building database servers, password reset emails, SMS verification codes, and Google OAuth tokens, Firebase provides an instant cloud engine that handles all authentication securely!",
        theory_sections=[
            {
                "heading": "The BaaS Paradigm for Rapid Mobile Development",
                "body": "Building a custom authentication backend requires managing servers, email verification, SMS gateways, and security audits. Backend-as-a-Service (BaaS) platforms like **Google Firebase** provide turnkey cloud backends that integrate directly into React Native via the official `@react-native-firebase` or modular Firebase JS SDK."
            },
            {
                "heading": "Email, Social, and Phone OTP Workflows",
                "body": "Firebase supports multiple identity providers: (1) Email and password (`createUserWithEmailAndPassword`), (2) Social Sign-In (Google and Apple), and (3) Phone number verification with SMS OTP codes. Firebase returns a persistent user object with automatic JWT token refresh."
            }
        ],
        code_snippets=[
            {
                "title": "Initializing Modular Firebase (firebaseConfig.ts)",
                "code": "import { initializeApp } from 'firebase/app';\nimport { initializeAuth, getReactNativePersistence } from 'firebase/auth';\nimport AsyncStorage from '@react-native-async-storage/async-storage';\n\nconst firebaseConfig = {\n  apiKey: 'AIzaSyA...', \n  authDomain: 'hunar-cycle.firebaseapp.com',\n  projectId: 'hunar-cycle',\n  storageBucket: 'hunar-cycle.appspot.com'\n};\n\nconst app = initializeApp(firebaseConfig);\n// Initialize Auth with AsyncStorage persistence so users stay logged in!\nexport const auth = initializeAuth(app, {\n  persistence: getReactNativePersistence(AsyncStorage)\n});"
            },
            {
                "title": "User Registration with Email & Password",
                "code": "import { createUserWithEmailAndPassword, signInWithEmailAndPassword } from 'firebase/auth';\n\nexport const registerUser = async (email: string, pass: string) => {\n  try {\n    const credential = await createUserWithEmailAndPassword(auth, email, pass);\n    console.log('Registered user UID:', credential.user.uid);\n    return credential.user;\n  } catch (error: any) {\n    alert(error.message);\n  }\n};"
            },
            {
                "title": "Listening to Global Auth State Changes (onAuthStateChanged)",
                "code": "import { onAuthStateChanged, User } from 'firebase/auth';\nimport { useEffect, useState } from 'react';\n\nexport const useFirebaseAuth = () => {\n  const [user, setUser] = useState<User | null>(null);\n  const [loading, setLoading] = useState(true);\n\n  useEffect(() => {\n    // Automatically triggers on login, logout, or token refresh!\n    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {\n      setUser(currentUser);\n      setLoading(false);\n    });\n    return () => unsubscribe();\n  }, []);\n\n  return { user, loading };\n};"
            },
            {
                "title": "Signing Out",
                "code": "import { signOut } from 'firebase/auth';\n\nconst handleSignOut = async () => {\n  await signOut(auth);\n};"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Firebase Error Code Formatter",
            description="Write a Python helper `format_firebase_auth_error(code)` that maps `'auth/email-already-in-use'` to 'Email already registered', `'auth/wrong-password'` to 'Invalid password', and returns 'Authentication failed' for others.",
            starter_code="def format_firebase_auth_error(code):\n    # TODO: Map error codes\n    pass\n",
            solution_code="def format_firebase_auth_error(code):\n    mapping = {\n        'auth/email-already-in-use': 'Email already registered',\n        'auth/wrong-password': 'Invalid password',\n        'auth/user-not-found': 'Account does not exist'\n    }\n    return mapping.get(code, 'Authentication failed')\n\nprint(format_firebase_auth_error('auth/email-already-in-use'))",
            expected_output="Email already registered"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What Firebase Auth method listens reactively to user login, logout, and token expiration events?",
                options=["onAuthStateChanged(auth, (user) => ...)", "onUserUpdate()", "listenAuth()", "auth.subscribe()"],
                correct_answer="onAuthStateChanged(auth, (user) => ...)",
                explanation="`onAuthStateChanged` is the canonical observer that triggers whenever the session changes."
            ),
            QuizQuestionBlueprint(
                question="Why must `getReactNativePersistence(AsyncStorage)` be passed to Firebase Auth initialization in React Native?",
                options=[
                    "React Native has no browser `localStorage`; AsyncStorage is required to persist login tokens across mobile app restarts.",
                    "Firebase cannot run on mobile without it.",
                    "To enable push notifications.",
                    "To compress the database."
                ],
                correct_answer="React Native has no browser `localStorage`; AsyncStorage is required to persist login tokens across mobile app restarts.",
                explanation="Mobile lacks browser storage; AsyncStorage provides the persistence layer for tokens."
            ),
            QuizQuestionBlueprint(
                question="What unique identifier does Firebase generate for every registered user account?",
                options=["UID (User ID string)", "Email hash", "Phone serial", "Social security number"],
                correct_answer="UID (User ID string)",
                explanation="`user.uid` is the unique 28-character identifier assigned to each Firebase user."
            ),
            QuizQuestionBlueprint(
                question="What method signs out the currently authenticated user in Firebase?",
                options=["signOut(auth)", "auth.logout()", "auth.disconnect()", "deleteSession()"],
                correct_answer="signOut(auth)",
                explanation="`signOut(auth)` purges the active session from device storage."
            ),
            QuizQuestionBlueprint(
                question="What method registers a new user with email and password in Firebase v9+ modular SDK?",
                options=["createUserWithEmailAndPassword(auth, email, password)", "auth.register(email, password)", "signUp(auth, email)", "newAccount()"],
                correct_answer="createUserWithEmailAndPassword(auth, email, password)",
                explanation="`createUserWithEmailAndPassword` creates the account and signs the user in."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 30
    # -------------------------------------------------------------
    DayBlueprint(
        order=30,
        title="Day 30: Cloud Firestore & Realtime Database",
        concept="Storing NoSQL documents, collections, and establishing real-time cloud listeners with onSnapshot",
        analogy="Think of Cloud Firestore like a digital collaborative whiteboard in the cloud. Instead of you having to ask the server every 5 seconds 'Did anyone write a new message?', you leave a walkie-talkie open (`onSnapshot`). The exact millisecond anyone in the world writes a new post, the whiteboard pushes the new text straight to your phone screen instantly!",
        theory_sections=[
            {
                "heading": "Cloud Firestore NoSQL Architecture",
                "body": "Cloud Firestore is a flexible, scalable NoSQL cloud database. Data is organized into **Collections** (like folders) containing **Documents** (JSON records). Unlike relational SQL tables with rigid columns, Firestore documents can contain arbitrary nested fields, arrays, and subcollections."
            },
            {
                "heading": "Real-Time Synchronization with onSnapshot",
                "body": "The defining superpower of Firestore is real-time synchronization. Instead of one-time `getDoc()` queries, you attach an `onSnapshot()` listener. When data changes in the cloud, Firestore immediately pushes a delta snapshot to all listening mobile devices over a persistent WebSocket connection."
            }
        ],
        code_snippets=[
            {
                "title": "Adding Documents to a Firestore Collection",
                "code": "import { getFirestore, collection, addDoc, serverTimestamp } from 'firebase/firestore';\n\nconst db = getFirestore();\n\nexport const postMessage = async (text: string, username: string) => {\n  await addDoc(collection(db, 'chat_messages'), {\n    text,\n    author: username,\n    createdAt: serverTimestamp()\n  });\n  console.log('Message saved to cloud!');\n};"
            },
            {
                "title": "Subscribing to Real-Time Updates with onSnapshot",
                "code": "import { query, orderBy, onSnapshot } from 'firebase/firestore';\nimport { useEffect, useState } from 'react';\n\nexport const useLiveMessages = () => {\n  const [messages, setMessages] = useState([]);\n\n  useEffect(() => {\n    const q = query(collection(db, 'chat_messages'), orderBy('createdAt', 'desc'));\n    \n    // Subscribes to live cloud changes!\n    const unsubscribe = onSnapshot(q, (snapshot) => {\n      const items = snapshot.docs.map(doc => ({\n        id: doc.id,\n        ...doc.data()\n      }));\n      setMessages(items);\n    });\n\n    return () => unsubscribe();\n  }, []);\n\n  return messages;\n};"
            },
            {
                "title": "Updating and Deleting Cloud Documents",
                "code": "import { doc, updateDoc, deleteDoc } from 'firebase/firestore';\n\n// Update specific document by ID\nconst updateTitle = async (docId: string, newTitle: string) => {\n  const docRef = doc(db, 'chat_messages', docId);\n  await updateDoc(docRef, { title: newTitle });\n};\n\n// Delete document\nconst deleteMessage = async (docId: string) => {\n  await deleteDoc(doc(db, 'chat_messages', docId));\n};"
            },
            {
                "title": "Firestore Offline Persistence",
                "code": "// Firestore automatically caches documents locally on device disk!\n// Reads and writes succeed even when offline and sync when online."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Firestore Document Snapshot Unpacker",
            description="Write a Python helper `unpack_firestore_snapshot(docs_list)` that converts a list of mock doc dicts `[{'id': str, 'data': dict}]` into flattened dicts `[{'id': str, **data}]`.",
            starter_code="def unpack_firestore_snapshot(docs_list):\n    # TODO: Flatten documents\n    pass\n",
            solution_code="def unpack_firestore_snapshot(docs_list):\n    return [{'id': d['id'], **d['data']} for d in docs_list]\n\nmock_docs = [{'id': 'doc_1', 'data': {'text': 'Hello', 'likes': 5}}]\nprint(unpack_firestore_snapshot(mock_docs))",
            expected_output="[{'id': 'doc_1', 'text': 'Hello', 'likes': 5}]"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What method in Cloud Firestore listens to real-time database modifications as they happen?",
                options=["onSnapshot()", "subscribe()", "listenDoc()", "watch()"],
                correct_answer="onSnapshot()",
                explanation="`onSnapshot(query, callback)` establishes a real-time data listener."
            ),
            QuizQuestionBlueprint(
                question="How is data structured hierarchically in Cloud Firestore?",
                options=[
                    "Collections containing Documents, which can contain Subcollections.",
                    "SQL Tables containing Rows and Columns.",
                    "A single flat JSON file.",
                    "CSV spreadsheets."
                ],
                correct_answer="Collections containing Documents, which can contain Subcollections.",
                explanation="Firestore organizes NoSQL data into Collections and Documents."
            ),
            QuizQuestionBlueprint(
                question="Why is `serverTimestamp()` preferred over device `Date.now()` when saving timestamps to Firestore?",
                options=[
                    "It uses the cloud server's synchronized clock, preventing inaccurate timestamps caused by incorrect device clocks.",
                    "It saves battery.",
                    "It converts to Roman numerals.",
                    "Device time is not supported."
                ],
                correct_answer="It uses the cloud server's synchronized clock, preventing inaccurate timestamps caused by incorrect device clocks.",
                explanation="`serverTimestamp()` ensures consistent chronological sorting regardless of client time errors."
            ),
            QuizQuestionBlueprint(
                question="What does calling the returned function from `onSnapshot()` do?",
                options=[
                    "It unsubscribes the listener and closes the real-time stream to conserve device memory and bandwidth.",
                    "It deletes the collection.",
                    "It restarts the app.",
                    "It prints the document to PDF."
                ],
                correct_answer="It unsubscribes the listener and closes the real-time stream to conserve device memory and bandwidth.",
                explanation="Invoking the unsubscribe function disconnects the real-time listener during component unmount."
            ),
            QuizQuestionBlueprint(
                question="Does Cloud Firestore support automatic offline data caching on mobile?",
                options=[
                    "Yes, Firestore automatically maintains a local on-device cache, enabling offline reads and queuing offline writes.",
                    "No, Firestore crashes without internet.",
                    "Only on tablets.",
                    "Only in development mode."
                ],
                correct_answer="Yes, Firestore automatically maintains a local on-device cache, enabling offline reads and queuing offline writes.",
                explanation="Firestore includes built-in offline persistence out of the box."
            )
        ]
    ),
]
