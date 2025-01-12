import {useForm} from "react-hook-form";
import {advertService} from "../services/advertService";

const AdvertForm = () => {
    const {register, handleSubmit, reset} = useForm();

    const save = async (advert) =>{
        await advertService.create(advert)
    }
    return (
        <form onSubmit={handleSubmit(save)}>
            <input type="text" placeholder={'name'} {...register('name')}/>
            <input type="text" placeholder={'size'} {...register('size')}/>
            <input type="text" placeholder={'price'} {...register('price')}/>
            <input type="text" placeholder={'day'} {...register('day')}/>
            <button>save</button>
        </form>
    );
};

export {AdvertForm};