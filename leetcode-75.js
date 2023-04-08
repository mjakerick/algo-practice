//////////////////////////////////
// 1. // 1. Two Sum
//////////////////////////////////

// function twoSum(nums, target) {
//
//   let ans = [];
//
//   for(i = 0; i < nums.length; i++) {
//     for(j = i + 1; j < nums.length; j++) {
//       if(nums[i] + nums[j] == target) {
//         ans.push(i, j);
//       }
//     }
//   }
//   return ans;
// };
//
// console.log(twoSum([3,3], 6));


//////////////////////////////////
// 2. // 121. Best Time to Buy and Sell Stock
//////////////////////////////////

// function maxProfit(prices) {
//
//   let buy = 0;
//   let sell = 1;
//   let maxP = 0;
//
//   while(sell < prices.length) {
//     if(prices[buy] < prices[sell]){
//       let profit = prices[sell] - prices[buy];
//       maxP = Math.max(maxP, profit);
//     } else {
//       buy = sell;
//     }
//     sell++;
//   }
//   return maxP;
// }
//
// console.log(maxProfit([7,1,5,3,6,4]));


//////////////////////////////////
// 3. // 217. Contains Duplicate
//////////////////////////////////

// function containsDuplicate(nums) {
//   const hashset = new Set();
//
//   for(i = 0; i < nums.length; i++) {
//     if(hashset.has(nums[i])) {
//       return true;
//     }
//     hashset.add(nums[i])
//   }
//   return false;
// }
//
// console.log(containsDuplicate([1,1,1,3,3,4,3,2,4,2]));


//////////////////////////////////
// 4. // 238. Product of Array Except Self
//////////////////////////////////

// function productExceptSelf(nums) {
//   let prefix = [];
//   for(i = 0; i < nums.length; i++) {
//     if(nums[i-1] === undefined) {
//       prefix[i] = nums[i];
//     } else {
//       prefix[i] = prefix[i-1] *nums[i];
//     }
//   }
//   let postfix = 1;
//   for(i = nums.length - 1; i >= 0; i--) {
//     if(nums[i+1] === undefined) {
//       prefix[i] = prefix[i-1];
//       postfix = nums[i];
//     } else {
//       prefix[i] = (prefix[i-1] === undefined ? 1: prefix[i-1]) * postfix;
//       postfix = postfix * nums[i];
//     }
//   }
//   return prefix;
// }
//
// console.log(productExceptSelf([1,2,3,4]));


//////////////////////////////////
// 5. // 53. Maximum Subarray
//////////////////////////////////

  // function maxSubArray(nums) {
  //   let maxSub = nums[0];
  //   let curSum = 0;
  //
  //   for(i = 0; i < nums.length; i++) {
  //     if(curSum < 0) {
  //       curSum = 0;
  //     }
  //     curSum += nums[i];
  //     maxSub = Math.max(maxSub, curSum);
  //   }
  //   return maxSub;
  // }
  //
  // console.log(maxSubArray([5,4,-1,7,8]));


  //////////////////////////////////
  // 6. //
  //////////////////////////////////
