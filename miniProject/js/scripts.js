// $(document).ready(function(){

//     $('#link').click(function(){
//         alert('Hello World!');
//       });
//     $.ajax({
//         url: 'http://ec2-54-162-20-24.compute-1.amazonaws.com:5000/records',
//         type: 'GET',
//         dataType: 'JSON',
//         success: function (data) {
//             console.log("success");
//         },
//         error: function(error) {
//             console.log(error);
//         }
//     });
  
//   });
  // Initialize the Amazon Cognito credentials provider
// CognitoCachingCredentialsProvider credentialsProvider = new CognitoCachingCredentialsProvider(
//     getApplicationContext(),
//     "us-east-1:7ac11cb9-d270-4c2e-b059-d87c505d2156", // Identity pool ID
//     Regions.US_EAST_1 // Region
// );
// AWS.config.credentials = { "accessKeyId": "ASIAU6AOXXNBQREMP3AI",
//                            "secretAccessKey": "unJuGI4KNJITH7hfX8Tb4ebR7og52GSeKTejT5Ow"};
// AWS.config.region = "us-east-1";
// [
// 'version' => '2016-11-15',
// 'credentials' => Array(
//   'key' = 'ASIAU6AOXXNBQREMP3AI',
//   'secrete' => 'unJuGI4KNJITH7hfX8Tb4ebR7og52GSeKTejT5Ow'
// ),
// 'region' => 'us-east-1',
// 'http' => [
//   'verify' => false 
// ]
// ]

// AWS.config.getCredentials(function(err) {  
//       if (err) {
//         console.log(err.stack);  
//         // credentials not loaded 
//       }
//      else {    
//          console.log("Access key:", AWS.config.credentials.accessKeyId);    
//          console.log("Secret access key:", AWS.config.credentials.secretAccessKey); 
//         } 
// });

var s3 = new AWS.s3({
  'version' : 'latest',
  'credentials' : {
    'key' : 'ASIAU6AOXXNB7HS3IWOP',
    'secrete' : 'VG4fNCVRc3eQBk0cBI2NA+3RAcVv+6GYBW1X0eKb'
  },
  'params': {'Bucket': 'myfirstbucketchuyrm'},
  'region' : 'us-east-1',
  'http' : {
    'verify' : false 
  }
});


s3.listObjects({Delimiter: '/'}, function(err, data) {
    if (err) {
      return alert('There was an error listing your albums: ' + err.message);
    } else {
      var message = data.length;
      console.log(message);
    }
      
  });

// // register callbacks on request to retrieve response data
// request.on('success', function(response) {
//   console.log(response.data);
// });
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