function elimination(arr){
    for(let element = 0;element<arr.length;element++){
      for(let element1 = element+1; element1<arr.length;element1++){
        if(arr[element] == arr[element1]){
          return arr[element]
        }
      }
    }
    return null
  }