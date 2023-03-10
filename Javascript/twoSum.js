/**
 *Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

*You may assume that each input would have exactly one solution, and you may not use the same element twice.

*You can return the answer in any order.
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
   const hash = {}
   
   for(let i = 0; i<nums.length; i++) {
       const n = nums[i]
       if(hash[target -n] !== undefined) {
           return [hash[target-n], i]
           
       }
       hash[n] = i
   }
    return[]
};
