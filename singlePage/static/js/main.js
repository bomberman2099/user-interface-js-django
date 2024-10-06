function showCase(text){
    
    document.querySelector('#content').innerHTML = text
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll("button").forEach((button)=>{
        button.onclick = function () {
            showCase(this.dataset.text)
        }
    })
})