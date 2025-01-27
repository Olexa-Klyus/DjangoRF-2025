import {useEffect, useState} from "react";
import {advertService} from "../../services/advertService";
import {AdvertComponent} from "../AdvertComponent";
import {socketService} from "../../services/socketService";
import {useNavigate} from "react-router-dom";

import styles from "./AdvertsComponent.module.css";

const AdvertsComponent = () => {
    const navigate = useNavigate();

    const [adverts, setAdverts] = useState([])
    const [trigger, setTrigger] = useState(null)

    useEffect(() => {
        advertService.getAll().then((data) => setAdverts(data))
    }, [trigger]);


    // useEffect(() => {
    //     socketInit().then()
    // }, []);
    //
    // const socketInit = async () => {
    //     const {adverts} = await socketService();
    //     const client = await adverts();
    //
    //     client.onopen = () => {
    //         console.log('Advert socket connected');
    //         client.send(JSON.stringify({
    //             action: 'subscribe_to_advert_model_changes',
    //             request_id: new Date().getTime()
    //         }))
    //     }
    //
    //     client.onmessage = ({data}) => {
    //         console.log(data);
    //         setTrigger(prev => !prev)
    //     }
    // }
    return (
        <div>
            <div>
                {adverts?.map(advert => <AdvertComponent key={advert.id} advert={advert}/>)}
            </div>
            <hr/>
            <button className={styles.add_button}
                    onClick={() => {
                        navigate('add')
                    }}>Додати оголошення
            </button>

        </div>

    );
};

export {AdvertsComponent};