////////////////////
// PRINT AN ARRAY
////////////////////

// create variable string and set that to an empty string
// loop over the array and push each element into the variable string with \n (newline)
// return string

// arr = ['sam', 'ed', 'harry']
//
// function printArr(arr){
//   let string = "";
//   for(let i = 0; i < arr.length; i++){
//     string = string + `${arr[i]} \n`
//   }
//   return string;
// }
// console.log(printArr(arr));


////////////////////
// REVERSE A STRING
////////////////////

// set variable reverse to an empty string
// begin looping over the string starting with the last element
// push this element to the new string reverse
// continue until all elements have been looped over
// return reverse

// str = "abcd"
//
// function reverseString(str){
//   let reverse = "";
//   for(let i = (str.length - 1); i >= 0; i--){
//     reverse += str[i];
//     // reverse = reverse + str[i];
//   }
//   return reverse
// }
//
// console.log(reverseString(str));


////////////////////
// PALINDROME
////////////////////

// create two variables
// str to remove spaces and set all characters to lowercase
// reverse to do the same as str, but also reverse the STRING
// check if the reverse and the str are the same
// if they are return true, else return false

// str1 = "Race Car";
// str2 = "12321";
// str3 = "race car";
// str4 = "taco";
// str5 = "radar"
//
// function isPalindrome(str){
//   str = str.toLowerCase().replace(' ', '')
//   reverse = str.toLowerCase().replace(' ', '').split('').reverse('').join('')
//   if (str == reverse){
//     return true;
//   }else{
//     return false;
//   }
// }
// console.log(isPalindrome(str1));
// console.log(isPalindrome(str2));
// console.log(isPalindrome(str3));
// console.log(isPalindrome(str4));
// console.log(isPalindrome(str5));


////////////////////
// FIND LARGEST NUMBER
////////////////////

// create a variable called max and set it to either the first element in the array or -Infinity
// loop over the array and if the current element in the array is greater than max, set it to the new max
// loop over each element in the array
// return max

// arr = [1,2,15,10]
//
// function largestNumber(arr){
//   let max = -Infinity;
//   for(i = 0; i < arr.length; i++){
//     if(arr[i] > max){
//       max = arr[i];
//     }
//   }
//   return max;
// }
// console.log(largestNumber(arr));


////////////////////
// PRINT A PYRAMID
////////////////////

// create a constant for the '^' symbol
// start with a single symbol by setting const symbolCount = 1
// create spaceCount variable and set it equal to the number of rows we want - 1
// create a variable pyramid and set it to an empty string
// we start by looping over the number of rows we have
  // for each row except for the last one, we add a number of spaces equal to the space count
  // for each row we add 2 symbols
  // after each loop over the rows, we decrease the spaceCount by 1 and increase the symbolCount by 2
  // we then add the string for that row to the pyramid STRING
// return pyramid

// function buildPyramid(rows){
//   const symbol = '^';
//   let symbolCount = 1;
//   let spaceCount = rows - 1;
//   let pyramid = '';
//   for(let i = 0; i < rows; i++){
//     let str = '';
//     for(let j = 0; j < spaceCount; j++){
//       str += ' ';
//     }
//     for(let k = 0; k < symbolCount; k++){
//       str += symbol;
//     }
//     spaceCount -= 1;
//     symbolCount += 2;
//     pyramid += `${str} \n`
//   }
//   return pyramid;
// }
// console.log(buildPyramid(4));


////////////////////
// URLify
////////////////////
//
// const input = 'Mr John Smith'
//
// function urlify(input){
//   let newInput = input.replace(/ /g, '%20')
//   return newInput
// }
// console.log(urlify('Mr John Smith'));


//////////////////
// Phone number
//////////////////
//
// const numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]
//
// // Need to return (123)456-7890
//
// function createPhoneNumber(numbers){
//
//   let area = ""
//   let mid = ""
//   let end = ""
//
//   function getArea(){
//     for (i=0; i<3; i++){
//         area = area + numbers[i]
//     }
//     return area;
//   }
//   getArea()
//   // console.log(getArea());
//
//   function getMid(){
//     for (i=3; i<6; i++){
//         mid = mid + numbers[i]
//     }
//     return mid;
//   }
//   getMid()
//   // console.log(getMid());
//
//   function getEnd(){
//     for (i=6; i<10; i++){
//         end = end + numbers[i]
//     }
//     return end;
//   }
//   getEnd()
//   // console.log(getEnd());
//
//   let phone = `(${area}) ${mid}-${end}`
//
//   return phone;
// }
//
// console.log(createPhoneNumber(numbers));


//////////////////
// List Filter
//////////////////
//
// // Return array with strings filtered out
// // Examples:
// // filter_list([1,2,'a','b']) == [1,2]
// // filter_list([1,'a','b',0,15]) == [1,0,15]
// // filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
//
// const list = [1,2,'a','b']
//
// function filter_list(list) {
//
// let items = []
//
//   for(i=0; i<list.length; i++){
//     if(typeof list[i]==='number')
//     items.push(list[i])
//   }
//   return items
// }
// console.log(filter_list(list));


