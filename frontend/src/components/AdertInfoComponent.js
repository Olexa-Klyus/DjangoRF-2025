import {useEffect, useState} from "react";
import {advertService} from "../services/advertService";
import {fetchHeaders, privatBankAPI} from "../constants/urls";
import axios from "axios";


const AdvertInfoComponent = () => {

    const [advert, setAdvert] = useState({})
    const [trigger, setTrigger] = useState(null)
    // const [points, setPoints] = useState({})

    useEffect(() => {
        advertService.getById(2).then((data) => {
            setAdvert(data);
            if (!data["point_is_actual"]) {
                setTrigger(prevState => !prevState);
            }
        })
    }, []);


    // if (trigger) {
    //     axios({
    //         url: privatBankAPI,
    //         headers: {
    //             "Content-Type": "application/json",
    //         },
    //         mode: "no-cors",
    //
    //     }).then(function (response) {
    //         console.log(response.data);
    //     })
    // }
    useEffect(() => {
        if (trigger) {
            fetch(privatBankAPI, fetchHeaders)
                .then((response) => response.json())
                .then((data) => console.log(data))
        }
    }, [trigger]);


    return (
        <div>
            {/*{points ? <div>Нові курси {points}</div> : <div></div>}*/}
            <div>{JSON.stringify(advert)}</div>
        </div>
    );
};

export {AdvertInfoComponent};