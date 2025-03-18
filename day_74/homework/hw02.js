function solution(number){
    let count = 0;
    if (String(number).length < 10){
        for (let element = 0; element<number; element++){
          if (element % 3 === 0 || element % 5 === 0){
            count+=element;
          }
        }
    }
    return count;
  }