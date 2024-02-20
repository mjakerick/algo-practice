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
// 6. // 152. Maximum Product Subarray
//////////////////////////////////

// function maxProduct(nums) {
//   let result = Math.max.apply(Math, nums);
//
//   let curMin = 1;
//   let curMax = 1;
//
//   for(i = 0; i < nums.length; i++) {
//     if(nums[i] == 0) {
//       curMin = 1;
//       curMax = 1;
//     }
//     let temp = curMax * nums[i];
//     curMax = Math.max(nums[i] * curMax, nums[i] * curMin, nums[i]);
//     curMin = Math.min(temp, nums[i] * curMin, nums[i]);
//     result = Math.max(result, curMax, curMin);
//   }
//   return result;
// }
//
// console.log(maxProduct([-2,0,-1]));


//////////////////////////////////
// 7. // 153. Find Minimum in Rotated Sorted Array
//////////////////////////////////

// function findMin(nums) {
//   let result = nums[0];
//   let left = 0;
//   let right = nums.length - 1;
//
//   while(left <= right) {
//     if(nums[left] < nums[right]) {
//       result = Math.min(result, nums[left]);
//       break;
//     }
//     let mid = Math.floor((left + right) / 2);
//     result = Math.min(result, nums[mid]);
//     if(nums[mid] >= nums[left]) {
//       left = mid + 1;
//     } else {
//       right = mid - 1;
//     }
//   }
//   return result;
// }
//
// console.log(findMin([11,13,15,17]));


//////////////////////////////////
// 8. // 33. Search in Rotated Sorted Array
//////////////////////////////////

// function search(nums, target) {
//   let left = 0;
//   let right = nums.length - 1;
//
//   while(left <= right) {
//     let mid = Math.floor((left + right) / 2);
//     if(target == nums[mid]) {
//       return mid;
//     }
//
//     // left sorted portion
//     if(nums[left] <= nums[mid]) {
//       if(target > nums[mid] || target < nums[left]) {
//         left = mid + 1;
//       } else {
//         right = mid - 1;
//       }
//       // right sorted portion
//     } else {
//       if(target < nums[mid] || target > nums[right]) {
//         right = mid - 1;
//       } else {
//         left = mid + 1;
//       }
//     }
//   }
//   return -1;
// }
//
// console.log(search([4,5,6,7,0,1,2], 0));


//////////////////////////////////
// 9. // 15. 3Sum
//////////////////////////////////

// function threeSum(nums) {
//   let result = [];
//   nums.sort(function(a, b){return a-b});
//
//   for(const [i, a] of nums.entries()) {
//
//     if(i > 0 && a == nums[i - 1]) {
//       continue;
//     }
//
//     let left = i + 1;
//     let right = nums.length - 1;
//
//     while(left < right) {
//       sum = a + nums[left] + nums[right];
//       if(sum > 0) {
//         right -= 1;
//       } else if (sum < 0) {
//         left += 1;
//       } else {
//         result.push([a, nums[left], nums[right]]);
//         left += 1;
//         while(nums[left] == nums[left -1] && left < right) {
//           left += 1;
//         }
//       }
//     }
//   }
//   return result;
// }
//
// console.log(threeSum([0,1,1]));


//////////////////////////////////
// 10. // 11. Container With Most Water
//////////////////////////////////

// function maxArea(height) {
//   let result = 0;
//   let left = 0;
//   let right = height.length - 1;
//
//   while(left < right) {
//     let area = (right - left) * Math.min(height[left], height[right]);
//     result = Math.max(result, area);
//
//     if(height[left] < height[right]) {
//       left += 1;
//     } else {
//       right -= 1;
//     }
//   }
//   return result;
// }
//
// console.log(maxArea([1,8,6,2,5,4,8,3,7]));


//////////////////////////////////
// 11. // 371. Sum of Two Integers
//////////////////////////////////

// var getSum = function(a, b) {
//     if (b == 0) {
//         return a;
//     } else {
//         return getSum(a ^ b, (a & b) << 1)
//     }
// };

// console.log(getSum(1, 2))


//////////////////////////////////
// 12. // 191. Number of 1 Bits
//////////////////////////////////

// var hammingWeight = function(n) {
//     let count = 0;
//     let mask = 1;

//     for (i=0; i<32; i++) {
//         if ((mask & n) != 0 ) {            
//             count++;
//         }
//         mask <<= 1;
//     }
//     return count;
// };

// console.log(hammingWeight(00000000000000000000000010000000))


//////////////////////////////////
// 13. // 338. Counting Bits
//////////////////////////////////

// var countBits = function(n) {
// 	let bits = []

// 	for(let i = 0; i <= n; i++) {
// 		bits.push(i.toString(2).split('1').length-1)
// 	}
// 	return bits
// };

// console.log(countBits(2))


//////////////////////////////////
// 14. // 268. Missing Number
//////////////////////////////////

// var missingNumber = function(nums) {
//     let len = nums.length;
// 	if(len===0) return 0;
	
// 	result = 0;
// 	for (let i = 0; i < len; i++) {
// 		result += nums[i] - i;
// 		console.log(result)
// 	}
// 	return len - result;
// };

// console.log(missingNumber([3,0,1]));
// console.log(missingNumber([9,6,4,2,3,5,7,0,1]));


//////////////////////////////////
// 15. // 
//////////////////////////////////