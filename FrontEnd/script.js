let filter = document.querySelector("#filter-check");
    filter.addEventListener('change', () =>{
        let items = document.querySelectorAll(".todoitem");
        if (filter.checked == true){
            items.forEach(el =>{
                if (el.childNodes[1].classList.contains("done")) {
                    el.classList.add("hide")
                    }
                })
            }
        else {
            items.forEach(el =>{
                if (el.childNodes[1].classList.contains("done")){
                    el.classList.remove("hide")
                }
        })
    }
})

let titleInput = document.getElementById('titletext');
let dataContent = document.getElementsByClassName('dataContent')[0]
titleInput.addEventListener('change', ()=>{
    if (titleInput.nodeValue.length >= 5){
        if (dataContent.classList.contains("hide")){
            dataContent.classList.remove("hide")
        }
    } else{
        if (!dataContent.classList.contains("hide")){
            dataContent.classList.add("hide")
        }  
    }
})

let addBtn = document.getElementsByClassName('addBtn')[0]
function hideMessage() {
    document.getElementsByClassName('event-message')[0].classList.add("hide");
  }
addBtn.addEventListener('click', ()=>{
    document.getElementsByClassName('event-message')[0].classList.remove("hide");
    setTimeout(hideMessage, 2000)
})


let filterClick = document.getElementsByClassName("fas")[0]
let hideElem = document.getElementsByClassName('filter-form')[0]

filterClick.addEventListener('click', ()=>{
    if (hideElem.classList.contains("hide")){
        hideElem.classList.remove("hide")
    } else{
    if (!hideElem.classList.contains("hide")){
        hideElem.classList.add("hide")
    }  
    }
})
