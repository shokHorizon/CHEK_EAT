'use strict';

const loginPopup = document.querySelector('.popup-login'),
    regPopup = document.querySelector('.popup-registration'),
    empPopup = document.querySelector('.popup-employee'),
    bookPopup = document.querySelector('.popup-confirm-book'),
    phonePopup = document.querySelector('.popup-confirm-phone');

const openModal = () => {

    document.addEventListener('click', e => {
        let target = e.target;

        if(target.closest('.login')){
            loginPopup.style.display = 'block';
        }
        if(target.closest('.registration')){
            regPopup.style.display = 'block';
        }

        if(target.closest('.login-a')){
            e.preventDefault();
            target.closest('.popup').style.display = 'none';
            empPopup.style.display = 'block';
        }

        if(target.closest('.popup-close') || target.matches('.popup-login') || target.matches('.popup-registration') || target.matches('.popup-confirm-book')){
            target.closest('.popup').style.display = 'none';
        }

        if(target.closest('.a-book')){
            e.preventDefault();
            phonePopup.style.display = 'block';
        }
    })

}

openModal();