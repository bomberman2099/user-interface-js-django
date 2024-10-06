function showCase(num){
    fetch(`http://127.0.0.1:8000/section/${num}/`)
    .then(Response => Response.text())
    .then(text => document.querySelector('#content').innerHTML = text)
    .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll("button").forEach((button)=>{
        button.onclick = function () {
            showCase(this.dataset.section)
        }
    })
})