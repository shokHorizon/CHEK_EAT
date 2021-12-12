'use strict'

const validateData = (f) => {

    const validator = (id) => {

        let form = document.querySelector(`#${id}`),
            inputs = [...form.querySelectorAll('input')],
            loginValid = /^[a-zA-Z](.[a-zA-Z0-9_-]*)$/,
            phoneValid = /^[\+\d- ]{11,}$/,
            nameValid = /^[А-яёA-z\ ]{2,50}$/i,
            passwordValid = /^[a-zA-Z0-9_.-]*$/,
            login, phone, name, password, loginBlock, phoneBlock, nameBlock, passwordBlock;
            
            if(form.querySelector('[name="login"]')){
                loginBlock = form.querySelector('[name="login"]');
                login = form.querySelector('[name="login"]').value;
            }
            
            if(form.querySelector('[name="phone"]')){
                phone = form.querySelector('[name="phone"]').value;
                phoneBlock = form.querySelector('[name="phone"]');
            }

            if(form.querySelector('[name="name"]')){
                name = form.querySelector('[name="name"]').value;
                nameBlock = form.querySelector('[name="name"]');
            }

            if(form.querySelector('[name="password"]')){
                password = form.querySelector('[name="password"]').value;
                passwordBlock = form.querySelector('[name="password"]');
            }

        inputs.forEach(item => {
            if(item.value === ''){
                item.classList.add('invalid');
                alert('Поле не может быть пустым!');
                return false
            } else {
                item.classList.remove('invalid');
            }
        })

        if(!loginValid.test(login) && login){
            loginBlock.classList.add('invalid');
            alert('Некорректное значение выделенного поля!');
            return false;
        } else if(login) {
            loginBlock.classList.remove('invalid');
        }
        if(!nameValid.test(name) && name){
            nameBlock.classList.add('invalid');
            alert('Некорректное значение выделенного поля!');
            return false;
        } else if(name){
            nameBlock.classList.remove('invalid');
        }
        if(!phoneValid.test(phone) && phone){
            phoneBlock.classList.add('invalid');
            alert('Некорректное значение выделенного поля!');
            return false;
        } else if(phone){
            phoneBlock.classList.remove('invalid');
        }
        if(!passwordValid.test(password) && password){
            passwordBlock.classList.add('invalid');
            alert('Некорректное значение выделенного поля!');
            return false;
        } else if(password){
            passwordBlock.classList.remove('invalid');
        }

        return true;
    }

    let form;

    document.addEventListener('submit', e => {

        let target = e.target;

        if(target.closest('form')){
            form = target;  
        }

        if(validator(form.id)){
            f.submit()
        } 
    })

}