import {useEffect, useState} from "react";

import {useParams} from "react-router-dom";
import {advertService} from "../../services/advertService";

const privatBankAPI = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

const AdvertInfoComponent = () => {
    const {id} = useParams();
    const [advert, setAdvert] = useState({})
    const [trigger, setTrigger] = useState(null)
    const [points, setPoints] = useState(null)


    useEffect(() => {

        advertService.getById(id).then((data) => {
            setAdvert(data);
            if (!data["point_is_actual"]) {
                setTrigger(prevState => !prevState);
            }
        })
    }, [points]);


    useEffect(() => {
        if (trigger) {
            fetch(privatBankAPI, {
                mode: "no-cors",
                headers: {
                    "Content-Type": "application/json",

                }
            })
                .then((response) => response.json())
                .then((data) => {
                        if (data) {
                            data.map(point => {
                                advertService.updatePoint(point['ccy'], point)
                                    .then((data) => {
                                        setPoints('true')
                                    })
                            })
                        }
                    }
                )
        }
    }, [trigger]);


    return (
        <div>
            {points ? <h2>Курси валют оновилися. Сторінка перезавантажилася</h2> : <div></div>}
            <div>id ={advert.id}</div>
            <div>user_id={advert.user_id}</div>
            {/*<div>{advert.categories.name}</div>*/}
            <div>price={advert.price}</div>
            <div>price_init={advert.price_init}</div>
            <div>---------------------------------------------------------------------------</div>
            <h3>ЛІЧИЛЬНИКИ - всього : {JSON.stringify(advert.counter)}</h3>
            <div>---------------------------------------------------------------------------</div>
            <h3>ЦІНИ - {JSON.stringify(advert.calc_prices)}</h3>
            <div>---------------------------------------------------------------------------</div>
            <h3>Курси валют Приватбанку станом на сьогодні - {JSON.stringify(advert.currency_points)}</h3>
            <div>---------------------------------------------------------------------------</div>
            <h3>Середні ціни на авто по регіону - {JSON.stringify(advert.avg_prices)}</h3>
            <div>---------------------------------------------------------------------------</div>
            <div>всі дані - {JSON.stringify(advert)}</div>

        </div>
    );
};

export {AdvertInfoComponent};