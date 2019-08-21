//执行用时 :72 ms, 在所有 JavaScript 提交中击败了94.28%的用户
//内存消耗 :35.6 MB, 在所有 JavaScript 提交中击败了34.02%的用户

/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    var res = new String('1');
    while (n>1)
    {
        var count = 1;
        var idx = 0;
        var tmp = new String();

        for (idx; idx<res.length-1; idx++)
        {
            if (res[idx] == res[idx+1])
            {
                count++;
            }
            else
            {
                tmp += count;
                tmp += res[idx];
                count = 1;
            }    
        }
        tmp += count;
        tmp += res[idx];        
        res = tmp;
        n--;
    }
    return res
};
