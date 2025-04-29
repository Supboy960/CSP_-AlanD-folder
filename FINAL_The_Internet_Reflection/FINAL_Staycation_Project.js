let images = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDT2mk0bedkevmQ4OQen1jQNVdmm98j-qn6H9z_L8sPPISBx7WSw&s=10&ec=72940545","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp5hch0Xnnwblh4xQQr5wtrBZLztGZ2NEbEIESEGaPjEcl_6K2mQ&s=10&ec=72940545" , "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhW9mFljQ_beob2j65LtfgD2TqP9KMzh5l0LFEbk_7h_oJUX9Trw&s=10&ec=72940545" 
]

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
function push(){
    document.getElementById("btn").style.backgroundColor = "red"
}

function show(){
    document.getElementById("hidden").style.display = "block"
}
function hoverChange() {
    document.getElementById("hover-img").src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYqbnR38aj7B1bya3peQ_0xfkGi7ZdoNpnb8WrgxhmYxwDAeAlag&s=10&ec=72940545"; // New image
}

function hoverReset() {
    document.getElementById("hover-img").src = "https://bearlake.org/wp-content/uploads/94385980_3269045716463689_7742076750342914048_o.jpg"; // Original image
}

function more(){
    if(document.getElementById("extra").style.display != "flex"){
       document.getElementById("extra").style.display = "flex"
    document.getElementById("shw").innerHTML = "Show Less" 
    }else{
            document.getElementById("extra").style.display = "none"
         document.getElementById("shw").innerHTML = "Show More"
    } 
}