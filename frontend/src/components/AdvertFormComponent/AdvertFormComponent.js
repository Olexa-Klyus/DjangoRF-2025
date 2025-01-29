import {useForm} from "react-hook-form";
import styles from "./AdvertFormComponent.module.css";
import {useEffect, useState} from "react";
import {advertService} from "../../services/advertService";
import {categoryService, markService} from "../../services/categoryService";

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


    const [marks, setMarks] = useState([])
    const [selectedMark, setSelectedMark] = useState('')
    const getValueMark = () => marks.find(mark => mark.name === selectedMark)
    const onChangeMark = (e) => setSelectedMark(e.target.value)
    useEffect(() => {
        if (selectedCategory) {
            console.log(getValueCategory())
            markService.getById(getValueCategory()?.value).then(values => {
                setMarks(values)
                console.log(values)
            })
        }
    }, [selectedCategory]);

    const [models, setModels] = useState([])
    const [selectedModel, setSelectedModel] = useState('')
    const getValueModel = () => models.find(model => model.name === selectedModel)
    const onChangeModel = (e) => setSelectedModel(e.target.value)
    useEffect(() => {
        if (selectedCategory) {
            console.log(getValueCategory())
            markService.getById(getValueCategory()?.value).then(values => {
                setMarks(values)
                console.log(values)
            })
        }
    }, [selectedCategory]);



    const save = async (advert) => {
        console.log(advert)
        advert['categories'] = getValueCategory()?.value
        advert['car_mark'] = getValueMark()?.value
        await advertService.create(advert)
    }


    return (<div>

            <h2>{selectedCategory}</h2>
            <h2>{selectedMark}</h2>
            <div className={styles.form_wrap}>

                <label className={styles.label_wrap}>Категорія
                    <select onChange={onChangeCategory} value={getValueCategory()?.name}>
                        {categories.map((opts, i) => <option key={i}>{opts.name}</option>)}
                    </select>
                </label>

                <label className={styles.label_wrap}>Марка авто
                    <select onChange={onChangeMark} value={getValueMark()?.name}>
                        {marks.map((opts, i) => <option key={i}>{opts.name}</option>)}
                    </select>
                </label>

                <label className={styles.label_wrap}>Модель авто
                    <select onChange={onChangeModel} value={getValueModel()?.name}>
                        {models.map((opts, i) => <option key={i}>{opts.name}</option>)}
                    </select>
                </label>

                <form className={styles.form_wrap} onSubmit={handleSubmit(save)} id={'advert'}>
                    <input type="text" placeholder={'car_model'} defaultValue={2} {...register('car_model')}/>
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