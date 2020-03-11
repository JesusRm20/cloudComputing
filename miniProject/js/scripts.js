$(document).ready(function(){

    $('#link').click(function(){
        alert('Hello World!');
      });
  
  });
  // Initialize the Amazon Cognito credentials provider
// CognitoCachingCredentialsProvider credentialsProvider = new CognitoCachingCredentialsProvider(
//     getApplicationContext(),
//     "us-east-1:7ac11cb9-d270-4c2e-b059-d87c505d2156", // Identity pool ID
//     Regions.US_EAST_1 // Region
// );
AWS.config.credentials = { "accessKeyId": "ASIAU6AOXXNBQRRPFP6N",
                           "secretAccessKey": "xDdMNZ9tEbkaXaaWjnB3FW20gpO/OJzIXtZG99tS"};
AWS.config.region = "us-east-1";


AWS.config.getCredentials(function(err) {  
      if (err) {
        console.log(err.stack);  
        // credentials not loaded 
      }
     else {    
         console.log("Access key:", AWS.config.credentials.accessKeyId);    
         console.log("Secret access key:", AWS.config.credentials.secretAccessKey); 
        } 
});

var ec2 = new AWS.EC2({region: 'us-east-1', maxRetries: 15, apiVersion: '2016-11-15'})

var request = ec2.describeInstances(function(err) {  
    if (err) {
      console.log(err.stack);  
      // credentials not loaded 
    }
});

// register callbacks on request to retrieve response data
request.on('success', function(response) {
  console.log(response.data);
});
// ec2.us-east-1.amazonaws.com

// const Http = new XMLHttpRequest();
// const url='http://ec2-54-162-20-24.compute-1.amazonaws.com:5000/records';
// Http.open("GET", url);
// Http.setRequestHeader('Content-Type', 'application/xml');
// Http.send();

// Http.onreadystatechange = (e) => {
// console.log(Http.responseText)
// }

// function createCORSRequest(method, url) {
//     var xhr = new XMLHttpRequest();
//     if ("withCredentials" in xhr) {
  
//       // Check if the XMLHttpRequest object has a "withCredentials" property.
//       // "withCredentials" only exists on XMLHTTPRequest2 objects.
//       xhr.open(method, url, true);
//       xhr.send();
  
//     } else if (typeof XDomainRequest != "undefined") {
  
//       // Otherwise, check if XDomainRequest.
//       // XDomainRequest only exists in IE, and is IE's way of making CORS requests.
//       xhr = new XDomainRequest();
//       xhr.open(method, url);
//       xhr.send();
  
//     } else {
  
//       // Otherwise, CORS is not supported by the browser.
//       xhr = null;
  
//     }
//     return xhr;
//   }
  
//   var xhr = createCORSRequest('GET', url);
//   if (!xhr) {
//     throw new Error('CORS not supported');
//   }
//   xhr.getAllResponseHeaders();
//   console.log(xhr.response);