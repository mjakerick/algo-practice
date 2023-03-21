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

// function isValidIP(str) {
//   const octets = str.split('.')               // Split into octets
//
//   return (octets.length === 4) &&             // Ensure str has exactly 4 octets
//     octets.reduce((acc, octet) =>             // Check all octets
//       (acc === true) &&                       // Ensure prior octets okay
//       (String(Number(octet)) === octet) &&    // Ensure octet has no spaces or leading 0's, ...
//       (Number(octet) >= 0) &&                 // Ensure octet is 0 or more
//       (Number(octet) <= 255)                  // Ensure octet is 255 or less
//     , true)
// }
//
// console.log(isValidIP('123.045.067.089'));

// True:
// 1.2.3.4
// 123.45.67.89

// False:
// 1.2.3
// 1.2.3.4.5
// 123.456.78.90
// 123.045.067.089


////////////////////////////
// Vowel Words
////////////////////////////

// let words = ['jon', 'ada', 'ppzpp', 'brgggg', 'eric', 'zeke', 'phil', 'ngmn']
//
// function hasVowels(words) {
//   let vowels = ['a', 'e', 'i', 'o', 'u']
//   const vowelWords = [];
//   for(let i = 0; i < words.length; i++){
//     for(let j = 0; j < vowels.length; j++){
//       if(words[i].includes(vowels[j])){
//         vowelWords.push(words[i])
//         break;
//       }
//     }
//   }
//   return vowelWords
// }
//
// console.log(hasVowels(words));


///////////////////////////////////////////////////////////////////////////
// Started the LeetCode grind
///////////////////////////////////////////////////////////////////////////


////////////////////////////
// 1. Two Sum
////////////////////////////

// // We want to return the position of the two numbers whose sum is equivalent to the target
//
// function twoSum(nums, target) {
//   let answer = [];
//   for (i = 0; i < nums.length; i++){
//     for (j = i + 1; j < nums.length; i++){
//       if (nums[i] + nums[j] === target){
//         answer.push(i, j)
//         return answer
//       }
//     }
//   }
//   return answer
// }
//
// console.log(twoSum([2, 7, 11, 15], 9));


////////////////////////////
// 3. Longest Substring Without Repeating Characters
////////////////////////////

function lengthOfLongestSubstring(s) {

}


////////////////////////////
// 9. Palindrome Number
////////////////////////////

// function isPalindrome(x) {
//   // Can use "* Math.sign(x)" to handle negative numbers as numbers instead of strings, which keeps the negative sign at the front of the number instead of at the end
//   reverse = parseFloat(x.toString().split('').reverse().join('')) //* Math.sign(x)
//   if (x == reverse){
//     return true;
//   }else{
//     return false;
//   }
// };
//
// console.log(isPalindrome(213));


////////////////////////////
// 13. Roman to Integer
////////////////////////////

// const romanHash = {
//   I: 1,
//   V: 5,
//   X: 10,
//   L: 50,
//   C: 100,
//   D: 500,
//   M: 1000,
// };
//
// function romanToInt(s) {
// let accumulator = 0;
//
//   for (i = 0; i < s.length; i++){
//     if(s[i] === "I" && s[i + 1] === "V"){
//       accumulator += 4;
//       i++;
//     } else if (s[i] === "I" && s[i + 1] === "X"){
//       accumulator += 9;
//       i++;
//     } else if (s[i] === "X" && s[i + 1] === "L"){
//       accumulator += 40;
//       i++;
//     }else if (s[i] === "X" && s[i + 1] === "C"){
//       accumulator += 90;
//       i++;
//     } else if (s[i] === "C" && s[i + 1] === "D"){
//       accumulator += 400;
//       i++;
//     } else if (s[i] === "C" && s[i + 1] === "M"){
//       accumulator += 900;
//       i++;
//     } else {
//       accumulator += romanHash[s[i]];
//     }
//   }
//   return accumulator;
// }
//
// console.log(romanToInt("MCMXCIV"));


