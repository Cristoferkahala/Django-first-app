var btn_preco = window.document.querySelectorAll('.car-price')

function show(btn_preco){

    for(i = 0; ; i++){
        btn_preco = window.document.querySelectorAll('.car-price')[i]
        btn_preco.style.color = 'white'
        btn_preco.style.background = '#1c232f !important'
        btn_preco.innerHTML = 'Subscrever'
    }
}

function hide(btn_preco){

    for(i = 0; ; i++){
        btn_preco = window.document.querySelectorAll('.car-price')[i]
        const preco = btn_preco.getAttribute('data-preco')
        btn_preco.innerHTML = `${preco}`
    }
}