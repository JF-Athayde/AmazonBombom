// Troca de imagens do bombom
// Recupera as imagens do atributo data-imagens do elemento img
const imgEl = document.getElementById('bombom-img');
const imagens = JSON.parse(imgEl.getAttribute('data-imagens'));
let idx = 0;

document.getElementById('prev-img').onclick = function() {
    idx = (idx - 1 + imagens.length) % imagens.length;
    imgEl.src = imagens[idx];
};
document.getElementById('next-img').onclick = function() {
    idx = (idx + 1) % imagens.length;
    imgEl.src = imagens[idx];
};