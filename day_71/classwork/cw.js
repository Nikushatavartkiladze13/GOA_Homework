let num1 = Number(prompt('Enter number: '))

let sum1 = 0
for (i=0; i<num1+1; i++) {
    if (i%2==0) {
        sum1+=i
    }
}

console.log(sum1)