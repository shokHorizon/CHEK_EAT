'use strict';



const waiterControl = () => {
    const container = document.querySelector('.order-container');

    // fetch('http://mymem.space/restaraunts/get_tables/1')
    // .then((response) => {
    // return response.json();
    // })
    // .then((data) => {
    //     console.log(data);
    // });

    const array = [1,2,3,4];
    let num = 1000;
    // let data = json.stringify();

    array.forEach(item => {
        console.log(item);
        const order = document.createElement('div');
    order.className = 'order-block col-lg-4';
    order.innerHTML = `
                    <div class="table-header justify-content-between">
                      <p class="col table-number">Столик: ${item}</p>
                      <p class="col small-tag close-table">Закрыть столик</p>  
                    </div>
                    <div class="order-header">
                        <p class="order">Заказ</p>
                    </div>
                    <div class="order-description justify-content-between">
                        <p class="dish">${item}</p>
                        <p class="price">${item}</p>
                    </div>
                    
                    <div class="total-block justify-content-between">
                        <p class="total">Итог:</p>
                        <p class="total-price">${item}</p>
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