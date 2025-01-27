import {useForm} from "react-hook-form";
import styles from "./AdvertFormComponent.module.css";
import {useEffect, useState} from "react";
import {advertService} from "../../services/advertService";
import {categoryService} from "../../services/categoryService";

const AdvertFormComponent = () => {
    const {register, handleSubmit, reset} = useForm({});

    const [categories, setCategories] = useState([])
    const [selectedCategory, setSelectedCategory] = useState('Легкові')

    const getValueCategory = () => {
        const res = categories.find(cat => cat.name === selectedCategory)
        console.log(res || 1)
        return res
    }

    useEffect(() => {
        categoryService.getAll().then(values => {
            setCategories(values);
        })
    }, []);

    const save = async (advert) => {
        console.log(advert)
        advert['categories']=getValueCategory()?.value
        await advertService.create(advert)
    }

    const onChange = (newValue) => {
        setSelectedCategory(newValue.target.value)
        console.log(newValue.target.value)
    }

    return (<div>

            <h2>{selectedCategory}</h2>
            <div className={styles.wrap_form} >

                <label>Категорія
                    <select onChange={onChange} value={getValueCategory()?.name} name={'categories'}>
                        {categories.map((opts) => <option key={opts.value}>{opts.name}</option>)}
                    </select>
                </label>


                <form className={styles.wrap_form} onSubmit={handleSubmit(save)} id={'advert'}>

                    <label>Модель авто
                        <input type="text" placeholder={'brand'}
                               defaultValue={1} {...register('brand')}/>
                    </label>

                    <input type="text" placeholder={'mark'} defaultValue={2} {...register('mark')}/>
                    <input type="text" placeholder={'year'} defaultValue={2012} {...register('year')}/>
                    <input type="text" placeholder={'mileage'} defaultValue={100000} {...register('mileage')}/>
                    <input type="text" placeholder={'region'} defaultValue={10} {...register('region')}/>
                    <input type="text" placeholder={'city'} defaultValue={25} {...register('city')}/>
                    <input type="text" placeholder={'price'} defaultValue={15000} {...register('price')}/>
                    <input type="text" placeholder={'currency'} defaultValue={2} {...register('currency')}/>
                    <input type="text" placeholder={'description'}
                           defaultValue={'my auto'} {...register('description')}/>
                    <input type="text" placeholder={'gearbox'} defaultValue={2} {...register('gearbox')}/>
                    <input type="text" placeholder={'fuel'} defaultValue={2} {...register('fuel')}/>

                    <button>save</button>

                </form>
            </div>
        </div>
    )
        ;
};
export {AdvertFormComponent};