":)"


// function a(){
//     console.log(":) <3")
// }
//
// function b(){
//     a()
// }
// function c(){
//     b()
//     console.log('2 steps')
// }
//
// c()

arr = [1,2,3,4]

class Set {
  constructor(arr) {
    this.arr = arr
  }

  add(val) {
    this.arr.push(val)
  }

}

const s = new Set([1,2,3,4])
s.add(5)

console.log(s)
