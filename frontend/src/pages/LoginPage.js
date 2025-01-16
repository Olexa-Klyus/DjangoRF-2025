import {useForm} from "react-hook-form";

import {useLocation, useNavigate} from "react-router-dom";
import {authService} from "../services/authService";


const LoginPage = () => {
    const location = useLocation();
    const {register, handleSubmit} = useForm();
    const navigate = useNavigate();

    const onSubmit = async (user) => {
        await authService.login(user)
        console.log(user)
        navigate('/adverts')
    }

    return (
        <div>
            <h2>УВІЙДІТЬ В АККАУНТ</h2>
            <form onSubmit={handleSubmit(onSubmit)}>
                <input type="text" defaultValue={location.state?.email}
                       placeholder={'email'} {...register('email')}/>
                <input type="text"
                       placeholder={'password'} {...register('password')}/>
                <button>login</button>
            </form>
        </div>
    );
};

export {
    LoginPage
};