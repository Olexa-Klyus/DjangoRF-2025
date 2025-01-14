import {useForm} from "react-hook-form";

import {useNavigate} from "react-router-dom";
import {authService} from "../services/authService";

const LoginPage = () => {
    const {register, handleSubmit} = useForm();
    const navigate = useNavigate();

    const onSubmit = async (user) => {
        await authService.login(user)
        navigate('/adverts')
    }
    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <input type="text" placeholder={'email'} {...register('email')}/>
            <input type="text" placeholder={'password'} {...register('password')}/>
            <button>login</button>
        </form>
    );
};

export {LoginPage};