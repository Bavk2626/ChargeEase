// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDZmiSBPCUpRfCkegjATrEe1057S4j_r1Q",
  authDomain: "chargeease-21f68.firebaseapp.com",
  databaseURL: "https://chargeease-21f68-default-rtdb.firebaseio.com",
  projectId: "chargeease-21f68",
  storageBucket: "chargeease-21f68.appspot.com",
  messagingSenderId: "255861292061",
  appId: "1:255861292061:web:2ae5ca02d54a45419a5af4",
  measurementId: "G-R1Y1JTCJ42"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);