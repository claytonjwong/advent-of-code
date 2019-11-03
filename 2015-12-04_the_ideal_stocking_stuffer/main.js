let crypto = require('crypto');
let input = '';
let md5 = s => crypto.createHash('md5').update(s).digest('hex');
let suffix = (input, n) => {
    let target = Array(n).fill('0').join('');
    let index = 0;
    for (let i=1;; ++i) {
        let hash = md5(`${input}${i}`);
        if (hash.substr(0, n) == target) {
            index = i;
            break;
        }
    }
    return index;
};
console.log('Answer 1: ' + suffix('ckczppom', 5));
console.log('Answer 2: ' + suffix('ckczppom', 6));