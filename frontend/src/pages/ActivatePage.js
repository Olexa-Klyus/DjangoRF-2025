import {useNavigate, useParams} from "react-router-dom";
import {authService} from "../services/authService";

const ActivatePage = () => {
    const navigate = useNavigate();
    const {token} = useParams();


    if (token) {
        authService.activate(token).then(user => {
            navigate('/login', {state: {email: user.email}});
        })
    }

    return (
        <div>
            <h2>АКТИВАЦІЯ...........{token}</h2>
        </div>
    );
};

export {ActivatePage};