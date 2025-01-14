import {useForm} from "react-hook-form";
import {useState} from "react";

import {useNavigate} from "react-router-dom";
import {authService} from "../services/authService";


const RegisterPage = () => {
    const {register, handleSubmit} = useForm();
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    const registerUser = async (user) => {
        try {
            await authService.register(user);
            setError(false);
            navigate('/login');
        } catch (e) {
            setError(true)
        }
    };

    return (
        <form onSubmit={handleSubmit(registerUser)}>
            <input type="text" placeholder={'username'} {...register('username')}/>
            <input type="text" placeholder={'password'} {...register('password')}/>
            <button>Register</button>
            {error && <div>Username already exists</div>}
        </form>
    );
};

export {RegisterPage};