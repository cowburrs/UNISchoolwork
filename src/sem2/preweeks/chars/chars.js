/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  let y = x.toString();
  if (y.length <= 1) {
    return true;
  }
  let start = y.charAt(0);
  let end = y.charAt(y.length - 1);
  let middle = y.substring(1, y.length - 1);
  if (start != end) {
    return false;
  } else {
    console.log(middle);
    return isPalindrome(middle);
  }
};
