/**
  Given an integer x, return true if x is a
palindrome
, and false otherwise.
*/
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
  // Check if the number is negative
  if (x < 0) {
    return false;
  }

  // Convert the number to a string
  let numStr = x.toString();

  // Check if the string is the same forwards and backwards
  let palindrome = true;
  for (let i = 0; i < numStr.length / 2; i++) {
    if (numStr[i] !== numStr[numStr.length - i - 1]) {
      palindrome = false;
      break;
    }
  }

  return palindrome;
};
