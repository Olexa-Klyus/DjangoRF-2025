import {useNavigate} from "react-router-dom";

const AdvertComponent = ({advert}) => {
    const navigate = useNavigate();
    return (
        <div>
            <div>{advert.description} - {advert.year}</div>
            <button onClick={() => {
                navigate(`advert_info/${advert.id}`)
            }}>Перейти до оголошення {advert.id}
            </button>
            <button onClick={() => {
                navigate(`update/${advert.id}`, {state: advert})
            }}>Змінити оголошення {advert.id}
            </button>
        </div>
    )
        ;
};

export {AdvertComponent};