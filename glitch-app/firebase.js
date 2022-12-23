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


const pwrRef = database.ref("power_usage");
const thRef = database.ref("temperature_and_humidity");

let dateInst = new Date();
let day = dateInst.getDate();
let month = dateInst.getMonth() + 1;
let year = dateInst.getFullYear();
let today = day + '/' + month + '/' + year;

// GET CURRENT TEMPERATURE AND HUMIDITY
thRef.limitToLast(1).on("value", function(snapshot) {
  snapshot.forEach(function(childSnapshot) {
    const temp = childSnapshot.val()["temperature"];
    const humid = childSnapshot.val()["humidity"];
    const time = childSnapshot.val()["date"];



    document.getElementById("temp").innerText = temp;
    document.getElementById("humid").innerText = humid;
    document.getElementById("time").innerText = time;

  });
});

// GET AVERAGE TEMPERATURE

let tempReadingsToday = [];
let humidReadingsToday = [];

thRef.on("value", function(snapshot) {
  snapshot.forEach(function(childSnapshot) {
    const timestamp = childSnapshot.val()["date"];

    if (timestamp.slice(0,10) == today) {
        const temps = childSnapshot.val()["temperature"];
        const humids = childSnapshot.val()["humidity"];
        tempReadingsToday.push(temps);
        humidReadingsToday.push(humids);
    }
    let tempSum = tempReadingsToday.reduce((partialTempSum, a) => partialTempSum + a, 0);
    let tempAvg = tempSum/(tempReadingsToday.length);
    let humidSum = humidReadingsToday.reduce((partialHumidSum, a) => partialHumidSum + a, 0);
    let humidAvg = humidSum/humidReadingsToday.length;
    
    



    document.getElementById("avgTemptoday").innerText = tempAvg;
    document.getElementById("avgHumidtoday").innerText = humidAvg;
    

  });
});



//GET LOWEST TEMP
/*
let lowestTemp = 100;

for (let temp in tempReadingsToday) {
  if (temp < lowestTemp) {
     lowestTemp = temp;
  }

//document.getElementById("lowestTemp").innerText = lowestTemp;
*/



// GET TODAY'S POWER USAGE
let todayheaterjoules = [];
let todaydehumidjoules = [];

pwrRef.on("value", function(snapshot) {
    snapshot.forEach(function(childSnapshot) {
      const appl = childSnapshot.val()["appliance"];  
      const date = childSnapshot.val()["date"]; 
     
      
      if (appl == "heater" && date.slice(0,10) == today) {
          const tdhjoules = childSnapshot.val()["joules"];
          todayheaterjoules.push(tdhjoules);
      } else if (appl == "dehumidifier" && date.slice(0,10) == today) {
          const tddjoules = childSnapshot.val()["joules"];
          todaydehumidjoules.push(tddjoules);
      }
      
      //let totalhJoules = heaterjoules.reduce(function(a, b) { return a + b; }, 0);
      const sumhjtd = todayheaterjoules.reduce((partialSumtdhj, a) => partialSumtdhj + a, 0);
      const hkjtd = sumhjtd/1000;
      const sumtddh = todaydehumidjoules.reduce((partialSumtdhj, a) => partialSumtdhj + a, 0);
      const dkjtd = sumtddh/1000;
      
      const total = hkjtd + dkjtd;
      
      //const avg = hkjtd/todayheaterjoules.length
      //document.getElementById("avg").innerText = avg;
  


      document.getElementById("todayhjoules").innerText = hkjtd;
      document.getElementById("todaydjoules").innerText = dkjtd;
      document.getElementById("todayTotalJoules").innerText = total;
  });
});





