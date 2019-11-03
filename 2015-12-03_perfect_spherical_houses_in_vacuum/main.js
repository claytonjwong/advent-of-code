/*
 * https://adventofcode.com/2015/day/3
 */

class Santa {
    constructor() {
        this.x = 0;
        this.y = 0;
        this.seen = new Set();
    }
    move(dir) {
        let addSeen = (x, y) => {
            let key = (x, y) => x * parseInt(1e6 + 1) + y;
            this.seen.add(key(x, y));
        };
        switch (dir) {
            case '^': --this.x; break;
            case '>': ++this.y; break;
            case 'v': ++this.x; break;
            case '<': --this.y; break;
        }
        addSeen(this.x, this.y)
    }
}

let getInput = () => {
    let fs = require('fs');
    let input = fs.readFileSync('./input.txt', 'utf-8');
    return input;
}

{
    let santa = new Santa();
    let input = getInput();
    for (let dir of input)
        santa.move(dir);
    console.log('Answer 1: ' + santa.seen.size);
}

{
    let santa = new Santa();
    let robot = new Santa();
    let isSanta = 1;
    let input = getInput();
    for (let dir of input) {
        if (isSanta)
            santa.move(dir);
        else
            robot.move(dir);
        isSanta ^= 1;
    }
    let all = new Set([...santa.seen, ...robot.seen]);
    console.log('Answer 2: ' + all.size);
}
