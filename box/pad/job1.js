function solution(n) {

  let last = null;
  let step = null;

  let castles = 0;

  for (const el in n) {
    if (step==null) {
      step = el;
    }
    else
    {
      if (el != step) {
        if (last!=null) {
          if ((last < step && el < step) || (last > step && el > step)) {
            last += 1
          } else {
            last = step;
            castles += 1;
            last = step;
            step = el
          }
        }
      }
    }

    if (last !== step) {
      castles += 1
    }

  }
  return castles

}

console.log(solution([-10,12,2,2,2,3,332,21,2]));