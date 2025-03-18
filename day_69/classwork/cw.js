let user = Number(prompt('Ente your number'))
let one = 1
while (one!=user) {
    if (one%3==0 && one%5==0) {
        console.log(one)
    }
    one++
}