import {useEffect, useState} from "react";
import {advertService} from "../services/advertService";

const privatBankAPI = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

const AdvertInfoComponent = () => {

    const [advert, setAdvert] = useState({})
    const [trigger, setTrigger] = useState(null)
    const [points, setPoints] = useState(null)

    useEffect(() => {
        advertService.getById(2).then((data) => {
            setAdvert(data);
            if (!data["point_is_actual"]) {
                setTrigger(prevState => !prevState);
            }
        })
    }, [points]);


    useEffect(() => {
        if (trigger) {
            fetch(privatBankAPI, {headers: {"Content-Type": "application/json"}})
                .then((response) => response.json())
                .then((data) => {
                        if (data) {
                            data.map(point => {
                                fetch("api/auto/currency_point", {
                                    method: 'POST',
                                    headers: {"Content-Type": "application/json"},
                                    body: JSON.stringify(point)
                                })
                                    .then(() => setPoints('true'))
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
            <h3>ЛІЧИЛЬНИКИ - всього : {advert.count_all}</h3>
            <div>---------------------------------------------------------------------------</div>
            <h3>ЦІНИ - {JSON.stringify(advert.calc_prices)}</h3>
            <div>---------------------------------------------------------------------------</div>
            <h3>Курси валют Приватбанку станом на сьогодні - {JSON.stringify(advert.currency_points)}</h3>
            <div>---------------------------------------------------------------------------</div>
            <div>всі дані - {JSON.stringify(advert)}</div>

        </div>
    );
};

export {AdvertInfoComponent};