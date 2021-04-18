let complate = document.querySelectorAll(".complete")[0];

complate.addEventListener('click', () =>{
    document.querySelector('.itemDate').classList.add("done");
    document.querySelector('.itemTitle').classList.add("done");
})