'use strict';

const confirmBook = () => {

    let places, newData, placeArray;
    let dataWrapper = document.createElement('div');
        dataWrapper.className = 'data-wrapper';
    const availableTime = document.querySelector('.available-time');

    fetch('http://mymem.space/restaraunts/get_tables/1')
    .then((response) => {
    return response.json();
    })
    .then((data) => {
        newData = data; //объект с типами столиков
    });

    fetch('http://mymem.space/restaraunts/get_free_time/1')
    .then((response) => {
    return response.json();
    })
    .then((data) => {
        placeArray = data; //массив свободных мест
    });

    document.addEventListener('click', e => {
        let target = e.target, timeItem;

        if(newData && target.matches('.first') && target.closest('.available-seats').querySelector('input').value === 'in'){
            availableTime.innerHTML = '';
            dataWrapper.innerHTML = '';

            console.log(placeArray['time']);
            places = newData[1]
            
            placeArray['time'].forEach(item => {
                
                timeItem = document.createElement('div');
                    timeItem.className = 'time-wrapper';
                    timeItem.innerHTML = `
                        <input type="radio" class="time-radio" name="time" value="out">
                        <label for="time-radio" class="">${item}</label>
                    `
                dataWrapper.append(timeItem);
            })
            availableTime.append(dataWrapper)
        }

        if(newData && target.matches('.second') && target.closest('.available-seats').querySelector('input').value === 'in'){
            availableTime.innerHTML = '';
            dataWrapper.innerHTML = '';

            places = newData[2];

            placeArray['time'].forEach(item => {
                timeItem = document.createElement('div');
                    timeItem.className = 'time-wrapper';
                    timeItem.innerHTML = `
                        <input type="radio" class="" name="seat" value="out">
                        <label for="" class="">${item}</label>
                    `
                console.log(timeItem)
                dataWrapper.append(timeItem);
            })
            availableTime.append(dataWrapper)
        }
    })
}

confirmBook();