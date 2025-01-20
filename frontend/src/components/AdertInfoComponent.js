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
            <div>{JSON.stringify(advert)}</div>
        </div>
    );
};

export {AdvertInfoComponent};