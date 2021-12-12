'use strict';

const confirmBook = () => {

    fetch('http://mymem.space/restaraunts/get_tables/1')
    .then((response) => {
    return response.json();
    })
    .then((data) => {
        console.log(data);
    });

    document.addEventListener('change', e => {
        let target = e.target;

        if(target.closest('#24') && target.closest('#24').value === 'in'){

        }
    })
}

confirmBook();