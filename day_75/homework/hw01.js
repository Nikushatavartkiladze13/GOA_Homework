const user = {
    name : 'Nika',
    surname : 'Tavartkiladze',
    age : 15,
    school : 179,
    greed : function(name){
        return `hello ${name}`
    }
}

for (let element in user){
    console.log(element)
}