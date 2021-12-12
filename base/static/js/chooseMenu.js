'use strict';

const amount = document.querySelector('.amount'),
        inputNumbers = [...document.querySelectorAll('.input-number')];
let     formInfo = document.querySelector('.form-order-info'),
        totalOrder = document.querySelector('.total-order');

const chooseMenu =() => {

let dishes = [], sum = 0;

    document.addEventListener('click', e => {
        let target = e.target;

        if(target.closest('.down') && target.closest('.amount').querySelector('.input-number').value > 0){

            target.closest('.amount').querySelector('.input-number').value--;

        } else if(target.closest('.down') && target.closest('.amount').querySelector('.input-number').value.value === 0){
            target.closest('.down').style.disabled = 'true'
        }

        if(target.closest('.up')){
            target.closest('.amount').querySelector('.input-number').value++;
        }

        if(target.matches('.down') || target.matches('.up')){
            dishes = [];
            formInfo.innerHTML = '';
            sum = 0;

            const inputNumbers = [...document.querySelectorAll('.input-number')];

            inputNumbers.forEach(item => {
                if(item.value > 0){
                    let dish = item.closest('.title-block').querySelector('.dish-p').innerText;
                    let price = +item.closest('.title-block').querySelector('.price-p').innerText.slice(0, -2) * item.value;

                    dishes.push([dish, price])
                }
            })

            dishes.forEach(item => {
                totalOrder.innerText = '';

                let elem = document.createElement('div');
                elem.className = 'elem';
                elem.innerHTML = `
                <p name="dish" style="display: inline-block">${item[0]}</p>
                <p name="price" style="display: inline-block">${item[1]+'p.'}</p>
                `
                formInfo.append(elem)

                sum+= item[1];
                totalOrder.append(sum)
            })

        }
    })


}

chooseMenu();