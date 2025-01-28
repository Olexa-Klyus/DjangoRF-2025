import {useForm} from "react-hook-form";
import styles from "./AdvertFormComponent.module.css";
import {useEffect, useState} from "react";
import {advertService} from "../../services/advertService";
import {brandService, categoryService} from "../../services/categoryService";

const AdvertFormComponent = () => {
    const {register, handleSubmit, reset} = useForm({});

    const [categories, setCategories] = useState([{name: 'Легкові', value: 1}])
    const [selectedCategory, setSelectedCategory] = useState('Легкові')
    const getValueCategory = () => categories.find(cat => cat.name === selectedCategory)
    const onChangeCategory = (e) => setSelectedCategory(e.target.value)
    useEffect(() => {
        categoryService.getAll().then(values => {
            setCategories(values)
        })
    }, []);


    const [brands, setBrands] = useState([])
    const [selectedBrand, setSelectedBrand] = useState('')
    const getValueBrand = () => brands.find(brand => brand.name === selectedBrand)
    const onChangeBrand = (e) => setSelectedBrand(e.target.value)
    useEffect(() => {
        if (selectedCategory) {
            brandService.getById(getValueCategory()?.value).then(values => {
                setBrands(values)
            })
        }
    }, [selectedCategory]);


    const save = async (advert) => {
        console.log(advert)
        advert['categories'] = getValueCategory()?.value
        advert['brand'] = getValueBrand()?.value
        await advertService.create(advert)
    }


    return (<div>

            <h2>{selectedCategory}</h2>
            <h2>{selectedBrand}</h2>
            <div className={styles.wrap_form}>

                <label>Категорія
                    <select onChange={onChangeCategory} value={getValueCategory()?.name}>
                        {categories.map((opts, i) => <option key={i}>{opts.name}</option>)}
                    </select>
                </label>

                <label>Модель авто
                    <select onChange={onChangeBrand} value={getValueBrand()?.name}>
                        {brands.map((opts, i) => <option key={i}>{opts.name}</option>)}
                    </select>
                </label>


                <form className={styles.wrap_form} onSubmit={handleSubmit(save)} id={'advert'}>
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