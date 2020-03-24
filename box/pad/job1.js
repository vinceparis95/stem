
/////////////////////////////

// // Functions
//
//
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

////////////////////////////////////////////////

//// Classes, constructors, methods

// arr = [1,2,3,4]

// class Set {
//   constructor(arr) {
//     this.arr = arr
//   }
//
//   add(val) {
//     if (!this.has(val)) this.arr.push(val)
//   }
//
//   delete(val){
//     this.arr = this.arr.filter(x =>  x !== val)
//   }
//
//   has(val){
//     return this.arr.includes(val)
//   }
//
//
// }
//
// const s = new Set([1,2,3,4])
// s.add(9)
// s.add(101)
// s.add(12)
//
// for (i=0;i<=arr.length; i++){
//   console.log(s.arr[i])
//   console.log(":)")
// }


////////////////////////////////


//// Child Sets, extends, super


// class Set2 extends Set{
//   constructor(){
//     super(arr)
//     this.original = arr
//   }
// }
//
// const s2 = new Set2
//
// for (i=0;i<=arr.length; i++){
//   console.log(s2.arr[i])
//   console.log("<3")
//
// }

/////////////////////////////////


// const elems = ['a','b','c']
//
// function Tele(){
//   return (
//     <Tele>
//     <Ele q={elems[0]} />
//     <Ele q={elems[1]} />
//     <Ele q={elems[2]} />
//     </Tele>
//   )
// }
//
// Tele()
