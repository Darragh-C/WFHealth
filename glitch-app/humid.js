// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDS6JXFWi4ZsamMwq4FQ2qNYynqA3yApGk",
    authDomain: "pibell-893ac.firebaseapp.com",
    databaseURL: "https://pibell-893ac-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "pibell-893ac",
    storageBucket: "pibell-893ac.appspot.com",
    messagingSenderId: "995656943564",
    appId: "1:995656943564:web:ffc2146267a359994dff69"
};

firebase.initializeApp(firebaseConfig);


// Get a reference to the file storage service
const storage = firebase.storage();
// Get a reference to the database service
const database = firebase.database();



const thRef = database.ref("temperature_and_humidity");

let dateInst = new Date();
let day = dateInst.getDate();
let month = dateInst.getMonth() + 1;
let year = dateInst.getFullYear();
let today = day + '/' + month + '/' + year;

// GET CURRENT TEMPERATURE AND HUMIDITY
thRef.limitToLast(1).on("value", function(snapshot) {
  snapshot.forEach(function(childSnapshot) {

    const humid = childSnapshot.val()["humidity"];
    const time = childSnapshot.val()["date"];




    document.getElementById("humid").innerText = humid;
    document.getElementById("time").innerText = time;

  });
});

// GET AVERAGE TEMPERATURE


let humidReadingsToday = [];

thRef.on("value", function(snapshot) {
  snapshot.forEach(function(childSnapshot) {
    const timestamp = childSnapshot.val()["date"];

    if (timestamp.slice(0,10) == today) {
  
        const humids = childSnapshot.val()["humidity"];

        humidReadingsToday.push(humids);
    }
  

    let humidSum = humidReadingsToday.reduce((partialHumidSum, a) => partialHumidSum + a, 0);
    let humidAvg = humidSum/humidReadingsToday.length;
    
    



  
    document.getElementById("avgHumidtoday").innerText = humidAvg;
    

  });
});