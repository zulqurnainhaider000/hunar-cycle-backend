"""
Mobile App Development 40-Day Curriculum - Module 7 (Part 2), Module 8, Module 9 & Module 10 (Days 31 to 40)
Module 7: Cloud Services & BaaS (Days 31-33)
Module 8: Advanced UI & Animations (Days 34-36)
Module 9: Architecture & Code Quality (Days 37-38)
Module 10: Publishing & CI/CD (Days 39-40)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_31_TO_40 = [
    # -------------------------------------------------------------
    # DAY 31
    # -------------------------------------------------------------
    DayBlueprint(
        order=31,
        title="Day 31: Cloud Storage & Media Uploads",
        concept="Uploading images, videos, and binary assets from the device filesystem to cloud object storage (Firebase Storage / S3 / Supabase)",
        analogy="Think of Cloud Storage like a giant warehouse with shipping containers. When you take a photo on your phone, it's sitting on your personal camera desk. To share it with friends across the world, you don't send the entire desk—you put the photo into a package, ship it to the warehouse (`uploadBytesResumable`), get back a public shipping barcode/URL (`getDownloadURL`), and tell everyone 'here is the link to see my photo'!",
        theory_sections=[
            {
                "heading": "Blob Conversion & File Streaming",
                "body": "Mobile devices store media as local file URIs (e.g. `file:///var/mobile/Containers/Data/...`). You cannot directly send a local URI path to a remote server; you must first read the file into raw bytes, a Blob, or a Base64 stream using `fetch(localUri).blob()` or a file system buffer before uploading to Firebase Storage or AWS S3."
            },
            {
                "heading": "Upload Tasks, Progress Tracking, and Download URLs",
                "body": "Because media files can be several megabytes in size over unreliable 4G/5G networks, cloud storage SDKs provide upload tasks that emit snapshot events (bytes transferred vs total bytes). Once the upload completes successfully, you retrieve an immutable HTTPS download URL and store that URL in your database (e.g., Firestore or PostgreSQL) instead of storing the heavy binary blob itself."
            }
        ],
        code_snippets=[
            {
                "title": "Converting a Local Device Image URI into an Uploadable Blob",
                "language": "typescript",
                "code": "import { storage } from '../firebaseConfig';\nimport { ref, uploadBytesResumable, getDownloadURL } from 'firebase/storage';\n\nexport const uriToBlob = async (uri: string): Promise<Blob> => {\n  const response = await fetch(uri);\n  const blob = await response.blob();\n  return blob;\n};",
                "explanation": "Native file URIs cannot be directly sent across HTTP without resolving them into binary byte arrays. `fetch(uri).blob()` loads the local file into memory as an uploadable Blob."
            },
            {
                "title": "Uploading File to Firebase Storage with Real-time Progress",
                "language": "typescript",
                "code": "export const uploadImageWithProgress = (\n  blob: Blob,\n  path: string,\n  onProgress: (percent: number) => void\n): Promise<string> => {\n  return new Promise((resolve, reject) => {\n    const storageRef = ref(storage, path);\n    const uploadTask = uploadBytesResumable(storageRef, blob);\n\n    uploadTask.on(\n      'state_changed',\n      (snapshot) => {\n        const progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;\n        onProgress(Math.round(progress));\n      },\n      (error) => reject(error),\n      async () => {\n        const downloadUrl = await getDownloadURL(uploadTask.snapshot.ref);\n        resolve(downloadUrl);\n      }\n    );\n  });\n};",
                "explanation": "`uploadBytesResumable` creates a task listener that informs the UI whenever chunk progress changes, allowing you to render a smooth progress bar."
            },
            {
                "title": "Avatar Upload Screen Component",
                "language": "typescript",
                "code": "import React, { useState } from 'react';\nimport { View, Text, Button, Image, ProgressBarAndroid } from 'react-native';\nimport * as ImagePicker from 'expo-image-picker';\n\nexport const AvatarUploadScreen = () => {\n  const [uploadPercent, setUploadPercent] = useState<number>(0);\n  const [remoteUrl, setRemoteUrl] = useState<string | null>(null);\n\n  const handlePickAndUpload = async () => {\n    const result = await ImagePicker.launchImageLibraryAsync({ quality: 0.7 });\n    if (!result.canceled && result.assets[0].uri) {\n      const blob = await uriToBlob(result.assets[0].uri);\n      const url = await uploadImageWithProgress(blob, `avatars/${Date.now()}.jpg`, setUploadPercent);\n      setRemoteUrl(url);\n    }\n  };\n\n  return (\n    <View style={{ padding: 20, alignItems: 'center' }}>\n      {remoteUrl && <Image source={{ uri: remoteUrl }} style={{ width: 120, height: 120, borderRadius: 60 }} />}\n      <Text>Upload Progress: {uploadPercent}%</Text>\n      <Button title=\"Select & Upload Avatar\" onPress={handlePickAndUpload} />\n    </View>\n  );\n};",
                "explanation": "Integrates image picking, blob conversion, and progressive upload into a clear mobile screen flow."
            },
            {
                "title": "Saving the Download URL to User Database Profile",
                "language": "typescript",
                "code": "import { doc, updateDoc } from 'firebase/firestore';\nimport { db } from '../firebaseConfig';\n\nexport const updateUserProfileImage = async (userId: string, photoUrl: string) => {\n  const userRef = doc(db, 'users', userId);\n  await updateDoc(userRef, {\n    avatarUrl: photoUrl,\n    updatedAt: new Date().toISOString()\n  });\n};",
                "explanation": "Databases should never store megabytes of image binaries directly. Instead, store the public CDN URL generated by your cloud storage bucket."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Cloud Storage File Uploader Function",
            description="Write a helper function `computeUploadProgress(bytesTransferred: number, totalBytes: number): number` that safely calculates the percentage from 0 to 100, rounding down to the nearest integer and returning 0 if totalBytes is 0.",
            starter_code="export function computeUploadProgress(bytesTransferred: number, totalBytes: number): number {\n  // Calculate percentage and prevent divide-by-zero\n}",
            solution_code="export function computeUploadProgress(bytesTransferred: number, totalBytes: number): number {\n  if (!totalBytes || totalBytes <= 0) return 0;\n  const percent = Math.floor((bytesTransferred / totalBytes) * 100);\n  return Math.min(100, Math.max(0, percent));\n}",
            expected_output="computeUploadProgress(450, 1000) === 45"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is it bad practice to store raw image binary blobs directly in a SQL or NoSQL database table?",
                options=[
                    "Databases cannot store binary data under any circumstances",
                    "It inflates database size, slows down indexing, and spikes query latency and bandwidth costs",
                    "Mobile devices can only display images stored on local SD cards",
                    "Databases immediately compress all binary data into plain text"
                ],
                correct_answer="It inflates database size, slows down indexing, and spikes query latency and bandwidth costs",
                explanation="Storing media files in databases degrades query speeds and causes database bloat. Media belongs in dedicated object storage like S3 or Cloud Storage."
            ),
            QuizQuestionBlueprint(
                question="What must typically be done to a local device URI (`file://...`) before uploading via Firebase Storage web SDK?",
                options=[
                    "It must be converted into a Blob or Uint8Array using fetch(uri).blob()",
                    "It must be renamed to index.html",
                    "It must be encoded using HTML entities",
                    "No conversion is ever needed; pass the file string directly to uploadBytes"
                ],
                correct_answer="It must be converted into a Blob or Uint8Array using fetch(uri).blob()",
                explanation="Standard web SDKs expect a Blob or ArrayBuffer rather than a mobile filesystem URI."
            ),
            QuizQuestionBlueprint(
                question="What does the `getDownloadURL()` function in Firebase Storage return?",
                options=[
                    "The local Android storage path on the user's device",
                    "A publicly accessible HTTPS CDN URL to read the uploaded asset",
                    "The user's Google password",
                    "A Base64 string of the file contents"
                ],
                correct_answer="A publicly accessible HTTPS CDN URL to read the uploaded asset",
                explanation="getDownloadURL() creates an HTTPS URL hosted on Firebase/Google Cloud CDN that can be loaded in an <Image source={{ uri }} /> component."
            ),
            QuizQuestionBlueprint(
                question="Which upload method allows listening to upload bytes transferred and handling network pauses?",
                options=[
                    "uploadBytesResumable",
                    "saveStringSynchronously",
                    "pushRawBinary",
                    "dumpBlobFast"
                ],
                correct_answer="uploadBytesResumable",
                explanation="uploadBytesResumable creates an UploadTask that emits state changes, bytes transferred, and pause/resume handlers."
            ),
            QuizQuestionBlueprint(
                question="What is the recommended approach to reduce upload bandwidth for user photos taken on mobile cameras?",
                options=[
                    "Always upload the RAW 48-megapixel uncompressed file",
                    "Compress and downscale image dimensions before initiating the cloud upload",
                    "Convert images to ASCII art before sending",
                    "Only upload when the battery is at 100%"
                ],
                correct_answer="Compress and downscale image dimensions before initiating the cloud upload",
                explanation="Resizing and compressing mobile camera pictures (which are often 10MB+) down to 1080p and ~300KB saves massive user bandwidth and improves upload speeds."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 32
    # -------------------------------------------------------------
    DayBlueprint(
        order=32,
        title="Day 32: Push Notifications & Device Tokens",
        concept="Configuring Firebase Cloud Messaging (FCM) / Expo Notifications, registering push tokens, and receiving background and foreground messages",
        analogy="Think of push notifications like the postal delivery system. Each phone has a unique physical mailbox address (the Push Token). Your backend server is the sender who hands a postcard to the postal service (FCM / APNs) stamped with that mailbox address. Even when you are sleeping with your front door locked (app closed in pocket), the mail carrier knocks on your door and drops the notification directly onto your lock screen!",
        theory_sections=[
            {
                "heading": "How Push Notifications Work Architecture-wise",
                "body": "Mobile devices do not maintain active TCP connections to your custom backend server 24/7 because it would rapidly drain the phone's battery. Instead, Apple (APNs) and Google (FCM) maintain a single, highly optimized, persistent OS-level socket. When your server wants to notify a user, it sends a payload to FCM/APNs along with the user's registered Push Token. Apple and Google then deliver the banner directly to the device."
            },
            {
                "heading": "Token Registration & Foreground vs Background Handling",
                "body": "On app launch, you must request notification permissions from the user. Once granted, you retrieve the device's Push Token (e.g. `ExponentPushToken[...]` or FCM registration token) and save it to the user's profile in your database. Notifications received while the app is in the foreground require custom in-app handling (e.g. banner alert), whereas background notifications are automatically rendered by the mobile OS."
            }
        ],
        code_snippets=[
            {
                "title": "Registering for Push Notifications & Getting Push Token",
                "language": "typescript",
                "code": "import * as Notifications from 'expo-notifications';\nimport * as Device from 'expo-device';\nimport { Platform } from 'react-native';\n\nexport async function registerForPushNotificationsAsync(): Promise<string | null> {\n  if (!Device.isDevice) {\n    alert('Must use physical device for Push Notifications');\n    return null;\n  }\n\n  const { status: existingStatus } = await Notifications.getPermissionsAsync();\n  let finalStatus = existingStatus;\n\n  if (existingStatus !== 'granted') {\n    const { status } = await Notifications.requestPermissionsAsync();\n    finalStatus = status;\n  }\n\n  if (finalStatus !== 'granted') return null;\n\n  const tokenData = await Notifications.getExpoPushTokenAsync();\n  return tokenData.data;\n}",
                "explanation": "Checks if the device is a real physical phone, requests permission from the user, and extracts the unique hardware-tied push registration token."
            },
            {
                "title": "Configuring Foreground Notification Presentation Handler",
                "language": "typescript",
                "code": "Notifications.setNotificationHandler({\n  handleNotification: async () => ({\n    shouldShowAlert: true,\n    shouldPlaySound: true,\n    shouldSetBadge: true,\n  }),\n});",
                "explanation": "By default, iOS and Android do not show banner popups if the app is already open and active. Setting this presentation handler instructs the OS to show alerts even in the foreground."
            },
            {
                "title": "Listening to Incoming Notifications & Taps",
                "language": "typescript",
                "code": "import React, { useEffect } from 'react';\nimport * as Notifications from 'expo-notifications';\n\nexport const useNotificationObserver = (onTapNotification: (data: any) => void) => {\n  useEffect(() => {\n    // Listener for when notification arrives while app is open\n    const receivedSubscription = Notifications.addNotificationReceivedListener(notification => {\n      console.log('Received notification:', notification.request.content);\n    });\n\n    // Listener for when user taps the notification banner\n    const responseSubscription = Notifications.addNotificationResponseReceivedListener(response => {\n      const customData = response.notification.request.content.data;\n      onTapNotification(customData);\n    });\n\n    return () => {\n      receivedSubscription.remove();\n      responseSubscription.remove();\n    };\n  }, [onTapNotification]);\n};",
                "explanation": "Listens for notification deliveries and user clicks, allowing your app to deep link directly into the relevant chat room or order status screen."
            },
            {
                "title": "Sending Push Notification from Backend (Node.js / Express)",
                "language": "javascript",
                "code": "const sendPushNotification = async (expoPushToken, title, body, data = {}) => {\n  const message = {\n    to: expoPushToken,\n    sound: 'default',\n    title: title,\n    body: body,\n    data: data,\n  };\n\n  await fetch('https://exp.host/--/api/v2/push/send', {\n    method: 'POST',\n    headers: {\n      Accept: 'application/json',\n      'Accept-encoding': 'gzip, deflate',\n      'Content-Type': 'application/json',\n    },\n    body: JSON.stringify(message),\n  });\n};",
                "explanation": "Your backend sends a JSON payload to the push gateway containing the recipient device token and notification body."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Push Notification Payload Formatter",
            description="Write a function `buildPushPayload(token: string, title: string, body: string, screen: string)` that returns a clean push notification object containing `to`, `title`, `body`, and a nested `data` object with `targetScreen`.",
            starter_code="export function buildPushPayload(token: string, title: string, body: string, screen: string) {\n  // Return formatted payload object\n}",
            solution_code="export function buildPushPayload(token: string, title: string, body: string, screen: string) {\n  return {\n    to: token,\n    sound: 'default',\n    title,\n    body,\n    data: {\n      targetScreen: screen,\n      timestamp: Date.now()\n    }\n  };\n}",
            expected_output="buildPushPayload('token123', 'Hi', 'Message', 'Chat') includes targetScreen: 'Chat'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why don't mobile apps maintain their own persistent socket to custom backend servers 24/7 for push notifications?",
                options=[
                    "Custom backend sockets would rapidly drain battery and consume excessive background cellular data",
                    "Mobile operating systems ban all network connections entirely",
                    "TCP sockets are not supported on smartphone processors",
                    "Smartphones only support Bluetooth signals"
                ],
                correct_answer="Custom backend sockets would rapidly drain battery and consume excessive background cellular data",
                explanation="Apple and Google use a unified, battery-optimized OS-level channel (APNs/FCM) so phones don't have hundreds of apps running individual background connections."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Push Token' in mobile development?",
                options=[
                    "A secret password the user enters into an input field",
                    "A unique identifier generated by the push service that addresses that specific app installation on that specific device",
                    "The phone's hardware serial number (IMEI)",
                    "A credit card token used for in-app purchases"
                ],
                correct_answer="A unique identifier generated by the push service that addresses that specific app installation on that specific device",
                explanation="A push token is an address given by FCM or APNs to identify where messages for this particular app should be delivered."
            ),
            QuizQuestionBlueprint(
                question="Where should a client app send its push token after successfully requesting permissions?",
                options=[
                    "It should save it only in local variables and never send it anywhere",
                    "It should send it to your backend server database to link it with the authenticated user",
                    "It must print it on paper",
                    "It must delete it immediately to conserve memory"
                ],
                correct_answer="It should send it to your backend server database to link it with the authenticated user",
                explanation="Your server must store the user's push token in order to send notifications when an event occurs (e.g. friend requests, order updates)."
            ),
            QuizQuestionBlueprint(
                question="What happens when a user taps a push notification banner while the app is in the background or killed?",
                options=[
                    "The device reboots into recovery mode",
                    "The OS launches the app and triggers the notification response listener with the payload data",
                    "The notification payload is erased and the app crashes",
                    "The notification is redirected to email"
                ],
                correct_answer="The OS launches the app and triggers the notification response listener with the payload data",
                explanation="The OS launches the app and passes the notification payload to response listeners so the app can route the user to the relevant screen."
            ),
            QuizQuestionBlueprint(
                question="Can push notifications be tested reliably on a standard iOS Simulator without special APNs entitlements?",
                options=[
                    "Yes, simulators always have identical hardware and cellular radios to physical iPhones",
                    "Physical devices are strongly recommended because simulators historically lack full APNs push registration capabilities",
                    "Simulators only support Android notifications",
                    "Push notifications only work when connected to a Mac via USB cable"
                ],
                correct_answer="Physical devices are strongly recommended because simulators historically lack full APNs push registration capabilities",
                explanation="Push notification registration requires physical devices or specific CLI drag-and-drop APNs payload simulation."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 33
    # -------------------------------------------------------------
    DayBlueprint(
        order=33,
        title="Day 33 (Project): Real-Time Chat App with Live Channels",
        concept="Building a complete end-to-end real-time chat application with live message feeds, optimistic UI updates, auto-scrolling, and instant delivery",
        analogy="Think of a real-time chat room like a whiteboard in a busy kitchen. Anyone can grab a marker and write a note (send message). The moment the ink touches the whiteboard, every single chef looking at the board sees the new note immediately without needing to walk over and ask 'are there new orders?' (live snapshot listener)!",
        theory_sections=[
            {
                "heading": "Architecture of a Production Chat App",
                "body": "A robust chat app combines three core layers: (1) A real-time data listener (`onSnapshot` in Firestore or WebSocket connection) to receive new messages in milliseconds; (2) An inverted `FlatList` that pins the newest messages to the bottom and maintains scroll position as older messages load; (3) Optimistic UI updates, rendering sent messages immediately with a 'sending' status before network confirmation."
            },
            {
                "heading": "Optimistic UI and Message Ordering",
                "body": "Waiting for server confirmation before displaying a typed chat message creates noticeable UI lag. In modern mobile apps, you append the message to your local state instantly with a temporary ID and status flag (`pending`), and then replace it with the confirmed server timestamp once the write succeeds."
            }
        ],
        code_snippets=[
            {
                "title": "Chat Message TypeScript Interface",
                "language": "typescript",
                "code": "export interface ChatMessage {\n  id: string;\n  channelId: string;\n  senderId: string;\n  senderName: string;\n  text: string;\n  createdAt: number;\n  status?: 'pending' | 'sent' | 'failed';\n}",
                "explanation": "Defines the shape of a chat message, including sender metadata, timestamps, and optimistic delivery status."
            },
            {
                "title": "Subscribing to Real-Time Room Messages (Firestore)",
                "language": "typescript",
                "code": "import { collection, query, where, orderBy, onSnapshot } from 'firebase/firestore';\nimport { db } from '../firebaseConfig';\nimport { ChatMessage } from '../types';\n\nexport const subscribeToRoomMessages = (\n  channelId: string,\n  onUpdate: (messages: ChatMessage[]) => void\n) => {\n  const q = query(\n    collection(db, 'messages'),\n    where('channelId', '==', channelId),\n    orderBy('createdAt', 'desc')\n  );\n\n  return onSnapshot(q, (snapshot) => {\n    const messages: ChatMessage[] = snapshot.docs.map(doc => ({\n      id: doc.id,\n      ...(doc.data() as Omit<ChatMessage, 'id'>)\n    }));\n    onUpdate(messages);\n  });\n};",
                "explanation": "Sets up a live reactive query ordered in descending order so the newest messages arrive first for the inverted FlatList."
            },
            {
                "title": "Optimistic Send Message Action",
                "language": "typescript",
                "code": "import { addDoc, collection } from 'firebase/firestore';\nimport { db } from '../firebaseConfig';\n\nexport const sendChatMessage = async (\n  channelId: string,\n  senderId: string,\n  senderName: string,\n  text: string\n) => {\n  const payload = {\n    channelId,\n    senderId,\n    senderName,\n    text,\n    createdAt: Date.now(),\n  };\n  await addDoc(collection(db, 'messages'), payload);\n};",
                "explanation": "Writes the new chat message directly to the cloud collection, immediately firing listeners on all connected devices."
            },
            {
                "title": "Complete Chat Screen with Inverted FlatList",
                "language": "typescript",
                "code": "import React, { useState, useEffect } from 'react';\nimport { View, FlatList, TextInput, TouchableOpacity, Text, StyleSheet } from 'react-native';\n\nexport const LiveChatScreen = ({ route }: any) => {\n  const { channelId, user } = route.params;\n  const [messages, setMessages] = useState<ChatMessage[]>([]);\n  const [inputText, setInputText] = useState('');\n\n  useEffect(() => {\n    const unsubscribe = subscribeToRoomMessages(channelId, setMessages);\n    return () => unsubscribe();\n  }, [channelId]);\n\n  const handleSend = async () => {\n    if (!inputText.trim()) return;\n    const text = inputText;\n    setInputText('');\n    await sendChatMessage(channelId, user.id, user.name, text);\n  };\n\n  return (\n    <View style={styles.container}>\n      <FlatList\n        data={messages}\n        inverted\n        keyExtractor={(item) => item.id}\n        renderItem={({ item }) => (\n          <View style={[styles.bubble, item.senderId === user.id ? styles.myBubble : styles.theirBubble]}>\n            <Text style={styles.sender}>{item.senderName}</Text>\n            <Text style={styles.messageText}>{item.text}</Text>\n          </View>\n        )}\n      />\n      <View style={styles.inputBar}>\n        <TextInput style={styles.input} value={inputText} onChangeText={setInputText} placeholder=\"Type a message...\" />\n        <TouchableOpacity style={styles.sendButton} onPress={handleSend}>\n          <Text style={styles.sendText}>Send</Text>\n        </TouchableOpacity>\n      </View>\n    </View>\n  );\n};\n\nconst styles = StyleSheet.create({\n  container: { flex: 1, backgroundColor: '#F8FAFC' },\n  bubble: { padding: 12, borderRadius: 16, marginVertical: 4, marginHorizontal: 12, maxWidth: '75%' },\n  myBubble: { alignSelf: 'flex-end', backgroundColor: '#3B82F6' },\n  theirBubble: { alignSelf: 'flex-start', backgroundColor: '#E2E8F0' },\n  sender: { fontSize: 10, color: '#64748B', marginBottom: 2 },\n  messageText: { fontSize: 15, color: '#0F172A' },\n  inputBar: { flexDirection: 'row', padding: 10, backgroundColor: '#FFFFFF', borderTopWidth: 1, borderColor: '#E2E8F0' },\n  input: { flex: 1, borderWidth: 1, borderColor: '#CBD5E1', borderRadius: 20, paddingHorizontal: 16, height: 42 },\n  sendButton: { marginLeft: 8, backgroundColor: '#3B82F6', borderRadius: 20, paddingHorizontal: 16, justifyContent: 'center' },\n  sendText: { color: '#FFF', fontWeight: 'bold' }\n});",
                "explanation": "A complete real-time chat interface featuring an inverted FlatList that automatically pins new content to the keyboard input area."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Chat Message Deduplication Filter",
            description="Write a helper function `mergeAndDeduplicateMessages(existing: ChatMessage[], incoming: ChatMessage[]): ChatMessage[]` that merges incoming messages with existing ones and ensures all message IDs are unique, sorted by `createdAt` descending.",
            starter_code="export function mergeAndDeduplicateMessages(existing: any[], incoming: any[]): any[] {\n  // Merge and deduplicate by item.id, sort by createdAt desc\n}",
            solution_code="export function mergeAndDeduplicateMessages(existing: any[], incoming: any[]): any[] {\n  const map = new Map<string, any>();\n  [...existing, ...incoming].forEach(msg => {\n    map.set(msg.id, msg);\n  });\n  return Array.from(map.values()).sort((a, b) => b.createdAt - a.createdAt);\n}",
            expected_output="mergeAndDeduplicateMessages([{id: '1', createdAt: 10}], [{id: '1', createdAt: 10}, {id: '2', createdAt: 20}]) has length 2"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is an inverted FlatList (`inverted={true}`) used for chat messaging screens?",
                options=[
                    "It flips the phone upside down to save screen pixels",
                    "It automatically anchors index 0 at the bottom near the text input bar and scrolls upwards for history",
                    "It translates English text into Latin automatically",
                    "It is mandatory for all FlatLists in React Native"
                ],
                correct_answer="It automatically anchors index 0 at the bottom near the text input bar and scrolls upwards for history",
                explanation="Inverted FlatLists render from bottom to top, making the newest message stay pinned to the bottom without manual scrollToOffset calculations."
            ),
            QuizQuestionBlueprint(
                question="What is the benefit of 'Optimistic UI' updates in a chat application?",
                options=[
                    "It makes the app believe it has full battery power at all times",
                    "It instantly renders the user's message on screen before the server roundtrip finishes, providing zero perceptual lag",
                    "It guarantees messages are delivered even if the user has no phone",
                    "It prevents users from sending messages with typos"
                ],
                correct_answer="It instantly renders the user's message on screen before the server roundtrip finishes, providing zero perceptual lag",
                explanation="Optimistic UI displays actions immediately so the app feels instant, updating message status once server confirmation arrives."
            ),
            QuizQuestionBlueprint(
                question="What must always be executed when leaving a chat screen to avoid memory leaks with real-time listeners?",
                options=[
                    "Call the unsubscribe function returned by onSnapshot inside the useEffect cleanup",
                    "Clear the phone's entire AsyncStorage database",
                    "Force close the entire mobile operating system",
                    "Delete all previous messages from the database"
                ],
                correct_answer="Call the unsubscribe function returned by onSnapshot inside the useEffect cleanup",
                explanation="Failing to call unsubscribe() leaves active socket listeners running in the background, consuming memory and triggering state updates on unmounted screens."
            ),
            QuizQuestionBlueprint(
                question="How should chat messages sent by the logged-in user be visually distinguished from messages sent by others?",
                options=[
                    "They should be blurred out completely",
                    "By aligning them to the right with a distinctive accent color and aligning others to the left with a neutral background",
                    "By playing a siren sound for every single message",
                    "By rotating the text 90 degrees"
                ],
                correct_answer="By aligning them to the right with a distinctive accent color and aligning others to the left with a neutral background",
                explanation="Standard mobile design patterns align the current user's bubbles to the right in brand colors and others to the left."
            ),
            QuizQuestionBlueprint(
                question="Which component helps prevent the on-screen keyboard from covering the chat input field on iOS?",
                options=[
                    "KeyboardAvoidingView",
                    "StatusBar",
                    "SafeAreaViewOnly",
                    "CanvasCover"
                ],
                correct_answer="KeyboardAvoidingView",
                explanation="KeyboardAvoidingView automatically adjusts its height or position when the virtual keyboard pops up."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 34
    # -------------------------------------------------------------
    DayBlueprint(
        order=34,
        title="Day 34: Micro-Interactions & Gestures",
        concept="Handling fluid multi-touch gestures, pan drags, pinches, and swipe actions using react-native-gesture-handler",
        analogy="Think of native gestures like a musical violin string. When you touch a violin string with your bow (finger), every tiny fraction of a millimeter movement produces an instant, continuous vibration (sound). Old web clicks were like flicking a simple light switch (on/off); `react-native-gesture-handler` runs directly on the native UI thread like a true acoustic instrument with zero delay!",
        theory_sections=[
            {
                "heading": "Why Native Gesture Handling Matters",
                "body": "In older React Native architectures, touch events were passed across the JavaScript bridge asynchronously. If the JS thread was busy calculating data, swipes and drags would stutter and lag behind the user's physical finger. `react-native-gesture-handler` declares gestures natively in Objective-C/Java and synchronizes gestures directly on the native rendering thread."
            },
            {
                "heading": "The Gesture Hierarchy (Pan, Tap, Pinch, Swipe)",
                "body": "Modern gesture systems use the declarative `Gesture` API from `react-native-gesture-handler` v2: `Gesture.Pan()`, `Gesture.Pinch()`, and `Gesture.Tap()`. Gestures can be combined simultaneously (`Gesture.Simultaneous`), raced (`Gesture.Race`), or chained sequentially (`Gesture.Exclusive`) for complex mobile interactions."
            }
        ],
        code_snippets=[
            {
                "title": "Wrapping App Root with GestureHandlerRootView",
                "language": "typescript",
                "code": "import React from 'react';\nimport { GestureHandlerRootView } from 'react-native-gesture-handler';\nimport AppNavigator from './navigation/AppNavigator';\n\nexport default function App() {\n  return (\n    <GestureHandlerRootView style={{ flex: 1 }}>\n      <AppNavigator />\n    </GestureHandlerRootView>\n  );\n}",
                "explanation": "Every React Native app using gesture-handler must wrap its root hierarchy inside `GestureHandlerRootView` to intercept native touch events."
            },
            {
                "title": "Creating a Draggable Card with PanGesture",
                "language": "typescript",
                "code": "import React from 'react';\nimport { StyleSheet } from 'react-native';\nimport { GestureDetector, Gesture } from 'react-native-gesture-handler';\nimport Animated, { useSharedValue, useAnimatedStyle, withSpring } from 'react-native-reanimated';\n\nexport const DraggableCard = () => {\n  const translationX = useSharedValue(0);\n  const translationY = useSharedValue(0);\n  const prevTranslationX = useSharedValue(0);\n  const prevTranslationY = useSharedValue(0);\n\n  const panGesture = Gesture.Pan()\n    .onUpdate((event) => {\n      translationX.value = prevTranslationX.value + event.translationX;\n      translationY.value = prevTranslationY.value + event.translationY;\n    })\n    .onEnd(() => {\n      // Snap back smoothly using spring physics\n      translationX.value = withSpring(0);\n      translationY.value = withSpring(0);\n      prevTranslationX.value = 0;\n      prevTranslationY.value = 0;\n    });\n\n  const animatedStyle = useAnimatedStyle(() => ({\n    transform: [\n      { translateX: translationX.value },\n      { translateY: translationY.value },\n    ],\n  }));\n\n  return (\n    <GestureDetector gesture={panGesture}>\n      <Animated.View style={[styles.card, animatedStyle]} />\n    </GestureDetector>\n  );\n};\n\nconst styles = StyleSheet.create({\n  card: { width: 140, height: 140, backgroundColor: '#6366F1', borderRadius: 24 }\n});",
                "explanation": "Declares a Pan gesture that tracks touch translation in real time and springs back to original position when released."
            },
            {
                "title": "Implementing Swipe-to-Delete Action on a List Item",
                "language": "typescript",
                "code": "import React from 'react';\nimport { Text, View, StyleSheet } from 'react-native';\nimport Swipeable from 'react-native-gesture-handler/Swipeable';\n\nexport const SwipeableItem = ({ title, onDelete }: { title: string; onDelete: () => void }) => {\n  const renderRightActions = () => (\n    <View style={styles.deleteBox}>\n      <Text style={styles.deleteText} onPress={onDelete}>Delete</Text>\n    </View>\n  );\n\n  return (\n    <Swipeable renderRightActions={renderRightActions}>\n      <View style={styles.item}>\n        <Text style={styles.itemTitle}>{title}</Text>\n      </View>\n    </Swipeable>\n  );\n};\n\nconst styles = StyleSheet.create({\n  item: { padding: 18, backgroundColor: '#FFF', borderBottomWidth: 1, borderColor: '#E2E8F0' },\n  itemTitle: { fontSize: 16, color: '#1E293B' },\n  deleteBox: { backgroundColor: '#EF4444', justifyContent: 'center', alignItems: 'center', width: 90 },\n  deleteText: { color: '#FFF', fontWeight: 'bold' }\n});",
                "explanation": "Uses the prebuilt `Swipeable` container to reveal an action button when swiping left, standard across iOS Mail and WhatsApp."
            },
            {
                "title": "Pinch-to-Zoom Gesture for Images",
                "language": "typescript",
                "code": "import { GestureDetector, Gesture } from 'react-native-gesture-handler';\nimport Animated, { useSharedValue, useAnimatedStyle, withTiming } from 'react-native-reanimated';\n\nexport const ZoomableImage = ({ source }: { source: any }) => {\n  const scale = useSharedValue(1);\n\n  const pinchGesture = Gesture.Pinch()\n    .onUpdate((e) => {\n      scale.value = e.scale;\n    })\n    .onEnd(() => {\n      scale.value = withTiming(1);\n    });\n\n  const animatedStyle = useAnimatedStyle(() => ({\n    transform: [{ scale: scale.value }],\n  }));\n\n  return (\n    <GestureDetector gesture={pinchGesture}>\n      <Animated.Image source={source} style={[{ width: 300, height: 300 }, animatedStyle]} />\n    </GestureDetector>\n  );\n};",
                "explanation": "Listens for two-finger pinch touch points and scales the image seamlessly on the UI thread."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Clamp Gesture Drag Distance",
            description="Write a utility function `clampDragOffset(currentOffset: number, minBound: number, maxBound: number): number` that ensures an item cannot be dragged beyond specified pixel boundaries.",
            starter_code="export function clampDragOffset(currentOffset: number, minBound: number, maxBound: number): number {\n  // Keep currentOffset within [minBound, maxBound]\n}",
            solution_code="export function clampDragOffset(currentOffset: number, minBound: number, maxBound: number): number {\n  return Math.max(minBound, Math.min(maxBound, currentOffset));\n}",
            expected_output="clampDragOffset(150, -100, 100) === 100"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is `react-native-gesture-handler` superior to standard React Native Touchable/PanResponder?",
                options=[
                    "It runs and coordinates touch interactions natively on the UI thread, eliminating bridge latency and stutter",
                    "It works without requiring any touch screen hardware",
                    "It converts touch gestures into speech automatically",
                    "It only works on Android devices"
                ],
                correct_answer="It runs and coordinates touch interactions natively on the UI thread, eliminating bridge latency and stutter",
                explanation="Native gesture handling processes touch streams directly on the mobile OS thread without asynchronous JS bridge roundtrips."
            ),
            QuizQuestionBlueprint(
                question="What mandatory component must wrap the entire application root when using `react-native-gesture-handler`?",
                options=[
                    "GestureHandlerRootView",
                    "ScrollView",
                    "TouchContainer",
                    "HardwareRoot"
                ],
                correct_answer="GestureHandlerRootView",
                explanation="GestureHandlerRootView intercepts native touch events and routes them to active gesture detectors."
            ),
            QuizQuestionBlueprint(
                question="Which gesture type in `Gesture.X()` handles multi-touch zoom and pinch operations?",
                options=[
                    "Gesture.Pan()",
                    "Gesture.Pinch()",
                    "Gesture.Fling()",
                    "Gesture.Hover()"
                ],
                correct_answer="Gesture.Pinch()",
                explanation="Gesture.Pinch() tracks the distance between two touch points and exposes an e.scale factor."
            ),
            QuizQuestionBlueprint(
                question="What does calling `withSpring()` inside a gesture callback achieve?",
                options=[
                    "It causes the phone to heat up",
                    "It animates a value toward a target using natural physical spring physics (damping, stiffness) instead of rigid linear time",
                    "It forces the screen to rotate 180 degrees",
                    "It immediately deletes the element from the DOM"
                ],
                correct_answer="It animates a value toward a target using natural physical spring physics (damping, stiffness) instead of rigid linear time",
                explanation="withSpring simulates real-world physical bounce, making micro-interactions feel tactile and natural."
            ),
            QuizQuestionBlueprint(
                question="How do you combine two gestures so that both can be recognized at the same time (e.g. pan while pinching)?",
                options=[
                    "Gesture.Simultaneous(gestureA, gestureB)",
                    "Gesture.CrashTogether(a, b)",
                    "Gesture.LockBoth(a, b)",
                    "It is technically impossible on mobile phones"
                ],
                correct_answer="Gesture.Simultaneous(gestureA, gestureB)",
                explanation="Gesture.Simultaneous allows multiple gestures to activate concurrently without canceling each other."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 35
    # -------------------------------------------------------------
    DayBlueprint(
        order=35,
        title="Day 35: Custom Animations & Lottie Vector Files",
        concept="Creating smooth 60fps/120fps animations using React Native Reanimated and embedding scalable vector animations with Lottie",
        analogy="Think of animations like a cartoon flipbook. If an artist draws 12 drawings a second, motion looks choppy. If they draw 60 fluid drawings a second, it feels like real life. Standard animations in code can be painful to calculate mathematically; Lottie lets an After Effects designer export the cartoon into a lightweight JSON file that your app plays like magic vector cinema at a blistering 120 FPS!",
        theory_sections=[
            {
                "heading": "React Native Reanimated & The UI Thread",
                "body": "`react-native-reanimated` executes animation calculations ('worklets') directly on the mobile device's UI thread rather than the JavaScript thread. Even if JavaScript is heavily occupied parsing JSON or sorting large datasets, Reanimated animations maintain a silky-smooth 60 to 120 frames per second without dropping a single frame."
            },
            {
                "heading": "Lottie Vector Animations",
                "body": "Lottie (`lottie-react-native`) parses Adobe After Effects animations exported via the Bodymovin plugin into lightweight JSON files. Because Lottie renders vectors rather than heavy GIF or MP4 video files, animations scale infinitely without pixelation, load instantly, and consume minimal storage."
            }
        ],
        code_snippets=[
            {
                "title": "Smooth Pulsing Heart Button with Reanimated",
                "language": "typescript",
                "code": "import React from 'react';\nimport { TouchableOpacity, StyleSheet } from 'react-native';\nimport Animated, {\n  useSharedValue,\n  useAnimatedStyle,\n  withRepeat,\n  withTiming,\n  withSequence\n} from 'react-native-reanimated';\n\nexport const PulsingHeart = () => {\n  const scale = useSharedValue(1);\n\n  const handlePress = () => {\n    scale.value = withSequence(\n      withTiming(1.3, { duration: 150 }),\n      withTiming(1, { duration: 150 })\n    );\n  };\n\n  const animatedStyle = useAnimatedStyle(() => ({\n    transform: [{ scale: scale.value }],\n  }));\n\n  return (\n    <TouchableOpacity onPress={handlePress}>\n      <Animated.Text style={[styles.heart, animatedStyle]}>❤️</Animated.Text>\n    </TouchableOpacity>\n  );\n};\n\nconst styles = StyleSheet.create({\n  heart: { fontSize: 48 }\n});",
                "explanation": "Uses `useSharedValue` and `withSequence` to create a snappy, fluid micro-interaction when the user taps a like button."
            },
            {
                "title": "Installing and Playing a Lottie JSON Animation",
                "language": "typescript",
                "code": "import React, { useRef } from 'react';\nimport { View, StyleSheet, Button } from 'react-native';\nimport LottieView from 'lottie-react-native';\n\nexport const SuccessAnimationScreen = () => {\n  const animationRef = useRef<LottieView>(null);\n\n  return (\n    <View style={styles.container}>\n      <LottieView\n        ref={animationRef}\n        source={require('../../assets/success-check.json')}\n        autoPlay\n        loop={false}\n        style={styles.animation}\n      />\n      <Button title=\"Replay Animation\" onPress={() => animationRef.current?.play()} />\n    </View>\n  );\n};\n\nconst styles = StyleSheet.create({\n  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },\n  animation: { width: 220, height: 220 },\n});",
                "explanation": "Renders a vector Lottie animation from a bundled JSON asset, offering full playback control (play, pause, reset)."
            },
            {
                "title": "Shared Element Transition (Layout Animation)",
                "language": "typescript",
                "code": "import Animated, { FadeInUp, FadeOutDown, Layout } from 'react-native-reanimated';\nimport { Text, StyleSheet } from 'react-native';\n\nexport const AnimatedListItem = ({ text }: { text: string }) => {\n  return (\n    <Animated.View\n      entering={FadeInUp.springify()}\n      exiting={FadeOutDown}\n      layout={Layout.springify()}\n      style={styles.card}\n    >\n      <Text style={styles.text}>{text}</Text>\n    </Animated.View>\n  );\n};\n\nconst styles = StyleSheet.create({\n  card: { padding: 16, backgroundColor: '#E0E7FF', marginVertical: 6, borderRadius: 12 },\n  text: { fontSize: 16, color: '#3730A3' }\n});",
                "explanation": "Reanimated layout animations automatically animate component mounting, unmounting, and position changes with spring physics."
            },
            {
                "title": "Continuous Skeleton Shimmer Animation",
                "language": "typescript",
                "code": "import React, { useEffect } from 'react';\nimport Animated, { useSharedValue, useAnimatedStyle, withRepeat, withTiming } from 'react-native-reanimated';\nimport { StyleSheet } from 'react-native';\n\nexport const SkeletonLoader = () => {\n  const opacity = useSharedValue(0.3);\n\n  useEffect(() => {\n    opacity.value = withRepeat(withTiming(0.8, { duration: 800 }), -1, true);\n  }, []);\n\n  const animatedStyle = useAnimatedStyle(() => ({\n    opacity: opacity.value,\n  }));\n\n  return <Animated.View style={[styles.skeleton, animatedStyle]} />;\n};\n\nconst styles = StyleSheet.create({\n  skeleton: { width: '90%', height: 24, backgroundColor: '#CBD5E1', borderRadius: 8, marginVertical: 6 }\n});",
                "explanation": "Creates a continuous breathing shimmer effect for placeholder loading states using `withRepeat(-1, true)`."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Lottie Progress Calculation",
            description="Write a function `calculateAnimationProgress(currentFrame: number, totalFrames: number): number` that returns a float between 0.0 and 1.0 clamped, representing normalized animation progress.",
            starter_code="export function calculateAnimationProgress(currentFrame: number, totalFrames: number): number {\n  // Return normalized progress between 0 and 1\n}",
            solution_code="export function calculateAnimationProgress(currentFrame: number, totalFrames: number): number {\n  if (!totalFrames || totalFrames <= 0) return 0;\n  const progress = currentFrame / totalFrames;\n  return Math.min(1, Math.max(0, Number(progress.toFixed(3))));\n}",
            expected_output="calculateAnimationProgress(60, 120) === 0.5"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why do animations created with React Native Reanimated perform better than standard Animated API?",
                options=[
                    "They run worklet functions directly on the device's native UI thread without JS bridge traffic",
                    "They force the device to run at a lower screen resolution",
                    "They only render text and never shapes",
                    "They require continuous cloud server rendering"
                ],
                correct_answer="They run worklet functions directly on the device's native UI thread without JS bridge traffic",
                explanation="Reanimated runs animations directly on the UI thread, ensuring continuous 60fps/120fps even when the JS thread is busy."
            ),
            QuizQuestionBlueprint(
                question="What file format does Lottie use to describe complex vector animations?",
                options=[
                    "JSON",
                    "MP4",
                    "GIF",
                    "FLV"
                ],
                correct_answer="JSON",
                explanation="Lottie animations are stored as structured JSON files created from Adobe After Effects vector layers."
            ),
            QuizQuestionBlueprint(
                question="What does `withRepeat(animation, -1, true)` do in Reanimated?",
                options=[
                    "It throws an error and stops the app",
                    "It repeats the animation infinitely (-1) and reverses direction each cycle (yoyo mode)",
                    "It cancels the animation after 1 millisecond",
                    "It slows the animation down by 100x"
                ],
                correct_answer="It repeats the animation infinitely (-1) and reverses direction each cycle (yoyo mode)",
                explanation="Passing -1 makes an animation loop indefinitely, while true creates a smooth yoyo/ping-pong effect."
            ),
            QuizQuestionBlueprint(
                question="What is the advantage of vector Lottie animations over animated GIF images?",
                options=[
                    "Lotties are vastly smaller in file size, scale crisply to any screen resolution without blur, and run at full native framerates",
                    "GIFs are always higher resolution than vectors",
                    "Lottie files can only be played once in an app's lifetime",
                    "Lottie animations do not require any memory"
                ],
                correct_answer="Lotties are vastly smaller in file size, scale crisply to any screen resolution without blur, and run at full native framerates",
                explanation="Vector Lottie animations are tiny JSON files that scale infinitely without pixelation, unlike heavy raster GIFs."
            ),
            QuizQuestionBlueprint(
                question="Which hook in Reanimated is used to create reactive animated styles bound to shared values?",
                options=[
                    "useAnimatedStyle",
                    "useStandardCss",
                    "useDomAnimation",
                    "useNativeScript"
                ],
                correct_answer="useAnimatedStyle",
                explanation="useAnimatedStyle connects shared values (like scale or opacity) to style props without triggering full component re-renders."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 36
    # -------------------------------------------------------------
    DayBlueprint(
        order=36,
        title="Day 36: Deep Linking & Universal Links",
        concept="Configuring custom URL schemes (`myapp://`), Android App Links, iOS Universal Links, and routing parameters into React Navigation",
        analogy="Think of deep linking like a direct teleporter into a room inside a skyscraper. When someone clicks a website link on their laptop (`https://example.com/product/42`), they load a web page. But when they click that same link in an email or SMS on their phone, deep linking teleports them straight past the lobby, opens your app, and lands them directly on the exact product detail page for item #42!",
        theory_sections=[
            {
                "heading": "Custom Schemes vs Universal Links / App Links",
                "body": "Custom URI schemes (e.g. `hunar://profile/123`) are easy to configure in `app.json`, but if the app isn't installed, clicking one in a web browser will result in a dead 'unknown protocol' error. Universal Links (iOS) and Android App Links use standard HTTPS URLs (e.g. `https://hunar.app/courses/42`) paired with two-way domain verification files (`assetlinks.json` and `apple-app-site-association`)."
            },
            {
                "heading": "React Navigation Linking Configuration",
                "body": "React Navigation has built-in deep link parsing through a `linking` configuration object. You define your URL prefixes and specify how paths map to screens and nested parameters. When the app is opened from a cold start via an external link, React Navigation automatically navigates to the target screen."
            }
        ],
        code_snippets=[
            {
                "title": "Declaring Custom Scheme in app.json (Expo)",
                "language": "javascript",
                "code": "{\n  \"expo\": {\n    \"name\": \"HunarCycle\",\n    \"slug\": \"hunar-cycle\",\n    \"scheme\": \"hunar\",\n    \"ios\": {\n      \"associatedDomains\": [\"applinks:hunar.app\"]\n    },\n    \"android\": {\n      \"intentFilters\": [\n        {\n          \"action\": \"VIEW\",\n          \"autoVerify\": true,\n          \"data\": [\n            { \"scheme\": \"https\", \"host\": \"hunar.app\", \"pathPrefix\": \"/courses\" }\n          ],\n          \"category\": [\"BROWSABLE\", \"DEFAULT\"]\n        }\n      ]\n    }\n  }\n}",
                "explanation": "Configures both the custom `hunar://` scheme and official HTTPS domain associations for Android App Links and iOS Universal Links."
            },
            {
                "title": "React Navigation Linking Configuration Object",
                "language": "typescript",
                "code": "import { LinkingOptions } from '@react-navigation/native';\nimport * as Linking from 'expo-linking';\n\nconst prefix = Linking.createURL('/');\n\nexport const linkingConfig: LinkingOptions<any> = {\n  prefixes: [prefix, 'hunar://', 'https://hunar.app'],\n  config: {\n    screens: {\n      HomeTab: {\n        screens: {\n          Feed: 'feed',\n          Explore: 'explore',\n        }\n      },\n      LessonDetail: 'courses/:courseId',\n      UserProfile: 'users/:userId',\n      NotFound: '*'\n    },\n  },\n};",
                "explanation": "Maps URLs like `hunar://courses/mobile-dev` or `https://hunar.app/courses/mobile-dev` directly into the `LessonDetail` screen with `courseId` as route params."
            },
            {
                "title": "Passing Linking Config to NavigationContainer",
                "language": "typescript",
                "code": "import React from 'react';\nimport { Text } from 'react-native';\nimport { NavigationContainer } from '@react-navigation/native';\nimport RootStackNavigator from './navigation/RootStackNavigator';\nimport { linkingConfig } from './linkingConfig';\n\nexport default function App() {\n  return (\n    <NavigationContainer\n      linking={linkingConfig}\n      fallback={<Text>Loading deep link...</Text>}\n    >\n      <RootStackNavigator />\n    </NavigationContainer>\n  );\n}",
                "explanation": "Attaches the linking configuration to the NavigationContainer so deep link arrivals automatically resolve screen transitions."
            },
            {
                "title": "Programmatically Handling Incoming Deep Links",
                "language": "typescript",
                "code": "import * as Linking from 'expo-linking';\nimport { useEffect } from 'react';\n\nexport const useDeepLinkListener = () => {\n  useEffect(() => {\n    // Handles deep link when app was already running in background\n    const subscription = Linking.addEventListener('url', (event) => {\n      console.log('App opened with URL:', event.url);\n      const parsed = Linking.parse(event.url);\n      console.log('Path:', parsed.path, 'Params:', parsed.queryParams);\n    });\n\n    // Handles deep link that opened the app from completely closed state\n    Linking.getInitialURL().then((url) => {\n      if (url) console.log('Initial launch URL:', url);\n    });\n\n    return () => subscription.remove();\n  }, []);\n};",
                "explanation": "Provides low-level observation for incoming deep links, both on cold start and background wake."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Deep Link URL Path Parameter Extractor",
            description="Write a utility function `extractCourseIdFromDeepLink(url: string): string | null` that parses URLs like `hunar://courses/1234` or `https://hunar.app/courses/5678` and returns the ID string, or `null` if the pattern does not match.",
            starter_code="export function extractCourseIdFromDeepLink(url: string): string | null {\n  // Extract courseId from deep link URL\n}",
            solution_code="export function extractCourseIdFromDeepLink(url: string): string | null {\n  const match = url.match(/courses\\/([a-zA-Z0-9_-]+)/);\n  return match ? match[1] : null;\n}",
            expected_output="extractCourseIdFromDeepLink('hunar://courses/react-native-101') === 'react-native-101'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary difference between a custom URL scheme (`myapp://`) and Universal Links / App Links (`https://myapp.com`)?",
                options=[
                    "Custom schemes only work on televisions",
                    "Universal Links use standard verified HTTPS domains, gracefully falling back to a website if the app is not installed",
                    "Custom schemes require a physical Ethernet cable",
                    "There is no difference; they are exact synonyms"
                ],
                correct_answer="Universal Links use standard verified HTTPS domains, gracefully falling back to a website if the app is not installed",
                explanation="Universal Links use verified web domains so users without the app are directed to the website or app store without broken protocol errors."
            ),
            QuizQuestionBlueprint(
                question="Where is the deep linking configuration hooked into React Navigation?",
                options=[
                    "In the `linking` prop of the top-level `<NavigationContainer />`",
                    "Inside package.json scripts",
                    "Directly in SQLite schema tables",
                    "Inside each individual `<Text>` component"
                ],
                correct_answer="In the `linking` prop of the top-level `<NavigationContainer />`",
                explanation="NavigationContainer takes a `linking` prop that tells it how to parse incoming URLs and route to nested screens."
            ),
            QuizQuestionBlueprint(
                question="What verification file must be hosted on an HTTPS server at `/.well-known/` to enable Android App Links?",
                options=[
                    "assetlinks.json",
                    "android.apk",
                    "google-service.xml",
                    "robots.txt"
                ],
                correct_answer="assetlinks.json",
                explanation="Google requires an `assetlinks.json` file hosted under `/.well-known/` containing the app's package name and SHA256 certificate fingerprint."
            ),
            QuizQuestionBlueprint(
                question="What verification file must be hosted on an HTTPS server to enable iOS Universal Links?",
                options=[
                    "apple-app-site-association",
                    "itunes.plist",
                    "ios-manifest.json",
                    "safari.config"
                ],
                correct_answer="apple-app-site-association",
                explanation="Apple checks the `apple-app-site-association` file on your domain to verify app ownership."
            ),
            QuizQuestionBlueprint(
                question="How does React Navigation map dynamic URL parameters like `/courses/:id` to screen props?",
                options=[
                    "It puts `id` into `route.params.id` inside the rendered screen component",
                    "It rewrites the phone's MAC address",
                    "It triggers an alert box that asks the user to retype the ID",
                    "It reloads the app from scratch"
                ],
                correct_answer="It puts `id` into `route.params.id` inside the rendered screen component",
                explanation="Route parameters specified with a colon (`:id`) are parsed automatically and populated on `route.params`."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 37
    # -------------------------------------------------------------
    DayBlueprint(
        order=37,
        title="Day 37: Architecture & Design Patterns (MVVM & Clean Code)",
        concept="Structuring scalable production codebases using Model-View-ViewModel (MVVM), custom hooks for business logic, and the Repository Pattern",
        analogy="Think of a restaurant kitchen. The dining table (View) only shows food and menus. The waiter (ViewModel) takes your order and brings back the dish. The chef and suppliers (Model & Repository) handle cooking and ingredients. If the waiter also had to butcher meat and wash dishes at the table, the restaurant would collapse into chaos! Separating concerns keeps your code clean, modular, and easy to maintain.",
        theory_sections=[
            {
                "heading": "The Model-View-ViewModel (MVVM) Pattern in React Native",
                "body": "In React Native, the **View** is the declarative JSX UI component (`<Text>`, `<FlatList>`). The **ViewModel** is a custom React hook (e.g. `useCourseList()`) that manages state, filters, and user actions. The **Model** represents pure TypeScript interfaces and entity data types. Keeping JSX free of heavy business logic makes testing and refactoring effortless."
            },
            {
                "heading": "The Repository Pattern & Service Abstraction",
                "body": "Screens should never make raw `fetch()` or `axios` calls directly inside UI components. Instead, create a Repository or Service layer (e.g. `CourseRepository.ts`). If tomorrow your company switches from Firebase to GraphQL or a custom PostgreSQL REST API, you only update the repository—the rest of your application code remains untouched."
            }
        ],
        code_snippets=[
            {
                "title": "Model Layer: TypeScript Domain Entities",
                "language": "typescript",
                "code": "export interface Product {\n  id: string;\n  title: string;\n  price: number;\n  inStock: boolean;\n}\n\nexport interface ICartItem extends Product {\n  quantity: number;\n}",
                "explanation": "Defines pure data contracts (Models) with no framework-specific UI or database logic."
            },
            {
                "title": "Repository Layer: Data Access Interface & Implementation",
                "language": "typescript",
                "code": "import { Product } from '../models/Product';\n\nexport interface IProductRepository {\n  getAll(): Promise<Product[]>;\n  getById(id: string): Promise<Product | null>;\n}\n\nexport class ApiProductRepository implements IProductRepository {\n  private baseUrl = 'https://api.example.com/products';\n\n  async getAll(): Promise<Product[]> {\n    const response = await fetch(this.baseUrl);\n    if (!response.ok) throw new Error('Failed to fetch products');\n    return response.json();\n  }\n\n  async getById(id: string): Promise<Product | null> {\n    const response = await fetch(`${this.baseUrl}/${id}`);\n    return response.ok ? response.json() : null;\n  }\n}",
                "explanation": "Abstracts data retrieval behind a clear contract so backend API changes do not ripple through UI screens."
            },
            {
                "title": "ViewModel Layer: Custom Hook Encapsulating Business Logic",
                "language": "typescript",
                "code": "import { useState, useEffect, useMemo } from 'react';\nimport { Product } from '../models/Product';\nimport { IProductRepository } from '../repositories/ProductRepository';\n\nexport const useProductCatalogViewModel = (repo: IProductRepository) => {\n  const [products, setProducts] = useState<Product[]>([]);\n  const [loading, setLoading] = useState(true);\n  const [searchQuery, setSearchQuery] = useState('');\n\n  useEffect(() => {\n    repo.getAll()\n      .then(setProducts)\n      .finally(() => setLoading(false));\n  }, [repo]);\n\n  const filteredProducts = useMemo(() => {\n    return products.filter(p => \n      p.title.toLowerCase().includes(searchQuery.toLowerCase())\n    );\n  }, [products, searchQuery]);\n\n  return {\n    products: filteredProducts,\n    loading,\n    searchQuery,\n    setSearchQuery,\n  };\n};",
                "explanation": "Encapsulates filtering, network loading state, and reactive state outside the view, making it 100% unit-testable without rendering any JSX."
            },
            {
                "title": "View Layer: Thin UI Component",
                "language": "typescript",
                "code": "import React from 'react';\nimport { View, FlatList, TextInput, Text, ActivityIndicator } from 'react-native';\nimport { useProductCatalogViewModel } from '../viewmodels/useProductCatalog';\nimport { ApiProductRepository } from '../repositories/ProductRepository';\n\nconst repo = new ApiProductRepository();\n\nexport const ProductCatalogScreen = () => {\n  const { products, loading, searchQuery, setSearchQuery } = useProductCatalogViewModel(repo);\n\n  if (loading) return <ActivityIndicator size=\"large\" style={{ flex: 1 }} />;\n\n  return (\n    <View style={{ flex: 1, padding: 16 }}>\n      <TextInput\n        placeholder=\"Search products...\"\n        value={searchQuery}\n        onChangeText={setSearchQuery}\n        style={{ height: 40, borderWidth: 1, borderRadius: 8, paddingHorizontal: 12, marginBottom: 12 }}\n      />\n      <FlatList\n        data={products}\n        keyExtractor={(item) => item.id}\n        renderItem={({ item }) => (\n          <View style={{ padding: 12, borderBottomWidth: 1, borderColor: '#EEE' }}>\n            <Text style={{ fontWeight: 'bold' }}>{item.title}</Text>\n            <Text>${item.price.toFixed(2)}</Text>\n          </View>\n        )}\n      />\n    </View>\n  );\n};",
                "explanation": "The View contains zero complex data transformations or HTTP calls—it merely displays ViewModel state and forwards user inputs."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Repository In-Memory Mock Implementation",
            description="Create a mock class `MockUserRepository` implementing `{ getById(id: string): Promise<{ id: string; name: string } | null> }` using an internal array of users `[{ id: '1', name: 'Alice' }, { id: '2', name: 'Bob' }]`.",
            starter_code="export class MockUserRepository {\n  // Implement getById(id) method\n}",
            solution_code="export class MockUserRepository {\n  private users = [\n    { id: '1', name: 'Alice' },\n    { id: '2', name: 'Bob' }\n  ];\n\n  async getById(id: string): Promise<{ id: string; name: string } | null> {\n    const user = this.users.find(u => u.id === id);\n    return user || null;\n  }\n}",
            expected_output="new MockUserRepository().getById('1') resolves to { id: '1', name: 'Alice' }"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary benefit of the Model-View-ViewModel (MVVM) pattern in mobile apps?",
                options=[
                    "It separates visual presentation from business logic, making code easier to test, maintain, and reuse",
                    "It automatically doubles the CPU speed of the mobile device",
                    "It compiles React Native into C++ without using JavaScript",
                    "It ensures apps never use memory"
                ],
                correct_answer="It separates visual presentation from business logic, making code easier to test, maintain, and reuse",
                explanation="MVVM isolates business rules inside ViewModels/hooks, leaving Views clean and declarative."
            ),
            QuizQuestionBlueprint(
                question="In React Native, what commonly serves as the 'ViewModel'?",
                options=[
                    "Custom React hooks that manage state, computations, and handlers",
                    "HTML <div> elements",
                    "The device camera lens",
                    "The Google Play Console"
                ],
                correct_answer="Custom React hooks that manage state, computations, and handlers",
                explanation="Custom hooks (e.g. `useCourseList`) encapsulate state, async queries, and handlers, acting as the ViewModel."
            ),
            QuizQuestionBlueprint(
                question="What does the Repository Pattern achieve?",
                options=[
                    "It abstracts the data source (API, local DB, cache) behind a consistent interface so the UI layer is agnostic to where data originates",
                    "It creates a Git repository on the user's phone",
                    "It downloads all internet data at midnight",
                    "It renders 3D graphics using WebGL"
                ],
                correct_answer="It abstracts the data source (API, local DB, cache) behind a consistent interface so the UI layer is agnostic to where data originates",
                explanation="Repositories provide clean data access interfaces, decoupling networking or database technologies from screens."
            ),
            QuizQuestionBlueprint(
                question="Why should raw HTTP `fetch()` calls be avoided directly inside JSX components?",
                options=[
                    "It tightly couples the UI to API endpoints, duplicates error handling, and complicates unit testing",
                    "Fetch calls are strictly illegal in React Native",
                    "Browsers will block all phones from accessing servers",
                    "It causes the phone screen to turn grayscale"
                ],
                correct_answer="It tightly couples the UI to API endpoints, duplicates error handling, and complicates unit testing",
                explanation="Scattering API calls across JSX makes UI testing difficult and leads to brittle, hard-to-maintain code."
            ),
            QuizQuestionBlueprint(
                question="What is Dependency Injection in software architecture?",
                options=[
                    "Passing dependencies (like API services) into a component or hook from outside rather than hardcoding them inside",
                    "Injecting malware into mobile apps",
                    "Installing packages using npm without internet",
                    "A hardware tool used to repair broken smartphone screens"
                ],
                correct_answer="Passing dependencies (like API services) into a component or hook from outside rather than hardcoding them inside",
                explanation="Dependency Injection makes systems modular and testable by letting you pass mock services during unit tests."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 38
    # -------------------------------------------------------------
    DayBlueprint(
        order=38,
        title="Day 38: Memory Management & Unit/UI Testing",
        concept="Diagnosing memory leaks, optimizing re-renders, and writing automated tests with Jest and React Native Testing Library",
        analogy="Think of building an app like engineering a race car. You wouldn't enter a championship race without checking for oil leaks (memory profiler) or testing that the brakes work properly under stress (automated unit tests). Testing gives you the confidence to drive fast and make code changes without fear of breaking the engine!",
        theory_sections=[
            {
                "heading": "Identifying & Preventing Mobile Memory Leaks",
                "body": "Common memory leaks in mobile apps stem from uncleaned event listeners, unclosed WebSocket connections, lingering timers (`setInterval`), and holding references to heavy unmounted views. In React Native, always return cleanup functions in `useEffect`, avoid creating inline closures in FlatList renderItem props, and utilize React Developer Tools and the Xcode/Android Studio Memory Profiler."
            },
            {
                "heading": "Automated Testing: Jest & React Native Testing Library (RNTL)",
                "body": "Automated testing guarantees that existing features don't break when you add new code. **Unit tests** test isolated functions and algorithms with Jest. **Component integration tests** use `@testing-library/react-native` to render components in a mock environment, simulate button presses (`fireEvent.press`), and assert that expected texts appear on screen."
            }
        ],
        code_snippets=[
            {
                "title": "Preventing Memory Leaks with Proper useEffect Cleanup",
                "language": "typescript",
                "code": "import { useEffect } from 'react';\nimport { AppState, AppStateStatus } from 'react-native';\n\nexport const useAppStateListener = (onChange: (status: AppStateStatus) => void) => {\n  useEffect(() => {\n    const subscription = AppState.addEventListener('change', onChange);\n\n    // CRITICAL: Always return cleanup function to unregister listeners\n    return () => {\n      subscription.remove();\n    };\n  }, [onChange]);\n};",
                "explanation": "Failing to remove event subscriptions or intervals causes components to remain referenced in memory after unmounting."
            },
            {
                "title": "Writing a Pure Unit Test in Jest",
                "language": "typescript",
                "code": "// mathUtils.test.ts\nexport function calculateDiscount(price: number, discountPercent: number): number {\n  if (discountPercent < 0 || discountPercent > 100) throw new Error('Invalid discount');\n  return Number((price * (1 - discountPercent / 100)).toFixed(2));\n}\n\ndescribe('calculateDiscount', () => {\n  it('correctly calculates 20% off 100', () => {\n    expect(calculateDiscount(100, 20)).toBe(80);\n  });\n\n  it('throws error for invalid discount percent', () => {\n    expect(() => calculateDiscount(100, 150)).toThrow('Invalid discount');\n  });\n});",
                "explanation": "Jest runs unit tests directly in Node.js at lightning speed, verifying algorithm correctness across edge cases."
            },
            {
                "title": "Component Testing with React Native Testing Library",
                "language": "typescript",
                "code": "import React from 'react';\nimport { render, fireEvent } from '@testing-library/react-native';\nimport { CounterScreen } from '../screens/CounterScreen';\n\ndescribe('CounterScreen Integration Test', () => {\n  it('increments the counter when button is clicked', () => {\n    const { getByText } = render(<CounterScreen />);\n\n    expect(getByText('Count: 0')).toBeTruthy();\n\n    const incrementButton = getByText('Increment');\n    fireEvent.press(incrementButton);\n\n    expect(getByText('Count: 1')).toBeTruthy();\n  });\n});",
                "explanation": "Renders the actual component tree in a simulated environment and asserts user-visible behavior upon interaction."
            },
            {
                "title": "Mocking API Services in Jest",
                "language": "typescript",
                "code": "import { renderHook, waitFor } from '@testing-library/react-native';\nimport { useProductCatalogViewModel } from '../viewmodels/useProductCatalog';\n\nconst mockRepo = {\n  getAll: jest.fn().mockResolvedValue([\n    { id: '1', title: 'React Native Handbook', price: 29.99 }\n  ]),\n  getById: jest.fn(),\n};\n\ntest('loads products on hook mount', async () => {\n  const { result } = renderHook(() => useProductCatalogViewModel(mockRepo));\n\n  expect(result.current.loading).toBe(true);\n  await waitFor(() => expect(result.current.loading).toBe(false));\n  expect(result.current.products.length).toBe(1);\n});",
                "explanation": "Mocks the repository layer with `jest.fn()` so tests run predictably without relying on real internet or backend databases."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Safe Discount Calculator Test Harness",
            description="Write a function `validateAndCalculateTotal(prices: number[], taxRate: number): number` that validates all prices are positive numbers, adds them up, applies taxRate (e.g. 0.1 for 10%), and returns the rounded total.",
            starter_code="export function validateAndCalculateTotal(prices: number[], taxRate: number): number {\n  // Sum valid prices and apply taxRate\n}",
            solution_code="export function validateAndCalculateTotal(prices: number[], taxRate: number): number {\n  const validPrices = prices.filter(p => typeof p === 'number' && p > 0);\n  const subtotal = validPrices.reduce((sum, p) => sum + p, 0);\n  const total = subtotal * (1 + (taxRate || 0));\n  return Number(total.toFixed(2));\n}",
            expected_output="validateAndCalculateTotal([10, 20, 30], 0.1) === 66.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the leading cause of memory leaks in React Native components?",
                options=[
                    "Neglecting to remove event listeners, intervals, and subscriptions in useEffect cleanup functions",
                    "Using CSS Flexbox instead of Absolute positioning",
                    "Writing code in TypeScript instead of JavaScript",
                    "Having more than 3 colors in a stylesheet"
                ],
                correct_answer="Neglecting to remove event listeners, intervals, and subscriptions in useEffect cleanup functions",
                explanation="Active subscriptions and uncleaned timers retain references to unmounted components, causing memory bloat."
            ),
            QuizQuestionBlueprint(
                question="What is the purpose of React Native Testing Library (RNTL)?",
                options=[
                    "To test components from the user's perspective by interacting with rendered elements and verifying visual output",
                    "To download apps from the Google Play Store automatically",
                    "To check battery voltage on smartphones",
                    "To compress video files"
                ],
                correct_answer="To test components from the user's perspective by interacting with rendered elements and verifying visual output",
                explanation="RNTL tests how users experience your app (text visibility, button taps) rather than implementation details."
            ),
            QuizQuestionBlueprint(
                question="How do you simulate a button tap when writing a component test in RNTL?",
                options=[
                    "fireEvent.press(buttonElement)",
                    "click(buttonElement)",
                    "screen.tapHardware()",
                    "window.triggerClick()"
                ],
                correct_answer="fireEvent.press(buttonElement)",
                explanation="`fireEvent.press(element)` triggers the press event handlers defined on React Native touchable components."
            ),
            QuizQuestionBlueprint(
                question="Why is `useCallback` used when passing functions to list item components in FlatList?",
                options=[
                    "It memoizes function references so child components don't unnecessarily re-render on every parent cycle",
                    "It translates the function into Swift",
                    "It uploads the function to AWS",
                    "It changes the color of the button"
                ],
                correct_answer="It memoizes function references so child components don't unnecessarily re-render on every parent cycle",
                explanation="useCallback prevents creating new function instances on each render, preserving memoized child component optimizations."
            ),
            QuizQuestionBlueprint(
                question="What command executes Jest unit and component tests in a React Native project?",
                options=[
                    "npm test (or npx jest)",
                    "npm run build:ios",
                    "expo start --tunnel",
                    "adb logcat"
                ],
                correct_answer="npm test (or npx jest)",
                explanation="`npm test` or `npx jest` executes test suites and outputs passing/failing assertions to the console."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 39
    # -------------------------------------------------------------
    DayBlueprint(
        order=39,
        title="Day 39: App Signing, Keystores & Store Guidelines",
        concept="Generating Android upload keystores, configuring iOS provisioning profiles, and meeting Apple App Store & Google Play submission guidelines",
        analogy="Think of app signing like getting a tamper-proof wax seal and digital passport for your software. Anyone could write an app and claim 'this is the official Hunar app.' A cryptographic keystore signs the bundle with your unique private key. The Google Play and Apple App Stores verify the seal—guaranteeing to millions of users that the app is authentic, unmodified, and safe to install!",
        theory_sections=[
            {
                "heading": "Android Signing (Keystore & AABs) vs iOS Certificates",
                "body": "For Android, you generate a private `.keystore` file using `keytool` and configure Gradle to sign your Android App Bundle (`.aab`). Google Play uses Play Feature Delivery and App Signing to optimize download sizes for end users. For iOS, you need an Apple Developer Account, a Distribution Certificate, an App ID with capabilities, and a Provisioning Profile that pairs your certificate with your app bundle identifier."
            },
            {
                "heading": "Navigating App Store Review Guidelines",
                "body": "Both stores enforce strict compliance rules: (1) **Privacy**: You must declare all collected user data and provide an in-app Account Deletion button (mandatory on Apple & Google); (2) **Purchases**: Digital goods must use Apple/Google In-App Purchases (IAP), while physical goods can use Stripe/PayPal; (3) **Stability**: Apps that crash on launch or display broken webviews are rejected immediately."
            }
        ],
        code_snippets=[
            {
                "title": "Generating an Android Upload Keystore with keytool",
                "language": "bash",
                "code": "# Run in terminal to generate a 2048-bit RSA private keystore\nkeytool -genkeypair -v -storetype PKCS12 -keystore my-upload-key.keystore \\\n  -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000",
                "explanation": "Generates a cryptographically secure key pair used to sign Android APKs and AABs before upload to Google Play."
            },
            {
                "title": "Configuring Gradle Signing Credentials (android/app/build.gradle)",
                "language": "groovy",
                "code": "android {\n    signingConfigs {\n        release {\n            if (project.hasProperty('MYAPP_UPLOAD_STORE_FILE')) {\n                storeFile file(MYAPP_UPLOAD_STORE_FILE)\n                storePassword MYAPP_UPLOAD_STORE_PASSWORD\n                keyAlias MYAPP_UPLOAD_KEY_ALIAS\n                keyPassword MYAPP_UPLOAD_KEY_PASSWORD\n            }\n        }\n    }\n    buildTypes {\n        release {\n            signingConfig signingConfigs.release\n            minifyEnabled true\n            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'\n        }\n    }\n}",
                "explanation": "Configures Gradle release builds to sign the binary with the keystore while keeping credentials safely in `gradle.properties`."
            },
            {
                "title": "Declaring Mandatory Privacy Permissions in app.json",
                "language": "javascript",
                "code": "{\n  \"expo\": {\n    \"ios\": {\n      \"bundleIdentifier\": \"com.hunar.mobileapp\",\n      \"infoPlist\": {\n        \"NSCameraUsageDescription\": \"This app requires camera access to allow you to take profile pictures.\",\n        \"NSPhotoLibraryUsageDescription\": \"This app needs photo library access so you can upload homework assignments.\"\n      }\n    },\n    \"android\": {\n      \"package\": \"com.hunar.mobileapp\",\n      \"permissions\": [\"CAMERA\", \"READ_EXTERNAL_STORAGE\"]\n    }\n  }\n}",
                "explanation": "Apple requires descriptive human-readable strings explaining why permissions are needed. Missing strings cause automatic rejection during store review."
            },
            {
                "title": "Mandatory Account Deletion Request Implementation",
                "language": "typescript",
                "code": "import React from 'react';\nimport { Alert, Button } from 'react-native';\nimport { deleteUserAccountFromDatabase } from '../services/authService';\n\nexport const DeleteAccountButton = ({ userId }: { userId: string }) => {\n  const handleDelete = () => {\n    Alert.alert(\n      'Delete Account',\n      'Are you sure you want to permanently delete your account and all associated data? This action cannot be undone.',\n      [\n        { text: 'Cancel', style: 'cancel' },\n        { text: 'Delete', style: 'destructive', onPress: () => deleteUserAccountFromDatabase(userId) }\n      ]\n    );\n  };\n\n  return <Button title=\"Delete My Account\" color=\"#EF4444\" onPress={handleDelete} />;\n};",
                "explanation": "Both Apple (App Store Review Guideline 5.1.1) and Google Play mandate that any app supporting account creation must allow users to delete their account directly within the app."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="App Bundle Identifier Validator",
            description="Write a validator `isValidBundleId(bundleId: string): boolean` that verifies an Android/iOS bundle ID follows reverse-domain notation (e.g., `com.company.appname`, at least 3 dot-separated segments of lowercase letters and numbers).",
            starter_code="export function isValidBundleId(bundleId: string): boolean {\n  // Validate reverse-domain bundle identifier\n}",
            solution_code="export function isValidBundleId(bundleId: string): boolean {\n  const regex = /^[a-z][a-z0-9_]*(\\.[a-z0-9_]+){2,}$/;\n  return regex.test(bundleId);\n}",
            expected_output="isValidBundleId('com.hunar.app') === true"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is the `.keystore` private key critical for Android developers?",
                options=[
                    "If lost, you can never update or push new versions of that existing app on Google Play under the same package name",
                    "It charges money from your bank account every time it compiles",
                    "It turns the app into an iOS app automatically",
                    "It is only used to change the app's desktop wallpaper"
                ],
                correct_answer="If lost, you can never update or push new versions of that existing app on Google Play under the same package name",
                explanation="The upload keystore cryptographically proves ownership of the application. Losing it prevents uploading subsequent updates."
            ),
            QuizQuestionBlueprint(
                question="What is an Android App Bundle (`.aab`) compared to a traditional `.apk`?",
                options=[
                    "A publishing format that lets Google Play generate device-optimized APKs containing only the resources needed for each user's specific screen and architecture",
                    "A virus scanning tool used by antivirus software",
                    "A special file format that only plays music",
                    "An APK that has been encrypted with a password"
                ],
                correct_answer="A publishing format that lets Google Play generate device-optimized APKs containing only the resources needed for each user's specific screen and architecture",
                explanation="AABs allow Google Play to serve dynamic, optimized APKs tailored to each user's device, significantly reducing download sizes."
            ),
            QuizQuestionBlueprint(
                question="Under Apple App Store Guideline 5.1.1, what feature is mandatory for any app that allows user account registration?",
                options=[
                    "An in-app mechanism for users to permanently delete their account and associated personal data",
                    "A dark mode toggle on the home screen",
                    "A link to play Apple Arcade games",
                    "A subscription price of at least $9.99"
                ],
                correct_answer="An in-app mechanism for users to permanently delete their account and associated personal data",
                explanation="Apple and Google strictly mandate that apps allowing account creation must provide an easy, discoverable in-app account deletion mechanism."
            ),
            QuizQuestionBlueprint(
                question="What payment system must be used when selling digital courses or virtual coins inside an iOS app?",
                options=[
                    "Apple In-App Purchases (StoreKit)",
                    "Cash on Delivery",
                    "Cryptocurrency only",
                    "Direct bank wire transfer instructions on screen"
                ],
                correct_answer="Apple In-App Purchases (StoreKit)",
                explanation="Apple requires StoreKit In-App Purchases for digital content consumed within the app."
            ),
            QuizQuestionBlueprint(
                question="Why must iOS apps include usage description strings (e.g. `NSCameraUsageDescription`) in `Info.plist`?",
                options=[
                    "Apple uses these strings in the system permission prompt to explain to the user why the app needs access to hardware",
                    "It determines how fast the camera shutter clicks",
                    "It is only read by Siri for voice search",
                    "It tells the phone how much storage space to allocate"
                ],
                correct_answer="Apple uses these strings in the system permission prompt to explain to the user why the app needs access to hardware",
                explanation="Missing privacy usage strings trigger an instant build rejection when uploading to App Store Connect."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 40
    # -------------------------------------------------------------
    DayBlueprint(
        order=40,
        title="Day 40 (Capstone): Beta Testing, Crash Analytics & CI/CD Deployment",
        concept="Automating builds with EAS Build / GitHub Actions, monitoring crashes with Sentry / Crashlytics, and distributing beta builds to TestFlight & Google Play Internal Testing",
        analogy="Think of shipping a mobile app like launching a commercial rocket. You don't build the rocket by hand in your backyard and hope for the best on launch day. You build an automated robotic assembly line (CI/CD pipeline), conduct rigorous test flights with test pilots (TestFlight / Google Play Beta), and equip the spacecraft with black-box flight data recorders (Sentry/Crashlytics) so if anything hiccups, you know the exact line of code that triggered it!",
        theory_sections=[
            {
                "heading": "Continuous Integration & Cloud Builds (EAS Build / Fastlane)",
                "body": "Compiling mobile binaries natively requires dedicated macOS environments for iOS and heavy Android SDKs. Tools like Expo Application Services (`eas build`) or GitHub Actions with Fastlane automate the entire compilation process in the cloud: linting code, running unit test suites, incrementing build version numbers, signing binaries, and distributing them to app stores automatically on every git commit."
            },
            {
                "heading": "Beta Distribution & Real-Time Crash Monitoring",
                "body": "Never release directly to 100% of production users. Use Apple TestFlight and Google Play Internal Testing to distribute beta builds to internal team members and beta testers. Integrate crash reporting SDKs (Sentry, Firebase Crashlytics) to capture uncaught JavaScript exceptions, native crashes, breadcrumbs, device battery levels, and stack traces in real time before users leave negative reviews."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring Cloud Builds with eas.json",
                "language": "json",
                "code": "{\n  \"cli\": { \"version\": \">= 5.0.0\" },\n  \"build\": {\n    \"development\": {\n      \"developmentClient\": true,\n      \"distribution\": \"internal\"\n    },\n    \"preview\": {\n      \"distribution\": \"internal\",\n      \"android\": { \"buildType\": \"apk\" }\n    },\n    \"production\": {\n      \"autoIncrement\": true,\n      \"android\": { \"buildType\": \"app-bundle\" },\n      \"ios\": { \"simulator\": false }\n    }\n  },\n  \"submit\": {\n    \"production\": {}\n  }\n}",
                "explanation": "Defines reproducible cloud build profiles for local development, internal QA testing, and production store deployment."
            },
            {
                "title": "Integrating Real-time Error Monitoring with Sentry",
                "language": "typescript",
                "code": "import * as Sentry from '@sentry/react-native';\n\nSentry.init({\n  dsn: 'https://examplePublicKey@o0.ingest.sentry.io/0',\n  enableInExpoDevelopment: false,\n  debug: false,\n  tracesSampleRate: 1.0,\n});\n\n// Wrap your Root App Component with Sentry Error Boundary\nexport default Sentry.wrap(App);",
                "explanation": "Initializes Sentry to automatically intercept unhandled promise rejections, native crashes, and UI freezes with stack traces."
            },
            {
                "title": "Capturing Custom Error Breadcrumbs and User Context",
                "language": "typescript",
                "code": "import * as Sentry from '@sentry/react-native';\n\nexport const logUserBreadcrumb = (category: string, message: string) => {\n  Sentry.addBreadcrumb({\n    category,\n    message,\n    level: 'info',\n  });\n};\n\nexport const reportErrorWithContext = (error: Error, extraData: Record<string, any>) => {\n  Sentry.withScope((scope) => {\n    scope.setExtras(extraData);\n    Sentry.captureException(error);\n  });\n};",
                "explanation": "Enriches crash reports with the trail of user actions leading up to the error, making reproduction and debugging trivial."
            },
            {
                "title": "GitHub Actions CI/CD Pipeline Workflow (.github/workflows/deploy.yml)",
                "language": "yaml",
                "code": "name: Mobile CI/CD Pipeline\non:\n  push:\n    branches: [main]\n\njobs:\n  test_and_build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v3\n      - uses: actions/setup-node@v3\n        with:\n          node-version: 18\n      - run: npm ci\n      - run: npm test\n      - name: Setup Expo\n        uses: expo/expo-github-action@v8\n        with:\n          expo-version: latest\n          token: ${{ secrets.EXPO_TOKEN }}\n      - name: Build and Deploy Production\n        run: eas build --platform all --profile production --non-interactive --auto-submit",
                "explanation": "Automates the entire lifecycle: checks out code, runs automated tests, triggers cloud binary builds, and auto-submits to app stores."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Semantic Version Bump Utility",
            description="Write a utility function `bumpSemanticVersion(version: string, type: 'major' | 'minor' | 'patch'): string` that takes a semantic version like '1.2.3' and increments the correct segment.",
            starter_code="export function bumpSemanticVersion(version: string, type: 'major' | 'minor' | 'patch'): string {\n  // Increment semantic version\n}",
            solution_code="export function bumpSemanticVersion(version: string, type: 'major' | 'minor' | 'patch'): string {\n  const parts = version.split('.').map(Number);\n  if (parts.length !== 3 || parts.some(isNaN)) return version;\n  if (type === 'major') {\n    return `${parts[0] + 1}.0.0`;\n  } else if (type === 'minor') {\n    return `${parts[0]}.${parts[1] + 1}.0`;\n  } else {\n    return `${parts[0]}.${parts[1]}.${parts[2] + 1}`;\n  }\n}",
            expected_output="bumpSemanticVersion('1.2.3', 'minor') === '1.3.0'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the role of Apple TestFlight in the iOS deployment lifecycle?",
                options=[
                    "It distributes prerelease beta builds to up to 10,000 testers with automated crash and feedback reporting before public App Store release",
                    "It books commercial airline tickets inside your mobile app",
                    "It increases iPhone battery life by 50%",
                    "It converts React Native code into Java"
                ],
                correct_answer="It distributes prerelease beta builds to up to 10,000 testers with automated crash and feedback reporting before public App Store release",
                explanation="TestFlight enables structured beta testing for internal and external testers prior to publishing on the public App Store."
            ),
            QuizQuestionBlueprint(
                question="What is a 'breadcrumb' in crash analytics tools like Sentry and Firebase Crashlytics?",
                options=[
                    "A chronological log of user events, screen transitions, and network requests leading right up to the crash",
                    "Food particles left on the smartphone touch screen",
                    "A special type of cookie stored in Safari",
                    "The app icon displayed on the home screen"
                ],
                correct_answer="A chronological log of user events, screen transitions, and network requests leading right up to the crash",
                explanation="Breadcrumbs trace the exact steps the user took before an exception occurred, making bug reproduction straightforward."
            ),
            QuizQuestionBlueprint(
                question="What is the benefit of using a cloud build system like EAS Build?",
                options=[
                    "Developers don't need a powerful physical Mac computer or local Android SDK setup to compile signed iOS and Android production binaries",
                    "It prevents users from ever uninstalling the application",
                    "It guarantees that apps receive 5-star ratings on Google Play",
                    "It hosts the backend database for free"
                ],
                correct_answer="Developers don't need a powerful physical Mac computer or local Android SDK setup to compile signed iOS and Android production binaries",
                explanation="EAS Build compiles native binaries in the cloud on managed macOS and Linux runners, eliminating local native tooling headaches."
            ),
            QuizQuestionBlueprint(
                question="What is Staged Rollout (Phased Release) on Google Play and Apple App Store?",
                options=[
                    "Releasing an update to a small percentage of users (e.g. 5%, 10%) initially to monitor crash rates before rolling out to 100%",
                    "Releasing the app only during daytime hours",
                    "Distributing the app on DVD discs",
                    "Translating the app into one language per month"
                ],
                correct_answer="Releasing an update to a small percentage of users (e.g. 5%, 10%) initially to monitor crash rates before rolling out to 100%",
                explanation="Phased rollouts protect your entire user base by catching unforeseen production bugs on a small percentage of users first."
            ),
            QuizQuestionBlueprint(
                question="Why is CI/CD (Continuous Integration and Continuous Deployment) crucial for high-velocity mobile engineering teams?",
                options=[
                    "It automates linting, test suites, build compilation, and store delivery, catching regressions early and eliminating manual human error",
                    "It writes all application features automatically without human programmers",
                    "It bypasses all Apple and Google App Store review policies",
                    "It eliminates the need for software design architecture"
                ],
                correct_answer="It automates linting, test suites, build compilation, and store delivery, catching regressions early and eliminating manual human error",
                explanation="CI/CD pipelines automate testing and deployment steps, ensuring every release is reliably tested, built, and delivered."
            )
        ]
    )
]
