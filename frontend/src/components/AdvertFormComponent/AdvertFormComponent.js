import {useForm} from "react-hook-form";
import styles from "./AdvertFormComponent.module.css";
import {useEffect, useState} from "react";
import {advertService} from "../../services/advertService";
import {categoryService, markService, modelService, regionService} from "../../services/categoryService";

const AdvertFormComponent = () => {
    const {register, handleSubmit, reset} = useForm({});

    const [categories, setCategories] = useState([{name: 'Легкові', value: 1}])
    const [selectedCategory, setSelectedCategory] = useState('Легкові')
    const getValueCategory = () => categories.find(cat => cat.name === selectedCategory)
    const onChangeCategory = (e) => {
        setSelectedCategory(e.target.value)
        setSelectedModel(prevState => '')
        setSelectedMark(prevState => '')
    }
    useEffect(() => {
        categoryService.getAll().then(values => setCategories(values))
    }, []);

// marks-------------------------------------------------------------------
    const [marks, setMarks] = useState([])
    const [selectedMark, setSelectedMark] = useState('')
    const getValueMark = () => marks.find(mark => mark.name === selectedMark)
    const onChangeMark = (e) => {
        setSelectedMark(e.target.value)
        setSelectedModel(prevState => '')
    }

    useEffect(() => {
        if (selectedCategory) {
            markService.getById(getValueCategory()?.value).then(values => setMarks(values))
        }
    }, [selectedCategory]);

// models--------------------------------------------------------------------
    const [models, setModels] = useState([])
    const [selectedModel, setSelectedModel] = useState('')
    const getValueModel = () => models.find(model => model.name === selectedModel)
    const onChangeModel = (e) => setSelectedModel(e.target.value)

    useEffect(() => {
        if (selectedMark) {
            modelService.getById(getValueCategory()?.value, getValueMark()?.value).then(values => {
                setModels(values)
            })
        }
    }, [selectedCategory, selectedMark]);

// regions--------------------------------------------------------------------
    const [regions, setRegions] = useState([])
    const [selectedRegion, setSelectedRegion] = useState('')
    const getValueRegion = () => regions.find(region => region.name === selectedRegion)
    const onChangeRegion = (e) => setSelectedRegion(e.target.value)
    useEffect(() => {
        regionService.getAll().then(values => setRegions(values))
    }, []);


    const save = async (advert) => {
        advert['categories'] = getValueCategory()?.value
        advert['car_mark'] = getValueMark()?.value
        advert['car_model'] = getValueModel()?.value
        advert['region'] = getValueRegion()?.value

        await advertService.create(advert)
    }


    return (<div>

            <h2>{selectedCategory}</h2>
            <h2>{selectedMark}</h2>
            <h2>{selectedModel}</h2>

            <h2>{selectedRegion}</h2>

            <div>
                <div className={styles.selects_wrap}>
                    <div className={styles.form_wrap}>
                        <label className={styles.label_wrap}>Категорія
                            <select onChange={onChangeCategory} size={10} value={getValueCategory()?.name}>
                                {categories.map((opts, i) => <option key={i}>{opts.name}</option>)}
                            </select>
                        </label>

                        <label className={styles.label_wrap}>Марка авто
                            <select onChange={onChangeMark} size={10} value={getValueMark()?.name}>
                                {marks.map((opts, i) => <option key={i}>{opts.name}</option>)}
                            </select>
                        </label>

                        <label className={styles.label_wrap}>Модель авто
                            <select onChange={onChangeModel} size={10} value={getValueModel()?.name}>
                                {models.map((opts, i) => <option key={i}>{opts.name}</option>)}
                            </select>
                        </label>
                    </div>


                    <div className={styles.form_wrap}>
                        <label className={styles.label_wrap}>Область
                            <select onChange={onChangeRegion} size={10} value={getValueRegion()?.name}>
                                {regions.map((opts, i) => <option key={i}>{opts.name}</option>)}
                            </select>
                        </label>
                    </div>

                </div>
                <form className={styles.form_wrap} onSubmit={handleSubmit(save)} id={'advert'}>

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