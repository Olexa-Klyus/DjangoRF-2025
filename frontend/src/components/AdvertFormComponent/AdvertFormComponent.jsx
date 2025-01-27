import {useForm} from "react-hook-form";
import styles from "./AdvertFormComponent.module.css";
import {useEffect, useState} from "react";
import {advertService} from "../../services/advertService";
import {categoryService} from "../../services/categoryService";

const AdvertFormComponent = () => {
    const {register, handleSubmit, reset} = useForm();

    const [categories, setCategories] = useState([])
    const [selectedCategory, setSelectedCategory] = useState('Ktu')

    // const getValueCategory = () => {
    //     return currentCategory ? categories.find(cat => cat.value === 2) : '1'
    //     // return '1'
    // }

    useEffect(() => {
        categoryService.getAll().then(values => {
            setCategories(values);
        })
    }, []);

    console.log(categories)


    const save = async (advert) => {
        await advertService.create(advert)
    }


    // console.log(getValueCategory())

    const onChange = (newValue) => {
        setSelectedCategory(newValue.value)
        console.log(newValue.value)
    }

    return (<div>
            <div>
                <form className={styles.wrap_form} onSubmit={handleSubmit(save)}>
                    <label>Категорія
                        <input type="text" placeholder={'categories'} defaultValue={1} {...register('categories')}/>
                    </label>


                    <select onChange={onChange}
                            {...register('categories_select')}>
                        {categories.map((opts, i) => <option key={i}>{opts.name}</option>)}
                    </select>
                    <h2>{selectedCategory}</h2>

                    <label>Модель авто
                        <input type="text" placeholder={'brand'} defaultValue={2} {...register('brand')}/>
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
    );
};
export {AdvertFormComponent};