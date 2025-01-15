import {useForm} from "react-hook-form";
import {useEffect, useState} from "react";

import {useNavigate} from "react-router-dom";
import {authService} from "../services/authService";


const RegisterPage = () => {
    const {register, handleSubmit} = useForm();
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
    }, [error]);

    const registerUser = async (user) => {
        try {
            await authService.register(user).then(data => console.log(data));
            setError(false);
            alert("Для підтвердження реєстрації перейдіть за посиланням на вашому email  ")
            navigate('/login');
        } catch (err) {
            setError(JSON.stringify([{"err_message":err.message}, err.response.data]))
        }
    };

    return (
        <form onSubmit={handleSubmit(registerUser)}>
            <input type="text" placeholder={'email'} {...register('email')}/>
            <input type="text" placeholder={'password'} {...register('password')}/>
            <input type="text" placeholder={'username'} {...register('profile.name')}/>
            <input type="text" placeholder={'surname'} {...register('profile.surname')}/>
            <button>Register</button>
            {error && <div>error! - {error}</div>}
        </form>
    );
};

export {RegisterPage};