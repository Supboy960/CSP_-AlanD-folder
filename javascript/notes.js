

let images = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhcUZpl8OWqEIF8Ovv2ehl6d3IdaVWrKOm4w_VeeOK-4JN7RpHyQ&s=10&ec=72940545","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmI64E8Soa1kYDYzCrsOeQnoW2-w3MoHOT7g7otm9UqJAXKsFIbA&s=10&ec=72940545" , "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsisMjDMgcDz1sH_fQYqH6tq-7cT5vjgwtqjJUMSzC3kGBbPSTOg&s=10&ec=72940545" 
]
function hello(){
     let name = window.prompt("What is your name?", "Koro Sensei")
    document.getElementById("title").innerHTML = "Hello " + name + "! You know that Challegers suck"
   
count = 0
function change(){
    document.getElementById("img").src = images[count]
    if(count === 2){
        count = 0
    }else{
        count += 1
    }
}

function highlight(){
    document.getElementById("btn").style.backgroundColor = "orange"
    document.getElementById("btn").style.color = "white"
}
function normal(){
    document.getElementById("btn").style.backgroundColor = "gray"
    document.getElementById("btn").style.color = "black"
}

function show(){
    document.getElementById("hidden").style.display = "block"
}
function pop(){
    window.alert("For real. Don't click this!")
}
