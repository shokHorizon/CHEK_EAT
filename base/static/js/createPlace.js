'use strict'

const place = document.querySelector('.create-places'),
    addPhoto = document.querySelector('.add-photo')

const createPlace = () => {

    document.addEventListener('click', e => {
        let target = e.target;

        const newPlace = document.createElement('div');
        newPlace.className = 'create-places';
        newPlace.innerHTML = `
            <div class="places-wrap-item row justify-content-between">
                <p class="col align-self-center">Место:</p>
                <div class="col align-self-end">
                    <input name="place-location" type="text" class="form-input-exact" placeholder="Столик на улице"> 
                </div>
            </div>
            
            <div class="places-wrap-item row justify-content-between">
                <p class="col align-self-center">Стол рассчитан на:</p>
                <div class="col align-self-end">
                    <input name="persons-number" type="text" class="form-input-exact" placeholder="12"> 
                </div>
            </div>
            
            <div class="places-wrap-item  row justify-content-between">
                <p class="col align-self-center">Количество столов:</p>
                <div class="col align-self-end">
                    <input name="tables-number" type="text" class="form-input-exact" placeholder="10">  
                </div> 
            </div>
            <div class="line"></div>
        `

        if(target.closest('.add-place')){
            place.append(newPlace)
        }
    })
}

createPlace()