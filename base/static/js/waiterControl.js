'use strict';



const waiterControl = () => {
    const container = document.querySelector('.order-container');
    // let response = await fetch('url');

    // if (response.ok) { 
    //     let json = await response.json();
    // } else {

    // }

    const array = [1,2,3,4,5,6,78];
    let num = 1000;
    // let data = json.stringify();

    array.forEach(item => {
        console.log(item);
        const order = document.createElement('div');
    order.className = 'order-block col-lg-4';
    order.innerHTML = `
                    <div class="table-header justify-content-between">
                      <p class="col table-number">Столик: ${num}</p>
                      <p class="col small-tag close-table">Закрыть столик</p>  
                    </div>
                    <div class="order-header">
                        <p class="order">Заказ</p>
                    </div>
                    <div class="order-description justify-content-between">
                        <p class="dish">${num}</p>
                        <p class="price">${num}</p>
                    </div>
                    
                    <div class="total-block justify-content-between">
                        <p class="total">Итог:</p>
                        <p class="total-price">${num}</p>
                    </div>
                    <div class="message justify-content-between">
                      <p class="col msg">Вас позвали!</p>
                      <p class="col small-tag tag-confirm">Подтвердить</p>  
                    </div>
                    <div class="message justify-content-between">
                      <p class="col msg">Принесите чек</p>
                      <p class="col small-tag tag-confirm">Подтвердить</p>  
                    </div>
    `
    container.append(order);
    })
}

waiterControl();