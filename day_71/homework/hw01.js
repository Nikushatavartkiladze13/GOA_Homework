let arr = [1,2,3,4,5,6,7,8,9,10]

let min = arr[0]
let max = arr[0]

for (let i of arr) {
    if (i>max) {
        max=i
    }else if (i<min) {
        min=i
    }
}
console.log(min, max)