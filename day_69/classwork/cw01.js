let user = Number(prompt('Enter number'))
let archevani = Number(prompt('Choose 1.even 2.odd. 3.squared 4.3 is jeradi 5.reversed'))
let one = 1
while (one < user) {
    if (archevani == 1){
        if (one % 2 == 0) {
            console.log(one)
        }
    }else if (archevani == 2){
        if (one % 2 != 0){
            console.log(one)
        }
    }else if (archevani == 3){
        console.log(one**2)
    }else if (archevani == 4){
        if (one % 3 == 0){
            console.log(one)
        }
    }else if (archevani == 5){
        console.log(one-(one*2))
    }
    one++
}