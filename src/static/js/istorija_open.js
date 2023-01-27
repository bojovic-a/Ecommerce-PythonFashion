window.addEventListener('load', init)

function init(){    
    korpe = document.getElementsByClassName('korpa-jedna')
    for (const korpa of korpe){
        korpa.addEventListener('click', otvori_korpu)
    }
}

function otvori_korpu(event){    
    var meta = event.target
    console.log(meta)      
    ostalo = document.querySelector(event.target,"+.stavke_div")
    console.log(ostalo)    
    // for (const st of stavke)
    //     console.log(stavke)
    
}