////////////////////////
// Dubstep Song Decoder
////////////////////////
//
// Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.
//
// Example:
// songDecoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
// =>  WE ARE THE CHAMPIONS MY FRIEND
//
// const song = "AWUBBWUBC"
//
// function songDecoder(song){
//
//   let newSong = song.split("WUB")
//   let cleanSong = []
//   let endSong = ""
//
//   for(i=0; i<newSong.length; i++){
//     if(newSong[i] !== ''){
//       cleanSong.push(newSong[i])
//     }
//   }
//   // return cleanSong
//   // console.log(cleanSong);
//
//   for(i=0; i<cleanSong.length; i++){
//     if(i<cleanSong.length-1){
//       endSong = endSong + cleanSong[i] + " "
//     } else {
//       endSong = endSong + cleanSong[i]
//     }
//   }
//   return endSong
//   // console.log(endSong);
// }
//
// console.log(songDecoder(song));


////////////////////////////
// Regex validate PIN code
////////////////////////////

// const pin = "0000"
//
// function validatePIN (pin) {
//
//   let trollFix = pin.replace("0", "1")
//
//   // console.log(trollFix);
//   // console.log(trollFix.length);
//
//   let newNum = parseInt(trollFix)
//
//   if(newNum.toString().length !== trollFix.length){
//     // console.log('false1');
//     return false
//   } else if ((trollFix.length === 4) || (trollFix.length === 6)) {
//     // console.log('true2');
//     return true
//   } else {
//     // console.log('false3');
//     return false
//   }
// }
// validatePIN(pin)


// const numbers = [1, 2, 3, 4, 5]
//
// function removeSmallest(numbers) {
//   throw "TODO: removeSmallest";
//
//   for(i=0; i<numbers.length; i++){
//
//   }
// }

////////////////////////////
// Descending Order
////////////////////////////

// function descendingOrder(n){
//
//   var arr = n;
//   // var arr = [6, 1, 7, 2, 8, 3, 4, 5, 0, 9, 10];
//
//   for (var i = 1; i < arr.length; i++) {
//     for (var j = 0; j < i; j++) {
//       // console.log("this is arr i " + arr[i]);
//       // console.log("this is arr j " + arr[j]);
//       if (arr[i] < arr[j]) {
//         var x = arr[i];
//         arr[i] = arr[j];
//         arr[j] = x;
//       };
//     };
//   };
//   return arr.reverse();
// };
//
// console.log(descendingOrder([4, 5, 5, 2, 1]));




////////////////////////////
// Unique in Order
////////////////////////////

// function uniqueInOrder(it) {
//   // empty arr
//   var result = []
//   // the last element that was iterated over
//   var last
//
//   // iterates over elements in a str or arr
//   for (var i = 0; i < it.length; i++) {
//     // if the element is not the same as the last element, push to new empty arr and set the element as the new last element
//     if (it[i] !== last) {
//       result.push(last = it[i])
//     }
//   }
//   return result
// }
//
// console.log(uniqueInOrder([1,2,2,3,3]));
//
// console.log(uniqueInOrder("AAAABBBCCCDAAAABBC"));


////////////////////////////
// Your Order, Please
////////////////////////////

// function order(words){
//
//   // splits str to an arr
//   var array = words.split(' ');
//
//   // new empty arr to push ordered words to
//   var sortedArray = [];
//
//   // iterates over words in the array
//   for(i = 0; i <= array.length; i++) {
//     // iterates over each char in each word
//     for(j = 0; j < array.length; j++) {
//       // if a char in a word matches the current index, push to new empty arr
//       if(array[j].indexOf(i) >= 0) {
//         sortedArray.push(array[j]);
//       }
//     }
//   }
//   // joins new sorted arr back to a string with spaces between each element
//   return sortedArray.join(' ');
// }
//
// console.log(order("4of Fo1r pe6ople g3ood th5e the2"));
//
// // "is2 Thi1s T4est 3a"
// // "4of Fo1r pe6ople g3ood th5e the2"


////////////////////////////
// IP Validation
////////////////////////////

function isValidIP(str) {
  const octets = str.split('.')               // Split into octets

  return (octets.length === 4) &&             // Ensure str has exactly 4 octets
    octets.reduce((acc, octet) =>             // Check all octets
      (acc === true) &&                       // Ensure prior octets okay
      (String(Number(octet)) === octet) &&    // Ensure octet has no spaces or leading 0's, ...
      (Number(octet) >= 0) &&                 // Ensure octet is 0 or more
      (Number(octet) <= 255)                  // Ensure octet is 255 or less
    , true)
}

console.log(isValidIP('123.045.067.089'));

// True:
// 1.2.3.4
// 123.45.67.89

// False:
// 1.2.3
// 1.2.3.4.5
// 123.456.78.90
// 123.045.067.089
