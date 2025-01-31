import {useForm} from "react-hook-form";
import styles from "./AdvertFormComponent.module.css";
import {useEffect, useState} from "react";
import {advertService} from "../../services/advertService";
import {
    categoryService, cityService, currencyService, markService, modelService, regionService
} from "../../services/categoryService";
import {useLocation, useNavigate, useParams} from "react-router-dom";
import {apiService} from "../../services/apiService";
import {urls} from "../../constants/urls";

const AdvertFormComponent = () => {
    const {register, handleSubmit, reset} = useForm({});
    const location = useLocation();
    const navigate = useNavigate();
    const {id} = useParams();

    const [categories, setCategories] = useState(
        [location?.state?.categories || {name: 'Легкові', value: 1}])
    const [selectedCategory, setSelectedCategory] = useState(location?.state?.categories?.name || 'Легкові')
    const getValueCategory = () => categories.find(cat => cat.name === selectedCategory)
    const onChangeCategory = (e) => {
        setSelectedCategory(e.target.value)
        setSelectedMark(prevState => '')
        setSelectedModel(prevState => '')
        setModels([])
    }
    useEffect(() => {
        console.log(location)
        console.log(selectedCategory)
        console.log(categories)
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

// cities--------------------------------------------------------------------
    const [cities, setCities] = useState([])
    const [selectedCity, setSelectedCity] = useState('')
    const getValueCity = () => cities.find(city => city.name === selectedCity)
    const onChangeCity = (e) => setSelectedCity(e.target.value)
    useEffect(() => {
        if (selectedRegion) {
            cityService.getById(getValueRegion()?.value).then(values => setCities(values))
        }
    }, [selectedRegion]);

// currency--------------------------------------------------------------------
    const [currency, setCurrency] = useState([{name: 'UAH', value: 1}])
    const [selectedCurrency, setSelectedCurrency] = useState('UAH')
    const getValueCurrency = () => currency.find(cur => cur.name === selectedCurrency)
    const onChangeCurrency = (e) => setSelectedCurrency(e.target.value)
    useEffect(() => {
        currencyService.getAll().then(values => setCurrency(values))
    }, []);


    const save = async (new_advert) => {
        new_advert['categories'] = getValueCategory()?.value
        new_advert['car_mark'] = getValueMark()?.value
        new_advert['car_model'] = getValueModel()?.value
        new_advert['region'] = getValueRegion()?.value
        new_advert['city'] = getValueCity()?.value
        new_advert['currency'] = getValueCurrency()?.value
        if (location?.state) {
            await advertService.update(id, new_advert);
        } else {
            await advertService.create(new_advert);
        }
        navigate('/adverts')
    }


    return (<div>

        <div>
            <div className={styles.selects_wrap}>
                <div className={styles.form_wrap}>
                    <label className={styles.select_wrap}>Категорія
                        <select onChange={onChangeCategory} size={10} value={getValueCategory()?.name}>
                            {categories.map((opts, i) => <option key={i}>{opts.name}</option>)}
                        </select>
                    </label>

                    <label className={styles.select_wrap}>Марка авто
                        <select onChange={onChangeMark} size={10} value={getValueMark()?.name}>
                            {marks.map((opts, i) => <option key={i}>{opts.name}</option>)}
                        </select>
                    </label>

                    <label className={styles.select_wrap}>Модель авто
                        <select onChange={onChangeModel} size={10} value={getValueModel()?.name}>
                            {models.map((opts, i) => <option key={i}>{opts.name}</option>)}
                        </select>
                    </label>
                </div>


                <div className={styles.form_wrap}>
                    <label className={styles.select_wrap}>Область
                        <select onChange={onChangeRegion} size={10} value={getValueRegion()?.name}>
                            {regions.map((opts, i) => <option key={i}>{opts.name}</option>)}
                        </select>
                    </label>

                    <label className={styles.select_wrap}>Місто
                        <select onChange={onChangeCity} size={10} value={getValueCity()?.name}>
                            {cities.map((opts, i) => <option key={i}>{opts.name}</option>)}
                        </select>
                    </label>
                </div>
                <div>
                    <h3>{selectedCategory}</h3>
                    <form className={styles.form_wrap} onSubmit={handleSubmit(save)} id={'advert'}>
                        <label className={styles.input_wrap}>Рік
                            <input type="text" placeholder={'year'} defaultValue={2012} {...register('year')}/>
                        </label>

                        <label className={styles.input_wrap}>Пробіг
                            <input type="text" placeholder={'mileage'} defaultValue={100000} {...register('mileage')}/>
                        </label>
                        <div>
                            <label className={styles.input_wrap}>Ціна
                                <input type="text" placeholder={'price'} defaultValue={15000} {...register('price')}/>
                            </label>
                            <label className={styles.input_wrap}>Валюта
                                <select onChange={onChangeCurrency} value={getValueCurrency()?.name}>
                                    {currency.map((opts, i) => <option key={i}>{opts.name}</option>)}
                                </select>
                            </label>
                        </div>
                        <label className={styles.input_wrap}>Опис
                            <input type="text" placeholder={'description'}
                                   defaultValue={'my auto'} {...register('description')}/>
                        </label>

                        <input type="text" placeholder={'gearbox'} defaultValue={2} {...register('gearbox')}/>

                        <input type="text" placeholder={'fuel'} defaultValue={2} {...register('fuel')}/>

                        {(location?.state) ? <button>змінити</button> : <button>створтити</button>}

                    </form>
                </div>
            </div>
        </div>
    </div>);
};
export {
    AdvertFormComponent
};