////////////////////////////
// 14. Longest Common Prefix
////////////////////////////

// Write a function to find the longest common prefix string amongst an array of strings.
//
// If there is no common prefix, return an empty string "".
//
// Example 1:
// Input: strs = ["flower","flow","flight"]
// Output: "fl"

// Example 2:
// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.
//
// Constraints:
// 1 <= strs.length <= 200
// 0 <= strs[i].length <= 200
// strs[i] consists of only lowercase English letters.

// function longestCommonPrefix(strs) {
//
//   let answer = "";
//
//   if (strs == null || strs.length == 0) {
//     return answer;
//   }
//
//   let minimumLength = strs[0].length;
//
//   for (let i = 1; i < strs.length; i++) {
//     minimumLength = Math.min(minimumLength, strs[i].length);
//   }
//
//   for (i = 0; i < minimumLength; i++) {
//
//     let letter = strs[0][i]
//
//     for (j = 0; j < strs.length; j++) {
//       if (strs[j][i] != letter) {
//         return answer
//       }
//     }
//     answer += letter;
//   }
//   return answer;
// };
//
// console.log(longestCommonPrefix(["flower","flow","flight"]));


////////////////////////////
// 20. Valid Parentheses
////////////////////////////

// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.

// Example 1:
// Input: s = "()"
// Output: true

// Example 2:
// Input: s = "()[]{}"
// Output: true

// Example 3:
// Input: s = "(]"
// Output: false

// 1 <= s.length <= 104
// s consists of parentheses only '()[]{}'

// function isValid(s) {
//   const stack = [];
//
//   for (let i = 0; i < s.length; i++) {
//
//     const top = stack[stack.length - 1];
//
//     if (s[i] === '(' || s[i] === '{' || s[i] === '[') {
//       stack.push(s[i]);
//     } else if (s[i] === ')' && top === '(' && stack.length !== 0) {
//       stack.pop();
//     } else if (s[i] === ']' && top === '[' && stack.length !== 0) {
//       stack.pop();
//     } else if (s[i] === '}' && top === '{' && stack.length !== 0) {
//       stack.pop();
//     } else {
//       return false;
//     }
//     console.log(stack);
//   }
//
//   return stack.length === 0;
// };
//
// console.log(isValid("()[{(({}){[]})}]"));


////////////////////////////
// 21. Merge Two Sorted Lists
////////////////////////////

// NEED MORE UNDERSTANDING OF LINKED LISTS

// var n3 = new ListNode(4, null);
// var n2 = new ListNode(2, n3);
// var n1 = new ListNode(1, n2);
// var list1 = n1;
//
// var n6 = new ListNode(4, null);
// var n5 = new ListNode(3, n6);
// var n4 = new ListNode(1, n5);
// var list2 = n4;
//
// function ListNode(val, next) {
//   this.val = (val===undefined ? 0 : val)
//   this.next = (val===undefined ? null : next)
// }
//
// function mergeTwoLists(list1, list2) {
//
//   let dummyHead = new ListNode();
//   let tail = dummyHead;
//   let curr1 = list1;
//   let curr2 = list2;
//
//   while(curr1 !== null && curr2 !== null){
//
//     if(curr1.val < curr2.val){
//       tail.next = curr1;
//       curr1 = curr1.next;
//     } else {
//       tail.next = curr2;
//       curr2 = curr2.next;
//     }
//
//     tail = tail.next;
//   }
//
//   if(curr1 !== null) {
//     tail.next = curr1;
//   }
//
//   if(curr2 !== null){
//     tail.next = curr2;
//   }
//
//   return dummyHead.next;
// }
//
// console.log(mergeTwoLists(list1, list2));


////////////////////////////
// 26. Remove Duplicates from Sorted Array
////////////////////////////

