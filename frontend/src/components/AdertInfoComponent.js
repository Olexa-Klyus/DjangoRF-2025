import {useEffect, useState} from "react";
import {advertService} from "../services/advertService";


const AdvertInfoComponent = () => {

    const [advert, setAdvert] = useState({})
    const [trigger, setTrigger] = useState(null)

    useEffect(() => {
        advertService.getById(2).then((data) => {
            setAdvert(data);
            if (!data["point_is_actual"]) {
                fetch('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
                    .then(response => response.json())
                    .then(data => console.log(data))
            }
        })
    }, []);


    return (
        <div>
            <div>{JSON.stringify(advert)}</div>
        </div>
    );
};

export {AdvertInfoComponent};