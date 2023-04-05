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

function maxProfit(prices) {

  let buy = 0;
  let sell = 1;
  let maxP = 0;

  while(sell < prices.length) {
    if(prices[buy] < prices[sell]){
      let profit = prices[sell] - prices[buy];
      maxP = Math.max(maxP, profit);
    } else {
      buy = sell;
    }
    sell++;
  }
  return maxP;
}

console.log(maxProfit([7,1,5,3,6,4]));

// output = 5 because 6 - 1 = 5