// // My answer, works local :p ... isn't working for LeetCode :(
// function removeDuplicates(nums) {
//
//   let k = 0;
//
//   for(i = 0; i < nums.length; i++) {
//     if(nums[i] !== nums[i + 1] && nums[i] !== nums[i - 1]){
//
//     } else {
//       nums.splice(i, 1);
//       k++;
//     }
//   }
//   return {nums, k}
// }
//
// console.log(removeDuplicates([1,1,2]));

// // New answer with research ... works LeetCode poggers :D
// function removeDuplicates(nums){
//   let startingIndex = 0
//
//   for(secondIndex = 1; secondIndex < nums.length; secondIndex++){
//     if(nums[startingIndex] != nums[secondIndex]){
//       startingIndex++
//       nums[startingIndex] = nums[secondIndex]
//     }
//   }
//   return startingIndex + 1
// };
//
// console.log(removeDuplicates([1,1,2]));


////////////////////////////
// 27. Remove Element
////////////////////////////

// function removeElement(nums, val) {
//   let k = 0;
//   // Iterates over array
//   for (i = 0; i < nums.length; i++) {
//     // If current element in arr does not equal the val, change it's position to k
//     // If it does, leave it
//     // This moves relevant value to the front, and items to be removed to the end of the arr
//     if (nums[i] !== val) {
//       nums[k++] = nums[i];
//     }
//   }
//   // We then cut the nums arr length to equal k, which removes elements from nums that are equal to val
//   nums.length = k;
//   return k;
// };
//
// console.log(removeElement([3,2,2,3], val = 3));


////////////////////////////
// 35. Search Insert Position
////////////////////////////

// Happy that I solved this without looking up any syntax or hints :)

// function searchInsert(nums, target) {
//   for (i = 0; i < nums.length; i++) {
//     if (target < nums[0]) {
//       return 0;
//     } else if (nums[i] === target){
//       return i;
//     } else if (nums[i+1] === undefined){
//       return i + 1;
//     } else if (nums[i] !== target && target > nums[i] && target < nums[i+1]) {
//       return i + 1;
//     }
//   }
// }
//
// console.log(searchInsert([2,5], 1));


////////////////////////////
// FIZZ BUZZ BAZZ
////////////////////////////

// loop through 1 - 105
// return FIZZ for number divisible by 3
// return BUZZ for numbers divisible by 5
// return BAZZ for numbers divisible by 7
// return the number for any that are not divisible by 3, 5, and/or 7

// function fizzBuzzBazz() {
//   for (i = 1; i <= 105; i++) {
//     if (i % 3 === 0) {
//       console.log('FIZZ');
//     }
//     if (i % 5 === 0) {
//       console.log('BUZZ');
//     }
//     if (i % 7 === 0) {
//       console.log('BAZZ');
//     }
//     else {
//       console.log(i);
//     }
//   }
// }
//
// fizzBuzzBazz();

// Better solution:

// function fizzBuzzBazz() {
//   for (i = 1; i <= 105; i++) {
//
//     let out = "";
//
//     if (i % 3 === 0) {
//       out += "FIZZ";
//     }
//     if (i % 5 === 0) {
//       out += "BUZZ";
//     }
//     if (i % 7 === 0) {
//       out += "BAZZ";
//     }
//     console.log(out || i);
//   }
// }
//
// fizzBuzzBazz();


////////////////////////////
// 3. Longest Substring Without Repeating Characters
////////////////////////////

// function lengthOfLongestSubstring(s) {
//
//   let currentStr = [];
//   let longestStrLength = 0;
//
//   for (i = 0; i < s.length; i++) {
//     const currentCharPosition = currentStr.indexOf(s[i]);
//
//     if (currentCharPosition !== -1) {
//       currentStr.splice(0, currentCharPosition + 1);
//     }
//
//     currentStr.push(s[i]);
//
//     longestStrLength = Math.max(
//       longestStrLength,
//       currentStr.length
//     );
//     console.log(currentStr);
//     console.log(currentStr.length);
//     console.log(longestStrLength);
//   }
//   return longestStrLength;
// }
//
// console.log(lengthOfLongestSubstring("abcabcbb"));
