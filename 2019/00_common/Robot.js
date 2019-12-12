class Robot {
  constructor(start = 0) {
    this.m = new Map();
    this.i = 0;
    this.j = 0;
    this.d = 0;
    this.D = [0, 1, 2, 3]; // clockwise dirs 0 = up, 1 = right, 2 = down, 3 = left
    this.L = [3, 0, 1, 2]; // left-turns (prev dir is index, next dir is value at that index)
    this.R = [1, 2, 3, 0]; // right-turns (prev dir is index, next dir is value at that index)
    this.painted = new Set();
    this.white = new Set();
    this.paint(start)
  }
  color() {
    let [i, j] = [this.i, this.j];
    if (!this.m.has(i))
      this.m.set(i, new Map());
    let row = this.m.get(i);
    if (!row.has(j))
      row.set(j, 0); // default value 0 for non-existent entries
    return row.get(j);
  }
  paint(v) {
    let [i, j] = [this.i, this.j];
    if (!this.m.has(i))
      this.m.set(i, new Map());
    let row = this.m.get(i);
    row.set(j, v);
    let key = `${i},${j}`;
    this.painted.add(key);
    if (this.color() == 1)
      this.white.add(key);
  }
  step() {
    let d = this.d;
    if (d == 0) --this.i; if (d == 2) ++this.i;
    if (d == 3) --this.j; if (d == 1) ++this.j;
  }
  turn(dir) {
    if (dir == 0) this.d = this.L[this.d];
    if (dir == 1) this.d = this.R[this.d];
  }
}
module.exports = Robot;