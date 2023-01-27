window.addEventListener('load', init)

function init(){    
    hamburger = document.getElementsByClassName('hamburger-icon')[0] 
    var close =document.getElementsByClassName('fa-window-close')[0]
    hamburger.addEventListener('click', otvori_meni)
    close.addEventListener('click', zatvori_meni)
    console.log("Ucitan JavaScript")    
}

var brojac = 0

function otvori_meni(event) {
    var meta_dogadjaja = event.target
    var meni = document.getElementsByClassName('hamburger-meni')[0]    
    
    if (brojac == 0){
        meni.classList.remove('hamburger-meni-zatvoren')
        meni.classList.add('hamburger-meni-otvoren')        
        console.log(meni)
        brojac = 1 
    }

}

function zatvori_meni(){
    var meni = document.getElementsByClassName('hamburger-meni')[0]

    if (brojac == 1){
        meni.classList.add('hamburger-meni-zatvoren')  
        meni.classList.remove('hamburger-meni-otvoren')                      
        console.log(meni)
        brojac = 0
    }
}